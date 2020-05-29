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
        display = self.display
        grid = display.grid
        grid[row][col] = "."
        if direction == "north" and row > 0:
            row -= 1
        elif direction == "south" and row < self.display.num_rows - 1:
            row += 1
        elif direction == "west" and col > 0:
            col -= 1
        elif direction == "east" and col < self.display.num_cols - 1:
            col += 1
        self.row = row
        self.col = col
        grid[row][col] = self
        display.draw_screen()
