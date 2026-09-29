import tkinter as tk

import story
from game_logic import Fight, clean_player_name
from maze import Maze


class MainWindow:
    symbol_colors = {
        Maze.player_symbol: "deep sky blue",
        Maze.treasure_symbol: "gold",
        Maze.boss_symbol: "red",
        Maze.goblin_symbol: "red",
        Maze.torch_symbol: "orange",
        Maze.potion_symbol: "lime green",
    }
    wall_background = "gray35"
    default_color = "white"
    maze_background = "black"
    typing_speed_ms = 30

    def __init__(self, maze, vision_range=2):
        self.initial_maze = maze
        self.vision_range = vision_range
        self.grid_size = vision_range * 2 + 1
        self.player_name = clean_player_name("")

        self.root = tk.Tk()
        self.root.title("Maze Runner")
        self.root.minsize(800, 700)

        self.create_header()
        self.create_footer()
        self.create_status_panel()
        self.create_maze_grid()
        self.create_story_label()
        self.create_name_input()
        self.create_buttons()
        self.bind_keys()

        self.typing_job = None
        self.new_game()

    def run(self):
        self.root.mainloop()

    # ---------- widgets ----------

    def create_header(self):
        self.header = tk.Label(self.root, text="Maze Runner", font=("Arial", 30), fg="purple")
        self.header.pack(fill="x", padx=20, pady=(20, 0))

    def create_status_panel(self):
        self.statusframe = tk.Frame(self.root)
        self.statusframe.columnconfigure(0, weight=1)
        self.statusframe.columnconfigure(1, weight=1)
        self.statusframe.pack(fill="x", padx=10, pady=10)

        self.statsframe = tk.Frame(self.statusframe)
        self.statsframe.columnconfigure(0, weight=1)
        self.statsframe.grid(row=0, column=0, sticky=tk.W + tk.E, padx=10, pady=10)

        self.char_name_label = tk.Label(self.statsframe, font=("Arial", 20))
        self.char_level_label = tk.Label(self.statsframe, font=("Arial", 16))
        self.char_exp_label = tk.Label(self.statsframe, font=("Arial", 16))
        self.char_hp_label = tk.Label(self.statsframe, font=("Arial", 16))
        self.char_attack_label = tk.Label(self.statsframe, font=("Arial", 16))
        self.char_defense_label = tk.Label(self.statsframe, font=("Arial", 16))
        stat_labels = [
            self.char_name_label,
            self.char_level_label,
            self.char_exp_label,
            self.char_hp_label,
            self.char_attack_label,
            self.char_defense_label,
        ]
        for row, label in enumerate(stat_labels):
            label.grid(row=row, column=0, sticky=tk.W + tk.E)

        self.enemy_label = tk.Label(self.statsframe, text="", font=("Arial", 16, "bold"), fg="red")
        self.enemy_label.grid(row=len(stat_labels), column=0, sticky=tk.W + tk.E, pady=(10, 0))

        self.inventory_frame = tk.Frame(self.statusframe)
        self.inventory_frame.grid(row=0, column=1, sticky=tk.W + tk.E + tk.N, padx=10, pady=10)
        self.inventory_label = tk.Label(self.inventory_frame, text="Inventory:", font=("Arial", 20))
        self.inventory_label.grid(row=0, column=0, sticky=tk.W + tk.E)
        self.inventory_items_label = tk.Label(self.inventory_frame, text="", font=("Arial", 16), justify="left")
        self.inventory_items_label.grid(row=1, column=0, sticky=tk.W + tk.E)

    def create_maze_grid(self):
        self.maze_frame = tk.Frame(self.root, bg=self.maze_background, padx=10, pady=10)
        self.maze_labels = []
        for row in range(self.grid_size):
            label_row = []
            for column in range(self.grid_size):
                label = tk.Label(
                    self.maze_frame,
                    text=" ",
                    width=2,
                    font=("Courier", 26, "bold"),
                    bg=self.maze_background,
                    fg=self.default_color,
                )
                label.grid(row=row, column=column, padx=1, pady=1)
                label_row.append(label)
            self.maze_labels.append(label_row)
        self.maze_frame.pack(pady=10, padx=10)

    def create_story_label(self):
        self.story_label = tk.Label(self.root, text="", font=("Arial", 16), height=7)
        self.story_label.pack(pady=10, padx=10)

    def create_name_input(self):
        self.name_frame = tk.Frame(self.root)
        self.name_label = tk.Label(self.name_frame, text="Your name:", font=("Arial", 16))
        self.name_label.grid(row=0, column=0, padx=5)
        self.name_entry = tk.Entry(self.name_frame, font=("Arial", 16), width=16, justify="center")
        self.name_entry.grid(row=0, column=1, padx=5)
        self.name_frame.pack(pady=(0, 10))
        self.name_entry.focus_set()

    def create_buttons(self):
        buttonframe = tk.Frame(self.root)
        self.attack_button = tk.Button(buttonframe, text="Attack (1)", font=("Arial", 16), command=lambda: self.fight_turn("attack"))
        self.defend_button = tk.Button(buttonframe, text="Defend (2)", font=("Arial", 16), command=lambda: self.fight_turn("defend"))
        self.potion_button = tk.Button(buttonframe, text="Potion (3)", font=("Arial", 16), command=self.use_potion)
        self.flee_button = tk.Button(buttonframe, text="Flee (4)", font=("Arial", 16), command=lambda: self.fight_turn("flee"))
        self.fight_buttons = [self.attack_button, self.defend_button, self.flee_button]
        for column, button in enumerate([self.attack_button, self.defend_button, self.potion_button, self.flee_button]):
            buttonframe.columnconfigure(column, weight=1)
            button.grid(row=0, column=column, sticky=tk.W + tk.E, padx=10, pady=10)
        buttonframe.pack(fill="x", pady=10, padx=10)

    def create_footer(self):
        self.copyright_label = tk.Label(self.root, text="© Eric & Niko", font=("Arial", 12), fg="gray")
        self.copyright_label.pack(side="bottom", pady=10)

    def bind_keys(self):
        for key in Maze.directions:
            self.root.bind(f"<{key}>", self.move_player)
        self.root.bind("<Return>", self.on_return)
        self.root.bind("<Key-1>", lambda event: self.fight_turn("attack"))
        self.root.bind("<Key-2>", lambda event: self.fight_turn("defend"))
        self.root.bind("<Key-3>", lambda event: self.use_potion())
        self.root.bind("<Key-4>", lambda event: self.fight_turn("flee"))

    # ---------- game flow ----------

    def new_game(self):
        self.maze = Maze(self.initial_maze, self.vision_range, self.player_name)
        self.story_happened = []
        self.stop_typing()
        self.game_started = False
        self.game_over = False
        self.fight = None
        self.clear_maze_grid()
        self.story_label.config(text="Type in your name and press Enter to start the game")
        self.update_stats()
        self.update_buttons()

    def on_return(self, event=None):
        if self.game_over:
            self.new_game()
            self.start_game()
        elif not self.game_started:
            self.set_player_name()
            self.start_game()

    def set_player_name(self):
        # the name is only asked once, a restart keeps it
        self.player_name = clean_player_name(self.name_entry.get())
        self.maze.character.name = self.player_name
        self.name_frame.pack_forget()
        self.root.focus_set()

    def start_game(self):
        self.game_started = True
        self.update_stats()
        self.update_buttons()
        self.update_maze_grid()
        self.update_story_label(self.maze.player_pos)

    def move_player(self, event):
        if not self.game_started or self.game_over or self.story_ongoing or self.fight:
            return
        enemy = self.maze.check_action(event.keysym)
        self.update_maze_grid()
        self.update_stats()
        if enemy:
            self.start_fight(enemy)
        elif self.maze.reached_exit:
            self.end_game(story.story_texts["exit_part"].format(name=self.player_name))
        else:
            self.update_story_label(self.maze.player_pos)

    def end_game(self, text):
        self.game_over = True
        self.update_buttons()
        self.type_text(f"{text}\n\nPress Enter to play again.")

    # ---------- fighting ----------

    def start_fight(self, enemy):
        self.fight = Fight(self.maze.character, enemy)
        intro = story.story_texts.get(enemy.name.lower(), f"A {enemy.name} appears!")
        self.show_text(f"{intro}\nAttack, defend, drink a potion or try to flee.")
        self.update_stats()
        self.update_buttons()

    def fight_turn(self, action):
        if self.fight is None or self.story_ongoing:
            return
        fight_round = self.fight.round
        if action == "attack":
            log = self.fight.player_attack()
        elif action == "defend":
            log = self.fight.player_defend()
        elif action == "potion":
            log = self.fight.player_use_potion()
        else:
            log = self.fight.player_flee()
        self.show_text(f"Round {fight_round}\n" + "\n".join(log))

        if self.fight.is_over:
            self.finish_fight()
        self.update_stats()
        self.update_buttons()

    def finish_fight(self):
        fight = self.fight
        self.fight = None
        if fight.player_won():
            self.maze.remove_enemy(fight.enemy)
            self.update_maze_grid()
        elif not self.maze.character.is_alive():
            self.game_over = True
            self.story_label.config(text=self.story_label.cget("text") + f"\n{story.story_texts['game_over']} - Press Enter to try again.")

    def use_potion(self):
        if not self.game_started or self.game_over:
            return
        if self.fight:
            self.fight_turn("potion")
            return
        _, message = self.maze.character.use_potion()
        self.show_text(message)
        self.update_stats()

    # ---------- drawing ----------

    def update_stats(self):
        character = self.maze.character
        name = character.name if self.game_started else "?"
        self.char_name_label.config(text=f"Name: {name}")
        self.char_level_label.config(text=f"Level: {character.level}")
        self.char_exp_label.config(text=f"EXP: {character.exp}/{character.exp_needed()}")
        self.char_hp_label.config(text=f"HP: {character.actual_hp}/{character.hp}")
        self.char_attack_label.config(text=f"Attack: {character.attack}")
        self.char_defense_label.config(text=f"Defense: {character.defense}")
        self.inventory_items_label.config(text=self.inventory_text(character.inventory))

        if self.fight:
            enemy = self.fight.enemy
            self.enemy_label.config(text=f"{enemy.name}: {enemy.actual_hp}/{enemy.hp} HP")
        else:
            self.enemy_label.config(text="")

    def inventory_text(self, inventory):
        # potions are stacked, e.g. "Small Potion (+10 HP) x2"
        item_counts = {}
        for item in inventory:
            item_counts[item] = item_counts.get(item, 0) + 1
        lines = []
        for item, count in item_counts.items():
            line = item.describe()
            if count > 1:
                line += f" x{count}"
            lines.append(line)
        return "\n".join(lines)

    def update_buttons(self):
        state = tk.NORMAL if self.fight else tk.DISABLED
        for button in self.fight_buttons:
            button.config(state=state)
        potion_state = tk.NORMAL if self.game_started and not self.game_over else tk.DISABLED
        self.potion_button.config(state=potion_state)

    def show_text(self, text):
        # instant text for fight messages
        self.stop_typing()
        self.story_label.config(text=text)

    def stop_typing(self):
        if self.typing_job is not None:
            self.root.after_cancel(self.typing_job)
            self.typing_job = None
        self.story_ongoing = False

    def clear_maze_grid(self):
        for label_row in self.maze_labels:
            for label in label_row:
                label.config(text=" ", bg=self.maze_background)

    def update_maze_grid(self):
        vision_maze = self.maze.show_vision_maze()
        for row, label_row in enumerate(self.maze_labels):
            for column, label in enumerate(label_row):
                symbol = vision_maze[row][column]
                if symbol == Maze.wall_symbol:
                    # walls are drawn as filled tiles instead of the letter
                    label.config(text=" ", bg=self.wall_background)
                else:
                    color = self.symbol_colors.get(symbol, self.default_color)
                    label.config(text=symbol, fg=color, bg=self.maze_background)

    def update_story_label(self, actual_pos):
        if actual_pos not in story.story_positions or actual_pos in self.story_happened:
            return
        self.story_happened.append(actual_pos)
        self.type_text(story.story_texts[story.story_positions[actual_pos]])

    def type_text(self, text, index=0):
        # writes the text letter by letter without freezing the window
        if index == 0:
            self.stop_typing()
            self.story_ongoing = True
        self.story_label.config(text=text[:index])
        if index < len(text):
            self.typing_job = self.root.after(self.typing_speed_ms, self.type_text, text, index + 1)
        else:
            self.typing_job = None
            self.story_ongoing = False
