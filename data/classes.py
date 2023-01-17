import data.constants as c
import data.helpers as h
from tabulate import tabulate
# create class
class Player:
    def __init__(self, name, fga, fta, fgm, ftm, threes, pts, reb, ast, stl, blk, tov, gp):
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
        d = [self.__name__(), self.__calulate_fg_z_score__(), self.__calculate_ft_z_score__(), self.return_threes_average(), self.return_pts_average(), self.return_reb_average(), self.return_ast_average(), self.return_stl_average(), self.return_blk_avov_average(), self.return_tov_average()];
        print(tabulate([d], headers=['Name', 'FG Z-Score', 'FT Z-Score', '3PM', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TOV'], tablefmt='orgtbl'));
       
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

        
    
