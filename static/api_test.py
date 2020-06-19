# from googleapiclient.discovery import build
#
# api_key = 'AIzaSyCvjOw9OAQAabyaIhtesjKXtGurpQ40e-g'
# service = build('youtube', 'v3', developerKey=api_key)
#
# request = service.channels().list(
#     part='statistics',
#     forUsername='schafer5'
# )
#
# response = request.execute()
# print(response['viewCount'])

import requests
import json

# teams_dict = {'philadelphia flyers': 4}
# team_input = input('Enter a team name: ')
# team_id = teams_dict[team_input.lower()]
# payload = {'teamId': team_id}

# with open('c:/Users/casey/python/django_projects/statsy/static/player_data.json',
#           'r') as json_file:
#     data = json.load(json_file)
#
# data = {k: v.lower() for k, v in data.items()}
#
# print(data)

# players = [k for k, v in data.items() if v == "Sebastian Aho"]
# player_data = {}
# for i in range(40000):
#     r = requests.get('https://statsapi.web.nhl.com/api/v1/people/{}'.format(8444000+i))
#     r_data = r.json()
#     if r.status_code == 200:
#         player_data[r_data['people'][0]['id']] = r_data['people'][0]['fullName'].lower()
#
#  with open('player_data.json', 'w') as f:
#     json.dump(player_data, f)
# search_result.append(r_data['people'][0])
#
# print(search_result[1])
r = requests.get(
    'https://statsapi.web.nhl.com/api/v1/people/8447400/stats?stats=yearByYear')
data = r.json()
stats = data['stats'][0]['splits']
total_points = 0
for i in range(len(stats)):
    if stats[i]['stat'] != {} and stats[i]['league']['name'] == 'National Hockey League':
        total_points += stats[i]['stat']['points']

print(total_points)

name = 'casey moore'
fullname = ''.join(name.split(' '))
print(fullname)
