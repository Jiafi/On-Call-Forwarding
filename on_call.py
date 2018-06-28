import requests
import json

def get_oncall(schedule):
    api_key = 'axyyL8GMBsyQycLXJGkw'
    url = 'https://api.pagerduty.com/oncalls?time_zone=UTC'
    headers = {"Accept": "application/vnd.pagerduty+json;version=2","Authorization": "Token token=" + api_key}
    r = requests.get(url, headers=headers)
    data = json.loads(r.text)
    on_call_user = ''
    for dat in data['oncalls']:
        if dat['schedule']['summary'] == schedule:
            on_call_user = dat['user']['summary']
    with open('employee_numbers.json', 'r') as f:
        data = json.load(f)
    # Only returns on call users for one group
    # If more than one group than need a loop to return multiple numbers
    return data[on_call_user]

def get_schedules():
    api_key = 'axyyL8GMBsyQycLXJGkw'
    url = 'https://api.pagerduty.com/schedules'
    headers = {"Accept": "application/vnd.pagerduty+json;version=2","Authorization": "Token token=" + api_key}
    r = requests.get(url, headers=headers)
    data = json.loads(r.text)
    schedules = []
    for dat in data['schedules']:
        schedules.append(dat['summary'])
    return schedules
