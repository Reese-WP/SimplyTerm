import shutil
import sys


class Screen:

    def __init__(self):
        self.resize()

    def resize(self):
        size = shutil.get_terminal_size()

        self.width = size.columns
        self.height = size.lines

        #the screen is what is being shown at the moment
        self.screen = [
            [" "] * self.width
            for _ in range(self.height)
        ]
        #the buffer is what will be shown next. by wrighting to the buffer, then swaping them, the user dose not see each edit to the buffer one by one, only the whole change in charecters when it wrights to the screen.
        self.buffer = [
            [" "] * self.width
            for _ in range(self.height)
        ]

        sys.stdout.write("\033[2J\033[H")

    def clear_buffer(self):
        self.buffer = [
            [" "] * self.width
            for _ in range(self.height)
        ]

    #push the buffer to the screen, only printing what has changes as to not reprint the whole screen. this save a lot of resources, expecialy on non-gpu based terminal emulators.
    def push(self):
        output = []

        for y in range(self.height):
            for x in range(self.width):
                if self.screen[y][x] != self.buffer[y][x]:
                    output.append(f"\033[{y+1};{x+1}H")
                    output.append(self.buffer[y][x])

        sys.stdout.write("\033[0m")
        sys.stdout.write("".join(output))
        sys.stdout.flush()

        self.screen = [row[:] for row in self.buffer]
        self.clear_buffer()