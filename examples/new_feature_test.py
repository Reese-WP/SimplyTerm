from simplyterm import *

#this sets up the isolated terminal environment, and will reset the terminal to normal when the program exits, even if it crashes.
enter()
try:
    #first you must make the screen object, witch holds the screen and buffer, and automatically resizes the screen when the terminal is resized to prevent wonky sizing and overflow.
    screen = Screen()

    while get_key() != "q":

        screen.foreground = "#23A820"

        box(0,0,screen.width, screen.height, screen)
        box((screen.width//2)-8, (screen.height//2-1), 16, 4, screen)

        text(0, screen.height//2, "Hello!", screen.width, screen, center=True)

        #screen.reset_styles()
        screen.italic = True
        screen.foreground = "#2F248D"

        text(0, (screen.height//2)+1, "Press q to quit", screen.width, screen, center=True)

        screen.push()
        #screen.reset_styles()

            
finally:
    exit()