class Object:
    def __init__(self, character, row, col, display):
        self.display_char = character
        self.row = row
        self.col = col

        self.display = display
        self.display.grid[row][col] = self
        self.display.objects.append(self)

        self.frame_to_act = 0
        self.x = col
        self.y = row
        self.v_x = -0.1
        self.v_y = 0.05

    def __str__(self):
        return self.display_char


    def act(self, frame):
        old_x = self.col
        old_y = self.row
        self.x += self.v_x
        self.y += self.v_y

        if int(self.x) > old_x:
            self.move("east")
        elif int(self.x) < old_x:
            self.move("west")
        if int(self.y) > old_y:
            self.move("south")
        elif int(self.y) < old_y:
            self.move("north")

        if self.x < 0.5:
            self.x = 0.5
            self.v_x *= -1
        if self.x > self.display.num_cols - 0.5:
            self.x = self.display.num_cols - 0.5
            self.v_x *= -1
        if self.y < 0.5:
            self.y = 0.5
            self.v_y *= -1
        if self.y > self.display.num_rows - 0.5:
            self.y = self.display.num_rows - 0.5
            self.v_y *= -1



    def move(self, direction):
        row = self.row
        col = self.col
        display = self.display
        grid = display.grid
        grid[row][col] = "."
        if direction == "north":
            if row > 0:
                row -= 1
                self.y -= 1
        elif direction == "south":
            if row < self.display.num_rows - 1:
                row += 1
                self.y += 1
        elif direction == "west":
            if col > 0:
                col -= 1
                self.col -= 1
        elif direction == "east":
            if col < self.display.num_cols - 1:
                col += 1
                self.col += 1
        self.row = row
        self.col = col
        grid[row][col] = self
        display.draw_screen()
