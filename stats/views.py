from django.shortcuts import render, redirect
from django.views import generic
from django.core.paginator import Paginator
from django_tables2 import SingleTableView, RequestConfig
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from .filters import PlayerFilter
from .models import Player, Team
from .tables import PlayerTable
import pandas as pd
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
        url = 'https://www.nhl.com/player/{}-{}-{}'.format(
            self.object.first_name, self.object.last_name, self.object.id)
        stat_data = pd.read_html(url)
        context['career_stats'] = stat_data
        context['test'] = 1
        self.object.view_count += 1
        self.object.save()
        return context


class PlayerListView(SingleTableView):
    model = Player
    table_class = PlayerTable

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = Player.objects.all()
        return context

    def get_query_set(self):
        qs = super().get_queryset()
        return qs.order_by("view_count")


def filter_player_list(request):
    queryset = Player.objects.all().order_by("view_count")
    f = PlayerFilter(request.GET, queryset=queryset)
    table = PlayerTable(f.qs)
    RequestConfig(request, paginate={
                  "per_page": 20, "page": 1}).configure(table)
    return render(request, "stats/player_filter.html", {"table": table, "filter": f})


def player_search(request):
    result = {}
    table = None
    data = None
    try:
        if 'player' in request.GET:
            # data = Player.objects.filter(full_name__search=request.GET['player'])
            name = request.GET['player'].split()
            data = Player.objects.filter(
                first_name__startswith=name[0],
                last_name__startswith=name[1]).all().order_by('first_name')
            table = PlayerTable(data)
            RequestConfig(request).configure(table)
            if len(data) == 1:
                return redirect(
                    'player_info',
                    pk=data[0].id,
                    first_name=data[0].first_name,
                    last_name=data[0].last_name
                )
            result['success'] = True
            result['name'] = ' '.join(name)

        # OLD CODE NOT USING DJANGO_TABLES2:
        # player = Player.objects.filter(
        # first_name__contains=name[0], last_name__contains=name[1]).all().order_by('last_name')
        # paginator = Paginator(player, 20)
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)

    except IndexError:
        result['message'] = "One character from first and last name is required! Try again."
    return render(
        request,
        'stats/player_search.html',
        {'table': table, 'result': result, 'data': data}
    )


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
