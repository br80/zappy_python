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

        # Create the display grid
        self.grid = []
        for i in range(self.rows):
            # Append a row of dots to the grid
            self.grid.append(["."] * self.cols)

        # Create a moveable object at position (5, 5)
        self.obj = Object("o", 5, 5, self)

    def process_command(self, c):
        # Process w/a/s/d inputs into directional movement
        directions = {"w": "north", "a": "west", "s": "south", "d": "east"}
        if c in directions:
            # Move in the direction specified
            self.obj.move(directions[c])

    def print_screen(self):
        clear_screen()

        # Print each row in the grid
        for row in self.grid:
            # Make sure every character in the row is a string
            char_row = [str(c) for c in row]
            # Separate each character in the row with a single space
            print(' '.join(char_row))
        print("Type `w`, `a`, `s`, `d` to move.")
        print("Type `q` to quit.")

    def run(self):

        self.print_screen()

        kb = kbhit.KBHit()

        while self.running:

            if kb.kbhit():
                c = kb.getch()
                if c == "q":  # Hit `q` to break out of the loop
                    self.running = False
                self.process_command(c)

                self.print_screen()

        kb.set_normal_term()  # Reset terminal to normal


d = Display()
d.run()

