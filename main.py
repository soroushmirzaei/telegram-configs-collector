#import requirement libraries
import os
import wget
import json
from pathlib import Path

import math
import string
import random

import jdatetime
from datetime import datetime, timezone, timedelta

#import web-based libraries
import html
import requests
from bs4 import BeautifulSoup

#import regex and encoding libraries
import re
import base64

#import custom python script
from title import check_modify_config, create_country, create_country_table, create_internet_protocol


# Create the geoip-lite folder if it doesn't exist
if not os.path.exists('./geoip-lite'):
    os.mkdir('./geoip-lite')

if os.path.exists('./geoip-lite/geoip-lite-country.mmdb'):
    os.remove('./geoip-lite/geoip-lite-country.mmdb')

# Download the file and rename it
url = 'https://github.com/P3TERX/GeoLite.mmdb/raw/download/GeoLite2-Country.mmdb'
filename = 'geoip-lite-country.mmdb'
wget.download(url, filename)

# Move the file to the geoip folder
os.rename(filename, os.path.join('./geoip-lite', filename))


# Clean up unmatched file
with open("./splitted/no-match", "w") as no_match_file:
    no_match_file.write("#Non-Adaptive Configurations\n")


# Load and read last date and time update
with open('./last update', 'r') as file:
    last_update_datetime = file.readline()
    last_update_datetime = datetime.strptime(last_update_datetime, '%Y-%m-%d %H:%M:%S.%f%z')

# Write the current date and time update
with open('./last update', 'w') as file:
    current_datetime_update = datetime.now(tz = timezone(timedelta(hours = 3, minutes = 30)))
    jalali_current_datetime_update = jdatetime.datetime.now(tz = timezone(timedelta(hours = 3, minutes = 30)))
    file.write(f'{current_datetime_update}')

print(f"Latest Update: {last_update_datetime.strftime('%a, %d %b %Y %X %Z')}\nCurrent Update: {current_datetime_update.strftime('%a, %d %b %Y %X %Z')}")


def get_absolute_paths(start_path):
    abs_paths = []
    for root, dirs, files in os.walk(start_path):
        for file in files:
            abs_path = Path(root).joinpath(file).resolve()
            abs_paths.append(str(abs_path))
    return abs_paths

dirs_list = ['./security', './protocols', './networks', './layers'
            './subscribe', './splitted', './channels']

if (int(jalali_current_datetime_update.day) == 1 and int(jalali_current_datetime_update.hour) == 0) or (int(jalali_current_datetime_update.day) == 15 and int(jalali_current_datetime_update.hour) == 0):
    print("The All Collected Configurations Cleared Based On Scheduled Day".title())
    last_update_datetime = last_update_datetime - timedelta(days=3)
    print(f"The Latest Update Time Is Set To {last_update_datetime.strftime('%a, %d %b %Y %X %Z')}".title())
    for root_dir in dirs_list:
        for path in get_absolute_paths(root_dir):
            if not path.endswith('readme.md'):
                with open(path, 'w') as file:
                    file.write('')
                    file.close
            else:
                continue


def json_load(path):
    # Open and read the json file
    with open(path, 'r') as file:
        # Load json file content into list
        list_content = json.load(file)
    # Return list of json content
    return list_content


def tg_channel_messages(channel_user):
    try:
        # Retrieve channels messages
        response = requests.get(f"https://t.me/s/{channel_user}")
        soup = BeautifulSoup(response.text, "html.parser")
        # Find all telegram widget messages
        div_messages = soup.find_all("div", class_="tgme_widget_message")
        # Return list of all messages in channel
        return div_messages
    except Exception as exc:
        pass


def find_matches(text_content):
    # Initialize configuration type patterns
    pattern_telegram_user = r'(?:@)(\w{4,})'
    pattern_url = r'(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))'
    pattern_shadowsocks = r"(?<![\w-])(ss://[^\s<>#]+)"
    pattern_trojan = r"(?<![\w-])(trojan://[^\s<>#]+)"
    pattern_vmess = r"(?<![\w-])(vmess://[^\s<>#]+)"
    pattern_vless = r"(?<![\w-])(vless://(?:(?!=reality)[^\s<>#])+(?=[\s<>#]))"
    pattern_reality = r"(?<![\w-])(vless://[^\s<>#]+?security=reality[^\s<>#]*)"
    pattern_tuic = r"(?<![\w-])(tuic://[^\s<>#]+)"
    pattern_hysteria = r"(?<![\w-])(hysteria://[^\s<>#]+)"
    pattern_hysteria_ver2 = r"(?<![\w-])(hy2://[^\s<>#]+)"
    pattern_juicity = r"(?<![\w-])(juicity://[^\s<>#]+)"

    # Find all matches of patterns in text
    matches_usersname = re.findall(pattern_telegram_user, text_content, re.IGNORECASE)
    matches_url = re.findall(pattern_url, text_content, re.IGNORECASE)
    matches_shadowsocks = re.findall(pattern_shadowsocks, text_content, re.IGNORECASE)
    matches_trojan = re.findall(pattern_trojan, text_content, re.IGNORECASE)
    matches_vmess = re.findall(pattern_vmess, text_content, re.IGNORECASE)
    matches_vless = re.findall(pattern_vless, text_content, re.IGNORECASE)
    matches_reality = re.findall(pattern_reality, text_content, re.IGNORECASE)
    matches_tuic = re.findall(pattern_tuic, text_content)
    matches_hysteria = re.findall(pattern_hysteria, text_content)
    matches_hysteria_ver2 = re.findall(pattern_hysteria_ver2, text_content)
    matches_juicity = re.findall(pattern_juicity, text_content)

    # Iterate over matches to subtract titles
    for index, element in enumerate(matches_vmess):
        matches_vmess[index] = re.sub(r"#[^#]+$", "", html.unescape(element))

    for index, element in enumerate(matches_shadowsocks):
        matches_shadowsocks[index] = (re.sub(r"#[^#]+$", "", html.unescape(element))+ f"#SHADOWSOCKS")

    for index, element in enumerate(matches_trojan):
        matches_trojan[index] = (re.sub(r"#[^#]+$", "", html.unescape(element))+ f"#TROJAN")

    for index, element in enumerate(matches_vless):
        matches_vless[index] = (re.sub(r"#[^#]+$", "", html.unescape(element))+ f"#VLESS")

    for index, element in enumerate(matches_reality):
        matches_reality[index] = (re.sub(r"#[^#]+$", "", html.unescape(element))+ f"#REALITY")

    for index, element in enumerate(matches_tuic):
        matches_tuic[index] = (re.sub(r"#[^#]+$", "", html.unescape(element))+ f"#TUIC")

    for index, element in enumerate(matches_hysteria):
        matches_hysteria[index] = (re.sub(r"#[^#]+$", "", html.unescape(element))+ f"#HYSTERIA")

    for index, element in enumerate(matches_hysteria_ver2):
        matches_hysteria_ver2[index] = (re.sub(r"#[^#]+$", "", html.unescape(element))+ f"#HYSTERIA")

    for index, element in enumerate(matches_juicity):
        matches_juicity[index] = (re.sub(r"#[^#]+$", "", html.unescape(element))+ f"#JUICITY")

    matches_shadowsocks = [x for x in matches_shadowsocks if "…" not in x]
    matches_trojan = [x for x in matches_trojan if "…" not in x]
    matches_vmess = [x for x in matches_vmess if "…" not in x]
    matches_vless = [x for x in matches_vless if "…" not in x]
    matches_reality = [x for x in matches_reality if "…" not in x]
    matches_tuic = [x for x in matches_tuic if "…" not in x]
    matches_hysteria = [x for x in matches_hysteria if "…" not in x]
    matches_hysteria_ver2 = [x for x in matches_hysteria_ver2 if "…" not in x]
    matches_juicity = [x for x in matches_juicity if "…" not in x]

    # Extend hysteria versions
    matches_hysteria.extend(matches_hysteria_ver2)
    
    return matches_usersname, matches_url, matches_shadowsocks, matches_trojan, matches_vmess, matches_vless, matches_reality, matches_tuic, matches_hysteria, matches_juicity


def tg_message_time(div_message):
    # Retrieve channel message info
    div_message_info = div_message.find('div', class_='tgme_widget_message_info')
    # Retrieve channel message datetime
    message_datetime_tag = div_message_info.find('time')
    message_datetime = message_datetime_tag.get('datetime')

    # Change message datetime type into object and convert into Iran datetime
    datetime_object = datetime.fromisoformat(message_datetime)
    datetime_object = datetime.astimezone(datetime_object, tz = timezone(timedelta(hours = 3, minutes = 30)))

    # Retrieve now datetime based on Iran timezone
    datetime_now = datetime.now(tz = timezone(timedelta(hours = 3, minutes = 30)))

    # Return datetime object, current datetime based on Iran datetime and delta datetime
    return datetime_object, datetime_now, datetime_now - datetime_object


def tg_message_text(div_message, content_extracter):
    # Retrieve message text class from telegram messages widget
    div_message_text = div_message.find("div", class_="tgme_widget_message_text")
    text_content = div_message_text.prettify()
    if content_extracter == 'url':
        text_content = re.sub(r"<code>([^<>]+)</code>", r"\1",re.sub(r"\s*", "", text_content),)
    elif content_extracter == 'config':
        text_content = re.sub(r"<code>([^<>]+)</code>", r"\1",
                              re.sub(r"<a[^<>]+>([^<>]+)</a>", r"\1",re.sub(r"\s*", "", text_content),),)
    
    # Return text content
    return text_content


# Load telegram channels usernames
telegram_channels = json_load('telegram channels.json')

# Initial channels messages array
channel_messages_array = list()
removed_channel_array = list()
channel_check_messages_array = list()

