import requests
import json

def get_oncall():
	api_key = 'axyyL8GMBsyQycLXJGkw'
	url = 'https://api.pagerduty.com/oncalls?time_zone=UTC'
	headers = {"Accept": "application/vnd.pagerduty+json;version=2","Authorization": "Token token=" + api_key}
	r = requests.get(url, headers=headers)
	data = json.loads(r.text)
	on_call_users = []
	for dat in data['oncalls']:
		on_call_users.append(dat['user']['summary'])
	with open('employee_numbers.json', 'r') as f:
		data = json.load(f)
	# Only returns on call users for one group
	# If more than one group than need a loop to return multiple numbers
	return data[on_call_users[0]]
