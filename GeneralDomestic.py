import requests

domestic = "https://ruleset.skk.moe/Clash/non_ip/domestic.txt"
resp = requests.get(domestic).text

results = set()
for line in resp.splitlines():
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    if line.startswith('DOMAIN-REGEX'):
        l = line.split('.')[-2].split('[')[0]
        line = f"DOMAIN-KEYWORD,{l}"
    results.add(line)

results = list(results)

with open('./non_ip/domestic.list', 'w+') as f:
    for result in results:
        f.write('%s\n' % result)