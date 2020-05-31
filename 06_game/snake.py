from enemy import Enemy
import random

class Snake(Enemy):
    def __init__(self, row, col, game):
        super().__init__("SNAKE", row, col, 1000, 0.5, game)
        self.energy = 3

    def wait(self):
        # Snakes store energy whenever they wait
        super().wait()
        self.energy += 1
        # Some randomization in how long snakes will store energy.
        self.should_wait = self.energy <= random.randint(1, 5)

    def action(self):
        # Snakes will move multiple times in a quick burst,
        # waiting when they run out of energy.
        self.random_move()
        self.frame_to_act += int(1 * self.move_speed)
        self.energy -= 1
        if self.energy <= 0:
            self.should_wait = True


