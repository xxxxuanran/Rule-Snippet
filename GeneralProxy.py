import requests

url1 = "https://ruleset.skk.moe/Clash/non_ip/cdn.txt"
list1 = requests.get(url1).text

results = set()

for line in list1.splitlines():
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    if line.startswith('DOMAIN-REGEX'):
        l = line.split(',^')[-1].split('\\.')
        if len(l) < 2:
            continue
        if l[-2].endswith(']'):
            l[-2] = l[-2].split('[')[0]
            line = f"DOMAIN-KEYWORD,{l[-2]}"
        else:
            line = f"DOMAIN-SUFFIX,{l[-2]}.{l[-1][:-1]}"
    results.add(line)

results = list(results)

with open('cdn.list', 'w+') as f:
    for result in results:
        f.write(result + '\n')