from game_logic import consume_messages, create_player, format_status
from key_input import read_key
from maze import Maze


# Small manual test file. It uses the same simple functions as main.py.
def main():
    player = create_player()
    maze = Maze()

    while True:
        print("\033[2J\033[H", end="")
        print(format_status(player))
        print()
        print(maze.render(player))
        print()

        prompt = maze.get_current_item_prompt()
        if prompt:
            print(prompt)
            print()

        key = read_key("W/A/S/D, Space, Q: ")

        if key == "q":
            print("Game over!")
            break

        if key == " ":
            result = maze.collect_current_item(player)
        elif key in ["w", "a", "s", "d"]:
            result = maze.move_player(key)
        else:
            continue

        print(result["message"])
        for message in consume_messages(player):
            print(message)

        read_key("Press any key...")


if __name__ == "__main__":
    main()
