from enemy import Enemy


class Snake(Enemy):
    def __init__(self, row, col, game):
        super().__init__("S", row, col, 800, 0.2, game)
