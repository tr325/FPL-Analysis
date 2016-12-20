def getDataFrame:
	p = pd.DataFrame()
	for i, player in enumerate(fpl_data['elements']):
    		q = pd.DataFrame(fpl_data['elements'][i]['history']['history'])
    		q['first_name'] = fpl_data['elements'][i]['first_name']
    		q['second_name'] = fpl_data['elements'][i]['second_name']
    		q['game_week'] = 'GW' + q['round'].map(str)
    		p = pd.concat([p,q])
		p = p.set_index(['game_week','first_name','second_name'])

	return p
