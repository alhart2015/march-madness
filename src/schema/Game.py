'''
Class to represent a game played in the schedule. Has a two competitors, a location, and a score

todo: type hints
todo: evaluate whether this is good enough

if team_1 is home, location = 1
if team_2 is home, location = 2
if neutreal site, location = 0
'''
class Game:

    def __init__(self, team_1, team_2, score_1, score_2, location, date):
        self.team_1 = team_1
        self.team_2 = team_2
        self.score_1 = score_1
        self.score_2 = score_2
        self.location = location
        self.date = date

    def is_neutral_site(self):
        return self.location == 0

    def home_team(self):
        if self.location == 0:
            raise RuntimeError("Game is neutral site game:", self)

        if self.location == 1:
            return self.team_1

        if self.location == 2:
            return self.team_2

        raise RuntimeError("Unexpected location for game:", self)


    def __str__(self):
         return 'Game on {0}. {1} {2}, {3} {4}. Location: {5}'.format(self.date, self.team_1, self.score_1, self.team_2, self.score_2, self.location)

    def __repr__(self):
        return 'Game on {0}. {1} {2}, {3} {4}. Location: {5}'.format(self.date, self.team_1, self.score_1, self.team_2, self.score_2, self.location)