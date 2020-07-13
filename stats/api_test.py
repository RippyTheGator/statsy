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
from datetime import date, datetime
from .models import Player, Team
from distutils.util import strtobool

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
# r = requests.get(
#     'https://statsapi.web.nhl.com/api/v1/people/8447400/stats?stats=yearByYear')
# data = r.json()
# stats = data['stats'][0]['splits']
# total_points = 0
# for i in range(len(stats)):
#     if stats[i]['stat'] != {} and stats[i]['league']['name'] == 'National Hockey League':
#         total_points += stats[i]['stat']['points']
#
# print(total_points)
#
# name = 'casey moore'
# fullname = ''.join(name.split(' '))
# print(fullname)


def add_team_to_db():
    for i in range(100):
        r = requests.get('https://statsapi.web.nhl.com/api/v1/teams/{}'.format(i))
        if r.status_code == 200:
            team_data = r.json()
            results = team_data['teams'][0]
            team = Team(
                id=results.get('id'),
                name=results.get('name'),
                venue_name=results.get('venue', {}).get('name', 'N/A'),
                abbrevation=results.get('abbreviation', 'N/A'),
                first_year_of_play=results.get('firstYearOfPlay', 'N/A'),
                division=results.get('division', {}).get('name', 'N/A'),
                conference=results.get('conference', {}).get('name', 'N/A'),
                team_active=results.get('active'),
                official_site=results.get('officialSiteUrl', 'N/A'),
            )
            team.save()
    print(True)


def add_player_to_db():

    with open('player_data.json', 'r') as file:
        data = json.load(file)
    for k, v in data.items():
        url = 'https://statsapi.web.nhl.com/api/v1/people/{}'
        r = requests.get(url.format(k))
        player_data = r.json()
        results = player_data['people'][0]
        player = Player(
            id=results.get('id'),
            full_name=results.get('fullName'),
            first_name=results.get('firstName'),
            last_name=results.get('lastName'),
            primary_number=results.get('primaryNumber', 'N/A'),
            birth_date=datetime.strptime(
                results.get('birthDate', '1900-01-01'), '%Y-%m-%d'
            ),
            birth_city=results.get('birthCity', 'N/A'),
            birth_country=results.get('birthCountry', 'N/A'),
            nationality=results.get('nationality', 'N/A'),
            height=results.get('height', 'N/A'),
            weight=results.get('weight', 'N/A'),
            active=results.get('active'),
            alternate_captain=results.get('alternateCaptain', False),
            captain=results.get('captain', False),
            rookie=results.get('rookie', False),
            shoot_catches=results.get('shootsCatches', 'N/A'),
            roster_status=results.get('rosterStatus', 'N'),
            team=Team(id=int(results.get('currentTeam', {}).get('id', 0))),
            primary_position=results.get('primaryPosition', {}).get('name', 'N/A')
        )
        player.save()
    return True


def get_draft_data():
    dict_list = []
    year = datetime.now()
    year = year.year
    for i in range(int(year)-1963):
        year_list = []
        r = requests.get('https://statsapi.web.nhl.com/api/v1/draft/{}'.format(1963+i))
        data = r.json()
        data1 = data['drafts'][0]['rounds']
        for j in range(len(data1)):
            data2 = data1[j]['picks']
            for k in range(len(data2)):
                results = data2[k]
                year_list.append({'{}'.format(results['prospect']['fullName']): {'year': results['year'],
                                                                                 'round': results['round'],
                                                                                 'pick': results['pickOverall'],
                                                                                 'team_id': results['team']['id'],
                                                                                 'team_name': results['team']['name']}})
        dict_list.append(year_list)
    with open('draft_details.json', 'w') as f:
        json.dump(dict_list, f)


def update_draft():
    with open('draft_details.json', 'r') as f:
        data = json.load(f)
    for i in range(len(data)):
        for j in range(len(data[i])):
            k = list(data[i][j].keys())
            print(k)
            players = Player.objects.filter(full_name=k[0], draft=0, player_age__lte=76)
            if players.exists() and len(players) == 1:
                k = k[0]
                players[0].draft = Team(id=data[i][j][k].get('team_id'))
                players[0].year_drafted = data[i][j][k]['year']
                players[0].round_drafted = data[i][j][k]['round']
                players[0].selection_number = data[i][j][k]['pick']
                players[0].save()


def set_age():
    players = Player.objects.all()
    today = date.today()
    for player in players:
        player.player_age = today.year - player.birth_date.year - ((today.month, today.day) <
                                                                   (player.birth_date.month, player.birth_date.day))
        player.save()
