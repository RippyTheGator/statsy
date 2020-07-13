from .models import Player, Team


def trending(request):
    return {
        'trending_player': Player.objects.all().order_by('-view_count')[:5],
        'trending_team': Team.objects.all().order_by('-view_count')[:5],
    }
