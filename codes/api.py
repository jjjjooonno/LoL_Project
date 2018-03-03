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
url = 'https://kr.api.riotgames.com/lol/summoner/v3/summoners/by-name/'
id = '쭈노쮸노'
r = requests.get(url+id, headers=apikey)
dc = r.json()
print(dc.keys())
accountid = dc['accountId']
print(accountid)
match_url = 'https://kr.api.riotgames.com/lol/match/v3/matchlists/by-account/'

r2 = requests.get(match_url+str(accountid),headers = apikey)
dc2 = r2.json()
print(dc2['matches'])

print(dc2['matches'][0].keys())
platformId = []
gameId = []
champion = []
queue = []
season = []
timestamp = []
role = []
lane = []
for i in dc2['matches']:
    platformId.append(i['platformId'])
    gameId.append(i['gameId'])
    champion.append(i['champion'])
    queue.append(i['queue'])
    season.append(i['season'])
    timestamp.append(i['timestamp'])
    role.append(i['role'])
    lane.append(i['lane'])
# dt = DataFrame({'pid' : platformId,
#                 'gid' : gameId,
#                 'champion' : champion,
#                 'queue' : queue,
#                 'season' : season,
#                 'timestamp' : timestamp,
#                 'role' : role,
#                 'lane' : lane})
# dt.to_csv('jnjn.csv')
print(gameId)
# for j in gameId: