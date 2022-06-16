class GameState:
    def __init__(self):
        self.status = 'init'    # 'init' or 'in progress' or 'exit'
        self.player = None
        self.opponent = None
        self.listOfOpponents = []
        self.result = None      # None or 'player won' or 'opponent won'

    def setStatus(self, status):
        self.status = status

    def setPlayer(self, player):
        self.player = player

    def setOpponent(self, opponent):
        self.opponent = opponent

    def addOpponent(self, opponent):
        self.listOfOpponents.append(opponent)

    def setResult(self, result):
        self.result = result

    def playAgain(self):
        self.player.resetPoints()
        self.opponent.resetPoints()
        self.result = None
        self.status = 'init'

    def exit(self):
        self.setStatus('exit')


gameState = GameState()
