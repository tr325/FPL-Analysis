import requests
import json
import pandas as pd
import numpy

FPL_DATA_PATH = 'https://fantasy.premierleague.com/drf/'

fpl_data = requests.get(FPL_DATA_PATH+'bootstrap-static').json()
print('request1 sorted')
for i, player in enumerate(fpl_data['elements']):
    print(player['id'])
    fpl_data['elements'][i]['history'] = requests.get(FPL_DATA_PATH+'element-summary/'+str(player['id'])).json()

frame = pd.DataFrame()
for i, player in enumerate(fpl_data['elements']):
	q = pd.DataFrame(fpl_data['elements'][i]['history']['history'])
	q['first_name'] = fpl_data['elements'][i]['first_name']
	q['second_name'] = fpl_data['elements'][i]['second_name']
	q['game_week'] = 'GW' + q['round'].map(str)
	frame = pd.concat([frame,q])
	frame = frame.set_index(['game_week','first_name','second_name'])

print('opening')

