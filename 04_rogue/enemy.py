import random

from object import GameObject



class Enemy(GameObject):
    def __init__(self, name, row, col, speed, wait_time, game):
        super().__init__(name, row, col, game)
        self.game.enemies.append(self)
        self.type = "ENEMY"
        self.speed = self.game.framerate * 100 / speed   # 100 = 1 second
        self.game.grid[row][col] = self
        self.wait_time = int(wait_time * self.game.framerate)  # Wait half second
        self.frame_to_act = self.wait_time
        self.is_waiting = True

    def act(self, frame):
        if frame >= self.frame_to_act:
            # Alternate between waiting and action
            if self.is_waiting:
                self.do_action()
                self.is_waiting = False
            else:
                self.do_wait()
                self.is_waiting = True
    def do_action(self):
          self.random_move()
          self.frame_to_act += int(1 * self.speed)
    def do_wait(self):
          self.frame_to_act += self.wait_time

    def valid_moves(self):
        directions = []
        if self.row > 0:
            object_n = self.game.grid[self.row-1][self.col]
            if object_n == " " or object_n.type == "PLAYER":
                directions.append("north")
        if self.row < self.game.num_rows - 1:
            object_s = self.game.grid[self.row+1][self.col]
            if object_s == " " or object_s.type == "PLAYER":
                directions.append("south")
        if self.col > 0:
            object_w = self.game.grid[self.row][self.col-1]
            if object_w == " " or object_w.type == "PLAYER":
                directions.append("west")
        if self.col < self.game.num_cols - 1:
            object_e = self.game.grid[self.row][self.col+1]
            if object_e == " " or object_e.type == "PLAYER":
                directions.append("east")
        return directions

    def random_move(self):
        move_choices = ["north", "south", "west", "east"]
        # Try again if the move is unsuccessful
        tries = 10
        choices = self.valid_moves()
        if len(choices) > 0:
            self.move(random.choice(choices))
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
        if self in self.game.enemies:
            self.game.enemies.remove(self)
        occupant = self.game.grid[self.row][self.col]
        if occupant == self:
            occupant = " "

