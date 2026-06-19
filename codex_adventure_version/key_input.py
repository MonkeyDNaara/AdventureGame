import sys


def read_key(prompt=""):
    if prompt:
        print(prompt, end="", flush=True)

    if not sys.stdin.isatty():
        text = input()
        return text[:1].lower() if text else "\n"

    try:
        import termios
        import tty
    except ImportError:
        text = input()
        return text[:1].lower() if text else "\n"

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setcbreak(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    if key == "\r":
        return "\n"

    return key.lower()
