'''
Model representing Colley.

todo: docs
todo: inherit from Model?
todo: port with type hints
'''
class Colley:
    
    def __init__(self):
        '''
        todo: this. what fields does it need?
        '''
        pass

    def rank(self) -> List[Team]:
        '''
        Given a matrix, create a power ranking of the teams
        '''
        pass

    def predict_bracket(self) -> Bracket:
        '''
        Given a ranking of the teams, and the draw for the bracket, predict who wins and stuff
        '''
        pass

    @staticmethod
    def from_file(filename: str) -> Colley:
        '''
        todo: docs
        todo: weighting param? does that apply for Colley?

        parse teams and games from file
        create matrix from teams and games
        '''
        pass