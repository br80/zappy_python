import kbhit # https://simondlevy.academic.wlu.edu/files/software/kbhit.py

import os
import time
import csv

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

        self.framerate = 60
        self.frame = 0
        self.running = True

        self.debug_prints = 0
        self.debug_fps = 0
        self.debug_last_frame_second = 0
        self.frame_at_last_second = 0

        self.cooldown = 0
        self.weapons = []
        self.enemies = []
        self.treasures = []

        self.print_this_frame = True

        self.win = False

        self.load_world("data/" + "maze_map.csv")

    def load_world(self, world_file=None):
        if world_file is None:
            self.load_default_world()
        else:
            with open(world_file, newline='') as csv_file:
                self.num_rows = 0
                self.num_cols = None
                self.grid = []
                file_reader = csv.reader(csv_file)
                for row in file_reader:
                    if self.num_cols is None:
                        self.num_cols = len(row)
                    self.grid.append(["  "] * self.num_cols)
                    col_i = 0
                    for col in row:
                        self.create(col, self.num_rows, col_i)
                        col_i += 1
                    self.num_rows += 1

    def create(self, key, row, col):
        if key == "G":
            Goblin(row, col, self)
        elif key == "S":
            Snake(row, col, self)
        elif key == "#":
            Barrier(row, col, self)
        elif key == "P":
            Player("😀", row, col, self)
        elif key == "T":
            Treasure(row, col, self)


    def load_default_world(self):
        self.num_rows = 20
        self.num_cols = 20
        self.grid = []
        for i in range(self.num_rows):
            self.grid.append(["  "] * self.num_cols)

        Player("Br80", 0, 0, self)

        Goblin(5, 0, self)
        Goblin(5, 1, self)
        Goblin(7, 0, self)
        Snake(6, 0, self)
        Snake(6, 1, self)


        Enemy("X", 5, 0, 100, 0.8, self)
        Enemy("X", 5, 1, 400, 0.8, self)
        Enemy("X", 7, 0, 400, 0.8, self)
        Enemy("Y", 6, 0, 400, 0.2, self)
        Enemy("Y", 6, 1, 400, 0.2, self)

        Treasure(7, 1, self)

        Barrier(4, 2, self)
        Barrier(5, 2, self)
        Barrier(6, 2, self)
        Barrier(7, 2, self)
        Barrier(8, 2, self)
        Barrier(9, 2, self)

        Barrier(0, 3, self)

    def draw_screen(self):
        self.print_this_frame = True

    def print_screen(self):
        clear_screen()
        print("")
        print("⬜️" * (self.num_cols + 2))
        for row in self.grid:
            char_row = [str(c) for c in row]
            print(f"⬜️{''.join(char_row)}⬜️")
        print("⬜️" * (self.num_cols + 2))
        print("")
        print(f"Gold: {self.player.gold}")
        print(self.player.cooldown)

        self.debug_prints += 1
        print(f"{self.debug_prints} prints")
        if time.time() - self.debug_last_frame_second > 1:
            self.debug_last_frame_second = time.time()
            self.debug_fps = self.frame // self.debug_last_frame_second
            self.debug_fps = self.frame - self.frame_at_last_second
            self.frame_at_last_second = self.frame
        print(f"FPS: {self.debug_fps}")

    def game_over(self):
        self.running = False

    def do_win(self):
        self.win = True
        self.game_over()


    def run(self):
        frame = 0
        t = time.time()
        frame_time = 1 / self.framerate

        kb = kbhit.KBHit()

        game_start = time.time()

        while self.running:

            # Print is expensive.
            # Only print if there have been
            # visual updates.
            if self.print_this_frame:
                self.print_screen()
                self.print_this_frame = False

            self.frame += 1
            start_time = time.time()
            if self.player.cooldown > 0:
                self.player.cooldown -= 1
            if kb.kbhit():
                c = kb.getch()
                if ord(c) == 27: # ESC
                    break
                if self.player.cooldown <= 0:
                    self.player.process_command(c)

            for enemy in self.enemies:
                enemy.act(self.frame)
            for weapon in self.weapons:
                weapon.act(self.frame)
            wait_time = max([0, frame_time - (time.time() - start_time)])
            time.sleep(wait_time)

        if self.win:
            print("You win!")
            print("You are an awesome treasure hunter!")
        else:
            print("Game Over")

        kb.set_normal_term()




g = Game()
g.draw_screen()
g.run()


