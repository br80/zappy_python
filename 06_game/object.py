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

        # As long as the object survived, place it in the grid
        if self.alive:
            grid[self.row][self.col] = self

        # If the object moved, draw the screen
        if moved:
            game.draw_screen()

    # This is called when the object tries to move
    # into a new space.
    # It will return True if the move succeeds
    # and False otherwise.
    def handle_collision(self, collision_object):
        if collision_object == "  ":
            # Empty spaces are fine.
            return True
        elif collision_object.type == "BARRIER":
            # Nothing can walk through a barrier
            return False
        elif collision_object.type == "WEAPON":
            # Anything that walks into a weapon will die
            self.die()
            return False

        # For object collisions that are not empty, barrier, or a weapon,
        # call this method.
        return self.object_collision(collision_object)

    # Handle unique collisions. Implemented by child-classes
    def object_collision(self, collision_object):
        return False

    def die(self):
        self.alive = False



