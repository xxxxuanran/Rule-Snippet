import requests
import re
import json

# https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide
url_365 = "https://endpoints.office.com/endpoints/worldwide?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7"
# https://www.microsoft.com/en-us/download/details.aspx?id=53602
url_az = 'https://www.microsoft.com/en-us/download/confirmation.aspx?id=53602'
resp = requests.get(url_365)

if resp.status_code == 200:
    data = json.loads(resp.content.decode('utf-8'))
    urls = set(['ms', 'msn.cn', 's-microsoft.com', 'microsoftpersonalcontent.com'])
    ips = set()
    others = set()
    for url in ["https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Microsoft.list",
                "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/OneDrive.list"]:
        resp = requests.get(url)
        for line in resp.text.splitlines():
            if line.startswith("DOMAIN-SUFFIX,"):
                urls.add(line.replace("DOMAIN-SUFFIX,", "").strip())
            elif not line.startswith('#'):
                others.add(line)
    for endpoint in data:
        if 'urls' in endpoint:
            for url in endpoint['urls']:
                urls.add(url.split(".")[-2] + "." + url.split(".")[-1])
        if 'ips' in endpoint:
            for ip in endpoint['ips']:
                if ":" not in ip:
                    ips.add(ip)
    urls = list(urls)
    ips = list(ips)
    others = list(others)
    with open('Microsoft.list', 'w+') as f:
        for url in urls:
            f.write('DOMAIN-SUFFIX,%s\n' % url)
        for ip in ips:
            f.write('IP-CIDR,%s,no-resolve\n' % ip)
        for other in others:
            f.write('%s\n' % other)
else:
    print("Error fetching data, status code: %d" % resp.status_code)