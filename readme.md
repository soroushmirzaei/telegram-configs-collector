## Introduction
The script systematically collects Vmess, Vless, ShadowSocks, Trojan, Reality, Hysteria, Tuic, and Juicity configurations from publicly accessible Telegram channels. It categorizes these configurations based on open and closed ports, eliminates any duplicate entries, resolves configuration addresses using IP addresses, and revises configuration titles to reflect server and protocol-type properties. These properties include network and security type, IP address and port, and the respective country associated with the configuration.

![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/soroushmirzaei/telegram-configs-collector?label=Last%20Commit&color=%2338914b)
![GitHub](https://img.shields.io/github/license/soroushmirzaei/telegram-configs-collector?label=License&color=yellow)
![GitHub Repo stars](https://img.shields.io/github/stars/soroushmirzaei/telegram-configs-collector?label=Stars&color=red&style=flat)
![GitHub forks](https://img.shields.io/github/forks/soroushmirzaei/telegram-configs-collector?label=Forks&color=blue&style=flat)
[![Execute On Schedule](https://github.com/soroushmirzaei/telegram-configs-collector/actions/workflows/schedule.yml/badge.svg)](https://github.com/soroushmirzaei/telegram-configs-collector/actions/workflows/schedule.yml)
[![Execute On Push](https://github.com/soroushmirzaei/telegram-configs-collector/actions/workflows/push.yml/badge.svg)](https://github.com/soroushmirzaei/telegram-configs-collector/actions/workflows/push.yml)

## Tutorial
The list of domains to bypass, block, and proxy based on the `ir` geo-location in the `nekoray` and `nekobox` according to the core is set to `sing-box`. To set these domains, create new routes in the `nekobox` and `nekoray` and enter the domains below in the relevant `domains` section. Set the outbound value as `bypass`, `proxy`, or `block` as specified.

- Bypass
```
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
geosite:whatsapp
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
Configuration subscription links based on protocol type and separated into Telegram channels and subscription links
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
Configuration subscription links based on network type and separated into Telegram channels and subscription links
| **Network Type** | **Mixed Configurations** | **Telegram Channels** | **Subscription Links** |
|:---:|:---:|:---:|:---:|
| **Google Remote Procedure Call (GRPC)** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/networks/grpc) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/networks/grpc) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/networks/grpc) |
| **Hypertext Transfer Protocol (HTTP)** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/networks/http) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/networks/http) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/networks/http) |
| **WebSocket Protocol (WS)** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/networks/ws) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/networks/ws) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/networks/ws) |
 | **Transmission Control Protocol (TCP)** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/networks/tcp) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/networks/tcp) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/networks/tcp) |

## Security Type Subscription Links
Configuration subscription links based on security type and separated into Telegram channels and subscription links
| **Security Type** | **Mixed Configurations** | **Telegram Channels** | **Subscription Links** |
|:---:|:---:|:---:|:---:|
| **Transport Layer Security (TLS)** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/security/tls) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/security/tls) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/security/tls) |
| **Non Transport Layer Security (Non-TLS)** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/security/non-tls) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/security/non-tls) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/security/non-tls) |

## Internet Protocol Type Subscription Links
Configuration subscription links based on internet protocol type and separated into Telegram channels and subscription links
| **Internet Protocol Type** | **Mixed Configurations** | **Telegram Channels** | **Subscription Links** |
|:---:|:---:|:---:|:---:|
| **Internet Protocol Version 4 (IPV4)** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/layers/ipv4) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/layers/ipv4) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/layers/ipv4) |
| **Internet Protocol Version 6 (IPV6)** | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/layers/ipv6) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/layers/ipv6) | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/layers/ipv6) |

## Country Subscription Links
Configuration subscription links based on country for services that result in account bans if the location is changed, such as social media and artificial intelligence services
| **Code** | **Country Name** | **Subscription Link** | **Code** | **Country Name** | **Subscription Link** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| AL | Albania | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/al/mixed) | AR | Argentina | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ar/mixed) |
| AM | Armenia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/am/mixed) | AU | Australia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/au/mixed) |
| AT | Austria | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/at/mixed) | BH | Bahrain | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/bh/mixed) |
| BY | Belarus | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/by/mixed) | BE | Belgium | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/be/mixed) |
| BO | Bolivia, Plurinational State of | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/bo/mixed) | BA | Bosnia and Herzegovina | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ba/mixed) |
| BR | Brazil | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/br/mixed) | BG | Bulgaria | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/bg/mixed) |
| CA | Canada | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ca/mixed) | CL | Chile | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/cl/mixed) |
| CN | China | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/cn/mixed) | HR | Croatia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/hr/mixed) |
| CY | Cyprus | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/cy/mixed) | CZ | Czechia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/cz/mixed) |
| DK | Denmark | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/dk/mixed) | EC | Ecuador | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ec/mixed) |
| EE | Estonia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ee/mixed) | FI | Finland | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/fi/mixed) |
| FR | France | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/fr/mixed) | GE | Georgia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ge/mixed) |
| DE | Germany | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/de/mixed) | GI | Gibraltar | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/gi/mixed) |
| GR | Greece | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/gr/mixed) | GT | Guatemala | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/gt/mixed) |
| HK | Hong Kong | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/hk/mixed) | HU | Hungary | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/hu/mixed) |
| IS | Iceland | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/is/mixed) | IN | India | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/in/mixed) |
| ID | Indonesia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/id/mixed) | IR | Iran, Islamic Republic of | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ir/mixed) |
| IE | Ireland | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ie/mixed) | IL | Israel | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/il/mixed) |
| IT | Italy | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/it/mixed) | JP | Japan | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/jp/mixed) |
| JO | Jordan | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/jo/mixed) | KZ | Kazakhstan | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/kz/mixed) |
| KE | Kenya | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ke/mixed) | KR | Korea, Republic of | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/kr/mixed) |
| LV | Latvia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/lv/mixed) | LT | Lithuania | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/lt/mixed) |
| LU | Luxembourg | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/lu/mixed) | MY | Malaysia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/my/mixed) |
| MT | Malta | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/mt/mixed) | MU | Mauritius | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/mu/mixed) |
| MX | Mexico | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/mx/mixed) | MD | Moldova, Republic of | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/md/mixed) |
| MA | Morocco | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ma/mixed) | NP | Nepal | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/np/mixed) |
| NL | Netherlands | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/nl/mixed) | NZ | New Zealand | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/nz/mixed) |
| MK | North Macedonia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/mk/mixed) | NO | Norway | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/no/mixed) |
| NA | Not Available | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/na/mixed) | PK | Pakistan | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/pk/mixed) |
| PA | Panama | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/pa/mixed) | PH | Philippines | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ph/mixed) |
| PL | Poland | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/pl/mixed) | PR | Puerto Rico | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/pr/mixed) |
| RO | Romania | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ro/mixed) | RU | Russian Federation | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ru/mixed) |
| RS | Serbia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/rs/mixed) | SC | Seychelles | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/sc/mixed) |
| SG | Singapore | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/sg/mixed) | SK | Slovakia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/sk/mixed) |
| SI | Slovenia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/si/mixed) | ZA | South Africa | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/za/mixed) |
| ES | Spain | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/es/mixed) | SE | Sweden | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/se/mixed) |
| CH | Switzerland | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ch/mixed) | TW | Taiwan, Province of China | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/tw/mixed) |
| TH | Thailand | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/th/mixed) | TR | Türkiye | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/tr/mixed) |
| UA | Ukraine | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ua/mixed) | AE | United Arab Emirates | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ae/mixed) |
| GB | United Kingdom | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/gb/mixed) | US | United States | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/us/mixed) |
| VN | Viet Nam | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/vn/mixed) |
## Stats
[![Stars](https://starchart.cc/soroushmirzaei/telegram-configs-collector.svg?variant=adaptive)](https://starchart.cc/soroushmirzaei/telegram-configs-collector)
## Activity
![Alt](https://repobeats.axiom.co/api/embed/6e88aa7d66986824532760b5b14120a22c8ca813.svg "Repobeats analytics image")