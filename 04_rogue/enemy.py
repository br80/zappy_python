import random

from object import GameObject



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
        if self in self.game.enemies:
            self.game.enemies.remove(self)
        occupant = self.game.grid[self.row][self.col]
        if occupant == self:
            occupant = " "

