from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa

# connect to yahoo fantasy api
filename = "../outh2.json"
sc = OAuth2(None, None, from_file=filename)

# get game object
gm = yfa.Game(sc, 'nba')

# get league ids in year 2022
lg = gm.league_ids(2022)

# create a league object of OGLeague(code 418.l.16470)
OGLeague = gm.to_league(lg[1])

teams = OGLeague.teams()
# get all teams in league
for team in teams:
    print(teams[team]['name'])
# ask for team name
team_name = input("Enter first team name: ")
team_name2 = input("Enter second team name: ")
# print team entered
for team in teams:
    if team_name == teams[team]['name'] or team_name2 == teams[team]['name']:
        # create stats category variables
        total_pts = 0
        total_reb = 0
        total_ast = 0
        total_stl = 0
        total_blk = 0
        total_fg = 0
        total_ft = 0
        total_3pt = 0
        total_to = 0
        curr_key = teams[team]['team_key']
        curr_team = OGLeague.to_team(curr_key)
        curr_roster = curr_team.roster()
        for player in curr_roster:
            curr_player = OGLeague.player_stats(player['player_id'], 'average_season')
            total_pts += float(curr_player[0]['PTS'])
            total_reb += float(curr_player[0]['REB'])
            total_ast += float(curr_player[0]['AST'])
            total_stl += float(curr_player[0]['ST'])
            total_blk += float(curr_player[0]['BLK'])
            total_3pt += float(curr_player[0]['3PTM'])
            total_to += float(curr_player[0]['TO'])
        print("Total Points: " + str(round(total_pts, 1)))
        print("Total Rebounds: " + str(round(total_reb, 1)))
        print("Total Assists: " + str(round(total_ast, 1)))
        print("Total Steals: " + str(round(total_stl, 1)))
        print("Total Blocks: " + str(round(total_blk, 1)))    
        print("Total Field Goal Percentage: " + str(total_fg) + "%")
        print("Total Free Throw Percentage: " + str(total_ft) + "%")
        print("Total 3 Pointers: " + str(round(total_3pt, 1)))
        print("Total Turnovers: " + str(round(total_to, 1)))
        print("---------------------------------")

        




