from playerFile import Player


class Opponent(Player):
    # def __init__(self, name, rating='', speed=10, skill=10, point=0):
    #     super().__init__(name, speed, skill, point)
    #     self.rating = rating
    def __init__(self, name, rating='', speed=0, skill=0, experience=0, point=0, lastPoint=False, lastAction=''):
        super().__init__(name, speed, skill, experience, point, lastPoint, lastAction)
        self.rating = rating

    def __str__(self):
        return self.name + ' - Rating: ' + self.rating
