"""statsy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from stats import views as stats_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', blog_views.home_posts, name='home'),
    path('player/', stats_views.player_search, name='player_search'),
    path('player/<int:pk>/<str:first_name>-<str:last_name>/',
         stats_views.PlayerDetailView.as_view(), name='player_info'),
    path('player/all/', stats_views.PlayerListView.as_view(), name='player_list'),
    path('team/<int:pk>/', stats_views.TeamDetailView.as_view(), name='team_info'),
    path('player/filter/', stats_views.filter_player_list, name='player_filter'),
]
