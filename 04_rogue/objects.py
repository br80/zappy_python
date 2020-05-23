import random

class GameObject():
    def __init__(self, name, row, col, game):
        self.name = name
        self.type = "NEUTRAL"
        self.game = game
        if game.grid[row][col] == " " or self.handle_collision(game.grid[row][col]):
            self.row = row
            self.col = col
            game.grid[row][col] = self

    def __str__(self):
        return self.name[0]
    def move(self, direction):
        row = self.row
        col = self.col
        game = self.game
        grid = game.grid
        grid[row][col] = " "
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
        grid[self.row][self.col] = self
        game.draw_grid()
        return moved
    def handle_collision(self, collision_object):
        if collision_object == " ":
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
        """
        Default, do nothing
        """
        pass



class Barrier(GameObject):
    def __init__(self, row, col, game):
        super().__init__("#", row, col, game)
        self.type = "BARRIER"


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
            game.grid[self.row][self.col] = self
            self.frame_to_destroy = game.frame + lifetime
            game.draw_grid()
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
        self.game.draw_grid()





class Player(GameObject):
    def __init__(self, name, row, col, game):
        super().__init__(name, row, col, game)
        self.type = "PLAYER"
        self.game.grid[row][col] = self
        self.attack_speed = int(self.game.framerate / 4)  # 1/4 second
        self.cooldown = 0
        self.facing = "east"
        self.weapon_size = 2
    def process_command(self, c):
        directions = {"w": "north", "a": "west", "s": "south", "d": "east"}
        if c in directions:
            self.move(directions[c])
            self.facing = directions[c]
        elif c == "p":
            self.attack()
    def object_collision(self, collision_object):
        self.die()
        return False
    def die(self):
        print("You have died.")
        self.game.running = False
    def attack(self):
        w = Weapon("+", self.row, self.col, self.facing, self.attack_speed, self.weapon_size, self.game)
        self.cooldown = self.attack_speed+1  # One frame longer than weapon


class Enemy(GameObject):
    def __init__(self, name, row, col, speed, game):
        super().__init__(name, row, col, game)
        self.game.enemies.append(self)
        self.type = "ENEMY"
        self.speed = self.game.framerate * 100 / speed
        self.game.grid[row][col] = self
        self.frame_to_act = int(1 * self.speed)
    def act(self, frame):
        if frame >= self.frame_to_act:
            self.do_action()
            self.frame_to_act += int(1 * self.speed)
    def do_action(self):
          self.random_move()
    def random_move(self):
        move_choices = ["north", "south", "west", "east"]
        # Try again if the move is unsuccessful
        tries = 10
        while tries > 0 and not self.move(random.choice(move_choices)):
            tries -= 1
        self.frame_to_act += self.speed
    def object_collision(self, collision_object):
        if collision_object.type == "PLAYER":
            collision_object.die()
            return True
        elif collision_object.type == "ENEMY":
            return False
        else:
            self.die()
            return False
    def die(self):
        self.game.enemies.remove(self)
        occupant = self.game.grid[self.row][self.col]
        if occupant == self:
            occupant = " "


