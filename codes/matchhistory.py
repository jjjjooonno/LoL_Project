import requests
import json
from pandas import DataFrame
apikey = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": "RGAPI-47a4414a-fc54-41c6-a3c0-b42eee5da15e",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
}
gameid = '3129275488'

url = 'https://kr.api.riotgames.com/lol/match/v3/timelines/by-match/' + gameid

r = requests.get(url, headers=apikey)
dc = r.json()
with open('matchhistory.json', 'w') as outfile:
    json.dump(dc, outfile)
print(dc.keys())

