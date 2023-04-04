# interesting, the timeouts are not happening anymore. I used to get timeouts nearly all the time when requesting data
# from the nba api. Now that I added a time.sleep(2) in the nba_stats_grabber function, I am not getting timeouts anymore
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import data.constants as constants
import data.helpers as helpers
import data.classes as classes
from PyQt5.QtWidgets import *

def main():
    nbaApi = classes.NBAApiClassHelper()
    player = nbaApi.get_player_stats("Lebron James", 5)
    player2 = helpers.nba_stats_grabber("Lebron James")
    player.display()
    player2.display()

    # league = classes.YahooFantasyApi('outh2.json')
    # league.get_league()
    # print("Enter the two teams you would like to compare")
    # team1_name = input("Enter first team name: ")
    # team2_name = input("Enter second team name: ")
    # print("------------------------------------")
    # team1 = league.get_team(team1_name)
    # team2 = league.get_team(team2_name)
    # team1.display()
    # team2.display()
    # comparison = classes.Analyzer(team1, team2)
    # comparison.display()
 

if __name__ == "__main__":
    main()





