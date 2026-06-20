from gui import MainWindow

# from game_logic import (
#     consume_messages,
#     create_player,
#     format_inventory,
#     format_status,
#     use_potion,
# )

# TEXT_DELAY = 0.05       # wie schnell wird der Text "getippt"
# PARAGRAPH_PAUSE = 1.0   # Wartezeit nach jedem Absatz in Sekunden 

# def clear_screen():                         # Terminal leeren
#     print("\033[2J\033[H", end="")          # Cursor nach oben links setzen

# def confirm_with_enter(question):
#     clear_screen()
#     print(question)
#     print()
#     print("Press Enter to confirm.")
#     print("Press any other key to cancel.")

#     # key = read_key("> ")
#     # return key == "\n"


# def show_instructions():
#     clear_screen()
#     print("Instructions")
#     print()
#     print("w  move up")
#     print("s  move down")
#     print("a  move left")
#     print("d  move right")
#     print("Space  pick up the item under your character")
#     print()
#     print("When an enemy blocks your way, choose fight or flee.")
#     input("\nPress Enter to return...")

# def show_start_menu():
#     while True:
#         clear_screen()
#         print("Welcome to Maze of Shadows")
#         print()
#         print('Press "i" for Instructions')
#         print("Press Enter to start the game")
#         print('Press "q" to quit')

#         # # key = read_key("> ")

#         # if key == "i":
#         #     show_instructions()
#         # elif key == "\n":
#         #     return "start"
#         # elif key == "q":
#         #     if confirm_with_enter("Do you want to quit the program?"):
#         #         return "quit"



# def show_inventory(player):
#     while True:
#         clear_screen()
#         print(format_status(player))
#         print()
#         print(format_inventory(player))
#         print()
#         print("9  use Small Potion")
#         print("0  use Big Potion")
#         print("Space  return")

#         # key = read_key("> ")

#         # if key == " ":
#         #     return
#         # elif key == "9":
#         #     use_potion(player, "small_potion")
#         # elif key == "0":
#         #     use_potion(player, "big_potion")
#         # else:
#         #     continue

#         clear_screen()
#         print(format_status(player))
#         print()
#         print(format_inventory(player))
#         print()
#         # show_messages(consume_messages(player))
#         # print()
#         # wait_for_space("Press Space to continue...")



# def main():
#     while True:
#         choice = show_start_menu()

#         if choice == "quit":
#             clear_screen()
#             print("Goodbye.")
#             return

#         # run_game()



# if __name__ == "__main__":
#     main()


first_maze = [
    [
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
    ],
    [
        "I",
        " ",
        " ",
        " ",
        "I",
        " ",
        "I",
        " ",
        " ",
        " ",
        " ",
        " ",
        "I",
        " ",
        "X",
        " ",
        "I",
        " ",
        " ",
        "I",
    ],
    [
        "I",
        "X",
        " ",
        " ",
        " ",
        " ",
        "I",
        " ",
        "I",
        "I",
        "I",
        "I",
        "I",
        " ",
        " ",
        " ",
        "I",
        " ",
        "I",
        "I",
    ],
    [
        "I",
        " ",
        " ",
        " ",
        "I",
        " ",
        "I",
        " ",
        " ",
        " ",
        " ",
        " ",
        "I",
        " ",
        " ",
        " ",
        "I",
        " ",
        "I",
        "I",
    ],
    [
        "I",
        "I",
        "I",
        "I",
        "I",
        " ",
        "I",
        "I",
        "I",
        "I",
        "I",
        " ",
        "I",
        "I",
        "I",
        " ",
        "I",
        " ",
        "I",
        "I",
    ],
    [
        "I",
        " ",
        " ",
        " ",
        " ",
        " ",
        "I",
        " ",
        " ",
        " ",
        " ",
        " ",
        "I",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "I",
    ],
    [
        "I",
        " ",
        "I",
        "I",
        "I",
        "I",
        "I",
        " ",
        "I",
        "I",
        " ",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        " ",
        "I",
    ],
    [
        "I",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "I",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "I",
    ],
    [
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        " ",
        "I",
        "I",
        "I",
        "I",
        " ",
        "I",
        "I",
        "I",
        " ",
        "I",
        "I",
    ],
    [
        "I",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "I",
        " ",
        " ",
        "I",
        " ",
        "I",
        " ",
        "I",
        " ",
        "I",
        " ",
        " ",
        "I",
    ],
    [
        "I",
        " ",
        "I",
        "I",
        " ",
        "I",
        " ",
        "I",
        "I",
        " ",
        "I",
        " ",
        "I",
        " ",
        "I",
        " ",
        " ",
        " ",
        " ",
        "I",
    ],
    [
        "I",
        " ",
        " ",
        "I",
        " ",
        "I",
        " ",
        " ",
        "I",
        " ",
        "I",
        " ",
        "I",
        " ",
        "I",
        "I",
        "I",
        "I",
        " ",
        "I",
    ],
    [
        "I",
        "I",
        "I",
        "I",
        " ",
        "I",
        "I",
        " ",
        "I",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "I",
    ],
    [
        "I",
        " ",
        " ",
        " ",
        " ",
        " ",
        "I",
        " ",
        "I",
        " ",
        "I",
        "I",
        "I",
        " ",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
    ],
    [
        "I",
        "F",
        "I",
        "I",
        "I",
        " ",
        "I",
        "I",
        "I",
        " ",
        "I",
        " ",
        "I",
        " ",
        " ",
        " ",
        "I",
        " ",
        " ",
        "I",
    ],
    [
        "I",
        " ",
        " ",
        " ",
        "I",
        " ",
        " ",
        " ",
        " ",
        " ",
        "I",
        " ",
        " ",
        " ",
        "I",
        " ",
        "I",
        " ",
        " ",
        "I",
    ],
    [
        "I",
        " ",
        "I",
        " ",
        "I",
        " ",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        " ",
        "I",
        " ",
        " ",
        "I",
    ],
    [
        "I",
        " ",
        "I",
        " ",
        "I",
        " ",
        " ",
        " ",
        " ",
        "I",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "I",
        "I",
        " ",
        "I",
    ],
    [
        "I",
        "O",
        "I",
        " ",
        "I",
        " ",
        "I",
        "I",
        " ",
        "I",
        "B",
        "I",
        " ",
        " ",
        "I",
        " ",
        " ",
        " ",
        " ",
        "I",
    ],
    [
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "A",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
        "I",
    ],
]


MainWindow(first_maze)
