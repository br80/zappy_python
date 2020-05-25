from enemy import Enemy


class Goblin(Enemy):
    def __init__(self, row, col, game):
        super().__init__("😈", row, col, 200, 0.5, game)
