from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import data.constants as constants
import data.helpers as helpers
import data.classes as classes

def main():
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
    print("------------------------------------")
    print("Enter the two teams you would like to compare")
    team_name = input("Enter first team name: ")
    team_name2 = input("Enter second team name: ")
    print("------------------------------------")
    # print team entered
    team1 = helpers.find_team(team_name, OGLeague)
    team2 = helpers.find_team(team_name2, OGLeague)

    roster1 = team1.roster()
    for player in roster1:
        helpers.nba_stats_grabber(player['name'])

    # helpers.display_team_category_stats(helpers.calculate_team_category_stats(OGLeague, team_name), team_name, helpers.get_fga_total_average(team_name, OGLeague), helpers.get_fta_total_average(team_name, OGLeague))
    # helpers.display_team_category_stats(helpers.calculate_team_category_stats(OGLeague, team_name2), team_name2, helpers.get_fga_total_average(team_name2, OGLeague), helpers.get_fta_total_average(team_name2, OGLeague))

    # helpers.display_team_comparison(helpers.calculate_team_category_stats(OGLeague, team_name), helpers.calculate_team_category_stats(OGLeague, team_name2), team_name, team_name2)

if __name__ == "__main__":
    main()





