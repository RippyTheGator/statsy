from django.shortcuts import render, redirect
from django.views import generic
from django.core.paginator import Paginator
from django_tables2 import SingleTableView
from .models import Player, Team
from .tables import PlayerTable
import requests
import json


class TeamDetailView(generic.DetailView):
    model = Team

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.view_count += 1
        self.object.save()
        return context


class PlayerDetailView(generic.DetailView):
    model = Player

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.view_count += 1
        self.object.save()
        return context


class PlayerListView(SingleTableView):
    model = Player
    table_class = PlayerTable


def player_search(request):
    player = {}
    result = {}
    page_obj = ''

    try:
        if 'player' in request.GET:
            name = request.GET['player'].split(' ')
            player = Player.objects.filter(
                first_name__contains=name[0], last_name__contains=name[1]).all().order_by('last_name')
            if len(player) == 1:
                return redirect('player_info', pk=player[0].id, first_name=player[0].first_name, last_name=player[0].last_name)
            paginator = Paginator(player, 20)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            result['success'] = True
            result['name'] = ' '.join(name)

    except IndexError:
        result['message'] = "One character from first and last name is required! Try again."
    return render(request, 'stats/player_search.html', {'page_obj': page_obj, 'result': result})


def player_stats(request):
    pass

# def player_info(request):
#     with open('static/player_data.json') as data_file:
#         player_data = json.load(data_file)
#
#     basic_data = []
#     message = {}
#     fullname = ''
#     if 'player' in request.GET:
#         full_name = request.GET['player']
#         players_id_list = [
#             k for k, v in player_data.items() if v == full_name.lower()
#         ]
#         fullname = '-'.join(full_name.split(' '))
#         if len(players_id_list) >= 1:
#             for i in range(len(players_id_list)):
#                 r = requests.get(
#                     'https://statsapi.web.nhl.com/api/v1/people/{}'.format(
#                         players_id_list[i]))
#                 r_basic_data = r.json()
#                 basic_data.append(r_basic_data['people'][0])
#         else:
#             message['error'] = '''
#                 {} not found. Try Again.'''.format(full_name.upper())
#
#     return render(request, 'stats/player_search.html', {
#         'basic_data': basic_data,
#         'message': message,
#         'fullname': fullname
#     }
#     )


# def total_pts(id, data, league):
#     t = 0
#     for i in range(len(data)):
#         if data[i]['stat'] != {} and data[i]['league']['name'] == league:
#             t += data[i]['stat']['points']
#     return t


# def player_stats(request, id, fullname, arg):
#     r = requests.get(
#         'https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats={}'.format(str(id), arg))
#     data = r.json()
#     stats = data['stats'][0]['splits']
#     total_points = total_pts(id, stats, 'National Hockey League')
#     return render(request, 'stats/player_stats.html', {
#         'stats': stats,
#         'fullname': fullname,
#         'total_points': total_points
#     })


def home(request):
    return render(request, 'stats/home.html')
