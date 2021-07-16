"""
Define a class, which have a class parameter and have a same instance parameter.
"""


class Player:
    def __init__(self, name, club, position):
        self.name = name
        self.club = club
        self.position = position


player1 = Player('Chiesa', 'Juventus', 'Winger')
print(f'{player1.name} plays for {player1.club} club')
