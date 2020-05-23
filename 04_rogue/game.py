import kbhit # https://simondlevy.academic.wlu.edu/files/software/kbhit.py

import os
import time
import csv

from objects import Barrier, Weapon, Enemy, Player

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    def __init__(self):
        # Init grid

        self.framerate = 60
        self.frame = 0
        self.running = True

        self.cooldown = 0
        self.weapons = []
        self.enemies = []

        self.load_world("maze_map.csv")

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
                    self.grid.append([" "] * self.num_cols)
                    col_i = 0
                    for col in row:
                        self.create(col, self.num_rows, col_i)
                        col_i += 1
                    self.num_rows += 1

    def create(self, key, row, col):
        if key == "X":
            Enemy("X", row, col, 200, self)
        elif key == "Y":
            Enemy("Y", row, col, 400, self)
        elif key == "#":
            Barrier(row, col, self)
        elif key == "P":
            Player("P", row, col, self)


    def load_default_world(self):
        self.num_rows = 20
        self.num_cols = 20
        self.grid = []
        for i in range(self.num_rows):
            self.grid.append([" "] * self.num_cols)

        Player("Br80", 0, 0, self)

        Enemy("X", 5, 0, 100, self)
        Enemy("X", 5, 1, 400, self)
        Enemy("Y", 6, 0, 400, self)
        Enemy("Y", 6, 1, 400, self)
        Enemy("X", 7, 0, 400, self)


        Barrier(4, 2, self)
        Barrier(5, 2, self)
        Barrier(6, 2, self)
        Barrier(7, 2, self)
        Barrier(8, 2, self)
        Barrier(9, 2, self)

        Barrier(0, 3, self)

    def draw_grid(self):
        clear_screen()
        print("# " * (self.num_cols + 1))
        for row in self.grid:
            char_row = [str(c)[0] for c in row]
            print(f"#{' '.join(char_row)}#")
        print("# " * (self.num_cols + 1))
        print(self.player.cooldown)


    def run(self):
        frame = 0
        t = time.time()
        frame_time = 1 / self.framerate

        kb = kbhit.KBHit()

        game_start = time.time()

        while self.running:
            # self.draw_grid()
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
            time.sleep(frame_time)

        print("Game Over!")
        kb.set_normal_term()




g = Game()
g.draw_grid()
g.run()