# Iterate over all public telegram chanels and store twenty latest messages
for channel_user in telegram_channels:
    try:
        print(f'{channel_user}')
        # Iterate over Telegram channels to Retrieve channel messages and extend to array
        div_messages = tg_channel_messages(channel_user)
        
        # Append destroyed Telegram channels
        if len(div_messages) == 0:
            removed_channel_array.append(channel_user)
        # Check configuation Telegram channels
        channel_check_messages_array.append((channel_user, div_messages))
        
        for div_message in div_messages:
            datetime_object, datetime_now, delta_datetime_now = tg_message_time(div_message)
            if datetime_object > last_update_datetime:
                print(f"\t{datetime_object.strftime('%a, %d %b %Y %X %Z')}")
                channel_messages_array.append((channel_user, div_message))
    except Exception as exc:
        continue

# Print out total new messages counter
print(f"\nTotal New Messages From {last_update_datetime.strftime('%a, %d %b %Y %X %Z')} To {current_datetime_update.strftime('%a, %d %b %Y %X %Z')} : {len(channel_messages_array)}\n")


# Initial arrays for protocols
array_usernames = list()
array_url = list()
array_shadowsocks = list()
array_trojan = list()
array_vmess = list()
array_vless = list()
array_reality = list()
array_tuic = list()
array_hysteria = list()
array_juicity = list()

for channel_user, message in channel_messages_array:
    try:
        # Iterate over channel messages to extract text content
        url_text_content = tg_message_text(message, 'url')
        config_text_content = tg_message_text(message, 'config')
        # Iterate over each message to extract configuration protocol types and subscription links
        matches_username, matches_url, _ , _ , _ , _ , _ , _ , _ , _ = find_matches(url_text_content)
        _ , _ , matches_shadowsocks, matches_trojan, matches_vmess, matches_vless, matches_reality, matches_tuic, matches_hysteria, matches_juicity = find_matches(config_text_content)

        # Extend protocol type arrays and subscription link array
        array_usernames.extend([element.lower() for element in matches_username if len(element) >= 5])
        array_url.extend(matches_url)
        array_shadowsocks.extend(matches_shadowsocks)
        array_trojan.extend(matches_trojan)
        array_vmess.extend(matches_vmess)
        array_vless.extend(matches_vless)
        array_reality.extend(matches_reality)
        array_tuic.extend(matches_tuic)
        array_hysteria.extend(matches_hysteria)
        array_juicity.extend(matches_juicity)

    except Exception as exc:
        continue


# Initialize Telegram channels list without configuration
channel_without_config = set()

for channel_user, messages in channel_check_messages_array:
    # Initialize Channel Configs Counter
    total_config = 0

    for message in messages:
        try:
            # Iterate over channel messages to extract text content
            url_text_content = tg_message_text(message, 'url')
            config_text_content = tg_message_text(message, 'config')
            # Iterate over each message to extract configuration protocol types and subscription links
            matches_username, matches_url, _ , _ , _ , _ , _ , _ , _ , _ = find_matches(url_text_content)
            _ , _ , matches_shadowsocks, matches_trojan, matches_vmess, matches_vless, matches_reality, matches_tuic, matches_hysteria, matches_juicity = find_matches(config_text_content)
            total_config = total_config + len(matches_shadowsocks) + len(matches_trojan) + len(matches_vmess) + len(matches_vless) + len(matches_reality) + len(matches_tuic) + len(matches_hysteria) + len(matches_juicity)

        except Exception as exc:
            continue

    if total_config == 0:
        channel_without_config.add(channel_user)


def tg_username_extract(url):
    telegram_pattern = r'((http|Http|HTTP)://|(https|Https|HTTPS)://|(www|Www|WWW)\.|https://www\.|)(?P<telegram_domain>(t|T)\.(me|Me|ME)|(telegram|Telegram|TELEGRAM)\.(me|Me|ME)|(telegram|Telegram|TELEGRAM).(org|Org|ORG)|telesco.pe|(tg|Tg|TG).(dev|Dev|DEV)|(telegram|Telegram|TELEGRAM).(dog|Dog|DOG))/(?P<username>[a-zA-Z0-9_+-]+)'
    matches_url = re.match(telegram_pattern, url)
    return matches_url.group('username')


# Split Telegram usernames and subscription url links
tg_username_list = set()
url_subscription_links = set()

for url in array_url:
    try:
        tg_user = tg_username_extract(url)
        if tg_user not in ['proxy', 'img', 'emoji', 'joinchat'] and '+' not in tg_user and '-' not in tg_user and len(tg_user)>=5:
            tg_user = ''.join([element for element in list(tg_user) if element in string.ascii_letters + string.digits + '_'])
            tg_username_list.add(tg_user.lower())
    except:
        url_subscription_links.add(url.split("\"")[0])
        continue

for index, tg_user in enumerate(array_usernames):
    tg_user = ''.join([element for element in list(tg_user) if element in string.ascii_letters + string.digits + '_'])
    array_usernames[index] = tg_user


# Retrive and update channels from telegram proxies Repository
url = 'https://raw.githubusercontent.com/soroushmirzaei/telegram-proxies-collector/main/telegram channels.json'
filename = 'telegram proxies channel.json'
wget.download(url, filename)

tg_username_list.update(array_usernames)
telegram_proxies_channel = json_load('./telegram proxies channel.json')
tg_username_list.update(telegram_proxies_channel)
os.remove('./telegram proxies channel.json')


# Subtract and get new telegram channels
new_telegram_channels = tg_username_list.difference(telegram_channels)

# Initial channels messages array
new_channel_messages = list()
invalid_array_channels = json_load('invalid telegram channels.json')
invalid_array_channels = set(invalid_array_channels)

# Iterate over all public telegram chanels and store twenty latest messages
for channel_user in new_telegram_channels:
    if channel_user not in invalid_array_channels:
        try:
            print(f'{channel_user}')
            # Iterate over Telegram channels to Retrieve channel messages and extend to array
            div_messages = tg_channel_messages(channel_user)
            channel_messages = list()
            for div_message in div_messages:
                datetime_object, datetime_now, delta_datetime_now = tg_message_time(div_message)
                print(f"\t{datetime_object.strftime('%a, %d %b %Y %X %Z')}")
                channel_messages.append(div_message)
            new_channel_messages.append((channel_user, channel_messages))
        except:
            continue
    else:
        continue

# Messages Counter
print(f"\nTotal New Messages From New Channels {last_update_datetime.strftime('%a, %d %b %Y %X %Z')} To {current_datetime_update.strftime('%a, %d %b %Y %X %Z')} : {len(new_channel_messages)}\n")


# Initial arrays for protocols
new_array_shadowsocks = list()
new_array_trojan = list()
new_array_vmess = list()
new_array_vless = list()
new_array_reality = list()
new_array_tuic = list()
new_array_hysteria = list()
new_array_juicity = list()

# Initialize array for channelswith configuration contents
new_array_channels = set()

for channel, messages in new_channel_messages:
    # Set Iterator to estimate each channel configurations
    total_config = 0
    new_array_url = set()
    new_array_usernames = set()

    for message in messages:
        try:
            # Iterate over channel messages to extract text content
            url_text_content = tg_message_text(message, 'url')
            config_text_content = tg_message_text(message, 'config')
            # Iterate over each message to extract configuration protocol types and subscription links
            matches_username, matches_url, _ , _ , _ , _ , _ , _ , _ , _ = find_matches(url_text_content)
            _ , _ , matches_shadowsocks, matches_trojan, matches_vmess, matches_vless, matches_reality, matches_tuic, matches_hysteria, matches_juicity = find_matches(config_text_content)
            total_config = total_config + len(matches_shadowsocks) + len(matches_trojan) + len(matches_vmess) + len(matches_vless) + len(matches_reality) + len(matches_tuic) + len(matches_hysteria) + len(matches_juicity)

            # Extend protocol type arrays and subscription link array
            new_array_usernames.update([element.lower() for element in matches_username if len(element) >= 5])
            new_array_url.update(matches_url)
            new_array_shadowsocks.extend(matches_shadowsocks)
            new_array_trojan.extend(matches_trojan)
            new_array_vmess.extend(matches_vmess)
            new_array_vless.extend(matches_vless)
            new_array_reality.extend(matches_reality)
            new_array_tuic.extend(matches_tuic)
            new_array_hysteria.extend(matches_hysteria)
            new_array_juicity.extend(matches_juicity)

        except Exception as exc:
            continue

    # Append to channels that conatins configurations
    if total_config != 0:
        new_array_channels.add(channel)
    else:
        invalid_array_channels.add(channel)

    # Split Telegram usernames and subscription url links
    tg_username_list_new = set()

    for url in new_array_url:
        try:
            tg_user = tg_username_extract(url)
            if tg_user not in ['proxy', 'img', 'emoji', 'joinchat'] and '+' not in tg_user and '-' not in tg_user and len(tg_user)>=5:
                tg_user = ''.join([element for element in list(tg_user) if element in string.ascii_letters + string.digits + '_'])
                tg_username_list_new.add(tg_user.lower())
        except:
            url_subscription_links.add(url.split("\"")[0])
            continue

    new_array_usernames = list(new_array_usernames)
    for index, tg_user in enumerate(new_array_usernames):
        tg_user = ''.join([element for element in list(tg_user) if element in string.ascii_letters + string.digits + '_'])
        new_array_usernames[index] = tg_user

    # Subtract and get new telegram channels
    tg_username_list_new.update([element.lower() for element in new_array_usernames])
    tg_username_list_new = tg_username_list_new.difference(telegram_channels)
    tg_username_list_new = tg_username_list_new.difference(new_telegram_channels)
    updated_new_channel = set(list(map(lambda element : element[0], new_channel_messages)))
    tg_username_list_new = tg_username_list_new.difference(updated_new_channel)

    # Iterate over all public telegram chanels and store twenty latest messages
    for channel_user in tg_username_list_new:
        if channel_user not in invalid_array_channels:
            try:
                print(f'{channel_user}')
                # Iterate over Telegram channels to Retrieve channel messages and extend to array
                div_messages = tg_channel_messages(channel_user)
                channel_messages = list()
                for div_message in div_messages:
                    datetime_object, datetime_now, delta_datetime_now = tg_message_time(div_message)
                    #print(f"\t{datetime_object.strftime('%a, %d %b %Y %X %Z')}")
                    channel_messages.append(div_message)
                #new_channel_messages.append((channel_user, channel_messages))
            except:
                continue
        else:
            continue


