import kbhit # https://simondlevy.academic.wlu.edu/files/software/kbhit.py

import os
import time

from objects import Barrier, Weapon, Enemy, Player

def clear_screen():
    '''
    Clears the game terminal
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    def __init__(self, num_rows, num_cols):
        # Init grid
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid = []
        for i in range(self.num_rows):
            self.grid.append([" "] * self.num_cols)

        self.framerate = 60
        self.frame = 0
        self.running = True

        self.player = Player("Br80", 0, 0, self)
        self.cooldown = 0
        self.weapons = []

        self.enemies = []
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

        print('Move with WASD')

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




g = Game(20, 20)
g.draw_grid()
g.run()


