class Player:
    def __init__(self, name, speed=0, skill=0, experience=0, point=0, lastPoint=False, lastAction='', ):
        self.name = name
        self.lastAction = lastAction
        self.experience = experience
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
