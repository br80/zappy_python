from object import GameObject


class Treasure(GameObject):
    def __init__(self, row, col, game):
        super().__init__("Treasure", row, col, game)
        self.type = "TREASURE"
        self.game.treasures.append(self)
        self.value = 100
    def act(self, frame):
        if frame >= self.frame_to_destroy:
            self.die()
    def die(self):
        self.game.grid[self.row][self.col] = " "
        self.game.treasures.remove(self)
        self.game.draw_grid()
        if len(self.game.treasures) == 0:
            self.game.do_win()
