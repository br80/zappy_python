from object import GameObject

class Barrier(GameObject):
    def __init__(self, row, col, game):
        super().__init__("BARRIER", row, col, game)
        self.type = "BARRIER"
