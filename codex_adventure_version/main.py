from game_logic import (
    consume_messages,
    create_player,
    format_inventory,
    format_status,
    use_potion,
)
from key_input import read_key
from maze import Maze
from story import DEFAULT_TYPE_DELAY, get_room_text, show_intro, type_text


TEXT_DELAY = DEFAULT_TYPE_DELAY


def clear_screen():
    print("\033[2J\033[H", end="")


def wait_for_space(prompt="Press Space to continue..."):
    print(prompt, end="", flush=True)

    while True:
        key = read_key()
        if key == " ":
            print()
            return


def wait_for_enter(prompt="Press Enter to confirm..."):
    print(prompt, end="", flush=True)

    while True:
        key = read_key()
        if key == "\n":
            print()
            return


def show_messages(messages):
    for message in messages:
        type_text(message, delay=TEXT_DELAY)


def confirm_with_enter(question):
    clear_screen()
    print(question)
    print()
    print("Press Enter to confirm.")
    print("Press any other key to cancel.")

    key = read_key("> ")
    return key == "\n"


def show_instructions():
    clear_screen()
    print("Instructions")
    print()
    print("W  move up")
    print("S  move down")
    print("A  move left")
    print("D  move right")
    print("Space  pick up an item or open a chest")
    print("I  open inventory")
    print("Q  return to the start screen")
    print()
    print("The player starts with no vision.")
    print("The torch gives vision once you pick it up.")
    print()
    wait_for_enter("Press Enter to return...")


def show_start_menu():
    while True:
        clear_screen()
        print("Welcome to Maze of Shadows")
        print()
        print('Press "i" for Instructions')
        print("Press Enter to start the game")
        print('Press "q" to quit')

        key = read_key("> ")

        if key == "i":
            show_instructions()
        elif key == "\n":
            return "start"
        elif key == "q":
            if confirm_with_enter("Do you want to quit the program?"):
                return "quit"


def render_game_screen(player, maze, messages=None, story_text=""):
    clear_screen()
    print(format_status(player))
    print()
    print(maze.render(player))
    print()

    item_prompt = maze.get_current_item_prompt()
    if item_prompt:
        print(item_prompt)
        print()

    if messages:
        show_messages(messages)
        print()

    if story_text:
        type_text(story_text, delay=TEXT_DELAY, wait_func=wait_for_space)
        print()


def show_inventory(player):
    while True:
        clear_screen()
        print(format_status(player))
        print()
        print(format_inventory(player))
        print()
        print("9  use Small Potion")
        print("0  use Big Potion")
        print("Space  return")

        key = read_key("> ")

        if key == " ":
            return
        elif key == "9":
            use_potion(player, "small_potion")
        elif key == "0":
            use_potion(player, "big_potion")
        else:
            continue

        clear_screen()
        print(format_status(player))
        print()
        print(format_inventory(player))
        print()
        show_messages(consume_messages(player))
        print()
        wait_for_space("Press Space to continue...")


def run_game():
    player = create_player()
    maze = Maze()
    seen_story_positions = set()
    pending_messages = []

    clear_screen()
    show_intro(wait_func=wait_for_space)

    while True:
        row, col = maze.player_position
        story_key = (maze.current_map, row, col)
        story_text = ""

        if story_key not in seen_story_positions:
            story_text = get_room_text(maze.current_map, row, col)
            if story_text:
                seen_story_positions.add(story_key)

        render_game_screen(player, maze, pending_messages, story_text)
        pending_messages = []

        key = read_key("W/A/S/D, Space, I, Q: ")

        if key == "q":
            if confirm_with_enter("Do you want to return to the start screen?"):
                return
            continue

        if key == "i":
            show_inventory(player)
            continue

        if key == " ":
            result = maze.collect_current_item(player)
            pending_messages = consume_messages(player)

            if result["outcome"] != "collected":
                pending_messages.append(result["message"])
            continue

        if key in ["w", "a", "s", "d"]:
            result = maze.move_player(key)

            if result["outcome"] == "win":
                pending_messages.append(result["message"])
                render_game_screen(player, maze, pending_messages)
                wait_for_space("Press Space to return to the start screen...")
                return

            if result["outcome"] != "moved":
                pending_messages.append(result["message"])
            continue

        pending_messages.append("Unknown key. Use W A S D, Space, I, or Q.")


def main():
    while True:
        choice = show_start_menu()

        if choice == "quit":
            clear_screen()
            print("Goodbye.")
            return

        run_game()


if __name__ == "__main__":
    main()
