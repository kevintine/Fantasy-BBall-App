import data.constants as c
import data.helpers as h
from tabulate import tabulate

categories = ['FG%', 'FT%', '3PM', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TOV']

class Player:
    def __init__(self, name, fga = 0, fta = 0, fgm = 0, ftm = 0, threes = 0, pts = 0, reb = 0, ast = 0, stl = 0, blk = 0, tov = 0, gp = 0):
        self.name = name
        self.fga = fga
        self.fta = fta
        self.fgm = fgm
        self.ftm = ftm
        self.threes = threes
        self.pts = pts
        self.reb = reb
        self.ast = ast
        self.stl = stl
        self.blk = blk
        self.tov = tov
        self.gp = gp
    # create copy method
    def copy(self):
        return Player(self.name, self.fga, self.fta, self.fgm, self.ftm, self.threes, self.pts, self.reb, self.ast, self.stl, self.blk, self.tov, self.gp)
    def __name__(self):
        return self.name
    def __calculate_fg_average__(self):
        return round(self.fgm / self.fga, 3)
    def __calculate_ft_average__(self):
        return round(self.ftm / self.fta, 3)
    def __calulate_fg_z_score__(self):
        x = self.__calculate_fg_average__() - c.league_fg
        z_score = x * round(self.fga/self.gp, 1)
        return round(z_score, 3)
    def __calculate_ft_z_score__(self):
        x = self.__calculate_ft_average__() - c.league_ft
        z_score = x * round(self.fta/self.gp, 1)
        return round(z_score, 3)
    def return_threes_average(self):
        return h.round_up(self.threes / self.gp)
    def return_pts_average(self):
        return h.round_up(self.pts / self.gp)
    def return_reb_average(self):
        return h.round_up(self.reb / self.gp)
    def return_ast_average(self):
        return h.round_up(self.ast / self.gp)
    def return_stl_average(self):
        return h.round_up(self.stl / self.gp)
    def return_blk_average(self):
        return h.round_up(self.blk / self.gp)
    def return_tov_average(self):
        return h.round_up(self.tov / self.gp)
    def return_gp(self):
        return self.gp
    def display(self):
        table_data = [self.__name__(), self.__calculate_fg_average__(), self.__calculate_ft_average__(), self.return_threes_average(), self.return_pts_average(), self.return_reb_average(), self.return_ast_average(), self.return_stl_average(), self.return_blk_average(), self.return_tov_average()]
        print(tabulate([table_data], headers = ['Name', 'FG%', 'FT%', '3PM', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TOV'], tablefmt = 'orgtbl'))          
class Team:
    def __init__(self, team_name = '', fg_z_score = 0, ft_z_score = 0, threes = 0, pts = 0, reb =  0, ast = 0, stl = 0, blk = 0, tov = 0, players = None):
        self.team_name = team_name
        self.fg_z_score = fg_z_score
        self.ft_z_score = ft_z_score
        self.threes = threes
        self.pts = pts
        self.reb = reb
        self.ast = ast
        self.stl = stl
        self.blk = blk
        self.tov = tov
        if (players == None):
            players = []
        self.players = players
    def add_player(self, player):
        self.fg_z_score += player.__calulate_fg_z_score__()
        self.ft_z_score += player.__calculate_ft_average__()
        self.threes += player.return_threes_average()
        self.pts += player.return_pts_average()
        self.reb += player.return_reb_average()
        self.ast += player.return_ast_average()
        self.stl += player.return_stl_average()
        self.blk += player.return_blk_average()
        self.tov += player.return_tov_average()
        self.players.append(player)
    def __name__(self):
        return self.team_name
    def return_fg_z_score(self):
        return self.fg_z_score
    def return_ft_z_score(self):
        return self.ft_z_score
    def return_threes_average(self):
        return self.threes
    def return_pts_average(self):
        return self.pts
    def return_reb_average(self):
        return self.reb
    def return_ast_average(self):
        return self.ast
    def return_stl_average(self):
        return self.stl
    def return_blk_average(self):
        return self.blk
    def return_tov_average(self):
        return self.tov
    def return_number_of_players(self):
        return self.players.__len__()
    def display(self):
        table_data = [self.__name__(), self.return_fg_z_score(), self.return_ft_z_score(), self.return_threes_average(), self.return_pts_average(), self.return_reb_average(), self.return_ast_average(), self.return_stl_average(), self.return_blk_average(), self.return_tov_average()]
        print(tabulate([table_data], headers = ['Name', 'FG%', 'FT%', '3PM', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TOV'], tablefmt = 'orgtbl'))
# takes two teams to initialize this class
# will compare the two teams and recommend a player to trade for
class Analyzer:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
    def team_comparison(self):
        team_stats = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        team_stats[0] = self.team1.return_fg_z_score() - self.team2.return_fg_z_score()
        team_stats[1] = self.team1.return_ft_z_score() - self.team2.return_ft_z_score()
        team_stats[2] = self.team1.return_threes_average() - self.team2.return_threes_average()
        team_stats[3] = self.team1.return_pts_average() - self.team2.return_pts_average()
        team_stats[4] = self.team1.return_reb_average() - self.team2.return_reb_average()
        team_stats[5] = self.team1.return_ast_average() - self.team2.return_ast_average()
        team_stats[6] = self.team1.return_stl_average() - self.team2.return_stl_average()
        team_stats[7] = self.team1.return_blk_average() - self.team2.return_blk_average()
        team_stats[8] = self.team1.return_tov_average() - self.team2.return_tov_average()
        return team_stats
    def display(self):
        # one way of printing it
        comparing_team_stats = self.team_comparison()
        for stat in comparing_team_stats:
            print(stat)
        # another way of printing it
        table_data = [self.team_comparison()]
        print(tabulate(table_data, headers = ['FG%', 'FT%', '3PM', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TOV'], tablefmt = 'orgtbl'))
# initilaize the yahoo api
class YahooFantasyApi:
    def __init__(self, filename):
        self.filename = filename
    def get_league(self):
        return 0



        



    

