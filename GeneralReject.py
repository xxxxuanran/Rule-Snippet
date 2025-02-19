import requests

reject = [
    "https://ruleset.skk.moe/Clash/non_ip/reject.txt",
    "https://ruleset.skk.moe/Clash/non_ip/reject-no-drop.txt",
    "https://ruleset.skk.moe/Clash/non_ip/reject-drop.txt",
    "https://ruleset.skk.moe/Clash/ip/reject.txt"
]
resp = ""
for url in reject:
    resp += requests.get(url).text

domain = set()
ips = set()
for line in resp.splitlines():
    line = line.strip()
    if not line or line.startswith('#') or line.startswith('DOMAIN-REGEX') or line.startswith('IP-ASN'):
        continue
    if line.startswith('IP-CIDR'):
        ips.add(line)
    else:
        domain.add(line)

domain = list(domain)
ips = list(ips)

with open('./non_ip/reject.list', 'w+') as f:
    for result in domain:
        f.write('%s\n' % result)

with open('./ip/reject.list', 'w+') as f:
    for result in ips:
        f.write('%s\n' % result)