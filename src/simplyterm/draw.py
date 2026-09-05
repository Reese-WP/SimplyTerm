from typing import Literal
from .screen import Screen
from .tile import Tile

def box(x, y, width, height, screen: Screen):
    
    if width < 2 or height < 2 or x+width > screen.width or y+height > screen.height or x < 0 or y < 0:
        return

    screen.set_tile(x,y, "┏")
    screen.set_tile(x + width - 1, y, "┓")
    screen.set_tile(x, y + height - 1, "┗")
    screen.set_tile(x + width - 1, y + height - 1, "┛")

    for w in range(1, width - 1):
        screen.set_tile(x + w, y, "━")
        screen.set_tile(x + w, y + height - 1, "━")

    for h in range(1, height - 1):
        screen.set_tile(x, y + h, "┃")
        screen.set_tile(x + width - 1, y + h, "┃")

        def box(x, y, width, height, screen: Screen):
            
            if width < 2 or height < 2 or x+width > screen.width or y+height > screen.height or x < 0 or y < 0:
                return
        
            screen.set_tile(x,y, "┏")
            screen.set_tile(x + width - 1, y, "┓")
            screen.set_tile(x, y + height - 1, "┗")
            screen.set_tile(x + width - 1, y + height - 1, "┛")
        
            for w in range(1, width - 1):
                screen.set_tile(x + w, y, "━")
                screen.set_tile(x + w, y + height - 1, "━")
        
            for h in range(1, height - 1):
                screen.set_tile(x, y + h, "┃")
                screen.set_tile(x + width - 1, y + h, "┃")

def fill(x, y, width, height, tile: Tile, screen: Screen):
    # Out of bounds check
    if width < 1 or height < 1 or x + width > screen.width or y + height > screen.height or x < 0 or y < 0:
        return
        
    # Standard nested loop covering every single coordinate from 0 to width/height
    for w in range(width):
        for h in range(height):
            screen.set_tile(x + w, y + h, tile)

def text(x, y, text, width, screen: Screen, center=False, truncate: Literal["end", "start", "none"] = "none"):
    if center:
        x += (width//2) - (len(text)//2)

    if len(text) > width and truncate != "none":
        if truncate == "end":
            text = text[:width]
        elif truncate == "start":   
            text = text[-width:]

    for i, c in enumerate(text):
        xx = x + i
        if (
            0 <= xx < len(screen.buffer[0])
            and 0 <= y < len(screen.buffer)
        ):
            screen.set_tile(xx, y, c)