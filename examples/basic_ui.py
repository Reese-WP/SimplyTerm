from terminalui import *

#this sets up the isolated terminal environment, and will reset the terminal to normal when the program exits, even if it crashes.
enter()
try:
    #first you must make the screen object, witch holds the screen and buffer, and automatically resizes the screen when the terminal is resized to prevent wonky sizing and overflow.
    screen = Screen()

    key = ""
    lastKey = " "

    while key != "q":

        box(0,0,screen.width, screen.height, screen.buffer)
        box((screen.width//2)-8, (screen.height//2-1), 16, 4, screen.buffer)

        text(0, screen.height//2, "Hello!", screen.width, screen.buffer, center=True)
        text(0, (screen.height//2)+1, "key " + lastKey + " pressed!", screen.width, screen.buffer, center=True)

        #the only thing you really need to do besides initalizing the screen, and enter() is to push the buffer to the screen, this will only print what has changed since the last push, keeping things efficient.
        screen.push()

        #in order to get a key and use it for more than that ecaxt loop (keep it untill a new key is pressed) only update last key when its not empty.
        #because of how get_key() works, it's best to only call it once per loop where after it will reset back to blank if nothing is pressed, so this check holds onto the key for longer
        key = get_key()
        if key != "":
            lastKey = key
            
#its good practice to always exit the terminal environment when the program ends, even if it crashes, so the user can keep using the terminal normally
#this is in a finally block to ensure it always runs.
finally:
    exit()