class Player:
    def __init__(self, name, lastPoint=False, lastAction='', speed=0, skill=0, point=0):
        self.name = name
        self.lastAction = lastAction
        self.speed = speed
        self.skill = skill
        self.points = point
        self.lastPoint = lastPoint

    def __str__(self):
        return self.name

    def resetAction(self):
        self.lastAction = ''

    def addPoint(self):
        self.points += 1
        self.lastPoint = True

    def resetPoints(self):
        self.points = 0

    def resetLastPoint(self):
        self.lastPoint = False
