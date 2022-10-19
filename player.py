class Player: 
    def __init__(self, human, ai) -> None:
        self.human = human
        self.ai = ai

    def player_one(self): 
        self.player_one = self.human
    input('Please select number of players: 1, 2, or 3: ') 
   