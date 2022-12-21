# Description: Helper functions for the Fantasy Basketball App
def display_team_category_stats(team_cat_stats, team_name):
    print(team_name + " Stats: ")
    print("---------------------------------")
    if team_cat_stats['PTS'] == 0:
        print("No players on team")
        print("---------------------------------")
        return
    print("Total Points: " + str(round(team_cat_stats['PTS'], 1)))
    print("Total Rebounds: " + str(round(team_cat_stats['REB'], 1)))
    print("Total Assists: " + str(round(team_cat_stats['AST'], 1)))
    print("Total Steals: " + str(round(team_cat_stats['ST'], 1)))
    print("Total Blocks: " + str(round(team_cat_stats['BLK'], 1)))
    print("Total Field Goal Percentage: " + str(round(team_cat_stats['FG%'], 1)))
    print("Total Free Throw Percentage: " + str(round(team_cat_stats['FT%'], 1)))
    print("Total 3 Pointers Made: " + str(round(team_cat_stats['3PTM'], 1)))
    print("Total Turnovers: " + str(round(team_cat_stats['TO'], 1)))
    print("---------------------------------")
def calculate_team_category_stats(league, team_name):
    teams = league.teams()
    # create dictionary to store team stats
    team_cat_stats = {'PTS': 0, 'REB': 0, 'AST': 0, 'ST': 0, 'BLK': 0, 'FG%': 0, 'FT%': 0, '3PTM': 0, 'TO': 0}
    for team in teams:
        if team_name == teams[team]['name']:
            curr_key = teams[team]['team_key']
            curr_team = league.to_team(curr_key)
            curr_roster = curr_team.roster()
            for player in curr_roster:
                curr_player = league.player_stats(player['player_id'], 'average_season')
                if curr_player[0]['PTS'] == '-':
                    break
                team_cat_stats['PTS'] += float(curr_player[0]['PTS'])
                team_cat_stats['REB'] += float(curr_player[0]['REB'])
                team_cat_stats['AST'] += float(curr_player[0]['AST'])
                team_cat_stats['ST'] += float(curr_player[0]['ST'])
                team_cat_stats['BLK'] += float(curr_player[0]['BLK'])
                team_cat_stats['FG%'] += float(curr_player[0]['FG%'])
                team_cat_stats['FT%'] += float(curr_player[0]['FT%'])
                team_cat_stats['3PTM'] += float(curr_player[0]['3PTM'])
                team_cat_stats['TO'] += float(curr_player[0]['TO'])
    return team_cat_stats
def display_team_comparison(team1, team2, team_name1, team_name2):
    team_comparison_dict = {'PTS': 0, 'REB': 0, 'AST': 0, 'ST': 0, 'BLK': 0, 'FG%': 0, 'FT%': 0, '3PTM': 0, 'TO': 0}
    for key in team1:
        team_comparison_dict[key] = team1[key] - team2[key]
    print("Team Comparison: ")
    print("---------------------------------")
    print("Total Points: " + str(round(team_comparison_dict['PTS'], 1)) + " In favour of " + display_in_favour_of(team_comparison_dict['PTS'], team_name1, team_name2))
    print("Total Rebounds: " + str(round(team_comparison_dict['REB'], 1)) + " In favour of " + display_in_favour_of(team_comparison_dict['REB'], team_name1, team_name2))
    print("Total Assists: " + str(round(team_comparison_dict['AST'], 1)) + " In favour of " + display_in_favour_of(team_comparison_dict['AST'], team_name1, team_name2))
    print("Total Steals: " + str(round(team_comparison_dict['ST'], 1)) + " In favour of " + display_in_favour_of(team_comparison_dict['ST'], team_name1, team_name2))
    print("Total Blocks: " + str(round(team_comparison_dict['BLK'], 1)) + " In favour of " + display_in_favour_of(team_comparison_dict['BLK'], team_name1, team_name2))
    print("Total Field Goal Percentage: " + str(round(team_comparison_dict['FG%'], 1)) + " In favour of " + display_in_favour_of(team_comparison_dict['FG%'], team_name1, team_name2))
    print("Total Free Throw Percentage: " + str(round(team_comparison_dict['FT%'], 1)) + " In favour of " + display_in_favour_of(team_comparison_dict['FT%'], team_name1, team_name2))
    print("Total 3 Pointers Made: " + str(round(team_comparison_dict['3PTM'], 1)) + " In favour of " + display_in_favour_of(team_comparison_dict['3PTM'], team_name1, team_name2))
    print("Total Turnovers: " + str(round(team_comparison_dict['TO'], 1)) + " In favour of " + favour_of_turnovers(team_comparison_dict['TO'], team_name1, team_name2))
    print("---------------------------------")
def display_in_favour_of(stat, team_name1, team_name2):
    if stat > 0:
        return team_name1
    else:
        return team_name2
def favour_of_turnovers(stat, team_name1, team_name2):
    if stat > 0:
        return team_name2
    else:
        return team_name1
def waiver_wire_analysis(OGLeague):
    players = OGLeague.waivers()
    pickup = []
    for player in players:
        if players[player]['is_owned'] == False:
            pickup.append(players[player])