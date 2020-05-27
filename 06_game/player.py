from object import GameObject

from weapon import Weapon

class Player(GameObject):
    def __init__(self, row, col, game):
        super().__init__("PLAYER", row, col, game)
        self.type = "PLAYER"
        self.game.grid[row][col] = self
        self.attack_speed = int(self.game.framerate / 4)  # 1/4 second
        self.cooldown = 0
        self.facing = "east"
        self.weapon_size = 2
        self.gold = 0
        self.game.player = self

    def process_command(self, c):
        directions = {"w": "north", "a": "west", "s": "south", "d": "east"}
        if c in directions:
            self.move(directions[c])
            self.facing = directions[c]
        elif c == "\n":  # Enter/Newline key
            self.attack()

    def object_collision(self, collision_object):
        if collision_object.type == "TREASURE":
            self.gold += collision_object.value
            collision_object.die()
            return True
        else:
            self.die()
            return False

    def die(self):
        self.alive = False
        self.game.game_over()

    def attack(self):
        w = Weapon("WEAPON", self.row, self.col, self.facing, self.attack_speed, self.weapon_size, self.game)
        self.cooldown = self.attack_speed+1  # One frame longer than weapon

    def collect_treasure(self, item):
        if item.type == "TREASURE":
            self.gold += item.value


