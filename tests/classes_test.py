import unittest
import sys
sys.path.append('..')
import data.classes as classes

class TestPlayer(unittest.TestCase):
    def test_name(self):
        team = classes.Player("Cole Anthony", 202, 55, 88, 50, 25, 251, 89, 90, 16, 8, 35, 20)
        team2 = classes.Player("Malcolm Brogdon", 392, 109, 190, 97, 74, 551, 161, 146, 22, 9, 60, 39)
        self.assertEqual(team.name, "Cole Anthony")
        self.assertEqual(team2.name, "Malcolm Brogdon")
    def test_fg_average(self):
        team = classes.Player("Cole Anthony", 202, 55, 88, 50, 25, 251, 89, 90, 16, 8, 35, 20)
        team2 = classes.Player("Malcolm Brogdon", 392, 109, 190, 97, 74, 551, 161, 146, 22, 9, 60, 39)
        self.assertEqual(team.__calculate_fg_average__(), .436)
        self.assertEqual(team2.__calculate_fg_average__(), .485)
    def test_ft_average(self):
        team = classes.Player("Cole Anthony", 202, 55, 88, 50, 25, 251, 89, 90, 16, 8, 35, 20)
        team2 = classes.Player("Malcolm Brogdon", 392, 109, 190, 97, 74, 551, 161, 146, 22, 9, 60, 39)
        self.assertEqual(team.__calculate_ft_average__(), .909)
        self.assertEqual(team2.__calculate_ft_average__(), .890)
    def test_fg_z_score(self):
        team = classes.Player("Cole Anthony", 202, 55, 88, 50, 25, 251, 89, 90, 16, 8, 35, 20)
        team2 = classes.Player("Malcolm Brogdon", 392, 109, 190, 97, 74, 551, 161, 146, 22, 9, 60, 39)
        self.assertEqual(team.__calulate_fg_z_score__(), -0.353)
        self.assertEqual(team2.__calulate_fg_z_score__(), 0.141)
    def test_threes_average(self):
        team = classes.Player("Cole Anthony", 202, 55, 88, 50, 25, 251, 89, 90, 16, 8, 35, 20)
        team2 = classes.Player("Malcolm Brogdon", 392, 109, 190, 97, 74, 551, 161, 146, 22, 9, 60, 39)
        self.assertEqual(team2.return_threes_average(), 1.9)
        self.assertEqual(team.return_threes_average(), 1.3)
    def test_pts_average(self):
        team = classes.Player("Cole Anthony", 202, 55, 88, 50, 25, 251, 89, 90, 16, 8, 35, 20)
        team2 = classes.Player("Malcolm Brogdon", 392, 109, 190, 97, 74, 551, 161, 146, 22, 9, 60, 39)
        self.assertEqual(team.return_pts_average(), 12.6)
        self.assertEqual(team2.return_pts_average(), 14.1)
    def test_reb_average(self):
        team = classes.Player("Cole Anthony", 202, 55, 88, 50, 25, 251, 89, 90, 16, 8, 35, 20)
        team2 = classes.Player("Malcolm Brogdon", 392, 109, 190, 97, 74, 551, 161, 146, 22, 9, 60, 39)
        self.assertEqual(team.return_reb_average(), 4.5)
        self.assertEqual(team2.return_reb_average(), 4.1)
    def test_ast_average(self):
        team = classes.Player("Cole Anthony", 202, 55, 88, 50, 25, 251, 89, 90, 16, 8, 35, 20)
        team2 = classes.Player("Malcolm Brogdon", 392, 109, 190, 97, 74, 551, 161, 146, 22, 9, 60, 39)
        self.assertEqual(team.return_ast_average(), 4.5)
        self.assertEqual(team2.return_ast_average(), 3.7)
    def test_stl_average(self):
        team = classes.Player("Cole Anthony", 202, 55, 88, 50, 25, 251, 89, 90, 16, 8, 35, 20)
        team2 = classes.Player("Malcolm Brogdon", 392, 109, 190, 97, 74, 551, 161, 146, 22, 9, 60, 39)
        self.assertEqual(team.return_stl_average(), 0.8)
        self.assertEqual(team2.return_stl_average(), 0.6)
    def test_blk_average(self):
        team = classes.Player("Cole Anthony", 202, 55, 88, 50, 25, 251, 89, 90, 16, 8, 35, 20)
        team2 = classes.Player("Malcolm Brogdon", 392, 109, 190, 97, 74, 551, 161, 146, 22, 9, 60, 39)
        self.assertEqual(team.return_blk_average(), 0.4)
        self.assertEqual(team2.return_blk_average(), 0.2)
    def test_to_average(self):
        team = classes.Player("Cole Anthony", 202, 55, 88, 50, 25, 251, 89, 90, 16, 8, 35, 20)
        team2 = classes.Player("Malcolm Brogdon", 392, 109, 190, 97, 74, 551, 161, 146, 22, 9, 60, 39)
        self.assertEqual(team.return_tov_average(), 1.8)
        self.assertEqual(team2.return_tov_average(), 1.5)
    def test_gp(self):
        team = classes.Player("Cole Anthony", 202, 55, 88, 50, 25, 251, 89, 90, 16, 8, 35, 20)
        team2 = classes.Player("Malcolm Brogdon", 392, 109, 190, 97, 74, 551, 161, 146, 22, 9, 60, 39)
        self.assertEqual(team.return_gp(), 20)
        self.assertEqual(team2.return_gp(), 39)

class TestTeam(unittest.TestCase):
    
    def test_name(self):
        team = classes.Team('Duke')
        team2 = classes.Team("Ain't No Jokic", 8.456, 6.864, 20.5, 225.4, 89.5, 44.8, 12.5, 7.0, 28.3)
        self.assertEqual(team.team_name, 'Duke')
        self.assertEqual(team2.team_name, "Ain't No Jokic")
    def test_fg_average(self):
        team = classes.Team('Duke')
        team2 = classes.Team("Ain't No Jokic", 8.456, 6.864, 20.5, 225.4, 89.5, 44.8, 12.5, 7.0, 28.3)
        self.assertEqual(team.return_fg_z_score(), 0)
        self.assertEqual(team2.return_fg_z_score(), 8.456)
    def test_add_player_stats(self):
        team = classes.Team("Ain't No Jokic", 8.456, 6.864, 20.5, 225.4, 89.5, 44.8, 12.5, 7.0, 28.3)
        player = classes.Player("Cole Anthony", 202, 55, 88, 50, 25, 251, 89, 90, 16, 8, 35, 20)
        team.add_player(player)
        self.assertEqual(team.return_fg_z_score(), 8.456 - 0.353)
        self.assertEqual(team.return_blk_average(), 7.0 + 0.4)
    def test_return_players(self):
        team = classes.Team("Ain't No Jokic")
        player = classes.Player("Cole Anthony", 202, 55, 88, 50, 25, 251, 89, 90, 16, 8, 35, 20)
        team.add_player(player)
        self.assertEqual(team.return_ast_average(), 4.5)
        self.assertEqual(team.return_number_of_players(), 1)