# Extend new configurations into list previous ones
array_shadowsocks.extend(new_array_shadowsocks)
array_trojan.extend(new_array_trojan)
array_vmess.extend(new_array_vmess)
array_vless.extend(new_array_vless)
array_reality.extend(new_array_reality)
array_tuic.extend(new_array_tuic)
array_hysteria.extend(new_array_hysteria)
array_juicity.extend(new_array_juicity)

print("New Telegram Channels Found")
for channel in new_array_channels:
    print('\t{value}'.format(value = channel))

print("Destroyed Telegram Channels Found")
for channel in removed_channel_array:
    print('\t{value}'.format(value = channel))

print("No Config Telegram Channels Found")
for channel in channel_without_config:
    print('\t{value}'.format(value = channel))

# Extend new channels into previous channels
telegram_channels.extend(new_array_channels)
#telegram_channels = [channel for channel in telegram_channels if channel not in removed_channel_array and channel not in channel_without_config]
telegram_channels = [channel for channel in telegram_channels if channel not in removed_channel_array]
telegram_channels = list(set(telegram_channels))
telegram_channels = sorted(telegram_channels)

invalid_telegram_channels = list(set(invalid_array_channels))
invalid_telegram_channels = sorted(invalid_telegram_channels)

with open('./telegram channels.json', 'w') as telegram_channels_file:
    json.dump(telegram_channels, telegram_channels_file, indent = 4)

with open('./invalid telegram channels.json', 'w') as invalid_telegram_channels_file:
    json.dump(invalid_telegram_channels, invalid_telegram_channels_file, indent = 4)


def html_content(html_address):
    # Retrieve subscription link content
    response = requests.get(html_address, timeout = 10)
    soup = BeautifulSoup(response.text, 'html.parser').text
    return soup


def is_valid_base64(string_value):
    try:
        # Decode the string using base64
        byte_decoded = base64.b64decode(string_value)
        # Encode the decoded bytes back to base64 and compare to the original string
        return base64.b64encode(byte_decoded).decode("utf-8") == string_value
    except:
        return False


def decode_string(content):
    # Decode strings and append to array
    if is_valid_base64(content):
            content = base64.b64decode(content).decode("utf-8")
    return content


def decode_vmess(vmess_config):
    try:
        encoded_config = re.sub(r"vmess://", "", vmess_config)
        decoded_config = base64.b64decode(encoded_config).decode("utf-8")
        decoded_config_dict = json.loads(decoded_config)
        
        decoded_config_dict["ps"] = f"VMESS"
        decoded_config = json.dumps(decoded_config_dict)

        encoded_config = decoded_config.encode('utf-8')
        encoded_config = base64.b64encode(encoded_config).decode('utf-8')
        encoded_config = f"vmess://{encoded_config}"
        return encoded_config
    except:
        return None


# Update url subscription links
url_subscription_links = list(url_subscription_links)

new_tg_username_list = set()
new_url_subscription_links = set()

for url in url_subscription_links:
    try:
        tg_user = tg_username_extract(url)
        if tg_user not in ['proxy', 'img', 'emoji', 'joinchat']:
            new_tg_username_list.add(tg_user.lower())
    except:
        new_url_subscription_links.add(url.split("\"")[0])
        continue

# Chnage type of url subscription links into list to be hashable
new_url_subscription_links = list(new_url_subscription_links)


accept_chars = ['sub', 'subscribe', 'token', 'workers', 'worker', 'dev', 'txt', 'vmess', 'vless', 'reality', 'trojan', 'shadowsocks']
avoid_chars = ['github', 'githubusercontent', 'gist', 'git', 'google', 'play', 'apple', 'microsoft']

new_subscription_links = set()

for index, element in enumerate(new_url_subscription_links):
    acc_cond = [char in element.lower() for char in accept_chars]
    avoid_cond = [char in element.lower() for char in avoid_chars]
    if any(acc_cond):
        if not any(avoid_cond):
            new_subscription_links.add(element)


# Load subscription links
subscription_links = json_load('subscription links.json')
# subscription_links.extend(new_subscription_links)

# Initial links contents array decoded content array
array_links_content = list()
array_links_content_decoded = list()

raw_array_links_content = list()
raw_array_links_content_decoded = list()

channel_array_links_content = list()
channel_array_links_content_decoded = list()

for url_link in subscription_links:
    try:
        # Retrieve subscription link content
        links_content = html_content(url_link)
        array_links_content.append((url_link, links_content))
        if 'soroushmirzaei' not in url_link:
            raw_array_links_content.append((url_link, links_content))
        elif 'soroushmirzaei' in url_link and 'channels' in url_link:
            channel_array_links_content.append((url_link, links_content))
    except:
        continue


# Separate encoded and unencoded strings
decoded_contents = list(map(lambda element : (element[0], decode_string(element[1])), array_links_content))
# Separate encoded and unencoded strings
raw_decoded_contents = list(map(lambda element : (element[0], decode_string(element[1])), raw_array_links_content))
# Separate encoded and unencoded strings
channel_decoded_contents = list(map(lambda element : (element[0], decode_string(element[1])), channel_array_links_content))

for url_link, content in decoded_contents:
    try:
        # Split each link contents into array and split by lines
        link_contents = content.splitlines()
        link_contents = [element for element in link_contents if element not in ['\n','\t','']]
        # Iterate over link contents to subtract titles
        for index, element in enumerate(link_contents):
            link_contents[index] = re.sub(r"#[^#]+$", "", element)
        array_links_content_decoded.append((url_link, link_contents))
    except:
        continue


for url_link, content in raw_decoded_contents:
    try:
        # Split each link contents into array and split by lines
        link_contents = content.splitlines()
        link_contents = [element for element in link_contents if element not in ['\n','\t','']]
        # Iterate over link contents to subtract titles
        for index, element in enumerate(link_contents):
            link_contents[index] = re.sub(r"#[^#]+$", "", element)
        raw_array_links_content_decoded.append((url_link, link_contents))
    except:
        continue


for url_link, content in channel_decoded_contents:
    try:
        # Split each link contents into array and split by lines
        link_contents = content.splitlines()
        link_contents = [element for element in link_contents if element not in ['\n','\t','']]
        # Iterate over link contents to subtract titles
        for index, element in enumerate(link_contents):
            link_contents[index] = re.sub(r"#[^#]+$", "", element)
        channel_array_links_content_decoded.append((url_link, link_contents))
    except:
        continue


new_subscription_urls = set()

matches_usernames = list()
matches_url = list()
matches_shadowsocks = list()
matches_trojan = list()
matches_vmess = list()
matches_vless = list()
matches_reality = list()
matches_tuic = list()
matches_hysteria = list()
matches_juicity = list()

raw_matches_usernames = list()
raw_matches_url = list()
raw_matches_shadowsocks = list()
raw_matches_trojan = list()
raw_matches_vmess = list()
raw_matches_vless = list()
raw_matches_reality = list()
raw_matches_tuic = list()
raw_matches_hysteria = list()
raw_matches_juicity = list()

channel_matches_usernames = list()
channel_matches_url = list()
channel_matches_shadowsocks = list()
channel_matches_trojan = list()
channel_matches_vmess = list()
channel_matches_vless = list()
channel_matches_reality = list()
channel_matches_tuic = list()
channel_matches_hysteria = list()
channel_matches_juicity = list()

for url_link, content in array_links_content_decoded:
    # Merge all subscription links content and find all protocols matches base on protocol pattern
    content_merged = "\n".join(content)
    match_user, match_url, match_socks, match_trojan, match_vmess, match_vless, match_reality, match_tuic, match_hysteria, match_juicity = find_matches(content_merged)

    if len(match_socks) + len(match_trojan) + len(match_vmess) + len(match_vless) + len(match_reality) + len(match_tuic) + len(match_hysteria) + len(match_juicity) != 0:
        new_subscription_urls.add(url_link)

    matches_usernames.extend(match_user)
    matches_url.extend(match_url)
    matches_shadowsocks.extend(match_socks)
    matches_trojan.extend(match_trojan)
    matches_vmess.extend(match_vmess)
    matches_vless.extend(match_vless)
    matches_reality.extend(match_reality)
    matches_tuic.extend(match_tuic)
    matches_hysteria.extend(match_hysteria)
    matches_juicity.extend(match_juicity)

for url_link, content in raw_array_links_content_decoded:
    # Merge all subscription links content and find all protocols matches base on protocol pattern
    raw_content_merged = "\n".join(content)
    match_user, match_url, match_socks, match_trojan, match_vmess, match_vless, match_reality, match_tuic, match_hysteria, match_juicity = find_matches(raw_content_merged)

    raw_matches_usernames.extend(match_user)
    raw_matches_url.extend(match_url)
    raw_matches_shadowsocks.extend(match_socks)
    raw_matches_trojan.extend(match_trojan)
    raw_matches_vmess.extend(match_vmess)
    raw_matches_vless.extend(match_vless)
    raw_matches_reality.extend(match_reality)
    raw_matches_tuic.extend(match_tuic)
    raw_matches_hysteria.extend(match_hysteria)
    raw_matches_juicity.extend(match_juicity)

