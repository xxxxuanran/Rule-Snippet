import requests

domestic = "https://ruleset.skk.moe/Clash/non_ip/domestic.txt"
resp = requests.get(domestic).text

results = set()
for line in resp.splitlines():
    line = line.strip()
    if not line or line.startswith('#') or line.startswith('DOMAIN-REGEX'):
        continue
    results.add(line)

results = list(results)

with open('domestic.list', 'w+') as f:
    for result in results:
        f.write('%s\n' % result)