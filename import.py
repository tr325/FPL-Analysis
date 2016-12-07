import requests
import json

FPL_DATA_PATH = 'https://fantasy.premierleague.com/drf/'

fpl_data = requests.get(FPL_DATA_PATH+'bootstrap-static').json()
print 'request1 sorted'
for i, player in enumerate(fpl_data['elements']):
    print player['id']
    fpl_data['elements'][i]['history'] = requests.get(FPL_DATA_PATH+'element-summary/'+str(player['id'])).json()

print 'opening'
f = open('data20161205.json', 'w')
f.write(json.dumps(fpl_data, sort_keys=True, indent=4, separators=(',', ': ')))
f.close()
