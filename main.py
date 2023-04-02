# interesting, the timeouts are not happening anymore. I used to get timeouts nearly all the time when requesting data
# from the nba api. Now that I added a time.sleep(2) in the nba_stats_grabber function, I am not getting timeouts anymore
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import data.constants as constants
import data.helpers as helpers
import data.classes as classes
from PyQt5.QtWidgets import *

def main():
    league = classes.YahooFantasyApi('outh2.json')
    league.get_league()
    league.find_and_compare_two_teams()
 

if __name__ == "__main__":
    main()