for url_link, content in channel_array_links_content_decoded:
    # Merge all subscription links content and find all protocols matches base on protocol pattern
    raw_content_merged = "\n".join(content)
    match_user, match_url, match_socks, match_trojan, match_vmess, match_vless, match_reality, match_tuic, match_hysteria, match_juicity = find_matches(raw_content_merged)

    channel_matches_usernames.extend(match_user)
    channel_matches_url.extend(match_url)
    channel_matches_shadowsocks.extend(match_socks)
    channel_matches_trojan.extend(match_trojan)
    channel_matches_vmess.extend(match_vmess)
    channel_matches_vless.extend(match_vless)
    channel_matches_reality.extend(match_reality)
    channel_matches_tuic.extend(match_tuic)
    channel_matches_hysteria.extend(match_hysteria)
    channel_matches_juicity.extend(match_juicity)

# Save New Subscription Links
# with open('./subscription links.json', 'w') as subscription_file:
#    json.dump(sorted(new_subscription_urls), subscription_file, indent = 4)


def remove_duplicate_modified(array_configuration):
    # Initialize list for sorted configs
    country_config_dict = dict()

    for config in array_configuration:
        try:
            if config.startswith('ss'):
                pattern = r"ss://(?P<id>[^@]+)@\[?(?P<ip>[a-zA-Z0-9\.:-]+?)\]?:(?P<port>[0-9]+)/?#?(?P<title>(?<=#).*)?"
                shadowsocks_match = re.match(pattern, config, flags=re.IGNORECASE)
                ip = shadowsocks_match.group("ip")
                port = shadowsocks_match.group("port")
                id = shadowsocks_match.group("id")
                non_title_config = f"SS-{ip}:{port}"
                country_config_dict[non_title_config] = config


            if config.startswith('trojan'):
                pattern = r"trojan://(?P<id>[^@]+)@\[?(?P<ip>[a-zA-Z0-9\.:-]+?)\]?:(?P<port>[0-9]+)/?\??(?P<params>[^#]+)?#?(?P<title>(?<=#).*)?"
                trojan_match = re.match(pattern, config, flags=re.IGNORECASE)
                ip = trojan_match.group("ip")
                port = trojan_match.group("port")
                id = trojan_match.group("id")
                non_title_config = f"TR-{ip}:{port}"
                country_config_dict[non_title_config] = config


            if config.startswith('vless'):
                pattern = r"vless://(?P<id>[^@]+)@\[?(?P<ip>[a-zA-Z0-9\.:-]+?)\]?:(?P<port>[0-9]+)/?\?(?P<params>[^#]+)#?(?P<title>(?<=#).*)?"
                vless_match = re.match(pattern, config, flags=re.IGNORECASE)
                ip = vless_match.group("ip")
                port = vless_match.group("port")
                id = vless_match.group("id")
                param = vless_match.group("params")

                # Split configuration parameters and initialize dict for parameters
                array_params_input = param.split("&")
                dict_params = {}

                # Iterate over parameters and split based on key value
                for pair in array_params_input:
                    try:
                        key, value = pair.split("=")
                        key = re.sub(r"servicename", "serviceName", re.sub(r"headertype", "headerType", re.sub(r"allowinsecure", "allowInsecure", key.lower()),),)
                        dict_params[key.lower()] = value.lower() if type(value) == str else value
                    except:
                        pass

                dict_params = {k: v for k, v in sorted(dict_params.items(), key=lambda item: item[0])}
                non_title_config = f"VL-{ip}:{port}"
                country_config_dict[non_title_config] = config


            if config.startswith('vmess'):
                vmess_pattern = r"vmess://(?P<json>[^#].*)"
                vmess_match = re.match(vmess_pattern, config, flags=re.IGNORECASE)
                json_string = vmess_match.group('json')

                json_string = base64.b64decode(json_string).decode("utf-8", errors="ignore")
                dict_params = json.loads(json_string)
                dict_params = {k.lower(): v.lower() if type(v) == str else v for k, v in dict_params.items()}
                ip = dict_params.get("ip")
                port = dict_params.get("port")
                id = dict_params.get("id")

                dict_params['ps'] = ''
                dict_params = {k: v for k, v in sorted(dict_params.items(), key=lambda item: item[0])}
                non_title_config = f"VM-{ip}:{port}"

                country_config_dict[non_title_config] = config

            
            if config.startswith('tuic'):
                pattern = r"tuic://(?P<id>[^:]+):(?P<pass>[^@]+)@\[?(?P<ip>[a-zA-Z0-9\.:-]+?)\]?:(?P<port>[0-9]+)/?\?(?P<params>[^#]+)#?(?P<title>(?<=#).*)?"
                tuic_match = re.match(pattern, config, flags=re.IGNORECASE)
                ip = tuic_match.group("ip")
                port = tuic_match.group("port")
                id = tuic_match.group("id")
                password = tuic_match.group("pass")
                non_title_config = f"TUIC-{ip}:{port}"
                country_config_dict[non_title_config] = config


            if config.startswith('hysteria'):
                pattern = r"hysteria://\[?(?P<ip>[a-zA-Z0-9\.:-]+?)\]?:(?P<port>[0-9]+)/?\?(?P<params>[^#]+)#?(?P<title>(?<=#).*)?"
                hysteria_match = re.match(pattern, config, flags=re.IGNORECASE)
                ip = hysteria_match.group("ip")
                port = hysteria_match.group("port")
                non_title_config = f"HYSTERIA1-{ip}:{port}"
                country_config_dict[non_title_config] = config


            if config.startswith('hy2'):
                pattern = r"hy2://(?P<pass>[^@]+)@\[?(?P<ip>[a-zA-Z0-9\.:-]+?)\]?:(?P<port>[0-9]+)/?\?(?P<params>[^#]+)#?(?P<title>(?<=#).*)?"
                hysteria_match = re.match(pattern, config, flags=re.IGNORECASE)
                ip = hysteria_match.group("ip")
                port = hysteria_match.group("port")
                password = hysteria_match.group("pass")
                non_title_config = f"HYSTERIA2-{ip}:{port}"
                country_config_dict[non_title_config] = config

        except:
            continue

    return list(country_config_dict.values())
    

def remove_duplicate(shadow_array, trojan_array, vmess_array, vless_array, reality_array, tuic_array, hysteria_array, juicity_array, vmess_decode_dedup = True):
    # Remove duplicate configurations of telegram channels
    shadow_array = list(set(shadow_array))
    trojan_array = list(set(trojan_array))
    vmess_array = list(set(vmess_array))
    vless_array = list(set(vless_array))
    reality_array = list(set(reality_array))
    tuic_array = list(set(tuic_array))
    hysteria_array = list(set(hysteria_array))
    juicity_array = list(set(juicity_array))

    if vmess_decode_dedup:
        # Decode vmess configs to change title and remove duplicate
        for index, element in enumerate(vmess_array):
            vmess_array[index] = decode_vmess(element)
        vmess_array = [config for config in vmess_array if config != None]
        vmess_array = list(set(vmess_array))

    return shadow_array, trojan_array, vmess_array, vless_array, reality_array, tuic_array, hysteria_array, juicity_array


def modify_config(shadow_array, trojan_array, vmess_array, vless_array, reality_array, tuic_array, hysteria_array, check_port_connection = True):
    # Checkout connectivity and modify title and protocol type address and resolve IP address
    shadow_array, shadow_tls_array, shadow_non_tls_array, shadow_tcp_array, shadow_ws_array, shadow_http_array, shadow_grpc_array = check_modify_config(array_configuration = shadow_array, protocol_type = "SHADOWSOCKS", check_connection = check_port_connection)
    trojan_array, trojan_tls_array, trojan_non_tls_array, trojan_tcp_array, trojan_ws_array, trojan_http_array, trojan_grpc_array = check_modify_config(array_configuration = trojan_array, protocol_type = "TROJAN", check_connection = check_port_connection)
    vmess_array, vmess_tls_array, vmess_non_tls_array, vmess_tcp_array, vmess_ws_array, vmess_http_array, vmess_grpc_array = check_modify_config(array_configuration = vmess_array, protocol_type = "VMESS", check_connection = check_port_connection)
    vless_array, vless_tls_array, vless_non_tls_array, vless_tcp_array, vless_ws_array, vless_http_array, vless_grpc_array = check_modify_config(array_configuration = vless_array, protocol_type = "VLESS", check_connection = check_port_connection)
    reality_array, reality_tls_array, reality_non_tls_array, reality_tcp_array, reality_ws_array, reality_http_array, reality_grpc_array = check_modify_config(array_configuration = reality_array, protocol_type = "REALITY", check_connection = check_port_connection)
    tuic_array, _, _, _, _, _, _ = check_modify_config(array_configuration = tuic_array, protocol_type = "TUIC", check_connection = False)
    hysteria_array, _, _, _, _, _, _ = check_modify_config(array_configuration = hysteria_array, protocol_type = "HYSTERIA", check_connection = False)

    # Initialize security and netowrk array
    tls_array = list()
    non_tls_array = list()

    tcp_array = list()
    ws_array = list()
    http_array = list()
    grpc_array = list()

    for array in [shadow_tls_array, trojan_tls_array, vmess_tls_array, vless_tls_array, reality_tls_array]:
        tls_array.extend(array)
    for array in [shadow_non_tls_array, trojan_non_tls_array, vmess_non_tls_array, vless_non_tls_array, reality_non_tls_array]:
        non_tls_array.extend(array)

    for array in [shadow_tcp_array, trojan_tcp_array, vmess_tcp_array, vless_tcp_array, reality_tcp_array]:
        tcp_array.extend(array)
    for array in [shadow_ws_array, trojan_ws_array, vmess_ws_array, vless_ws_array, reality_ws_array]:
        ws_array.extend(array)
    for array in [shadow_http_array, trojan_http_array, vmess_http_array, vless_http_array, reality_http_array]:
        http_array.extend(array)
    for array in [shadow_grpc_array, trojan_grpc_array, vmess_grpc_array, vless_grpc_array, reality_grpc_array]:
        grpc_array.extend(array)

    return shadow_array, trojan_array, vmess_array, vless_array, reality_array, tuic_array, hysteria_array, tls_array, non_tls_array, tcp_array, ws_array, http_array, grpc_array


