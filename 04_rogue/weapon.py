from object import GameObject


class Weapon(GameObject):
    def __init__(self, name, player_row, player_col, facing, lifetime, size, game):
        self.name = name
        self.type = "WEAPON"
        self.game = game

        row_col = self.set_row_col(player_row, player_col, facing)
        if row_col and size > 0:
            game.weapons.append(self)
            for enemy in game.enemies:
                if enemy.row == self.row and enemy.col == self.col:
                    enemy.die()
            if game.grid[self.row][self.col] != " " and game.grid[self.row][self.col].type in ["BARRIER", "TREASURE"]:
                if self in self.game.weapons:
                   self.game.weapons.remove(self)
            else:
                game.grid[self.row][self.col] = self
                self.frame_to_destroy = game.frame + lifetime
                game.refresh_screen()
                Weapon(name, self.row, self.col, facing, lifetime, size-1, game)

    def set_row_col(self, player_row, player_col, facing):
        self.row = player_row
        self.col = player_col
        if facing == "north" and player_row > 0:
            self.row -= 1
        elif facing == "south" and player_row < self.game.num_rows - 1:
            self.row += 1
        elif facing == "west" and player_col > 0:
            self.col -= 1
        elif facing == "east" and player_col < self.game.num_cols - 1:
            self.col += 1
        else:
            return False
        return True
    def act(self, frame):
        if frame >= self.frame_to_destroy:
            self.die()
    def die(self):
        self.game.grid[self.row][self.col] = " "
        self.game.weapons.remove(self)
        self.game.refresh_screen()



