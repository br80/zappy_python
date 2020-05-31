from object import GameObject


class Treasure(GameObject):
    def __init__(self, row, col, game):
        super().__init__("TREASURE", row, col, game)
        self.type = "TREASURE"
        self.game.treasures.append(self)

        # How much gold the player gets upon collecting
        self.value = 100

    def die(self):
        self.game.grid[self.row][self.col] = "  "
        self.game.treasures.remove(self)
        self.game.draw_screen()
        if len(self.game.treasures) == 0:
            self.game.do_win()
