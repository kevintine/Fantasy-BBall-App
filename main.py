from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import data.constants as constants
import data.helpers as helpers

# connect to yahoo fantasy api
filename = "outh2.json"
sc = OAuth2(None, None, from_file=filename)

# get game object
gm = yfa.Game(sc, 'nba')

# get league ids in year 2022
lg = gm.league_ids(constants.CURRENT_YEAR)

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
helpers.display_team_category_stats(helpers.calculate_team_category_stats(OGLeague, team_name), team_name)
helpers.display_team_category_stats(helpers.calculate_team_category_stats(OGLeague, team_name2), team_name2)

helpers.display_team_comparison(helpers.calculate_team_category_stats(OGLeague, team_name), helpers.calculate_team_category_stats(OGLeague, team_name2), team_name, team_name2)
print("Based off of this comparison, your top waiver wire picks should be:")
players = OGLeague.waivers()
print(players)


