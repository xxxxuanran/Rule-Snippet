import requests

non_ip = "https://ruleset.skk.moe/List/non_ip/direct.conf"

direct = requests.get(non_ip).text

results = set()
for line in direct.splitlines():
    line = line.strip()
    if not line or line.startswith('#') or line.startswith('URL-REGEX'):
        continue
    results.add(line)

results = list(results)

with open('direct.list', 'w+') as f:
    for result in results:
        f.write('%s\n' % result)