import shutil
import sys
from .tile import Tile

class Screen:
    
    def __init__(self):
        self.resize()
        self.foreground: str | None = None
        self.background: str | None = None
        self.bold = False
        self.dim = False
        self.italic = False
        self.underline = False
        self.blink = False
        self.reverse = False
        self.hidden = False
        self.strikethrough = False


    def resize(self):
        size = shutil.get_terminal_size()

        self.width = size.columns
        self.height = size.lines

        #the screen is what is being shown at the moment
        self.screen = [
            [Tile() for _ in range(self.width)] 
            for _ in range(self.height)
        ]

        #the buffer is what will be shown next. by wrighting to the buffer, then swaping them, the user dose not see each edit to the buffer one by one, only the whole change in charecters when it wrights to the screen.
        self.buffer = [
            [Tile() for _ in range(self.width)] 
            for _ in range(self.height)
        ]

        sys.stdout.write("\033[2J\033[H")
    
    def reset_style(self):
        self.resize()
        self.foreground: str | None = None
        self.background: str | None = None
        self.bold = False
        self.dim = False
        self.italic = False
        self.underline = False
        self.blink = False
        self.reverse = False
        self.hidden = False
        self.strikethrough = False

    def set_tile(self, x, y, tile: str | Tile = Tile()):            
        if isinstance(tile, str):
            tile = Tile(char=tile, foreground=self.foreground, background=self.background, bold=self.bold, dim=self.dim, italic=self.italic, underline=self.underline, blink=self.blink, reverse=self.reverse, hidden=self.hidden, strikethrough=self.strikethrough)

        x, y = int(x), int(y)

        if 0 <= x < self.width and 0 <= y < self.height:
            self.buffer[y][x] = tile

    def clear_buffer(self):
        self.buffer = [
            [Tile() for _ in range(self.width)]
            for _ in range(self.height)
        ]


    #push the buffer to the screen, only printing what has changes as to not reprint the whole screen. this save a lot of resources, expecialy on non-gpu based terminal emulators.
    def push(self):
        output = []

        for y in range(self.height):
            for x in range(self.width):
                if self.screen[y][x] != self.buffer[y][x]:
                    output.append(f"\033[{y+1};{x+1}H")
                    output.append(self.buffer[y][x].export())
                    output.append(self.buffer[y][x].char)

        sys.stdout.write("".join(output))
        sys.stdout.flush()

        self.screen = [
            [tile.copy() for tile in row]
            for row in self.buffer
        ]

        self.clear_buffer()
        self.resize()