import sys
import termios
import tty

_old_settings = None

def enter():
    global _old_settings
    print("\033[?1049h" + "\033[?25l", end="", flush=True)
    _old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())


def exit():
    global _old_settings

    print("\033[0m", end="")
    if _old_settings:
        termios.tcsetattr(
            sys.stdin,
            termios.TCSADRAIN,
            _old_settings
        )
    print("\033[?1049l" + "\033[?25h", end="", flush=True)