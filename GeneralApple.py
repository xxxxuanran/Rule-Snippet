import requests
from ruamel.yaml import YAML

yaml = YAML()
yaml.default_flow_style = False
# mapping 列条目破折号距离左侧距离
# sequence 列条目内容距离左侧距离
# offset 列条目内容距离破折号距离
yaml.indent(mapping=2, sequence=4, offset=2)

from pathlib import Path

file_yml = Path("apple_cdn.yaml")

domainset = "https://ruleset.skk.moe/List/domainset/apple_cdn.conf"

domainset_text = requests.get(domainset).text

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

apple_list = list(result)
apple_dict = {'payload': apple_list}
yaml.dump(apple_dict, file_yml)
