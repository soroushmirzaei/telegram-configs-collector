#import requirement libraries
import os
import uuid
import time
import random
import json
import pycountry_convert as pc

#import web-based libraries
import html
import requests
import socket
import ipaddress
import ssl
import tldextract
import geoip2.database
import json
from dns import resolver, rdatatype

#import regex and encoding libraries
import re
import base64


def is_valid_base64(string_value):
    try:
        # Decode the string using base64
        byte_decoded = base64.b64decode(string_value)
        # Encode the decoded bytes back to base64 and compare to the original string
        return base64.b64encode(byte_decoded).decode("utf-8") == string_value
    except:
        # If an exception is raised during decoding, the string is not valid base64
        return False


def is_valid_uuid(value):
    try:
        # Try out to checkout valid UUID and return True
        uuid.UUID(str(value))
        return True
    except ValueError:
        # Return False If it's invalid
        return False


def is_valid_domain(hostname):
    # Extract the TLD, domain, and subdomain from the hostname
    ext = tldextract.extract(hostname)
    # Check if the domain and TLD are not empty
    return ext.domain != "" and ext.suffix != ""


def is_valid_ip_address(ip):
    try:
        if ip.startswith("[") and ip.endswith("]"):
            ip = ip.replace("[", "")
            ip = ip.replace("]", "")
        # Try out to return True if it's IPV4 or IPV6
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        # Else it returns False
        return False


def is_ipv6(ip):
    try:
        # Try out to return True if it's IPV6
        ipaddress.ip_address(ip)
        if ":" in ip:
            return True
        else:
            # Else it returns False
            return False
    except ValueError:
        return False


def get_ips(node):
    try:
        res = resolver.Resolver()
        res.nameservers = ["8.8.8.8"]

        # Retrieve IPV4 and IPV6
        answers_ipv4 = res.resolve(node, rdatatype.A, raise_on_no_answer=False)
        answers_ipv6 = res.resolve(node, rdatatype.AAAA, raise_on_no_answer=False)

        # Initialize set for IPV4 and IPV6
        ips = set()

        # Append IPV4 and IPV6 into set
        for rdata in answers_ipv4:
            ips.add(rdata.address)

        for rdata in answers_ipv6:
            ips.add(rdata.address)

        return ips
    except Exception:
        return None


def get_ip(node):
    try:
        # Get node and return the current hostname
        return socket.gethostbyname(node)
    except Exception:
        return None


def get_country_from_ip(ip):
    if not is_valid_ip_address(ip):
        ips_list = list(get_ips(ip))
        ip = ips_list[0]
    try:
        with geoip2.database.Reader("./geoip-lite/geoip-lite-country.mmdb") as reader:
            response = reader.country(ip)
            country_code = response.country.iso_code
        if not country_code is None:
            return country_code
        else:
            # If country code is NoneType, Returns 'NA'
            return "NA"
    except:
        return "NA"


def get_country_flag(country_code):
    if country_code == 'NA':
        return html.unescape("\U0001F3F4\u200D\u2620\uFE0F")

    base = 127397  # Base value for regional indicator symbol letters
    codepoints = [ord(c) + base for c in country_code.upper()]
    return html.unescape("".join(["&#x{:X};".format(c) for c in codepoints]))


def get_continent(country_code):
    continent_code = pc.country_alpha2_to_continent_code(country_code)
    if continent_code in ['NA', 'SA']:
        continent_emoji = "\U0001F30E"
    elif continent_code in ['EU', 'AF', 'AN']:
        continent_emoji = "\U0001F30D"
    elif continent_code in ['AS', 'OC']:
        continent_emoji = "\U0001F30F"
    
    return continent_emoji


def check_port(ip, port, timeout=1):
    """
    Check if a port is open on a given IP address.

    Args:
    ip (str): The IP address.
    port (int): The port number.
    timeout (int, optional): The timeout in seconds. Defaults to 5.

    Returns:
    bool: True if the port is open, False otherwise.
    """
    try:
        sock = socket.create_connection(address=(ip, port), timeout=timeout)
        sock.close()
        print("Connection Port: Open".upper())
        return True
    except:
        print("Connection Port: Closed\n".upper())
        return False


def ping_ip_address(ip, port):
    try:
        it = time.time()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        ft = time.time()
        sock.close()
        if result == 0:
            return round((ft - it) * 1000, 2)
        else:
            return round(0, 2)
    except:
        return round(0, 2)


def get_isp(node):
    if node.startswith("[") and node.endswith("]"):
        node = node.replace("[", "")
        node = node.replace("]", "")
    try:
        ip_geo_info = requests.get(f'http://ip-api.com/json/{node}')
        ip_geo_info_dict = json.loads(ip_geo_info.text)
        isp_value = [char for char in list(ip_geo_info_dict["isp"]) if char not in [',', '.', '"']]
        isp_value = ''.join(isp_value)
        return isp_value
    except:
        return "Not Available"


