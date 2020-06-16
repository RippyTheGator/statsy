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

with open('teams.txt') as json_file:
    data = json.loads(json_file)
print(data)
