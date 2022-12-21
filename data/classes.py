class Player:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
    def add_player(self, player):
        self.players.append(player)