def check_modify_config(array_configuration, protocol_type, check_connection = True):
    # Initialize list for modified elements of configuration array
    modified_array = list()
    
    # Initialize array for security types of configuration
    tls_array = list()
    non_tls_array = list()

    # Initialize array for network types of configuration
    tcp_array = list()
    ws_array = list()
    http_array = list()
    grpc_array = list()
    
    if protocol_type == 'SHADOWSOCKS':
        for element in array_configuration:
            # Define ShadowSocks protocol type pattern
            shadowsocks_pattern = r"ss://(?P<id>[^@]+)@\[?(?P<ip>[a-zA-Z0-9\.:-]+?)\]?:(?P<port>[0-9]+)/?#?(?P<title>(?<=#).*)?"

            # Print out original element
            print(f"ORIGINAL CONFIG: {element}")

            # Try out to match pattern and configuration
            shadowsocks_match = re.match(shadowsocks_pattern, element, flags=re.IGNORECASE)


            if shadowsocks_match is None:
                # Define ShadowSocks protocol type second pattern
                shadowsocks_pattern = r"ss://(?P<id>[^#]+)#?(?P<title>(?<=#).*)?(?P<ip>(?:))(?P<port>(?:))"

                # Try out to match second pattern and configuration
                shadowsocks_match = re.match(shadowsocks_pattern, element, flags=re.IGNORECASE)

                if shadowsocks_match is None:
                    # Append no matches ShadowSocks into unmatched file
                    with open("./splitted/no-match", "a") as no_match_file:
                        no_match_file.write(f"{element}\n")
                    print("NO MATCH\n")
                    # Continue for next element
                    continue


            # Initialize dict to separate match groups by name capturing
            config = {
                "id": shadowsocks_match.group("id"),
                "ip": shadowsocks_match.group("ip"),
                "port": shadowsocks_match.group("port"),
                "title": shadowsocks_match.group("title"),
            }

            config["id"] += "=" * ((4 - len(config["id"]) % 4) % 4)

            # Checkout config ID type
            if not is_valid_base64(config["id"]):
                # Append no matches ShadowSocks into unmatched file
                with open("./splitted/no-match", "a") as no_match_file:
                    no_match_file.write(f"{element}\n")
                print(f"INVALID ENCODED STRING: {config['id']}\n")
                # Continue for next element
                continue


            # Try out to match pattern for ShadowSocks config and extract IP and
            if config["ip"] == "":
                # Define ShadowSocks protocol type Third pattern
                shadowsocks_pattern = (r"(?P<id>[^@]+)@\[?(?P<ip>[a-zA-Z0-9\.:-]+?)\]?:(?P<port>[0-9]+)")

                # Try out to match pattern and configuration
                shadowsocks_match = re.match(shadowsocks_pattern, base64.b64decode(config["id"]).decode("utf-8", errors="ignore"), flags=re.IGNORECASE)

                if shadowsocks_match is None:
                    # Append no matches ShadowSocks into unmatched file
                    with open("./splitted/no-match", "a") as no_match_file:
                        no_match_file.write(f"{element}\n")
                    print("NO MATCH\n")
                    # Continue for next element
                    continue

                # Initialize dict to separate match groups by name capturing
                config = {
                    "id": base64.b64encode(shadowsocks_match.group("id").encode("utf-8")).decode("utf-8"),
                    "ip": shadowsocks_match.group("ip"),
                    "port": shadowsocks_match.group("port"),
                    "title": config["title"],
                }


            # Initialize set to append IP addresses
            ips_list = {config["ip"]}

            # Try out to retrieve config IP adresses if It's url link
            if not is_valid_ip_address(config["ip"]):
                ips_list = get_ips(config["ip"])

            # Continue for next element
            if ips_list is None:
                print("NO IP\n")
                continue


            # Iterate over IP addresses to checkout connectivity
            for ip_address in ips_list:
                # Set config dict IP address
                config["ip"] = ip_address

                # Checkout IP address and port connectivity
                if check_connection:
                    if not check_port(config["ip"], int(config["port"])):
                        continue
                        
                # config_ping = ping_ip_address(config["ip"], int(config["port"]))

                # Try out to retrieve country code
                country_code = get_country_from_ip(config["ip"])
                country_flag = get_country_flag(country_code)
                continent_emoji = get_continent(country_code)

                # Modify the IP address if it's IPV6
                if is_ipv6(config["ip"]):
                    config["ip"] = f"[{config['ip']}]"

                '''
                # Continue for next IP address if exists in modified array
                if any(f"ss://{config['id']}@{config['ip']}:{config['port']}" in array_element for array_element in modified_array):
                    continue
                '''
                # Retrieve config network type and security type
                config_secrt = 'NA'
                config_type = 'TCP'

                # Modify configuration title based on server and protocol properties
                config["title"] = f"\U0001F512 SS-TCP-NA {country_flag} {country_code}-{config['ip']}:{config['port']}"
                
                # Print out modified configuration
                print(f"MODIFIED CONFIG: ss://{config['id']}@{config['ip']}:{config['port']}#{config['title']}\n")

                # Append modified configuration into modified array
                modified_array.append(f"ss://{config['id']}@{config['ip']}:{config['port']}#{config['title']}")

                # Append security type array
                if config_secrt == 'TLS' or config_secrt == 'REALITY':
                    tls_array.append(f"ss://{config['id']}@{config['ip']}:{config['port']}#{config['title']}")
                elif config_secrt == 'NA':
                    non_tls_array.append(f"ss://{config['id']}@{config['ip']}:{config['port']}#{config['title']}")

                # Append network type array
                if config_type == 'TCP':
                    tcp_array.append(f"ss://{config['id']}@{config['ip']}:{config['port']}#{config['title']}")
                elif config_type == 'WS':
                    ws_array.append(f"ss://{config['id']}@{config['ip']}:{config['port']}#{config['title']}")
                elif config_type == 'HTTP':
                    http_array.append(f"ss://{config['id']}@{config['ip']}:{config['port']}#{config['title']}")
                elif config_type == 'GRPC':
                    grpc_array.append(f"ss://{config['id']}@{config['ip']}:{config['port']}#{config['title']}")


    elif protocol_type == 'TROJAN':
        for element in array_configuration:
            # Define Trojan protocol type pattern
            trojan_pattern = r"trojan://(?P<id>[^@]+)@\[?(?P<ip>[a-zA-Z0-9\.:-]+?)\]?:(?P<port>[0-9]+)/?\??(?P<params>[^#]+)?#?(?P<title>(?<=#).*)?"

            # Print out original element
            print(f"ORIGINAL CONFIG: {element}")

            # Try out to match pattern and configuration
            trojan_match = re.match(trojan_pattern, element, flags=re.IGNORECASE)

            if trojan_match is None:
                # Append no matches ShadowSocks into unmatched file
                with open("./splitted/no-match", "a") as no_match_file:
                    no_match_file.write(f"{element}\n")
                print("NO MATCH\n")
                # Continue for next element
                continue


            # Initialize dict to separate match groups by name capturing
            config = {
                "id": trojan_match.group("id"),
                "ip": trojan_match.group("ip"),
                "host": trojan_match.group("ip"),
                "port": trojan_match.group("port"),
                "params": trojan_match.group("params") or "",
                "title": trojan_match.group("title"),
            }

            # Initialize set to append IP addresses
            ips_list = {config["ip"]}

            # Try out to retrieve config IP adresses if It's url link
            if not is_valid_ip_address(config["ip"]):
                ips_list = get_ips(config["ip"])

            # Continue for next element
            if ips_list is None:
                print("NO IP\n")
                continue


            # Split configuration parameters and initialize dict for parameters
            array_params_input = config["params"].split("&")
            dict_params = {}
            
            # Iterate over parameters and split based on key value
            for pair in array_params_input:
                try:
                    key, value = pair.split("=")
                    key = re.sub(r"servicename", "serviceName", re.sub(r"headertype", "headerType", re.sub(r"allowinsecure", "allowInsecure", key.lower()),),)
                    dict_params[key] = value
                except:
                    pass

            # Set parameters for servicename and allowinsecure keys
            if (dict_params.get("security", "") in ["reality", "tls"] and dict_params.get("sni", "") == "" and is_valid_domain(config["host"])):
                dict_params["sni"] = config["host"]
                dict_params["allowInsecure"] = 1

            # Ignore the configurations with specified security and None servicename
            if (dict_params.get("security", "") in ["reality", "tls"] and dict_params.get("sni", "") == ""):
                continue


            # Iterate over IP addresses to checkout connectivity
            for ip_address in ips_list:
                # Set config dict IP address
                config["ip"] = ip_address

                # Checkout IP address and port connectivity
                if check_connection:
                    if not check_port(config["ip"], int(config["port"])):
                        continue

                # config_ping = ping_ip_address(config["ip"], int(config["port"]))

                # Try out to retrieve country code
                country_code = get_country_from_ip(config["ip"])
                country_flag = get_country_flag(country_code)
                continent_emoji = get_continent(country_code)

                # Modify the IP address if it's IPV6
                if is_ipv6(config["ip"]):
                    config["ip"] = f"[{config['ip']}]"

                # Define configuration parameters string value and stripped based on & character
                config["params"] = f"security={dict_params.get('security', '')}&flow={dict_params.get('flow', '')}&sni={dict_params.get('sni', '')}&encryption={dict_params.get('encryption', '')}&type={dict_params.get('type', '')}&serviceName={dict_params.get('serviceName', '')}&host={dict_params.get('host', '')}&path={dict_params.get('path', '')}&headerType={dict_params.get('headerType', '')}&fp={dict_params.get('fp', '')}&pbk={dict_params.get('pbk', '')}&sid={dict_params.get('sid', '')}&alpn={dict_params.get('alpn', '')}&allowInsecure={dict_params.get('allowInsecure', '')}&"
                config["params"] = re.sub(r"\w+=&", "", config["params"])
                config["params"] = re.sub(r"(?:encryption=none&)|(?:headerType=none&)", "", config["params"], flags=re.IGNORECASE,)
                config["params"] = config["params"].strip("&")

                '''
                # Continue for next IP address if exists in modified array
                if any(f"trojan://{config['id']}@{config['ip']}:{config['port']}?{config['params']}" in array_element for array_element in modified_array):
                    continue
                '''
                # Retrieve config network type and security type
                config_type = dict_params.get('type', 'TCP').upper() if dict_params.get('type') not in [None, ''] else 'TCP'
                config_secrt = dict_params.get('security', 'TLS').upper() if dict_params.get('security') not in [None, ''] else 'NA'

                # Modify configuration title based on server and protocol properties
                config["title"] = f"\U0001F512 TR-{config_type}-{config_secrt} {country_flag} {country_code}-{config['ip']}:{config['port']}"

                # Print out modified configuration
                print(f"MODIFIED CONFIG: trojan://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}\n")

                # Append modified configuration into modified array
                modified_array.append(f"trojan://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}")

                # Append security type array
                if config_secrt == 'TLS' or config_secrt == 'REALITY':
                    tls_array.append(f"trojan://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}")
                elif config_secrt == 'NA':
                    non_tls_array.append(f"trojan://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}")

                # Append network type array
                if config_type == 'TCP':
                    tcp_array.append(f"trojan://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}")
                elif config_type == 'WS':
                    ws_array.append(f"trojan://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}")
                elif config_type == 'HTTP':
                    http_array.append(f"trojan://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}")
                elif config_type == 'GRPC':
                    grpc_array.append(f"trojan://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}")


    
    elif protocol_type == 'VMESS':
        for element in array_configuration:
            # Define VMESS protocol type pattern
            vmess_pattern = r"vmess://(?P<json>[^#].*)"

            # Print out original element
            print(f"ORIGINAL CONFIG: {element}")

            # Try out to match pattern and configuration
            vmess_match = re.match(vmess_pattern, element, flags=re.IGNORECASE)

            if vmess_match is None:
                # Append no matches ShadowSocks into unmatched file
                with open("./splitted/no-match", "a") as no_match_file:
                    no_match_file.write(f"{element}\n")
                print("NO MATCH\n")
                # Continue for next element
                continue


            # Initialize dict to separate match groups by name capturing
            json_string = vmess_match.group("json")
            json_string += "=" * ((4 - len(json_string) % 4) % 4)
            
            # Checkout config json encoded string
            if not is_valid_base64(json_string):
                # Append invalid json encoded string config into unmatched file
                with open("./splitted/no-match", "a") as no_match_file:
                    no_match_file.write(f"{element}\n")
                print(f"INVALID ENCODED STRING: {json_string}\n")
                # Continue for next element
                continue


            # Decode json string match
            json_string = base64.b64decode(json_string).decode("utf-8", errors="ignore")

            try:
                # Convert decoded json string into dictionary
                dict_params = json.loads(json_string)
                # Modify dictionary parameters with lower keys and values
                dict_params = {k.lower(): v for k, v in dict_params.items()}
            except:
                # Append invalid json encoded string config into unmatched file
                with open("./splitted/no-match", "a") as no_match_file:
                    no_match_file.write(f"{element}\n")
                print(f"INVALID JSON STRING: {json_string}\n")
                # Continue for next element
                continue


            # Initialize dict to separate match groups by name capturing
            config = {
                "id": dict_params.get("id", ""),
                "ip": dict_params.get("add", ""),
                "host": dict_params.get("add", ""),
                "port": dict_params.get("port", ""),
                "params": "",
                "title": dict_params.get("ps", "")
            }

            # Checkout configuration UUID
            if not is_valid_uuid(config["id"]):
                print(f"INVALID UUID: {config['id']}\n")
                continue

            # Initialize set to append IP addresses
            ips_list = {config["ip"]}

            # Try out to retrieve config IP adresses if It's url link
            if not is_valid_ip_address(config["ip"]):
                ips_list = get_ips(config["ip"])

            # Continue for next element
            if ips_list is None:
                print("NO IP\n")
                continue


            # Set parameters for servicename and allowinsecure keys
            if (dict_params.get("tls", "") in ["tls"] and dict_params.get("sni", "") == "" and is_valid_domain(config["host"])):
                dict_params["sni"] = config["host"]
                dict_params["allowInsecure"] = 1

            # Ignore the configurations with specified security and None servicename
            if (dict_params.get("tls", "") in ["tls"] and dict_params.get("sni", "") == ""):
                continue


            # Iterate over IP addresses to checkout connectivity
            for ip_address in ips_list:
                # Set config dict IP address
                config["ip"] = ip_address

                # Checkout IP address and port connectivity
                if check_connection:
                    if not check_port(config["ip"], int(config["port"])):
                        continue

                # config_ping = ping_ip_address(config["ip"], int(config["port"]))

                # Try out to retrieve country code
                country_code = get_country_from_ip(config["ip"])
                country_flag = get_country_flag(country_code)
                continent_emoji = get_continent(country_code)

                # Modify the IP address if it's IPV6
                if is_ipv6(config["ip"]):
                    config["ip"] = f"[{config['ip']}]"
                    
                # Define configuration parameters string value and stripped based on & character
                config["params"] = f"tls={dict_params.get('tls', '')}&sni={dict_params.get('sni', '')}&scy={dict_params.get('scy', '')}&net={dict_params.get('net', '')}&host={dict_params.get('host', '')}&path={dict_params.get('path', '')}&type={dict_params.get('type', '')}&fp={dict_params.get('fp', '')}&alpn={dict_params.get('alpn', '')}&aid={dict_params.get('aid', '')}&v={dict_params.get('v', '')}&allowInsecure={dict_params.get('allowInsecure', '')}&"
                config["params"] = re.sub(r"\w+=&", "", config["params"])
                config["params"] = re.sub(r"(?:tls=none&)|(?:type=none&)|(?:scy=none&)|(?:scy=auto&)", "", config["params"], flags=re.IGNORECASE,)
                config["params"] = config["params"].strip("&")
                
                # Retrieve config network type and security type
                config_type = dict_params.get('net', 'TCP').upper() if dict_params.get('net') not in [None, ''] else 'TCP'
                config_secrt = dict_params.get('tls','NA').upper() if dict_params.get('tls') not in [None, ''] else 'NA'

                # Modify configuration title based on server and protocol properties
                config["title"] = f"\U0001F512 VM-{config_type}-{config_secrt} {country_flag} {country_code}-{config['ip']}:{config['port']}"

                dict_params["add"] = config["ip"]
                dict_params["ps"] = config["title"]

                # Print out modified configuration
                print(f"MODIFIED CONFIG: vmess://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}\n")
                
                # Append modified configuration into modified array
                modified_array.append(f"vmess://{base64.b64encode(json.dumps(dict_params).encode('utf-8')).decode('utf-8')}")

                # Append security type array
                if config_secrt == 'TLS' or config_secrt == 'REALITY':
                    tls_array.append(f"vmess://{base64.b64encode(json.dumps(dict_params).encode('utf-8')).decode('utf-8')}")
                elif config_secrt == 'NA':
                    non_tls_array.append(f"vmess://{base64.b64encode(json.dumps(dict_params).encode('utf-8')).decode('utf-8')}")

                # Append network type array
                if config_type == 'TCP':
                    tcp_array.append(f"vmess://{base64.b64encode(json.dumps(dict_params).encode('utf-8')).decode('utf-8')}")
                elif config_type == 'WS':
                    ws_array.append(f"vmess://{base64.b64encode(json.dumps(dict_params).encode('utf-8')).decode('utf-8')}")
                elif config_type == 'HTTP':
                    http_array.append(f"vmess://{base64.b64encode(json.dumps(dict_params).encode('utf-8')).decode('utf-8')}")
                elif config_type == 'GRPC':
                    grpc_array.append(f"vmess://{base64.b64encode(json.dumps(dict_params).encode('utf-8')).decode('utf-8')}")

    

    elif protocol_type == 'VLESS' or protocol_type == 'REALITY':
        for element in array_configuration:
            # Define VMESS protocol type pattern
            vless_pattern = r"vless://(?P<id>[^@]+)@\[?(?P<ip>[a-zA-Z0-9\.:\-:\_]+?)\]?:(?P<port>[0-9]+)/?\?(?P<params>[^#]+)#?(?P<title>(?<=#).*)?"

            # Print out original element
            print(f"ORIGINAL CONFIG: {element}")

            # Try out to match pattern and configuration
            vless_match = re.match(vless_pattern, element, flags=re.IGNORECASE)

            if vless_match is None:
                # Append no matches ShadowSocks into unmatched file
                with open("./splitted/no-match", "a") as no_match_file:
                    no_match_file.write(f"{element}\n")
                print("NO MATCH\n")
                # Continue for next element
                continue


            # Initialize dict to separate match groups by name capturing
            config = {
                "id": vless_match.group("id"),
                "ip": vless_match.group("ip"),
                "host": vless_match.group("ip"),
                "port": vless_match.group("port"),
                "params": vless_match.group("params"),
                "title": vless_match.group("title"),
            }
            
            # Checkout configuration UUID
            if not is_valid_uuid(config["id"]):
                print(f"INVALID UUID: {config['id']}\n")
                continue

            # Initialize set to append IP addresses
            ips_list = {config["ip"]}

            # Try out to retrieve config IP adresses if It's url link
            if not is_valid_ip_address(config["ip"]):
                ips_list = get_ips(config["ip"])

            # Continue for next element
            if ips_list is None:
                print("NO IP\n")
                continue


            # Split configuration parameters and initialize dict for parameters
            array_params_input = config["params"].split("&")
            dict_params = {}

            # Iterate over parameters and split based on key value
            for pair in array_params_input:
                try:
                    key, value = pair.split("=")
                    key = re.sub(r"servicename", "serviceName", re.sub(r"headertype", "headerType", re.sub(r"allowinsecure", "allowInsecure", key.lower()),),)
                    dict_params[key] = value
                except:
                    pass

            # Set parameters for servicename and allowinsecure keys
            if (dict_params.get("security", "") in ["reality", "tls"] and dict_params.get("sni", "") == "" and is_valid_domain(config["host"])):
                dict_params["sni"] = config["host"]
                dict_params["allowInsecure"] = 1

            # Ignore the configurations with specified security and None servicename
            if (dict_params.get("security", "") in ["reality", "tls"] and dict_params.get("sni", "") == ""):
                continue


            # Iterate over IP addresses to checkout connectivity
            for ip_address in ips_list:
                # Set config dict IP address
                config["ip"] = ip_address

                # Checkout IP address and port connectivity
                if check_connection:
                    if not check_port(config["ip"], int(config["port"])):
                        continue

                # config_ping = ping_ip_address(config["ip"], int(config["port"]))

                # Try out to retrieve country code
                country_code = get_country_from_ip(config["ip"])
                country_flag = get_country_flag(country_code)
                continent_emoji = get_continent(country_code)

                # Modify the IP address if it's IPV6
                if is_ipv6(config["ip"]):
                    config["ip"] = f"[{config['ip']}]"

                # Define configuration parameters string value and stripped based on & character
                config["params"] = f"security={dict_params.get('security', '')}&flow={dict_params.get('flow', '')}&sni={dict_params.get('sni', '')}&encryption={dict_params.get('encryption', '')}&type={dict_params.get('type', '')}&serviceName={dict_params.get('serviceName', '')}&host={dict_params.get('host', '')}&path={dict_params.get('path', '')}&headerType={dict_params.get('headerType', '')}&fp={dict_params.get('fp', '')}&pbk={dict_params.get('pbk', '')}&sid={dict_params.get('sid', '')}&alpn={dict_params.get('alpn', '')}&allowInsecure={dict_params.get('allowInsecure', '')}&"
                config["params"] = re.sub(r"\w+=&", "", config["params"])
                config["params"] = re.sub(r"(?:encryption=none&)|(?:headerType=none&)", "", config["params"], flags=re.IGNORECASE,)
                config["params"] = config["params"].strip("&")
                
                '''
                # Continue for next IP address if exists in modified array
                if any(f"vless://{config['id']}@{config['ip']}:{config['port']}?{config['params']}" in array_element for array_element in modified_array):
                    continue
                '''
                # Retrieve config network type and security type
                config_type = dict_params.get('type', 'TCP').upper() if dict_params.get('type') not in [None, ''] else 'TCP'
                config_secrt = dict_params.get('security','NA').upper() if dict_params.get('security') not in [None, ''] else 'NA'
                if config_secrt == 'REALITY':
                    config_secrt = 'RLT'

                # Modify configuration title based on server and protocol properties
                config["title"] = f"\U0001F512 VL-{config_type}-{config_secrt} {country_flag} {country_code}-{config['ip']}:{config['port']}"

                # Print out modified configuration
                print(f"MODIFIED CONFIG: vless://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}\n")
                
                # Append modified configuration into modified array
                modified_array.append(f"vless://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}")

                # Append security type array
                if config_secrt == 'TLS' or config_secrt == 'REALITY':
                    tls_array.append(f"vless://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}")
                elif config_secrt == 'NA':
                    non_tls_array.append(f"vless://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}")

                # Append network type array
                if config_type == 'TCP':
                    tcp_array.append(f"vless://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}")
                elif config_type == 'WS':
                    ws_array.append(f"vless://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}")
                elif config_type == 'HTTP':
                    http_array.append(f"vless://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}")
                elif config_type == 'GRPC':
                    grpc_array.append(f"vless://{config['id']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}")


    elif protocol_type == 'TUIC':
        for element in array_configuration:
            # Define ShadowSocks protocol type pattern
            tuic_pattern = r"tuic://(?P<id>[^:]+):(?P<pass>[^@]+)@\[?(?P<ip>[a-zA-Z0-9\.:-]+?)\]?:(?P<port>[0-9]+)/?\?(?P<params>[^#]+)#?(?P<title>(?<=#).*)?"

            # Print out original element
            print(f"ORIGINAL CONFIG: {element}")

            # Try out to match pattern and configuration
            tuic_match = re.match(tuic_pattern, element, flags=re.IGNORECASE)

            if tuic_match is None:
                # Append no matches ShadowSocks into unmatched file
                with open("./splitted/no-match", "a") as no_match_file:
                    no_match_file.write(f"{element}\n")
                print("NO MATCH\n")
                # Continue for next element
                continue


            # Initialize dict to separate match groups by name capturing
            config = {
                "id": tuic_match.group("id"),
                "pass": tuic_match.group("pass"),
                "ip": tuic_match.group("ip"),
                "port": tuic_match.group("port"),
                "params": tuic_match.group("params"),
                "title": tuic_match.group("title")
            }

            # Checkout configuration UUID
            if not is_valid_uuid(config["id"]):
                print(f"INVALID UUID: {config['id']}\n")
                continue

            # Initialize set to append IP addresses
            ips_list = {config["ip"]}

            # Try out to retrieve config IP adresses if It's url link
            if not is_valid_ip_address(config["ip"]):
                ips_list = get_ips(config["ip"])

            # Continue for next element
            if ips_list is None:
                print("NO IP\n")
                continue


            # Iterate over IP addresses to checkout connectivity
            for ip_address in ips_list:
                # Set config dict IP address
                config["ip"] = ip_address

                # Checkout IP address and port connectivity
                if check_connection:
                    if not check_port(config["ip"], int(config["port"])):
                        continue

                # config_ping = ping_ip_address(config["ip"], int(config["port"]))

                # Try out to retrieve country code
                country_code = get_country_from_ip(config["ip"])
                country_flag = get_country_flag(country_code)
                continent_emoji = get_continent(country_code)

                # Modify the IP address if it's IPV6
                if is_ipv6(config["ip"]):
                    config["ip"] = f"[{config['ip']}]"


                # Modify configuration title based on server and protocol properties
                config["title"] = f"\U0001F512 TUIC-UDP {country_flag} {country_code}-{config['ip']}:{config['port']}"

                # Print out modified configuration
                print(f"MODIFIED CONFIG: tuic://{config['id']}:{config['pass']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}\n")

                # Append modified configuration into modified array
                modified_array.append(f"tuic://{config['id']}:{config['pass']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}")



    elif protocol_type == 'HYSTERIA':
        for element in array_configuration:
            if element.startswith('hysteria'):
                # Define ShadowSocks protocol type pattern
                hysteria_1_pattern = r"hysteria://\[?(?P<ip>[a-zA-Z0-9\.:-]+?)\]?:(?P<port>[0-9]+)/?\?(?P<params>[^#]+)#?(?P<title>(?<=#).*)?"

                # Print out original element
                print(f"ORIGINAL CONFIG: {element}")

                # Try out to match pattern and configuration
                hysteria_match = re.match(hysteria_1_pattern, element, flags=re.IGNORECASE)

                if hysteria_match is None:
                    # Append no matches ShadowSocks into unmatched file
                    with open("./splitted/no-match", "a") as no_match_file:
                        no_match_file.write(f"{element}\n")
                    print("NO MATCH\n")
                    # Continue for next element
                    continue


                # Initialize dict to separate match groups by name capturing
                config = {
                    "ip": hysteria_match.group("ip"),
                    "port": hysteria_match.group("port"),
                    "params": hysteria_match.group("params"),
                    "title": hysteria_match.group("title")
                }


                # Initialize set to append IP addresses
                ips_list = {config["ip"]}

                # Try out to retrieve config IP adresses if It's url link
                if not is_valid_ip_address(config["ip"]):
                    ips_list = get_ips(config["ip"])

                # Continue for next element
                if ips_list is None:
                    print("NO IP\n")
                    continue


                # Iterate over IP addresses to checkout connectivity
                for ip_address in ips_list:
                    # Set config dict IP address
                    config["ip"] = ip_address

                    # Checkout IP address and port connectivity
                    if check_connection:
                        if not check_port(config["ip"], int(config["port"])):
                            continue

                    # config_ping = ping_ip_address(config["ip"], int(config["port"]))

                    # Try out to retrieve country code
                    country_code = get_country_from_ip(config["ip"])
                    country_flag = get_country_flag(country_code)
                    continent_emoji = get_continent(country_code)

                    # Modify the IP address if it's IPV6
                    if is_ipv6(config["ip"]):
                        config["ip"] = f"[{config['ip']}]"


                    # Modify configuration title based on server and protocol properties
                    config["title"] = f"\U0001F512 HYSTERIA-UDP {country_flag} {country_code}-{config['ip']}:{config['port']}"

                    # Print out modified configuration
                    print(f"MODIFIED CONFIG: hysteria://{config['ip']}:{config['port']}?{config['params']}#{config['title']}\n")

                    # Append modified configuration into modified array
                    modified_array.append(f"hysteria://{config['ip']}:{config['port']}?{config['params']}#{config['title']}")


            elif element.startswith('hy2'):
                # Define ShadowSocks protocol type pattern
                hysteria_2_pattern = r"hy2://(?P<pass>[^@]+)@\[?(?P<ip>[a-zA-Z0-9\.:-]+?)\]?:(?P<port>[0-9]+)/?\?(?P<params>[^#]+)#?(?P<title>(?<=#).*)?"

                # Print out original element
                print(f"ORIGINAL CONFIG: {element}")

                # Try out to match pattern and configuration
                hysteria_match = re.match(hysteria_2_pattern, element, flags=re.IGNORECASE)

                if hysteria_match is None:
                    # Append no matches ShadowSocks into unmatched file
                    with open("./splitted/no-match", "a") as no_match_file:
                        no_match_file.write(f"{element}\n")
                    print("NO MATCH\n")
                    # Continue for next element
                    continue


                # Initialize dict to separate match groups by name capturing
                config = {
                    "pass": hysteria_match.group("pass"),
                    "ip": hysteria_match.group("ip"),
                    "port": hysteria_match.group("port"),
                    "params": hysteria_match.group("params"),
                    "title": hysteria_match.group("title")
                }


                # Initialize set to append IP addresses
                ips_list = {config["ip"]}

                # Try out to retrieve config IP adresses if It's url link
                if not is_valid_ip_address(config["ip"]):
                    ips_list = get_ips(config["ip"])

                # Continue for next element
                if ips_list is None:
                    print("NO IP\n")
                    continue


                # Iterate over IP addresses to checkout connectivity
                for ip_address in ips_list:
                    # Set config dict IP address
                    config["ip"] = ip_address

                    # Checkout IP address and port connectivity
                    if check_connection:
                        if not check_port(config["ip"], int(config["port"])):
                            continue

                    # config_ping = ping_ip_address(config["ip"], int(config["port"]))

                    # Try out to retrieve country code
                    country_code = get_country_from_ip(config["ip"])
                    country_flag = get_country_flag(country_code)
                    continent_emoji = get_continent(country_code)

                    # Modify the IP address if it's IPV6
                    if is_ipv6(config["ip"]):
                        config["ip"] = f"[{config['ip']}]"


                    # Modify configuration title based on server and protocol properties
                    config["title"] = f"\U0001F512 HYSTERIA-UDP {country_flag} {country_code}-{config['ip']}:{config['port']}"

                    # Print out modified configuration
                    print(f"MODIFIED CONFIG: hy2://{config['pass']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}\n")

                    # Append modified configuration into modified array
                    modified_array.append(f"hy2://{config['pass']}@{config['ip']}:{config['port']}?{config['params']}#{config['title']}")                

    else:
        modified_array = array_configuration

    return modified_array, tls_array, non_tls_array, tcp_array, ws_array, http_array, grpc_array


