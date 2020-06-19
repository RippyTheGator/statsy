from django.shortcuts import render
import requests
import json


def player_info(request):
    with open('static/player_data.json') as data_file:
        player_data = json.load(data_file)

    basic_data = []
    message = {}
    fullname = ''
    if 'player' in request.GET:
        full_name = request.GET['player']
        players_id_list = [
            k for k, v in player_data.items() if v == full_name.lower()
        ]
        fullname = '-'.join(full_name.split(' '))
        if len(players_id_list) >= 1:
            for i in range(len(players_id_list)):
                r = requests.get(
                    'https://statsapi.web.nhl.com/api/v1/people/{}'.format(
                        players_id_list[i]))
                r_basic_data = r.json()
                basic_data.append(r_basic_data['people'][0])
        else:
            message['error'] = '''
                {} not found. Try Again.'''.format(full_name.upper())

    return render(request, 'stats/player_search.html', {
        'basic_data': basic_data,
        'message': message,
        'fullname': fullname
    }
    )


def total_pts(id, data, league):
    t = 0
    for i in range(len(data)):
        if data[i]['stat'] != {} and data[i]['league']['name'] == league:
            t += data[i]['stat']['points']
    return t


def player_stats(request, id, fullname, arg):
    r = requests.get(
        'https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats={}'.format(str(id), arg))
    data = r.json()
    stats = data['stats'][0]['splits']
    total_points = total_pts(id, stats, 'National Hockey League')
    return render(request, 'stats/player_stats.html', {
        'stats': stats,
        'fullname': fullname,
        'total_points': total_points
    })
