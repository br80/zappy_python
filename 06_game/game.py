import kbhit # https://simondlevy.academic.wlu.edu/files/software/kbhit.py

import os
import time
import csv

from graphics import Graphics

from barrier import Barrier

from player import Player
from treasure import Treasure

from snake import Snake
from goblin import Goblin

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    def __init__(self):
        # Init grid

        # The game will run as long as this is True
        self.running = True
        # When the game is over, show "win" screen if this is True
        self.win = False

        # How often should we check for updates?
        self.framerate = 60  # frames per second
        self.frame = 0  # Start on frame 0

        # Determines which graphics are printed.
        # Defaults to "ascii", or text
        # Change to "emoji" for icons if your OS supports it.
        self.graphics = Graphics("ascii", self)

        # This icon will frame the edges of the map.
        self.border_icon = self.graphics.get_border_icon()

        # When the player uses their weapon, there is a short
        # cooldown before they can act again.
        self.cooldown = 0

        # These contain every weapon, enemy and treasure object in the game
        self.weapons = []
        self.enemies = []
        self.treasures = []

        # At the end of every frame, the display will check this flag
        # and print if this is True.
        # It is reset to False at the end of every frame.
        self.print_this_frame = True

        # Load the map from this path
        self.load_world("data/maze_map.csv")

        self.show_help = True  # Turn this on to display help messages

    # Load the world from CSV
    def load_world(self, world_file=None):
        if world_file is None:
            self.load_default_world()
        else:
            with open(world_file, newline='') as csv_file:
                self.rows = 0
                self.cols = None
                self.grid = []
                file_reader = csv.reader(csv_file)
                for row in file_reader:
                    if self.cols is None:
                        self.cols = len(row)
                    self.grid.append(["  "] * self.cols)
                    col_i = 0
                    for col in row:
                        self.create(col, self.rows, col_i)
                        col_i += 1
                    self.rows += 1

    # Create objects with the given keys:
    #
    # G: Goblin
    # S: Snake
    # #: Barrier
    # P: Player
    # T: Treasure
    def create(self, key, row, col):
        if key == "G":
            Goblin(row, col, self)
        elif key == "S":
            Snake(row, col, self)
        elif key == "#":
            Barrier(row, col, self)
        elif key == "P":
            Player(row, col, self)
        elif key == "T":
            Treasure(row, col, self)

    # Any object can call this function.
    # When print_this_frame is True,
    # the display will print at the end of the frame,
    # then reset print_this_frame back to False
    def draw_screen(self):
        self.print_this_frame = True

    def print_screen(self):

        # Clear the previous display from the screen
        clear_screen()

        # Print a blank line
        print("")
        # Fill the top border with barriers
        print(self.border_icon * (self.cols + 2))
        for row in self.grid:
            char_row = [str(c) for c in row]
            print(f"{self.border_icon}{''.join(char_row)}{self.border_icon}")
        # Fill the bottom border with barriers
        print(self.border_icon * (self.cols + 2))
        # Print a blank line
        print("")
        # Show Player Gold
        print(f"Gold: {self.player.gold}")

        if self.show_help:
            print("")
            print("Type `w`, `a`, `s`, `d` to move.")
            print("Type `p` to attack.")
            print("Type `q` to quit.")

    def game_over(self):
        self.running = False

    def do_win(self):
        self.win = True
        self.game_over()

    def run(self):
        # This is how many seconds each frame should take.
        # E.g. framerate of 10 frames per second is 1/10 sec per frame
        frame_time = 1 / self.framerate

        # Initialize keyboard reader
        kb = kbhit.KBHit()

        # Run this loop each frame
        while self.running:
            # Mark the time at the start of the frame
            start_time = time.time()
            self.frame += 1

            # Tick down cooldown by 1 each frame
            if self.player.cooldown > 0:
                self.player.cooldown -= 1

            if kb.kbhit():
                c = kb.getch()
                if c == 'q':  # 'q' to quit
                    self.game_over()

                # Only process inputs if cooldown is inactive
                if self.player.cooldown <= 0:
                    self.player.process_command(c)

            # Check each enemy to see if it's ready to act this frame
            for enemy in self.enemies:
                enemy.act(self.frame)

            # Check each weapon to see if it's ready to act this frame
            for weapon in self.weapons:
                weapon.act(self.frame)

            # Print is expensive.
            # Only print if there have been
            # visual updates this frame
            if self.print_this_frame:
                self.print_screen()
                self.print_this_frame = False

            # Subtract current time from the time the frame started
            #    (time.time() - start_time)
            # This will give you how long the frame has taken so far.
            #
            # If it's less than our target frame time, put the display
            # to sleep for that many seconds.
            processing_time = time.time() - start_time
            wait_time = max([0, frame_time - processing_time])
            time.sleep(wait_time)


        # We get here after the game stops running.
        # Print the final map and an appropriate game over messge.
        self.print_screen()
        if self.win:
            print("You win!")
            print("You are an awesome treasure hunter!")
        else:
            print("You are dead!")
            print("Game Over")

        # This will set the terminal back to normal.
        kb.set_normal_term()




g = Game()
g.run()
