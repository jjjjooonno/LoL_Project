from pandas import *
import requests
apikey = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": "RGAPI-3aab9814-0eeb-4bc3-9e9d-9a9b0f157259",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
}
url = 'https://kr.api.riotgames.com/lol/static-data/v3/champions?locale=ko_KR&champListData=all&tags=all&dataById=false'
r = requests.get(url,headers = apikey)
dt = r.json()
print(dt.keys())
name = []
id = []
armorperlevel = []
attackdamage = []
mpperlevel = []
attackspeedoffset = []
mp = []
armor = []
hp = []
hpregenperlevel = []
attackspeedperlevel = []
attackrange = []
movespeed = []
attackdamageperlevel = []
mpregenperlevel = []
critperlevel = []
spellblockperlevel = []
crit = []
mpregen = []
spellblock = []
hpregen = []
hpperlevel = []
for i in dt:
    print(i)
    name.append(i['name'])
    id.append(i['id'])
    armorperlevel.append(i['stats']['armorperlevel'])
    attackdamage.append(i['stats']['armorperlevel'])
    mpperlevel.append(i['stats']['armorperlevel'])
    attackspeedoffset.append(i['stats']['armorperlevel'])
    mp.append(i['stats']['armorperlevel'])
    armor.append(i['stats']['armorperlevel'])
    hp.append(i['stats']['armorperlevel'])
    hpregenperlevel.append(i['stats']['armorperlevel'])
    attackspeedperlevel.append(i['stats']['armorperlevel'])
    attackrange.append(i['stats']['armorperlevel'])
    movespeed.append(i['stats']['armorperlevel'])
    attackdamageperlevel.append(i['stats']['armorperlevel'])
    mpregenperlevel.append(i['stats']['armorperlevel'])
    critperlevel.append(i['stats']['armorperlevel'])
    spellblockperlevel.append(i['stats']['armorperlevel'])
    crit.append(i['stats']['armorperlevel'])
    mpregen.append(i['stats']['armorperlevel'])
    spellblock.append(i['stats']['armorperlevel'])
    hpregen.append(i['stats']['armorperlevel'])
    hpperlevel.append(i['stats']['armorperlevel'])
dtt = DataFrame({'name' : name,
                 'id' : id,
                 'armorperlevel' :armorperlevel,
                 'attackdamage' : attackdamage,
                 'mpperlevel' : mpperlevel,'attackspeedoffset' : attackspeedoffset,
                 'mp' : mp,
                 'armor' : armor,
                 'hp' : hp,
                 'hpregenperlevel' : hpregenperlevel,
                 'attackspeedperlevel' : attackspeedperlevel,
                 'attackrange' : attackrange,
                 'movespeed' : movespeed,
                 'attackdamageperlevel' : attackdamageperlevel,
                 'mpregenperlevel' : mpregenperlevel,
                 'critperlevel' : critperlevel,
                 'spellblockperlevel' : spellblockperlevel,
                 'crit' : crit,
                 'mpregen' : mpregen,
                 'spellblock' : spellblock,
                 'hpregen' : hpregen,
                 'hpperlevel' : hpperlevel})

dtt.to_excel('champions.xlsx')
