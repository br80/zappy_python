import time

import os
import kbhit # https://simondlevy.academic.wlu.edu/files/software/kbhit.py

from object import Object

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Display:

    def __init__(self):

        self.running = True

        self.rows = 10
        self.cols = 20

        self.grid = []
        for i in range(self.rows):
          self.grid.append(["."] * self.cols)

        self.obj = Object("o", 5, 5, self)

    def process_command(self, c):
        directions = {"w": "north", "a": "west", "s": "south", "d": "east"}
        if c in directions:
            self.obj.move(directions[c])

    def print_screen(self):
        clear_screen()
        for row in self.grid:
            char_row = [str(c) for c in row]
            print(' '.join(char_row))
        print("Type `q` to quit")

    def run(self):

        self.print_screen()

        kb = kbhit.KBHit()

        while self.running:

            if kb.kbhit():
                c = kb.getch()
                if c == "q":  # Hit `q` to break out of the loop
                    break
                self.process_command(c)
                last_c = c

                self.print_screen()
                print(f"Last character is: [{last_c}]")

        kb.set_normal_term()  # Reset terminal to normal




d = Display()
d.run()

