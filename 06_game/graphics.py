class Graphics
    def __init__(self, mode, game):
        self.game = game
        self.mode = mode
        self.default_mode = "ascii"
        self.icons = {
                      "SNAKE": {
                          "ascii": "S ",
                          "emoji": "🐍"
                      },
                      "GOBLIN": {
                          "ascii": "G ",
                          "emoji": "😈"
                      },
                      "PLAYER": {
                              "ascii": "P ",
                              "emoji": "😀"
                      },
                      "WEAPON": {
                              "ascii": "+ ",
                              "emoji": "🔥"
                      },
                      "EMPTY": {
                              "ascii": "  ",
                              "emoji": "  "
                      },
                     }

        def get_icon(self, icon_id):
            if icon_id in self.icons:
                icons = self.icons[icon_id]
                if self.mode in icons:
                    return icons[self.mode]
                return icons[self.default_mode]