# Remove Duplicate Configurations
configs_list_array = [array_shadowsocks, array_trojan, array_vmess, array_vless, array_reality, array_tuic, array_hysteria, matches_shadowsocks, matches_trojan, matches_vmess, matches_vless, matches_reality, matches_tuic, matches_hysteria, raw_matches_shadowsocks, raw_matches_trojan, raw_matches_vmess, raw_matches_vless, raw_matches_reality, raw_matches_tuic, raw_matches_hysteria, channel_matches_shadowsocks, channel_matches_trojan, channel_matches_vmess, channel_matches_vless, channel_matches_reality, channel_matches_tuic, channel_matches_hysteria]
array_removed_duplicate_list_configurations = list()

for array in configs_list_array:
    print(f"Before Removing Duplicates : {len(array)}", end = '\t')
    array = remove_duplicate_modified(array)
    print(f"After Removing Duplicates : {len(array)}")
    array_removed_duplicate_list_configurations.append(array)

# Dedicate removed array of the list of elements
array_shadowsocks, array_trojan, array_vmess, array_vless, array_reality, array_tuic, array_hysteria, matches_shadowsocks, matches_trojan, matches_vmess, matches_vless, matches_reality, matches_tuic, matches_hysteria, raw_matches_shadowsocks, raw_matches_trojan, raw_matches_vmess, raw_matches_vless, raw_matches_reality, raw_matches_tuic, raw_matches_hysteria, channel_matches_shadowsocks, channel_matches_trojan, channel_matches_vmess, channel_matches_vless, channel_matches_reality, channel_matches_tuic, channel_matches_hysteria = array_removed_duplicate_list_configurations


# Remove duplicate configurations of telegram channels and subscription links contents
array_shadowsocks, array_trojan, array_vmess, array_vless, array_reality, array_tuic, array_hysteria, array_juicity = remove_duplicate(array_shadowsocks, array_trojan, array_vmess, array_vless, array_reality, array_tuic, array_hysteria, array_juicity)
matches_shadowsocks, matches_trojan, matches_vmess, matches_vless, matches_reality, matches_tuic, matches_hysteria, matches_juicity = remove_duplicate(matches_shadowsocks, matches_trojan, matches_vmess, matches_vless, matches_reality, matches_tuic, matches_hysteria, matches_juicity)
raw_matches_shadowsocks, raw_matches_trojan, raw_matches_vmess, raw_matches_vless, raw_matches_reality, raw_matches_tuic, raw_matches_hysteria, raw_matches_juicity = remove_duplicate(raw_matches_shadowsocks, raw_matches_trojan, raw_matches_vmess, raw_matches_vless, raw_matches_reality, raw_matches_tuic, raw_matches_hysteria, raw_matches_juicity)
channel_matches_shadowsocks, channel_matches_trojan, channel_matches_vmess, channel_matches_vless, channel_matches_reality, channel_matches_tuic, channel_matches_hysteria, channel_matches_juicity = remove_duplicate(channel_matches_shadowsocks, channel_matches_trojan, channel_matches_vmess, channel_matches_vless, channel_matches_reality, channel_matches_tuic, channel_matches_hysteria, channel_matches_juicity)

# Checkout connectivity and modify title and protocol type address and resolve IP address
array_shadowsocks, array_trojan, array_vmess, array_vless, array_reality,  array_tuic, array_hysteria, array_tls, array_non_tls, array_tcp, array_ws, array_http, array_grpc = modify_config(array_shadowsocks, array_trojan, array_vmess, array_vless, array_reality, array_tuic, array_hysteria)
matches_shadowsocks, matches_trojan, matches_vmess, matches_vless, matches_reality, matches_tuic, matches_hysteria, matches_tls, matches_non_tls, matches_tcp, matches_ws, matches_http, matches_grpc = modify_config(matches_shadowsocks, matches_trojan, matches_vmess, matches_vless, matches_reality, matches_tuic, matches_hysteria)
raw_matches_shadowsocks, raw_matches_trojan, raw_matches_vmess, raw_matches_vless, raw_matches_reality, raw_matches_tuic, raw_matches_hysteria, raw_matches_tls, raw_matches_non_tls, raw_matches_tcp, raw_matches_ws, raw_matches_http, raw_matches_grpc = modify_config(raw_matches_shadowsocks, raw_matches_trojan, raw_matches_vmess, raw_matches_vless, raw_matches_reality, raw_matches_tuic, raw_matches_hysteria, check_port_connection = False)
channel_matches_shadowsocks, channel_matches_trojan, channel_matches_vmess, channel_matches_vless, channel_matches_reality, channel_matches_tuic, channel_matches_hysteria, channel_matches_tls, channel_matches_non_tls, channel_matches_tcp, channel_matches_ws, channel_matches_http, channel_matches_grpc = modify_config(channel_matches_shadowsocks, channel_matches_trojan, channel_matches_vmess, channel_matches_vless, channel_matches_reality, channel_matches_tuic, channel_matches_hysteria, check_port_connection = True)


# Extend channel subscription links contents to telegram channel contents
array_shadowsocks_channels = array_shadowsocks
array_trojan_channels = array_trojan
array_vmess_channels = array_vmess
array_vless_channels = array_vless
array_reality_channels = array_reality
array_tuic_channels = array_tuic
array_hysteria_channels = array_hysteria
array_juicity_channels = array_juicity

array_shadowsocks_channels.extend(channel_matches_shadowsocks)
array_trojan_channels.extend(channel_matches_trojan)
array_vmess_channels.extend(channel_matches_vmess)
array_vless_channels.extend(channel_matches_vless)
array_reality_channels.extend(channel_matches_reality)
array_tuic_channels.extend(channel_matches_tuic)
array_hysteria_channels.extend(channel_matches_hysteria)
array_juicity_channels.extend(channel_matches_juicity)

# Remove duplicate configurations after modifying telegram channels and subscription links contents
array_shadowsocks_channels, array_trojan_channels, array_vmess_channels, array_vless_channels, array_reality_channels, array_tuic_channels, array_hysteria_channels, array_juicity_channels = remove_duplicate(array_shadowsocks_channels, array_trojan_channels, array_vmess_channels, array_vless_channels, array_reality_channels, array_tuic_channels, array_hysteria_channels, array_juicity_channels, vmess_decode_dedup = False)
channel_matches_shadowsocks, channel_matches_trojan, channel_matches_vmess, channel_matches_vless, channel_matches_reality, channel_matches_tuic, channel_matches_hysteria, channel_matches_juicity = remove_duplicate(channel_matches_shadowsocks, channel_matches_trojan, channel_matches_vmess, channel_matches_vless, channel_matches_reality, channel_matches_tuic, channel_matches_hysteria, channel_matches_juicity, vmess_decode_dedup = False)

# Extend channel subscription links contents to telegram channel contents based on networks and security
array_tls_channels = array_tls
array_non_tls_channels = array_non_tls
array_tcp_channels = array_tcp
array_ws_channels = array_ws
array_http_channels = array_http
array_grpc_channels = array_grpc

array_tls_channels.extend(channel_matches_tls)
array_non_tls_channels.extend(channel_matches_non_tls)
array_tcp_channels.extend(channel_matches_tcp)
array_ws_channels.extend(channel_matches_ws)
array_http_channels.extend(channel_matches_http)
array_grpc_channels.extend(channel_matches_grpc)

array_tls_channels = list(set(array_tls_channels))
array_non_tls_channels = list(set(array_non_tls_channels))
array_tcp_channels = list(set(array_tcp_channels))
array_ws_channels = list(set(array_ws_channels))
array_http_channels = list(set(array_http_channels))
array_grpc_channels = list(set(array_grpc_channels))


# Extend subscription links contents to telegram channel contents
array_shadowsocks.extend(matches_shadowsocks)
array_trojan.extend(matches_trojan)
array_vmess.extend(matches_vmess)
array_vless.extend(matches_vless)
array_reality.extend(matches_reality)
array_tuic.extend(matches_tuic)
array_hysteria.extend(matches_hysteria)
array_juicity.extend(matches_juicity)

# Remove duplicate configurations after modifying telegram channels and subscription links contents
array_shadowsocks, array_trojan, array_vmess, array_vless, array_reality, array_tuic, array_hysteria, array_juicity = remove_duplicate(array_shadowsocks, array_trojan, array_vmess, array_vless, array_reality, array_tuic, array_hysteria, array_juicity, vmess_decode_dedup = False)
matches_shadowsocks, matches_trojan, matches_vmess, matches_vless, matches_reality, matches_tuic, matches_hysteria, matches_juicity = remove_duplicate(matches_shadowsocks, matches_trojan, matches_vmess, matches_vless, matches_reality, matches_tuic, matches_hysteria, matches_juicity, vmess_decode_dedup = False)
raw_matches_shadowsocks, raw_matches_trojan, raw_matches_vmess, raw_matches_vless, raw_matches_reality, raw_matches_tuic, raw_matches_hysteria, raw_matches_juicity = remove_duplicate(raw_matches_shadowsocks, raw_matches_trojan, raw_matches_vmess, raw_matches_vless, raw_matches_reality, raw_matches_tuic, raw_matches_hysteria, raw_matches_juicity, vmess_decode_dedup = False)

# Extend subscription links contents to telegram channel contents
array_tls.extend(matches_tls)
array_non_tls.extend(matches_non_tls)
array_tcp.extend(matches_tcp)
array_ws.extend(matches_ws)
array_http.extend(matches_http)
array_grpc.extend(matches_grpc)

