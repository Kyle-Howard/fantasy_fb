from django.urls import path
from fantasy_fb import views

urlpatterns = [
    path('select_matchup', views.select_matchup),
    path('matchup_view', views.matchup_view),
    path('home', views.home),
    path('league_view', views.league_view),
    path('team_view', views.team_view)
]