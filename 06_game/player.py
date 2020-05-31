from object import GameObject

from weapon import Weapon

class Player(GameObject):
    def __init__(self, row, col, game):
        super().__init__("PLAYER", row, col, game)
        self.type = "PLAYER"

        # Add player to the game
        self.game.player = self

        # How many frames player must wait after attacking to act again.
        self.attack_speed = int(self.game.framerate / 4)  # 1/4 second

        # Current number of frames to wait.
        self.cooldown = 0

        # Direction the player is facing
        self.facing = "east"

        # Number of squares the player's weapon will extend.
        self.weapon_size = 2

        # This has no purpose other than score.
        self.gold = 0

    def process_command(self, c):
        directions = {"w": "north", "a": "west", "s": "south", "d": "east"}
        # Check if `c` is a valid directional input
        if c in directions:
            # Move and update the direction player is facing
            self.move(directions[c])
            self.facing = directions[c]

        elif c == "p":  # 'p' to attack
            self.attack()

    def object_collision(self, collision_object):
        # Player dies upon collision with any objects besides
        # treasure
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
        # Spawn a weapon in the direction player is facing
        w = Weapon("WEAPON", self.row, self.col, self.facing, self.attack_speed, self.weapon_size, self.game)

        # Cooldown lasts one frame longer than weapon.
        # This prevents player from walking into their weapon and dying.
        self.cooldown = self.attack_speed + 1

    # Get gold upon collecting treasure
    def collect_treasure(self, item):
        if item.type == "TREASURE":
            self.gold += item.value


