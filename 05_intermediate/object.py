class Object:
    def __init__(self, character, row, col, display):
        self.display_char = character
        self.row = row
        self.col = col

        self.display = display
        self.display.grid[row][col] = self


    def __str__(self):
        return self.display_char


    def move(self, direction):
        # Set the current position to empty
        self.display.grid[self.row][self.col] = "."
        # If we're not in the top row, move up one row
        if direction == "north" and self.row > 0:
            self.row -= 1
        # If we're not in the last row, move down one row
        elif direction == "south" and self.row < self.display.rows - 1:
            self.row += 1
        # If we're not in the far-left column, move left one column
        elif direction == "west" and self.col > 0:
            self.col -= 1
        # If we're not in the far-right column, move right one column
        elif direction == "east" and self.col < self.display.cols - 1:
            self.col += 1
        # Put ourself in the updated grid position
        self.display.grid[self.row][self.col] = self
