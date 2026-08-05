from typing import Literal

def box(x, y, width, height, buffer):
    #if width and height reach outside of the buffer an error will be thrown.
    #it is good practice to dynamicaly set the width and height of the box to be drawn based on the buffer size to avoid this.
    
    if width < 2 or height < 2:
        return

    buffer[y][x] = "┏"
    buffer[y][x + width - 1] = "┓"
    buffer[y + height - 1][x] = "┗"
    buffer[y + height - 1][x + width - 1] = "┛"

    for w in range(1, width - 1):
        buffer[y][x + w] = "━"
        buffer[y + height - 1][x + w] = "━"

    for h in range(1, height - 1):
        buffer[y + h][x] = "┃"
        buffer[y + h][x + width - 1] = "┃"

def text(x, y, text, width, buffer, center=False, truncate: Literal["end", "start", "none"] = "none"):
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
            0 <= xx < len(buffer[0])
            and 0 <= y < len(buffer)
        ):
            buffer[y][xx] = c