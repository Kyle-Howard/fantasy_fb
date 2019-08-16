from django.shortcuts import render
import requests
from ff_espn_api import League

# Create your views here.
# import pdb; pdb.set_trace()
# 1246423
# 1625692

def home(request):
    return render(request, 'create.html')

def league_view(request):
    idLeague1 = request.GET.get('leagueid1')
    idLeague2 = request.GET.get('leagueid2')
    year1 = request.GET.get('year1')
    year2 = request.GET.get('year2')
    league1 = League(idLeague1, int(year1))
    league2 = League(idLeague2, int(year2))
    return render(request, 'league_view.html', context = {'leagueid1': idLeague1,'leagueid2': idLeague2, 'teams1': league1.teams,'teams2': league2.teams, 'year1': year1, 'year2': year2})

def team_view(request):
    #team = request.GET.get('team')
    #roster = request.GET.get('roster')
    return render(request, 'team_view.html')

def select_matchup(request):
    idLeague1 = request.GET.get('leagueid1')
    idLeague2 = request.GET.get('leagueid2')
    year1 = request.GET.get('year1')
    year2 = request.GET.get('year2')
    league1 = League(idLeague1, int(year1))
    league2 = League(idLeague2, int(year2))
    return render(request, 'select.html', context = {'league1': idLeague1,'league2': idLeague2, 'teams1': league1.teams,'teams2': league2.teams, 'year1': year1, 'year2': year2, 'range': range(17)})
    
def matchup_view(request):
    # reacquire league, team, and year info
    team1 = request.GET.get('team1')
    team2 = request.GET.get('team2')
    year1 = request.GET.get('year1')
    year2 = request.GET.get('year2')
    week = int(request.GET.get('week'))
    league1 = League(request.GET.get('league1'), int(year1))
    league2 = League(request.GET.get('league2'), int(year2))
    team1 = league1.get_team_data(int(team1))
    team2 = league2.get_team_data(int(team2))

    # acquire matchup data
    if week > 0 :
        matchups1 = league1.scoreboard(week)
        matchups2 = league2.scoreboard(week)
    else:
        matchups1 = league1.scoreboard()
        matchups2 = league2.scoreboard()
    

    # correlate data to the teams selected
    for index in range(len(matchups1)):
        if matchups1[index].home_team.team_id == team1.team_id:
            score1 = matchups1[index].home_score
            # temp = matchups1[index].home_team.team_id

        elif matchups1[index].away_team.team_id == team1.team_id:
            score1 = matchups1[index].away_score
            # temp = matchups1[index].away_team.team_id
    for index in range(len(matchups2)):
        if matchups2[index].home_team.team_id == team2.team_id:
            score2 = matchups2[index].home_score
            # temp = matchups2[index].home_team.team_id

        elif matchups2[index].away_team.team_id == team2.team_id:
            score2 = matchups2[index].away_score
            # temp = matchups2[index].away_team.team_id

    roster1 = team1.roster
    roster2 = team2.roster
    return render(request, 'compare.html', context = {'team1': team1, 'team2': team2, 'roster1': roster1, 'roster2': roster2, 'score1': score1, 'score2': score2})