import requests
import json
from pandas import DataFrame
import sys
apikey = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": "RGAPI-82605de7-c3cf-48ce-a909-9d07a3753c07",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
}

url = 'https://kr.api.riotgames.com/lol/static-data/v3/items?locale=ko_KR'

r = requests.get(url, headers=apikey)
dc = r.json()
with open(sys.path[1]+'/data/items.json', 'w') as outfile:
    json.dump(dc, outfile)
print(dc.keys())



