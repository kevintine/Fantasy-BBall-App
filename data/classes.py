class Player:
    def __init__(self, name, pts, pf, tov, blk, stl, ast, rb):
        self.name = name
        self.pts = pts
        self.pf = pf
        self.tov = tov
        self.blk = blk
        self.stl = stl
        self.ast = ast
        self.rb = rb
    def get_name(self):
        return self.name
class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
    def add_player(self, player):
        self.players.append(player)