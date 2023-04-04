from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd
import data.classes as classes
import time
from math import ceil
stats = ['FG%', 'FT%', '3PM', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TOV']
# Description: Helper functions for the Fantasy Basketball App
# updated helper functions
def round_up(num):
    other_num = round(num % 0.1, 10)
    if ((num * 10) % 1 == 0):
        return num
    if other_num == 0.05:
        return round((ceil(num * 10 ** 1) / 10 ** 1), 10)
    elif other_num < 0.05:
        return round((ceil(num * 10 ** 1) / 10 ** 1) - 0.1, 10)
    else:
        return round((ceil(num * 10 ** 1) / 10 ** 1), 10)
    # return round(num, 10) 
# get team
def find_team(team_name, league):
    teams = league.teams()
    for team in teams:
        if team_name == teams[team]['name']:
            curr_key = teams[team]['team_key']
            curr_team = league.to_team(curr_key)
            return curr_team
# get individual playerSS
# why in this function sometimes the api can successfully get the player details and sometimes it can't
# requests.exceptions.ReadTimeout: HTTPSConnectionPool(host='stats.nba.com', port=443): Read timed out. (read timeout=30)
def nba_stats_grabber(player_name):
    pd.set_option('display.max_columns', None)  
    if (player_name == 'OG Anunoby'):
        player_name = 'O.G. Anunoby'
    player = players.find_players_by_full_name(player_name)
    player_statistics = playercareerstats.PlayerCareerStats(player[0]['id']).get_data_frames()[0].tail(1)
    #     PLAYER_ID SEASON_ID LEAGUE_ID     TEAM_ID TEAM_ABBREVIATION  PLAYER_AGE  \
    # 19       2544   2022-23        00  1610612747               LAL        38.0   

    #     GP  GS     MIN  FGM   FGA  FG_PCT  FG3M  FG3A  FG3_PCT  FTM  FTA  FT_PCT  \
    # 19  51  50  1818.0  563  1128   0.499   103   340    0.303  239  312   0.766

    #     OREB  DREB  REB  AST  STL  BLK  TOV  PF   PTS
    # 19    64   368  432  350   47   29  160  85  1468
    playerObj = classes.Player(player_name, player_statistics.iloc[0]['FGA'], player_statistics.iloc[0]['FTA'], player_statistics.iloc[0]['FGM'], player_statistics.iloc[0]['FTM'], player_statistics.iloc[0]['FG3M'], player_statistics.iloc[0]['PTS'], player_statistics.iloc[0]['REB'], player_statistics.iloc[0]['AST'], player_statistics.iloc[0]['STL'], player_statistics.iloc[0]['BLK'], player_statistics.iloc[0]['TOV'], player_statistics.iloc[0]['GP'])
    time.sleep(2)
    print("Found Player: " + player_name)
    return playerObj
# team comparison
def team_comparison(team1, team2):
    #initialize team stats list
    team_stats = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    team_stats[0] = team1.return_fg_z_score() - team2.return_fg_z_score()
    team_stats[1] = team1.return_ft_z_score() - team2.return_ft_z_score()
    team_stats[2] = team1.return_threes_average() - team2.return_threes_average()
    team_stats[3] = team1.return_pts_average() - team2.return_pts_average()
    team_stats[4] = team1.return_reb_average() - team2.return_reb_average()
    team_stats[5] = team1.return_ast_average() - team2.return_ast_average()
    team_stats[6] = team1.return_stl_average() - team2.return_stl_average()
    team_stats[7] = team1.return_blk_average() - team2.return_blk_average()
    team_stats[8] = team1.return_tov_average() - team2.return_tov_average()
    return team_stats
#print team comparison
def print_team_comparison(team_stats):      
    print("Team Comparison: ")
    print("---------------------------------")
    print("FG%: " + print_team_comparison_helper(team_stats[0]))
    print("FT%: " + print_team_comparison_helper(team_stats[1]))
    print("3PTM: " + print_team_comparison_helper(team_stats[2]))
    print("PTS: " + print_team_comparison_helper(team_stats[3]))
    print("REB: " + print_team_comparison_helper(team_stats[4]))
    print("AST: " + print_team_comparison_helper(team_stats[5]))
    print("STL: " + print_team_comparison_helper(team_stats[6]))
    print("BLK: " + print_team_comparison_helper(team_stats[7]))
    print("TO: " + print_team_comparison_helper(team_stats[8]))
    print("---------------------------------")
def print_team_comparison_helper(team_stats, cat):
    return_string = ''
    if (cat == 'FG%' or cat == 'FT%'):
        if (team_stats < 0):
            team_stats = team_stats * -1
            return_string = str(round_up(team_stats)) + '% losing'
            return return_string
        else:
            return_string = str(round_up(team_stats)) + '% winning'
            return return_string
    if (team_stats < 0):
        team_stats = team_stats * -1
        return_string = str(round_up(team_stats)) + ' losing'
        return return_string
    else:
        return_string = str(round_up(team_stats)) + ' winning'
        return return_string


############################################################################################################
def display_team_category_stats(team_cat_stats, team_name, fga, fta):
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
    print("Total Field Goal Percentage: " + "{:.3f}".format(round(fga, 3)))
    print("Total Free Throw Percentage: " + "{:.3f}".format(round(fta, 3)))
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
            team_cat_stats['FG%'] == float(get_fga_total_average(curr_team, league))
            team_cat_stats['FT%'] == float(get_fta_total_average(curr_team, league))
            for player in curr_roster:
                curr_player = league.player_stats(player['player_id'], 'average_season')
                if curr_player[0]['PTS'] == '-':
                    break
                team_cat_stats['PTS'] += float(curr_player[0]['PTS'])
                team_cat_stats['REB'] += float(curr_player[0]['REB'])
                team_cat_stats['AST'] += float(curr_player[0]['AST'])
                team_cat_stats['ST'] += float(curr_player[0]['ST'])
                team_cat_stats['BLK'] += float(curr_player[0]['BLK'])
                # team_cat_stats['FG%'] += float(curr_player[0]['FG%'])
                # team_cat_stats['FT%'] += float(curr_player[0]['FT%'])
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
    print("Total Field Goal Percentage: " + str(round(team_comparison_dict['FG%'], 3)) + " In favour of " + display_in_favour_of(team_comparison_dict['FG%'], team_name1, team_name2))
    print("Total Free Throw Percentage: " + str(round(team_comparison_dict['FT%'], 3)) + " In favour of " + display_in_favour_of(team_comparison_dict['FT%'], team_name1, team_name2))
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
def get_fga_total_average(curr_team, league):
    fga = 0
    fgm = 0
    fgp = 0
    teams = league.teams()
    for team in teams:
        if curr_team == teams[team]['name']:
            curr_key = teams[team]['team_key']
            curr_team = league.to_team(curr_key)
            curr_roster = curr_team.roster()
            for player in curr_roster:
                curr_player_details = league.player_details(player['name'])
                fgaftm = (curr_player_details[0]['player_stats']['stats'][0]['stat']['value'])
                if fgaftm == '-/-':
                    continue
                # add two fractions together
                fga = fgaftm.split('/')[1]
                fgm = fgaftm.split('/')[0]
                fgp = float(fgm) / float(fga)
    return fgp
def get_fta_total_average(curr_team, league):
    fga = 0
    fgm = 0
    fgp = 0
    teams = league.teams()
    for team in teams:
        if curr_team == teams[team]['name']:
            curr_key = teams[team]['team_key']
            curr_team = league.to_team(curr_key)
            curr_roster = curr_team.roster()
            for player in curr_roster:
                curr_player_details = league.player_details(player['name'])
                fgaftm = (curr_player_details[0]['player_stats']['stats'][2]['stat']['value'])
                if fgaftm == '-/-':
                    continue
                # add two fractions together
                fga = fgaftm.split('/')[1]
                fgm = fgaftm.split('/')[0]
                fgp = float(fgm) / float(fga)
    return fgp



    