# Remove duplicate configurations after modifying telegram channels and subscription links contents
array_tls = list(set(array_tls))
array_non_tls = list(set(array_non_tls))
array_tcp = list(set(array_tcp))
array_ws = list(set(array_ws))
array_http = list(set(array_http))
array_grpc = list(set(array_grpc))

raw_matches_tls = list(set(raw_matches_tls))
raw_matches_non_tls = list(set(raw_matches_non_tls))
raw_matches_tcp = list(set(raw_matches_tcp))
raw_matches_ws = list(set(raw_matches_ws))
raw_matches_http = list(set(raw_matches_http))
raw_matches_grpc = list(set(raw_matches_grpc))


# Remove Duplicate Configurations
array_list_configurations = [array_shadowsocks, array_trojan, array_vmess, array_vless, array_reality, array_tuic, array_hysteria, matches_shadowsocks, matches_trojan, matches_vmess, matches_vless, matches_reality, matches_tuic, matches_hysteria, raw_matches_shadowsocks, raw_matches_trojan, raw_matches_vmess, raw_matches_vless, raw_matches_reality, raw_matches_tuic, raw_matches_hysteria, channel_matches_shadowsocks, channel_matches_trojan, channel_matches_vmess, channel_matches_vless, channel_matches_reality, channel_matches_tuic, channel_matches_hysteria]
array_removed_duplicate_list_configurations = list()

for array in array_list_configurations:
    print(f"Before Removing Duplicates : {len(array)}", end = '\t')
    array = remove_duplicate_modified(array)
    print(f"After Removing Duplicates : {len(array)}")
    array_removed_duplicate_list_configurations.append(array)

# Dedicate removed array of the list of elements 
array_shadowsocks, array_trojan, array_vmess, array_vless, array_reality, array_tuic, array_hysteria, matches_shadowsocks, matches_trojan, matches_vmess, matches_vless, matches_reality, matches_tuic, matches_hysteria, raw_matches_shadowsocks, raw_matches_trojan, raw_matches_vmess, raw_matches_vless, raw_matches_reality, raw_matches_tuic, raw_matches_hysteria, channel_matches_shadowsocks, channel_matches_trojan, channel_matches_vmess, channel_matches_vless, channel_matches_reality, channel_matches_tuic, channel_matches_hysteria = array_removed_duplicate_list_configurations


# Combine all configurations into one mixed configuration array and shuffle
array_mixed = array_shadowsocks + array_trojan + array_vmess + array_vless + array_reality

# Define chunk size for splitted arrays
chunk_size = math.ceil(len(array_mixed)/10)
chunks = list()

# Split and get chunks of mixed configurations array 
for i in range(0, len(array_mixed), chunk_size):
    chunk = array_mixed[i : i + chunk_size]
    chunks.append(chunk)


def create_title(title, port):
    uuid_ranks = ['abcabca','abca','abca','abcd','abcabcabcabc']
    for index, value in enumerate(uuid_ranks):
        char_value = list(value)
        random.shuffle(char_value)
        uuid_ranks[index] = ''.join(char_value)

    uuid = '-'.join(uuid_ranks)

    # Define configurations based on protocol
    reality_config_title = f"vless://{uuid}@127.0.0.1:{port}?security=tls&type=tcp#{title}"
    vless_config_title = f"vless://{uuid}@127.0.0.1:{port}?security=tls&type=tcp#{title}"
    vmess_config_title = {"add":"127.0.0.1","aid":"0","host":"","id":uuid,"net":"tcp","path":"",
                          "port":port,"ps":title,"scy":"auto","sni":"","tls":"","type":"","v":"2"}
    vmess_config_title = json.dumps(vmess_config_title)
    vmess_config_title = base64.b64encode(vmess_config_title.encode('utf-8')).decode('utf-8')
    vmess_config_title = f'vmess://{vmess_config_title}'
    trojan_config_title = f"trojan://{uuid}@127.0.0.1:{port}?security=tls&type=tcp#{title}"
    shadowsocs_uuid = base64.b64encode(f"none:{uuid}".encode('utf-8')).decode('utf-8')
    shadowsocks_config_title = f"ss://{shadowsocs_uuid}@127.0.0.1:{port}#{title}"

    return reality_config_title, vless_config_title, vmess_config_title, trojan_config_title, shadowsocks_config_title


# Define update date and time based on Iran timezone and calendar
datetime_update = jdatetime.datetime.now(tz = timezone(timedelta(hours = 3, minutes = 30)))
datetime_update_str = datetime_update.strftime("\U0001F504 LATEST-UPDATE \U0001F4C5 %a-%d-%B-%Y \U0001F551 %H:%M").upper()
# Define update time based on protocol type
reality_update, vless_update, vmess_update, trojan_update, shadowsocks_update = create_title(datetime_update_str, port = 1080)

# Define develooper sign
dev_sign = "\U0001F468\U0001F3FB\u200D\U0001F4BB DEVELOPED-BY SOROUSH-MIRZAEI \U0001F4CC FOLLOW-CONTACT SYDSRSMRZ"
# Define develooper based on protocol type
reality_dev_sign, vless_dev_sign, vmess_dev_sign, trojan_dev_sign, shadowsocks_dev_sign = create_title(dev_sign, port = 8080)

# Define Advertisement row
adv_bool = True
adv_sign = "\U0001F916 TELEGRAM-CHANNEL \U0001F4A1 NEUROVANCE \U0001F9E0"
# Define develooper based on protocol type
reality_adv_sign, vless_adv_sign, vmess_adv_sign, trojan_adv_sign, shadowsocks_adv_sign = create_title(adv_sign, port = 2080)


# Save configurations based on splitted and chunks
for i in range(0, 10):
    if i < len(chunks):
        with open(f"./splitted/mixed-{i}", "w", encoding="utf-8") as file:
            chunks[i].insert(0, trojan_update)
            if adv_bool:
                chunks[i].insert(1, trojan_adv_sign)
            chunks[i].append(trojan_dev_sign)
            file.write(base64.b64encode("\n".join(chunks[i]).encode("utf-8")).decode("utf-8"))
    else:
        with open(f"./splitted/mixed-{i}", "w", encoding="utf-8") as file:
            file.write("")


# Create dictionary type of country based configuration list 
country_based_configs_dict = create_country(array_mixed)

for country in country_based_configs_dict.keys():
    country_based_configs_dict[country].insert(0, trojan_update)
    if adv_bool:
        country_based_configs_dict[country].insert(1, trojan_adv_sign)
    country_based_configs_dict[country].append(trojan_dev_sign)
    if not os.path.exists('./countries'):
        os.mkdir('./countries')
    if not os.path.exists(f'./countries/{country}'):
        os.mkdir(f'./countries/{country}')
    with open(f'./countries/{country}/mixed', "w", encoding="utf-8") as file:
        file.write(base64.b64encode("\n".join(country_based_configs_dict[country]).encode("utf-8")).decode("utf-8"))


# Split and save mixed array based on internet protocol
array_mixed_ipv4, array_mixed_ipv6 = create_internet_protocol(array_mixed)
with open("./layers/ipv4", "w", encoding="utf-8") as file:
    array_mixed_ipv4.insert(0, trojan_update)
    if adv_bool:
        array_mixed_ipv4.insert(1, trojan_adv_sign)
    array_mixed_ipv4.append(trojan_dev_sign)
    file.write(base64.b64encode("\n".join(array_mixed_ipv4).encode("utf-8")).decode("utf-8"))

with open("./layers/ipv6", "w", encoding="utf-8") as file:
    array_mixed_ipv6.insert(0, trojan_update)
    if adv_bool:
        array_mixed_ipv6.insert(1, trojan_adv_sign)
    array_mixed_ipv6.append(trojan_dev_sign)
    file.write(base64.b64encode("\n".join(array_mixed_ipv6).encode("utf-8")).decode("utf-8"))


# Save all mixed array and subscription links content
with open("./splitted/mixed", "w", encoding="utf-8") as file:
    array_mixed.insert(0, trojan_update)
    if adv_bool:
        array_mixed.insert(1, trojan_adv_sign)
    array_mixed.append(trojan_dev_sign)
    file.write(base64.b64encode("\n".join(array_mixed).encode("utf-8")).decode("utf-8"))


# Decode vmess configs to change title and remove duplicate
all_subscription_matches = matches_shadowsocks + matches_trojan + matches_vmess + matches_vless + matches_reality
all_subscription_matches = list(set(all_subscription_matches))

# Split and save mixed array based on internet protocol
array_subscription_ipv4, array_subscription_ipv6 = create_internet_protocol(all_subscription_matches)
with open("./subscribe/layers/ipv4", "w", encoding="utf-8") as file:
    array_subscription_ipv4.insert(0, trojan_update)
    if adv_bool:
        array_subscription_ipv4.insert(1, trojan_adv_sign)
    array_subscription_ipv4.append(trojan_dev_sign)
    file.write(base64.b64encode("\n".join(array_subscription_ipv4).encode("utf-8")).decode("utf-8"))

with open("./subscribe/layers/ipv6", "w", encoding="utf-8") as file:
    array_subscription_ipv6.insert(0, trojan_update)
    if adv_bool:
        array_subscription_ipv6.insert(1, trojan_adv_sign)
    array_subscription_ipv6.append(trojan_dev_sign)
    file.write(base64.b64encode("\n".join(array_subscription_ipv6).encode("utf-8")).decode("utf-8"))

# Save subscription configurations file
with open("./splitted/subscribe", "w", encoding="utf-8") as file:
    all_subscription_matches.insert(0, trojan_update)
    if adv_bool:
        all_subscription_matches.insert(1, trojan_adv_sign)
    all_subscription_matches.append(trojan_dev_sign)
    file.write(base64.b64encode("\n".join(all_subscription_matches).encode("utf-8")).decode("utf-8"))


