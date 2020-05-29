import time

import os
import kbhit # https://simondlevy.academic.wlu.edu/files/software/kbhit.py


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Display:

    def __init__(self):

        self.framerate = 60
        self.frame = 0
        self.running = True

        self.cooldown = 1

        self.grid = []
        for i in range(10):
          self.grid.append(["."] * 20)


    def draw_screen(self):
        self.print_this_frame = True

    def print_screen(self):
        clear_screen()
        print("")
        for row in self.grid:
            char_row = [str(c) for c in row]
            print(''.join(char_row))

    def process_command(self, c):
        pass

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
            if self.cooldown > 0:
                self.cooldown -= 1
            if kb.kbhit():
                c = kb.getch()
                if ord(c) == 27: # ESC
                    break
                if self.cooldown <= 0:
                    self.process_command(c)

            wait_time = max([0, frame_time - (time.time() - start_time)])
            time.sleep(wait_time)

        self.print_screen()

        if self.win:
            print("You win!")
            print("You are an awesome treasure hunter!")
        else:
            print("Game Over")

        kb.set_normal_term()




d = Display()
d.draw_screen()
d.run()