def config_sort(array_configuration, bound_ping = 50):
    # Initialize list for sorted configs
    sort_init_list = list()

    for config in array_configuration:
        if config.startswith('vless') or config.startswith('trojan') or config.startswith('ss'):
            ping_time = float(config.split(' ')[-1].split('-')[1])
            ping_config_tp = (ping_time, config)
            sort_init_list.append(ping_config_tp)

        if config.startswith('vmess'):
            vmess_pattern = r"vmess://(?P<json>[^#].*)"
            vmess_match = re.match(vmess_pattern, config, flags=re.IGNORECASE)
            json_string = vmess_match.group('json')

            json_string = base64.b64decode(json_string).decode("utf-8", errors="ignore")
            dict_params = json.loads(json_string)
            dict_params = {k.lower(): v for k, v in dict_params.items()}

            config_title = dict_params.get('ps')
            ping_time = float(config_title.split(' ')[-1].split('-')[1])
            ping_config_tp = (ping_time, config)
            sort_init_list.append(ping_config_tp)

    # Iterate over array configuration to separate configurations
    forward_sorted_list = [(ping, config) for ping, config in sort_init_list if ping >= bound_ping]
    reversed_sorted_list = [(ping, config) for ping, config in sort_init_list if ping < bound_ping]

    # Sort configurations based on ping on forawarded and reversed
    forward_sorted_list = [config for ping, config in sorted(forward_sorted_list, key = lambda element: element[0])]
    reversed_sorted_list = [config for ping, config in sorted(reversed_sorted_list, key = lambda element: element[0], reverse = True)]

    forward_sorted_list.extend(reversed_sorted_list)
    array_configuration = forward_sorted_list

    return array_configuration


