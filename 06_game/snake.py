from enemy import Enemy
import random

class Snake(Enemy):
    def __init__(self, row, col, game):
        super().__init__("🐍", row, col, 1000, 0.5, game)
        self.energy = 3

    def action(self):
        self.random_move()
        self.frame_to_act += int(1 * self.speed)
        self.energy -= 1
        if self.energy <= 0:
            self.should_wait = True

    def wait(self):
        super().wait()
        self.energy += 1
        self.should_wait = self.energy <= random.randint(1, 5)


