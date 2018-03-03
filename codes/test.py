import json

json_data=open('matchhistory.json').read()
data = json.loads(json_data)
print(data['frames'][0].keys())

