import requests
import json
from datetime import date, datetime
from .models import Player, Team
from distutils.util import strtobool
import environ


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
    count = 1100
    with open('draft_details.json', 'r') as f:
        data = json.load(f)
    for i in range(len(data)):
        for j in range(len(data[i])):
            k = list(data[i][j].keys())
            print(k)
            players = Player.objects.filter(full_name=k[0])
            if players.exists() and len(players) == 1:
                k = k[0]
                name = k.split()
                players[0].first_name = name[0]
                players[0].last_name = name[1]
                players[0].draft = Team(id=data[i][j][k]['team_id'])
                players[0].year_drafted = data[i][j][k]['year']
                players[0].round_drafted = data[i][j][k]['round']
                players[0].selection_number = data[i][j][k]['pick']
                players[0].save()
            elif players.exists() == False:
                name = k[0].split()
                player = Player(
                    id=count,
                    full_name=k[0],
                    first_name=name[0],
                    last_name=name[1],
                    draft=Team(id=data[i][j][k[0]]['team_id']),
                    year_drafted=data[i][j][k[0]]['year'],
                    round_drafted=data[i][j][k[0]]['round'],
                    selection_number=data[i][j][k[0]]['pick']
                )
                player.save()
                print(True)
                count += 1


def set_age():
    players = Player.objects.all()
    today = date.today()
    for player in players:
        player.player_age = today.year - player.birth_date.year - ((today.month, today.day) <
                                                                   (player.birth_date.month, player.birth_date.day))
        player.save()
