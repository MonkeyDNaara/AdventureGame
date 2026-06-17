from game_logic import consume_messages, create_player, format_status
from maze import Maze


def main():
    player = create_player("Niko")
    maze = Maze()

    print(format_status(player))
    maze.print_maze(player)

    command = ""
    while command.lower() != "q":
        command = input("W/A/S/D or Space: ")

        if command.lower() == "q":
            print("Game over!")
            break

        if command == " " or command.lower() == "space":
            result = maze.pickup_current_item(player)
        else:
            result = maze.move_player(player, command)

        print(result["message"])

        for message in consume_messages(player):
            print(message)

        print(format_status(player))
        maze.print_maze(player)
        prompt = maze.get_current_item_prompt()
        if prompt:
            print(prompt)


if __name__ == "__main__":
    main()
