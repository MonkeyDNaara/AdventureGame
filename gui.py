import tkinter as tk

import story
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

        self.root = tk.Tk()
        self.root.title("Maze Runner")
        self.root.minsize(800, 700)

        self.create_header()
        self.create_footer()
        self.create_status_panel()
        self.create_maze_grid()
        self.create_story_label()
        self.create_buttons()
        self.bind_keys()

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
        self.char_hp_label = tk.Label(self.statsframe, font=("Arial", 16))
        self.char_attack_label = tk.Label(self.statsframe, font=("Arial", 16))
        self.char_defense_label = tk.Label(self.statsframe, font=("Arial", 16))
        stat_labels = [
            self.char_name_label,
            self.char_level_label,
            self.char_hp_label,
            self.char_attack_label,
            self.char_defense_label,
        ]
        for row, label in enumerate(stat_labels):
            label.grid(row=row, column=0, sticky=tk.W + tk.E)

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
        self.story_label = tk.Label(self.root, text="", font=("Arial", 16), height=5)
        self.story_label.pack(pady=10, padx=10)

    def create_buttons(self):
        buttonframe = tk.Frame(self.root)
        self.potion_button = tk.Button(buttonframe, text="Potion", font=("Arial", 16), command=self.use_potion)
        self.potion_button.pack(padx=10, pady=10)
        buttonframe.pack(fill="x", pady=10, padx=10)

    def create_footer(self):
        self.copyright_label = tk.Label(self.root, text="© Eric & Niko", font=("Arial", 12), fg="gray")
        self.copyright_label.pack(side="bottom", pady=10)

    def bind_keys(self):
        for key in Maze.directions:
            self.root.bind(f"<{key}>", self.move_player)
        self.root.bind("<Return>", self.start_game)

    # ---------- game flow ----------

    def new_game(self):
        self.maze = Maze(self.initial_maze, self.vision_range)
        self.story_happened = []
        self.story_ongoing = False
        self.typing_job = None
        self.game_started = False
        self.clear_maze_grid()
        self.story_label.config(text="Press Enter to start the game")
        self.update_stats()

    def start_game(self, event=None):
        if self.game_started:
            return
        self.game_started = True
        self.update_maze_grid()
        self.update_story_label(self.maze.player_pos)

    def move_player(self, event):
        if not self.game_started or self.story_ongoing or self.maze.character.be_infight:
            return
        self.maze.check_action(event.keysym)
        self.update_maze_grid()
        self.update_story_label(self.maze.player_pos)
        self.update_stats()

    def use_potion(self):
        self.maze.character.use_potion()
        self.update_stats()

    # ---------- drawing ----------

    def update_stats(self):
        character = self.maze.character
        self.char_name_label.config(text=f"Name: {character.name}")
        self.char_level_label.config(text=f"Level: {character.level}")
        self.char_hp_label.config(text=f"HP: {character.actual_hp}/{character.hp}")
        self.char_attack_label.config(text=f"Attack: {character.attack}")
        self.char_defense_label.config(text=f"Defense: {character.defense}")
        inventory_lines = [
            f"{item.name}: +{item.attack} attack, +{item.defense} defense, +{item.heal} heal"
            for item in character.inventory
        ]
        self.inventory_items_label.config(text="\n".join(inventory_lines))

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
            if self.typing_job is not None:
                self.root.after_cancel(self.typing_job)
            self.story_ongoing = True
        self.story_label.config(text=text[:index])
        if index < len(text):
            self.typing_job = self.root.after(self.typing_speed_ms, self.type_text, text, index + 1)
        else:
            self.typing_job = None
            self.story_ongoing = False
