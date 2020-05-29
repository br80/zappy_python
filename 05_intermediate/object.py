class Object:
    def __init__(self, character, row, col, display):
        self.display_char = character
        self.row = row
        self.col = col

        self.display = display
        self.display.grid[row][col] = self
        self.display.objects.append(self)

    def __str__(self):
        return self.display_char

    def move(self, direction):
        row = self.row
        col = self.col
        game = self.game
        grid = game.grid
        grid[row][col] = "  "
        if direction == "north" and row > 0:
            row -= 1
        elif direction == "south" and row < self.game.num_rows - 1:
            row += 1
        elif direction == "west" and col > 0:
            col -= 1
        elif direction == "east" and col < self.game.num_cols - 1:
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