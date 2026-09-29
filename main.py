from pathlib import Path

from gui import MainWindow
from maze import load_maze

LEVEL_FILE = Path(__file__).parent / "levels" / "level_1.txt"


if __name__ == "__main__":
    first_maze = load_maze(LEVEL_FILE)
    MainWindow(first_maze).run()
