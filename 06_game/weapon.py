from object import GameObject


class Weapon(GameObject):
    def __init__(self, game_id, player_row, player_col, facing, lifetime, size, game):
        self.game_id = game_id
        self.icon = game.graphics.get_icon(game_id)
        self.type = "WEAPON"
        self.game = game
        self.alive = True

        row_col_valid = self.set_row_col(player_row, player_col, facing)

        if row_col_valid and size > 0:

            # Kill any enemies where the weapon has spawned
            for enemy in game.enemies:
                if enemy.row == self.row and enemy.col == self.col:
                    enemy.die()

            # Weapons cannot spawn on barriers or treasures
            if game.grid[self.row][self.col] != "  " and game.grid[self.row][self.col].type in ["BARRIER", "TREASURE"]:
                if self in self.game.weapons:
                   self.game.weapons.remove(self)

            # Otherwise, spawn the weapon
            else:
                game.weapons.append(self)
                game.grid[self.row][self.col] = self
                self.frame_to_destroy = game.frame + lifetime
                game.draw_screen()

                # If weapon size is greater than 1, keep spawning weapons
                Weapon(game_id, self.row, self.col, facing, lifetime, size-1, game)

    def set_row_col(self, player_row, player_col, facing):
        # Starting from the origin position, spawn the weapon one block
        # in the given direction.
        self.row = player_row
        self.col = player_col
        if facing == "north" and player_row > 0:
            self.row -= 1
        elif facing == "south" and player_row < self.game.rows - 1:
            self.row += 1
        elif facing == "west" and player_col > 0:
            self.col -= 1
        elif facing == "east" and player_col < self.game.cols - 1:
            self.col += 1
        else:
            return False
        return True

    def act(self, frame):
        if frame >= self.frame_to_destroy:
            self.die()

    def die(self):
        self.game.grid[self.row][self.col] = "  "
        self.game.weapons.remove(self)
        self.game.draw_screen()



