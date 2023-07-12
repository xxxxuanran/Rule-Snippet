import requests
from ruamel.yaml import YAML

yaml = YAML()
yaml.default_flow_style = False
# mapping 列条目破折号距离左侧距离
# sequence 列条目内容距离左侧距离
# offset 列条目内容距离破折号距离
yaml.indent(mapping=2, sequence=4, offset=2)

from pathlib import Path

file_yml = Path("cdn.yaml")

domainset = "https://ruleset.skk.moe/List/domainset/cdn.conf"
internal = "https://ruleset.skk.moe/List/internal/cdn.txt"

domainset_text = requests.get(domainset).text
internal_text = requests.get(internal).text

result = set()
for line in domainset_text.splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    if line.startswith("."):
        line = "DOMAIN-SUFFIX," + line[1:]
    else:
        line = "DOMAIN," + line
    result.add(line)
for line in internal_text.splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    if line.startswith("SUFFIX"):
        line = "DOMAIN-" + line
    result.add(line)

akas = """*.akadns.net
*.akam.net
*.akamai.com
*.akamai.net
*.akamaiedge.net
*.akamaihd.net
*.akamaized.net
*.edgekey.net
*.edgesuite.net"""
for aka in akas.splitlines():
    aka = aka.strip()
    aka = "DOMAIN-SUFFIX," + line[2:]
    result.add(aka)

cdn_list = list(result)
cdn_dict = {'payload': cdn_list}
yaml.dump(cdn_dict, file_yml)
