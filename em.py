import random
import time
import os
import pyfiglet
from termcolor import colored

# Clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fireworks animation
def fireworks():
    symbols = ['🎈', '🎆', '✨', '🎉', '🎊']
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

    for _ in range(30):
        clear()
        for i in range(15):
            line = ""
            for j in range(40):
                if random.random() > 0.9:
                    line += colored(random.choice(symbols), random.choice(colors))
                else:
                    line += " "
            print(line)
        time.sleep(0.1)

# Eid text animation
def eid_text():
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    text = "Eid Mubarak !"

    for i in range(10):
        clear()
        spaces = " " * (i % 10)
        ascii_art = pyfiglet.figlet_format(text, font="slant")

        for line in ascii_art.split("\n"):
            print(spaces + colored(line, random.choice(colors)))

        time.sleep(0.2)

# Main function
def main():
    fireworks()
    eid_text()
    print(colored("\n✨ May Allah bless you! ✨", "cyan"))

# Run program
main()
