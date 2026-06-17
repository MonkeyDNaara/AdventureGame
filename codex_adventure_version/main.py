from game_logic import (
    consume_messages,
    create_player,
    format_combat_view,
    format_status,
)
from maze import Maze
from story import DEFAULT_PARAGRAPH_PAUSE, get_room_text, show_intro, type_text


TEXT_DELAY = 0.05
PARAGRAPH_PAUSE = DEFAULT_PARAGRAPH_PAUSE


def clear_screen():
    print("\033[2J\033[H", end="")


def render_typed_lines(lines):
    for line in lines:
        if line:
            type_text(line, delay=TEXT_DELAY, paragraph_pause=PARAGRAPH_PAUSE)


def show_instructions():
    clear_screen()
    print("Instructions")
    print()
    print("w  move up")
    print("s  move down")
    print("a  move left")
    print("d  move right")
    print("Space  pick up the item under your character")
    print()
    print("When an enemy blocks your way, choose fight or flee.")
    print("Once a fight starts, you cannot run away.")
    input("\nPress Enter to return...")


def show_start_menu():
    while True:
        clear_screen()
        print("Welcome to Maze of Shadows")
        print()
        print('Press "i" for Instructions')
        print("Press Enter to start the game")
        choice = input("> ").lower()

        if choice == "i":
            show_instructions()
        elif choice == "":
            return


def render_game_screen(player, maze, messages=None, story_text="", reveal_all=False):
    clear_screen()
    print(format_status(player))
    print()
    print(maze.render(player, reveal_all=reveal_all))
    print()

    item_prompt = maze.get_current_item_prompt()
    if item_prompt:
        print(item_prompt)
        print()

    if messages:
        render_typed_lines(messages)

    if story_text:
        if messages:
            print()
        type_text(story_text, delay=TEXT_DELAY, paragraph_pause=PARAGRAPH_PAUSE)


def ask_combat_action(player, enemy):
    while True:
        clear_screen()
        print(format_combat_view(player, enemy))
        print()

        messages = consume_messages(player)
        if messages:
            render_typed_lines(messages)
            print()

        choice = input("Attack or use potion? ").strip().lower()

        if choice in {"", "attack", "a"}:
            return "attack"

        if choice in player["inventory"]:
            return choice

        if choice in {"small", "small potion", "small_potion"} and "small_potion" in player["inventory"]:
            return "small_potion"

        if choice in {"big", "big potion", "big_potion"} and "big_potion" in player["inventory"]:
            return "big_potion"

        if choice in {"potion", "p"}:
            potion = input("Which potion? ").strip().lower().replace(" ", "_")
            if potion in player["inventory"]:
                return potion

        print("You can attack or use a potion. You cannot flee once combat starts.")
        input("Press Enter to continue...")


def main():
    player = create_player()
    maze = Maze()
    seen_story_positions = set()
    pending_messages = []

    show_start_menu()
    clear_screen()
    show_intro(delay=TEXT_DELAY)

    while player["alive"]:
        y, x = maze.player_position
        story_text = ""

        if (y, x) not in seen_story_positions:
            story_text = get_room_text("level_1", y, x)
            if story_text:
                seen_story_positions.add((y, x))

        render_game_screen(player, maze, messages=pending_messages, story_text=story_text)
        pending_messages = []

        raw_command = input("> ")
        command = raw_command.strip().lower()

        if command in {"q", "quit", "exit"}:
            clear_screen()
            print("Game over.")
            break

        if command == "help" or command == "i":
            show_instructions()
            continue

        if command == "status":
            pending_messages = format_status(player).splitlines()
            continue

        if command == "inventory":
            small = player["inventory"].count("small_potion")
            big = player["inventory"].count("big_potion")
            pending_messages = [f"Small Potion: {small}", f"Big Potion: {big}"]
            continue

        if raw_command == " " or command == "space":
            result = maze.pickup_current_item(player)
            pending_messages = consume_messages(player)

            if result["outcome"] == "nothing_to_pick_up":
                pending_messages.append(result["message"])
            continue

        if maze.normalize_direction(command) not in maze.DirDict:
            pending_messages = ["Unknown command. Move with W A S D, or press Space to pick up an item."]
            continue

        clear_screen()
        result = maze.move_player(
            player,
            command,
            input_func=input,
            combat_action_provider=ask_combat_action,
        )
        pending_messages = consume_messages(player)

        if result["outcome"] == "blocked":
            pending_messages.append(result["message"])
        elif result["outcome"] == "dead":
            render_game_screen(player, maze, messages=pending_messages)
            print("Your run ends here.")
            break
        elif result["outcome"] == "win":
            render_game_screen(player, maze, messages=pending_messages, reveal_all=True)
            print("You escaped the maze.")
            break


if __name__ == "__main__":
    main()
