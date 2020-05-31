import kbhit
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

kb = kbhit.KBHit()

last_c = "NONE"

clear_screen()
while True:
    if kb.kbhit():
        c = kb.getch()
        if c == "q":  # Hit `q` to break out of the loop
            break
        last_c = c
    clear_screen()
    print(last_c)
