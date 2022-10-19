class Player: 
    def __init__(self, human, ai) -> None:
        self.human = human
        self.ai = ai

    def player_one(self): 
        self.player_one = self.human
    input('Please select number of players: 1, 2, or 3: ') 
   
    
    def player_two(self): 
        self.player_two = self.ai
    print('Player 2 is an ai player')

    def player_three(self):
        self.player_three = ['Human, AI']
    input('Choose 1 for human player or 2 for ai player: ' )