def create_country(array_configuration):
    # Initialize list for sorted configs
    country_based_init_list = list()
    country_config_dict = dict()

    for config in array_configuration:
        if config.startswith('vless') or config.startswith('trojan') or config.startswith('ss'):
            country_code = config.split(' ')[-1].split('-')[0]
            country = country_code.lower()
            country_config_tp = (country, config)
            country_based_init_list.append(country_config_tp)

        if config.startswith('vmess'):
            vmess_pattern = r"vmess://(?P<json>[^#].*)"
            vmess_match = re.match(vmess_pattern, config, flags=re.IGNORECASE)
            json_string = vmess_match.group('json')

            json_string = base64.b64decode(json_string).decode("utf-8", errors="ignore")
            dict_params = json.loads(json_string)
            dict_params = {k.lower(): v for k, v in dict_params.items()}

            config_title = dict_params.get('ps')
            country_code = config_title.split(' ')[-1].split('-')[0]
            country = country_code.lower()
            country_config_tp = (country, config)
            country_based_init_list.append(country_config_tp)


    for country, config in country_based_init_list:
        if country not in country_config_dict.keys():
            country_config_dict[country] = list()
        country_config_dict[country].append(config)
    
    return country_config_dict


def create_country_table(country_path):
    # Retrive Country List
    country_code_list = os.listdir(country_path)

    # Counvert country code into country name
    country_url_pattern = '[Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/{country_code}/mixed)'
    country_code_name_url = sorted(list(map(lambda element : (element.upper(), pc.country_alpha2_to_country_name(element.upper()) if element.upper() != 'NA' else 'Not Available', country_url_pattern.format(country_code = element)), country_code_list)), key = lambda element : element[1])

    for index, element in enumerate(country_code_name_url):
        tail_string = ' | '.join(element)
        country_code_name_url[index] = tail_string

    chunks = list()
    for i in range(0, len(country_code_name_url), 2):
        chunk = country_code_name_url[i : i + 2]
        chunks.append(chunk)

    tail_srtring_list = list()
    for element in chunks:
        start = '| '
        tail_string = ' | '.join(element)
        end = ' |'
        tail_string = start + tail_string + end
        tail_srtring_list.append(tail_string)

    tail_srtring_list = '\n'.join(tail_srtring_list)
    table_hedar = '''| **Code** | **Country Name** | **Subscription Link** | **Code** | **Country Name** | **Subscription Link** |\n|:---:|:---:|:---:|:---:|:---:|:---:|'''
    table = table_hedar + '\n' + tail_srtring_list

    return table


def create_internet_protocol(array_configuration):
    # Initialize list for sorted configs
    internet_protocol_ver4 = list()
    internet_protocol_ver6 = list()

    for config in array_configuration:
        if config.startswith('vless') or config.startswith('trojan') or config.startswith('ss'):
            ip_port = config.split(' ')[-1].split('-')[-1]
            if '[' in ip_port or ']' in ip_port:
                internet_protocol_ver6.append(config)
            else:
                internet_protocol_ver4.append(config)

        if config.startswith('vmess'):
            vmess_pattern = r"vmess://(?P<json>[^#].*)"
            vmess_match = re.match(vmess_pattern, config, flags=re.IGNORECASE)
            json_string = vmess_match.group('json')

            json_string = base64.b64decode(json_string).decode("utf-8", errors="ignore")
            dict_params = json.loads(json_string)
            dict_params = {k.lower(): v for k, v in dict_params.items()}

            config_title = dict_params.get('ps')
            ip_port = config_title.split(' ')[-1].split('-')[-1]
            if '[' in ip_port or ']' in ip_port:
                internet_protocol_ver6.append(config)
            else:
                internet_protocol_ver4.append(config)

    return internet_protocol_ver4, internet_protocol_ver6


