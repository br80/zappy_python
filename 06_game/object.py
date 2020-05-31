import random
from graphics import Graphics

class GameObject():
    def __init__(self, game_id, row, col, game):
        self.game_id = game_id
        self.icon = game.graphics.get_icon(game_id)
        self.type = "NEUTRAL"
        self.game = game
        self.alive = True
        if game.grid[row][col] == "  " or self.handle_collision(game.grid[row][col]):
            self.row = row
            self.col = col
            game.grid[row][col] = self

    def __str__(self):
        return self.icon

    def move(self, direction):
        row = self.row
        col = self.col
        game = self.game
        grid = game.grid
        grid[row][col] = "  "
        if direction == "north" and row > 0:
            row -= 1
        elif direction == "south" and row < self.game.rows - 1:
            row += 1
        elif direction == "west" and col > 0:
            col -= 1
        elif direction == "east" and col < self.game.cols - 1:
            col += 1
        # If the collision is valid (True), update position
        moved = self.handle_collision(grid[row][col])
        if moved:
            self.row = row
            self.col = col
        if self.alive:
            grid[self.row][self.col] = self
        game.draw_screen()
        return moved

    def handle_collision(self, collision_object):
        if collision_object == "  ":
            return True
        elif collision_object.type == "BARRIER":
            return False
        elif collision_object.type == "WEAPON":
            self.die()
            return False
        return self.object_collision(collision_object)

    def object_collision(self, collision_object):
        """
        Default, do nothing
        """
        return False

    def die(self):
        self.alive = False



