import random

from object import GameObject


class Enemy(GameObject):
    def __init__(self, name, row, col, move_speed, wait_time, game):
        super().__init__(name, row, col, game)

        self.type = "ENEMY"

        # Add this to the list of enemies in the game
        self.game.enemies.append(self)

        # Enemies alternate between waiting and moving.
        # This flag is active if the enemy's next action is to wait.
        self.should_wait = True

        # Pause this many frames on each wait
        self.wait_time = int(wait_time * self.game.framerate)

        # This is the next frame to act after a wait or an action.
        # Start the game with a wait.
        self.frame_to_act = self.wait_time

        # How many frames to wait after each move.
        self.move_speed = self.game.framerate * 100 / move_speed   # 100 = 1 second


    def act(self, frame):
        # This gets called every frame but don't do anything
        # unless it's the enemy's frame to act.
        if frame >= self.frame_to_act:
            # Alternate between waiting and action
            if self.should_wait:
                self.wait()
            else:
                self.action()

    # Default enemy action is to move randomly, then wait.
    def action(self):
        self.random_move()
        self.frame_to_act += int(1 * self.move_speed)
        self.should_wait = True


    # Wait is done by incrementing the next action frame
    def wait(self):
        self.frame_to_act += self.wait_time
        self.should_wait = False

    # This will return a list of all valid moves for the enemy.
    def valid_moves(self):
        directions = []

        # If we're not on the top row...
        if self.row > 0:
            object_n = self.game.grid[self.row-1][self.col]
            # and the north is open...
            if object_n == "  " or object_n.type == "PLAYER":
                # then north is a valid enemy move.
                directions.append("north")

        # If we're not on the bottom row...
        if self.row < self.game.rows - 1:
            object_s = self.game.grid[self.row+1][self.col]
            # and the south is open...
            if object_s == "  " or object_s.type == "PLAYER":
                # then south is a valid enemy move.
                directions.append("south")

        # If we're not on the first column...
        if self.col > 0:
            object_w = self.game.grid[self.row][self.col-1]
            # and the west is open...
            if object_w == "  " or object_w.type == "PLAYER":
                # then west is a valid enemy move.
                directions.append("west")

        # If we're not on the last column...
        if self.col < self.game.cols - 1:
            object_e = self.game.grid[self.row][self.col+1]
            # and the east is open...
            if object_e == "  " or object_e.type == "PLAYER":
                # then east is a valid enemy move.
                directions.append("east")

        return directions

    def random_move(self):
        # Get a list of valid moves
        choices = self.valid_moves()
        # If there's at least one, pick one at random
        if len(choices) > 0:
            self.move(random.choice(choices))
        self.frame_to_act += self.move_speed

    def object_collision(self, collision_object):

        # If enemy collides with the player,
        # the player dies.
        if collision_object.type == "PLAYER":
            collision_object.die()
            return True

        # Enemies cannot move on top of enemies.
        elif collision_object.type == "ENEMY":
            return False

        # Default
        else:
            self.die()
            return False

    def die(self):
        # Upon death, remove enemy from the game and grid
        if self in self.game.enemies:
            self.game.enemies.remove(self)
        occupant = self.game.grid[self.row][self.col]
        if occupant == self:
            occupant = "  "