# Decode vmess configs to change title and remove duplicate
all_channel_matches = array_shadowsocks_channels + array_trojan_channels + array_vmess_channels + array_vless_channels + array_reality_channels
all_channel_matches = list(set(all_channel_matches))

# Split and save mixed array based on internet protocol
array_channel_ipv4, array_channel_ipv6 = create_internet_protocol(all_channel_matches)
with open("./channels/layers/ipv4", "w", encoding="utf-8") as file:
    array_channel_ipv4.insert(0, trojan_update)
    if adv_bool:
        array_channel_ipv4.insert(1, trojan_adv_sign)
    array_channel_ipv4.append(trojan_dev_sign)
    file.write(base64.b64encode("\n".join(array_channel_ipv4).encode("utf-8")).decode("utf-8"))

with open("./channels/layers/ipv6", "w", encoding="utf-8") as file:
    array_channel_ipv6.insert(0, trojan_update)
    if adv_bool:
        array_channel_ipv6.insert(1, trojan_adv_sign)
    array_channel_ipv6.append(trojan_dev_sign)
    file.write(base64.b64encode("\n".join(array_channel_ipv6).encode("utf-8")).decode("utf-8"))

# Save channel configurations file
with open("./splitted/channels", "w", encoding="utf-8") as file:
    all_channel_matches.insert(0, trojan_update)
    if adv_bool:
        all_channel_matches.insert(1, trojan_adv_sign)
    all_channel_matches.append(trojan_dev_sign)
    file.write(base64.b64encode("\n".join(all_channel_matches).encode("utf-8")).decode("utf-8"))


array_shadowsocks.insert(0, shadowsocks_update)
array_trojan.insert(0, trojan_update)
array_vmess.insert(0, vmess_update)
array_vless.insert(0, vless_update)
array_reality.insert(0, reality_update)
array_tuic.insert(0, vless_update)
array_hysteria.insert(0, vless_update)
array_juicity.insert(0, vless_update)

if adv_bool:
    array_shadowsocks.insert(1, shadowsocks_adv_sign)
    array_trojan.insert(1, trojan_adv_sign)
    array_vmess.insert(1, vmess_adv_sign)
    array_vless.insert(1, vless_adv_sign)
    array_reality.insert(1, reality_adv_sign)
    array_tuic.insert(1, vless_adv_sign)
    array_hysteria.insert(1, vless_adv_sign)
    array_juicity.insert(1, vless_adv_sign)

array_shadowsocks.append(shadowsocks_dev_sign)
array_trojan.append(trojan_dev_sign)
array_vmess.append(vmess_dev_sign)
array_vless.append(vless_dev_sign)
array_reality.append(reality_dev_sign)
array_tuic.append(vless_dev_sign)
array_hysteria.append(vless_dev_sign)
array_juicity.append(vless_dev_sign)

# Save configurations into files splitted based on configuration type
with open("./protocols/shadowsocks", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_shadowsocks).encode("utf-8")).decode("utf-8"))
with open("./protocols/trojan", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_trojan).encode("utf-8")).decode("utf-8"))
with open("./protocols/vmess", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_vmess).encode("utf-8")).decode("utf-8"))
with open("./protocols/vless", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_vless).encode("utf-8")).decode("utf-8"))
with open("./protocols/reality", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_reality).encode("utf-8")).decode("utf-8"))
with open("./protocols/tuic", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_tuic).encode("utf-8")).decode("utf-8"))
with open("./protocols/hysteria", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_hysteria).encode("utf-8")).decode("utf-8"))
with open("./protocols/juicity", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_juicity).encode("utf-8")).decode("utf-8"))

array_tls.insert(0, vless_update)
array_non_tls.insert(0, vless_update)
array_tcp.insert(0, vless_update)
array_ws.insert(0, vless_update)
array_http.insert(0, vless_update)
array_grpc.insert(0, vless_update)

if adv_bool:
    array_tls.insert(1, vless_adv_sign)
    array_non_tls.insert(1, vless_adv_sign)
    array_tcp.insert(1, vless_adv_sign)
    array_ws.insert(1, vless_adv_sign)
    array_http.insert(1, vless_adv_sign)
    array_grpc.insert(1, vless_adv_sign)

array_tls.append(vless_dev_sign)
array_non_tls.append(vless_dev_sign)
array_tcp.append(vless_dev_sign)
array_ws.append(vless_dev_sign)
array_http.append(vless_dev_sign)
array_grpc.append(vless_dev_sign)

# Save configurations into files splitted based on configuration type
with open("./security/tls", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_tls).encode("utf-8")).decode("utf-8"))
with open("./security/non-tls", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_non_tls).encode("utf-8")).decode("utf-8"))
with open("./networks/tcp", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_tcp).encode("utf-8")).decode("utf-8"))
with open("./networks/ws", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_ws).encode("utf-8")).decode("utf-8"))
with open("./networks/http", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_http).encode("utf-8")).decode("utf-8"))
with open("./networks/grpc", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_grpc).encode("utf-8")).decode("utf-8"))


raw_matches_shadowsocks.insert(0, shadowsocks_update)
raw_matches_trojan.insert(0, trojan_update)
raw_matches_vmess.insert(0, vmess_update)
raw_matches_vless.insert(0, vless_update)
raw_matches_reality.insert(0, reality_update)
raw_matches_tuic.insert(0, vless_update)
raw_matches_hysteria.insert(0, vless_update)
raw_matches_juicity.insert(0, vless_update)

if adv_bool:
    raw_matches_shadowsocks.insert(1, shadowsocks_adv_sign)
    raw_matches_trojan.insert(1, trojan_adv_sign)
    raw_matches_vmess.insert(1, vmess_adv_sign)
    raw_matches_vless.insert(1, vless_adv_sign)
    raw_matches_reality.insert(1, reality_adv_sign)
    raw_matches_tuic.insert(1, vless_adv_sign)
    raw_matches_hysteria.insert(1, vless_adv_sign)
    raw_matches_juicity.insert(1, vless_adv_sign)

raw_matches_shadowsocks.append(shadowsocks_dev_sign)
raw_matches_trojan.append(trojan_dev_sign)
raw_matches_vmess.append(vmess_dev_sign)
raw_matches_vless.append(vless_dev_sign)
raw_matches_reality.append(reality_dev_sign)
raw_matches_tuic.append(vless_dev_sign)
raw_matches_hysteria.append(vless_dev_sign)
raw_matches_juicity.append(vless_dev_sign)

# Save configurations into files splitted based on configuration type
with open("./subscribe/protocols/shadowsocks", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(raw_matches_shadowsocks).encode("utf-8")).decode("utf-8"))
with open("./subscribe/protocols/trojan", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(raw_matches_trojan).encode("utf-8")).decode("utf-8"))
with open("./subscribe/protocols/vmess", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(raw_matches_vmess).encode("utf-8")).decode("utf-8"))
with open("./subscribe/protocols/vless", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(raw_matches_vless).encode("utf-8")).decode("utf-8"))
with open("./subscribe/protocols/reality", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(raw_matches_reality).encode("utf-8")).decode("utf-8"))
with open("./subscribe/protocols/tuic", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(raw_matches_tuic).encode("utf-8")).decode("utf-8"))
with open("./subscribe/protocols/hysteria", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(raw_matches_hysteria).encode("utf-8")).decode("utf-8"))
with open("./subscribe/protocols/juicity", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(raw_matches_juicity).encode("utf-8")).decode("utf-8"))


raw_matches_tls.insert(0, vless_update)
raw_matches_non_tls.insert(0, vless_update)
raw_matches_tcp.insert(0, vless_update)
raw_matches_ws.insert(0, vless_update)
raw_matches_http.insert(0, vless_update)
raw_matches_grpc.insert(0, vless_update)

if adv_bool:
    raw_matches_tls.insert(1, vless_adv_sign)
    raw_matches_non_tls.insert(1, vless_adv_sign)
    raw_matches_tcp.insert(1, vless_adv_sign)
    raw_matches_ws.insert(1, vless_adv_sign)
    raw_matches_http.insert(1, vless_adv_sign)
    raw_matches_grpc.insert(1, vless_adv_sign)

raw_matches_tls.append(vless_dev_sign)
raw_matches_non_tls.append(vless_dev_sign)
raw_matches_tcp.append(vless_dev_sign)
raw_matches_ws.append(vless_dev_sign)
raw_matches_http.append(vless_dev_sign)
raw_matches_grpc.append(vless_dev_sign)

# Save configurations into files splitted based on configuration type
with open("./subscribe/security/tls", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(raw_matches_tls).encode("utf-8")).decode("utf-8"))
with open("./subscribe/security/non-tls", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(raw_matches_non_tls).encode("utf-8")).decode("utf-8"))
with open("./subscribe/networks/tcp", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(raw_matches_tcp).encode("utf-8")).decode("utf-8"))
with open("./subscribe/networks/ws", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(raw_matches_ws).encode("utf-8")).decode("utf-8"))
with open("./subscribe/networks/http", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(raw_matches_http).encode("utf-8")).decode("utf-8"))
with open("./subscribe/networks/grpc", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(raw_matches_grpc).encode("utf-8")).decode("utf-8"))

array_shadowsocks_channels.insert(0, shadowsocks_update)
array_trojan_channels.insert(0, trojan_update)
array_vmess_channels.insert(0, vmess_update)
array_vless_channels.insert(0, vless_update)
array_reality_channels.insert(0, reality_update)
array_tuic_channels.insert(0, vless_update)
array_hysteria_channels.insert(0, vless_update)
array_juicity_channels.insert(0, vless_update)

if adv_bool:
    array_shadowsocks_channels.insert(1, shadowsocks_adv_sign)
    array_trojan_channels.insert(1, trojan_adv_sign)
    array_vmess_channels.insert(1, vmess_adv_sign)
    array_vless_channels.insert(1, vless_adv_sign)
    array_reality_channels.insert(1, reality_adv_sign)
    array_tuic_channels.insert(1, vless_adv_sign)
    array_hysteria_channels.insert(1, vless_adv_sign)
    array_juicity_channels.insert(1, vless_adv_sign)

array_shadowsocks_channels.append(shadowsocks_dev_sign)
array_trojan_channels.append(trojan_dev_sign)
array_vmess_channels.append(vmess_dev_sign)
array_vless_channels.append(vless_dev_sign)
array_reality_channels.append(reality_dev_sign)
array_tuic_channels.append(vless_dev_sign)
array_hysteria_channels.append(vless_dev_sign)
array_juicity_channels.append(vless_dev_sign)

# Save configurations into files splitted based on configuration type
with open("./channels/protocols/shadowsocks", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_shadowsocks_channels).encode("utf-8")).decode("utf-8"))
with open("./channels/protocols/trojan", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_trojan_channels).encode("utf-8")).decode("utf-8"))
with open("./channels/protocols/vmess", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_vmess_channels).encode("utf-8")).decode("utf-8"))
with open("./channels/protocols/vless", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_vless_channels).encode("utf-8")).decode("utf-8"))
with open("./channels/protocols/reality", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_reality_channels).encode("utf-8")).decode("utf-8"))
with open("./channels/protocols/tuic", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_tuic_channels).encode("utf-8")).decode("utf-8"))
with open("./channels/protocols/hysteria", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_hysteria_channels).encode("utf-8")).decode("utf-8"))
with open("./channels/protocols/juicity", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_juicity_channels).encode("utf-8")).decode("utf-8"))


array_tls_channels.insert(0, vless_update)
array_non_tls_channels.insert(0, vless_update)
array_tcp_channels.insert(0, vless_update)
array_ws_channels.insert(0, vless_update)
array_http_channels.insert(0, vless_update)
array_grpc_channels.insert(0, vless_update)

if adv_bool:
    array_tls_channels.insert(1, vless_adv_sign)
    array_non_tls_channels.insert(1, vless_adv_sign)
    array_tcp_channels.insert(1, vless_adv_sign)
    array_ws_channels.insert(1, vless_adv_sign)
    array_http_channels.insert(1, vless_adv_sign)
    array_grpc_channels.insert(1, vless_adv_sign)

array_tls_channels.append(vless_dev_sign)
array_non_tls_channels.append(vless_dev_sign)
array_tcp_channels.append(vless_dev_sign)
array_ws_channels.append(vless_dev_sign)
array_http_channels.append(vless_dev_sign)
array_grpc_channels.append(vless_dev_sign)

# Save configurations into files splitted based on configuration type
with open("./channels/security/tls", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_tls_channels).encode("utf-8")).decode("utf-8"))
with open("./channels/security/non-tls", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_non_tls_channels).encode("utf-8")).decode("utf-8"))
with open("./channels/networks/tcp", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_tcp_channels).encode("utf-8")).decode("utf-8"))
with open("./channels/networks/ws", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_ws_channels).encode("utf-8")).decode("utf-8"))
with open("./channels/networks/http", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_http_channels).encode("utf-8")).decode("utf-8"))
with open("./channels/networks/grpc", "w", encoding="utf-8") as file:
    file.write(base64.b64encode("\n".join(array_grpc_channels).encode("utf-8")).decode("utf-8"))


readme = '''## Introduction
The script systematically collects Vmess, Vless, ShadowSocks, Trojan, Reality, Hysteria, Tuic, and Juicity configurations from publicly accessible Telegram channels. It categorizes these configurations based on open and closed ports, eliminates duplicate entries, resolves configuration addresses using IP addresses, and revises configuration titles to reflect server and protocol-type properties. These properties include network and security type, IP address and port, and the respective country associated with the configuration.

![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/soroushmirzaei/telegram-configs-collector?label=Last%20Commit&color=%2338914b)
![GitHub](https://img.shields.io/github/license/soroushmirzaei/telegram-configs-collector?label=License&color=yellow)
![GitHub Repo stars](https://img.shields.io/github/stars/soroushmirzaei/telegram-configs-collector?label=Stars&color=red&style=flat)
![GitHub forks](https://img.shields.io/github/forks/soroushmirzaei/telegram-configs-collector?label=Forks&color=blue&style=flat)
[![Execute On Schedule](https://github.com/soroushmirzaei/telegram-configs-collector/actions/workflows/schedule.yml/badge.svg)](https://github.com/soroushmirzaei/telegram-configs-collector/actions/workflows/schedule.yml)
[![Execute On Push](https://github.com/soroushmirzaei/telegram-configs-collector/actions/workflows/push.yml/badge.svg)](https://github.com/soroushmirzaei/telegram-configs-collector/actions/workflows/push.yml)

## Tutorial
This is a guide for configuring domains by routing type in the `nekoray` and `nekobox` applications when using the `sing-box` core. To implement these domain settings, create new routes in either application and add the appropriate domains to the relevant `domains` section. Configure the outbound setting as `bypass`, `proxy`, or `block` according to the specifications provided for each domain category.

- Bypass
```
geosite:category-ir
geosite:category-bank-ir
geosite:category-bourse-ir
geosite:category-education-ir
geosite:category-forums-ir
geosite:category-gov-ir
geosite:category-insurance-ir
geosite:category-media-ir
geosite:category-news-ir
geosite:category-payment-ir
geosite:category-scholar-ir
geosite:category-shopping-ir
geosite:category-social-media-ir
geosite:category-tech-ir
geosite:category-travel-ir
```

- Proxy
```
geosite:apple
geosite:adobe
geosite:anthropic
geosite:openai
geosite:clubhouse
geosite:netflix
geosite:nvidia
geosite:intel
geosite:amd
geosite:signal
geosite:soundcloud
geosite:youtube
geosite:telegram
geosite:twitter
geosite:instagram
geosite:facebook
geosite:pinterest
geosite:tiktok
geosite:spotify
geosite:twitch
geosite:discord
```

- Block
```
geosite:category-ads-all
geosite:category-ads-ir
geosite:google-ads
geosite:spotify-ads
geosite:adobe-ads
geosite:apple-ads
```

## Protocol Type Subscription Links
Subscription links for configurations are organized according to protocol type and categorized into separate Telegram channels and subscription links. These links provide access to configurations based on specific protocol requirements.
| **Protocol Type** | **Mixed Configurations** | **Telegram Channels** | **Subscription Links** |
|:---:|:---:|:---:|:---:|
| **Juicity Configurations** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/juicity) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/juicity) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/juicity) |
| **Hysteria Configurations** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/hysteria) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/hysteria) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/hysteria) |
| **Tuic Configurations** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/tuic) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/tuic) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/tuic) |
| **Reality Configurations** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/reality) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/reality) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/reality) |
| **Vless Configurations** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vless) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/vless) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/vless) |
| **Vmess Configurations** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vmess) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/vmess) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/vmess) |
| **Trojan Configurations** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/trojan) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/trojan) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/trojan) |
| **Shadowsocks Configurations** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/shadowsocks) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/shadowsocks) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/shadowsocks) |
| **Mixed Type Configurations** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/splitted/mixed) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/splitted/channels) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/splitted/subscribe) |

## Network Type Subscription Links
Subscription links for configurations are organized according to network type and categorized into separate Telegram channels and subscription links. These links facilitate access to configurations optimized for specific network architectures.
| **Network Type** | **Mixed Configurations** | **Telegram Channels** | **Subscription Links** |
|:---:|:---:|:---:|:---:|
| **Google Remote Procedure Call (GRPC)** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/networks/grpc) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/networks/grpc) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/networks/grpc) |
| **Hypertext Transfer Protocol (HTTP)** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/networks/http) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/networks/http) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/networks/http) |
| **WebSocket Protocol (WS)** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/networks/ws) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/networks/ws) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/networks/ws) |
 | **Transmission Control Protocol (TCP)** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/networks/tcp) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/networks/tcp) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/networks/tcp) |

## Security Type Subscription Links
Subscription links for configurations are organized according to security type and categorized into separate Telegram channels and subscription links. These links provide access to configurations with specific security implementations.
| **Security Type** | **Mixed Configurations** | **Telegram Channels** | **Subscription Links** |
|:---:|:---:|:---:|:---:|
| **Transport Layer Security (TLS)** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/security/tls) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/security/tls) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/security/tls) |
| **Non Transport Layer Security (Non-TLS)** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/security/non-tls) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/security/non-tls) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/security/non-tls) |

## Internet Protocol Type Subscription Links
Subscription links for configurations are organized according to internet protocol type and categorized into separate Telegram channels and subscription links. These links enable access to configurations designed for specific internet protocol versions.
| **Internet Protocol Type** | **Mixed Configurations** | **Telegram Channels** | **Subscription Links** |
|:---:|:---:|:---:|:---:|
| **Internet Protocol Version 4 (IPV4)** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/layers/ipv4) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/layers/ipv4) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/layers/ipv4) |
| **Internet Protocol Version 6 (IPV6)** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/layers/ipv6) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/layers/ipv6) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/layers/ipv6) |

## Country Subscription Links
Subscription links for configurations are organized according to country and provide access to specialized configurations for services that implement location-based restrictions. These configurations are particularly relevant for social media and artificial intelligence services that may restrict access or ban accounts when location changes are detected.'''

stats = """## Stats
[![Stars](https://starchart.cc/soroushmirzaei/telegram-configs-collector.svg?variant=adaptive)](https://starchart.cc/soroushmirzaei/telegram-configs-collector)
## Activity
![Alt](https://repobeats.axiom.co/api/embed/6e88aa7d66986824532760b5b14120a22c8ca813.svg "Repobeats analytics image")"""

with open('./readme.md', 'w') as file:
    file.write(readme + '\n' + create_country_table('./countries') + '\n' + stats)
