import tkinter as tk
from tkinter import messagebox
from maze import Maze
import story
import time


class MainWindow:
    def __init__(self, maze, vision_range = 2):
        self.initial_maze = maze
        self.vision_range = vision_range
        self.maze = Maze(self.initial_maze, self.vision_range)
        self.char_name = self.maze.character.name
        self.char_hp = self.maze.character.hp
        self.char_attack = self.maze.character.attack
        self.char_defense = self.maze.character.defense
        self.story_happened = []

        self.root = tk.Tk()
        self.root.title("Maze Runner")
        self.root.geometry("1400x1000")

        self.header = tk.Label(self.root, text="Maze Runner", font=("Arial", 30), fg='purple')
        self.header.pack(padx=20, pady=20)
        self.header.pack(fill="x")
        
        self.statusframe = tk.Frame(self.root)
        self.statusframe.columnconfigure(0, weight=1)
        self.statusframe.columnconfigure(1, weight=1)
        self.statusframe.pack(fill="x", padx=10, pady=10)

        self.statsframe = tk.Frame(self.statusframe)
        self.statsframe.columnconfigure(
            0, weight=1
        )
        self.statsframe.rowconfigure(
            0, weight=1
        )
        self.statsframe.rowconfigure(
            1, weight=1)
        self.statsframe.rowconfigure(
            2, weight=1)
        self.statsframe.rowconfigure(
            3, weight=1)
        self.statsframe.grid(row=0, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
        
        self.char_name_label = tk.Label(self.statsframe, text=f"Name: {self.maze.character.name}", font=("Arial", 20))
        self.char_name_label.grid(row=0, column=0, sticky=tk.W + tk.E, padx=10, pady=10)

        self.char_hp_label = tk.Label(self.statsframe, text=f"HP: {self.maze.character.actual_hp}/{self.maze.character.hp}", font=("Arial", 16))
        self.char_hp_label.grid(row=1, column=0, sticky=tk.W + tk.E, padx=10, pady=10)

        self.char_attack_label = tk.Label(self.statsframe, text=f"Attack: {self.maze.character.attack}", font=("Arial", 16))
        self.char_attack_label.grid(row=2, column=0, sticky=tk.W + tk.E, padx=10, pady=10)

        self.char_defense_label = tk.Label(self.statsframe, text=f"Defense: {self.maze.character.defense}", font=("Arial", 16))
        self.char_defense_label.grid(row=3, column=0, sticky=tk.W + tk.E, padx=10, pady=10)

        self.inventory_frame = tk.Frame(self.statusframe)
        self.inventory_frame.rowconfigure(0, weight=1)
        self.inventory_frame.rowconfigure(1, weight=3)
        self.inventory_label = tk.Label(self.inventory_frame, text="Inventory:", font=("Arial", 20))
        self.inventory_label.grid(row=0, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
        self.inventory_items_label = tk.Label(self.inventory_frame, text=f" ", font=("Arial", 16))
        self.inventory_items_label.grid(row=1, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
        self.inventory_frame.grid(row=1, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
        self.inventory_frame.grid(row=0, column=1, sticky=tk.W + tk.E, padx=10, pady=10)

        self.maze_frame = tk.Frame(self.root)
        self.maze_frame.columnconfigure(0, weight = 1)
        self.maze_frame.columnconfigure(1, weight = 1)
        self.maze_frame.columnconfigure(2, weight = 1)
        self.maze_frame.columnconfigure(3, weight = 1)
        self.maze_frame.columnconfigure(4, weight = 1)
        self.maze_frame.rowconfigure(0, weight = 1)
        self.maze_frame.rowconfigure(1, weight = 1)
        self.maze_frame.rowconfigure(2, weight = 1)
        self.maze_frame.rowconfigure(3, weight = 1)
        self.maze_frame.rowconfigure(4, weight = 1)
        self.maze_label1 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label1.grid(row=0, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label2 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label2.grid(row=0, column=1, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label3 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label3.grid(row=0, column=2, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label4 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label4.grid(row=0, column=3, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label5 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label5.grid(row=0, column=4, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label6 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label6.grid(row=1, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label7 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label7.grid(row=1, column=1, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label8 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label8.grid(row=1, column=2, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label9 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label9.grid(row=1, column=3, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label10 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label10.grid(row=1, column=4, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label11 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label11.grid(row=2, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label12 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20), fg = "blue")
        self.maze_label12.grid(row=2, column=1, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label13 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label13.grid(row=2, column=2, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label14 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label14.grid(row=2, column=3, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label15 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label15.grid(row=2, column=4, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label16 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label16.grid(row=3, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label17 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label17.grid(row=3, column=1, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label18 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label18.grid(row=3, column=2, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label19 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label19.grid(row=3, column=3, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label20 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label20.grid(row=3, column=4, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label21 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label21.grid(row=4, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label22 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label22.grid(row=4, column=1, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label23 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label23.grid(row=4, column=2, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label24 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label24.grid(row=4, column=3, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label25 = tk.Label(self.maze_frame, text=f" ", font=("Arial", 20))
        self.maze_label25.grid(row=4, column=4, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_frame.pack(pady=10, padx=10)
        self.story_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.story_label.pack(pady=10, padx=10)

        buttonframe = tk.Frame(self.root)
        buttonframe.columnconfigure(
            0, weight=1
        )
        buttonframe.columnconfigure(
            1, weight=1
        )
        buttonframe.columnconfigure(2, weight=1)
        self.attack_button = tk.Button(
            buttonframe,
            text="Attack",
            font=("Arial", 16)
        )
        self.attack_button.grid(row=0, column=0, sticky=tk.W + tk.E, padx=10, pady=10)

        self.defend_button = tk.Button(
            buttonframe,
            text="Defend",
            font=("Arial", 16)
        )
        self.defend_button.grid(row=0, column=1, sticky=tk.W + tk.E, padx=10, pady=10)

        self.potion_button = tk.Button(
            buttonframe,
            text="Potion",
            font=("Arial", 16)
        )
        self.potion_button.grid(row=0, column=2, sticky=tk.W + tk.E, padx=10, pady=10)

        # buttonframe.pack(fill="x", pady=10, padx=10)


        self.root.update()
        self.root.bind("<w>", self.key_event)
        self.root.bind("<a>", self.key_event)
        self.root.bind("<s>", self.key_event)
        self.root.bind("<d>", self.key_event)
        self.root.bind("<q>", self.key_event)
        self.root.bind("<Enter>", self.key_event)

        self.root.mainloop()
    
    def key_event(self, event):
        if event.keysym == "w" or event.keysym == "a" or event.keysym == "s" or event.keysym == "d":
            actual_vision_maze = self.maze.check_action(event.keysym)
        else:
            actual_vision_maze = self.maze.check_action()
        self.update_label(actual_vision_maze)
        self.update_story_label(self.maze.check_position(self.maze.maze, self.maze.player_symbol))
        self.update_stats()

    def update_stats(self):
        self.char_hp_label.config(text=f"HP: {self.maze.character.actual_hp}/{self.maze.character.hp}")
        self.char_attack_label.config(text=f"Attack: {self.maze.character.attack}")
        self.char_defense_label.config(text=f"Defense: {self.maze.character.defense}")
        self.inventory_items_label.config(text = f"{'\n'.join([f"{item.name}: +{item.attack} attack, +{item.defense} defense, +{item.heal} heal" for item in self.maze.character.inventory])}")

    def update_story_label(self, actual_pos):
            if actual_pos in story.story_positions.keys():
                if story.story_positions[actual_pos] not in self.story_happened:
                    story_text = ""
                    self.story_label.config(text = " ")
                    self.story_happened.append(story.story_positions[actual_pos])
                    for char in story.story_texts[story.story_positions[actual_pos]]:
                        story_text += char
                        self.story_label.config(text = story_text)
                        self.root.update()
                        time.sleep(0.03)               

    def update_label(self, vision_maze):
        self.maze_label1.config(text = f"{vision_maze[0][0]}", fg = "white")
        self.maze_label2.config(text = f"{vision_maze[0][1]}", fg = "white")
        self.maze_label3.config(text = f"{vision_maze[0][2]}", fg = "white")
        self.maze_label4.config(text = f"{vision_maze[0][3]}", fg = "white")
        self.maze_label5.config(text = f"{vision_maze[0][4]}", fg = "white")
        self.maze_label6.config(text = f"{vision_maze[1][0]}", fg = "white")
        self.maze_label7.config(text = f"{vision_maze[1][1]}", fg = "white")
        self.maze_label8.config(text = f"{vision_maze[1][2]}", fg = "white")
        self.maze_label9.config(text = f"{vision_maze[1][3]}", fg = "white")
        self.maze_label10.config(text = f"{vision_maze[1][4]}", fg = "white")
        self.maze_label11.config(text = f"{vision_maze[2][0]}", fg = "white")
        self.maze_label12.config(text = f"{vision_maze[2][1]}", fg = "white")
        self.maze_label13.config(text = f"{vision_maze[2][2]}", fg = "white")
        self.maze_label14.config(text = f"{vision_maze[2][3]}", fg = "white")
        self.maze_label15.config(text = f"{vision_maze[2][4]}", fg = "white")
        self.maze_label16.config(text = f"{vision_maze[3][0]}", fg = "white")
        self.maze_label17.config(text = f"{vision_maze[3][1]}", fg = "white")
        self.maze_label18.config(text = f"{vision_maze[3][2]}", fg = "white")
        self.maze_label19.config(text = f"{vision_maze[3][3]}", fg = "white")
        self.maze_label20.config(text = f"{vision_maze[3][4]}", fg = "white")
        self.maze_label21.config(text = f"{vision_maze[4][0]}", fg = "white")
        self.maze_label22.config(text = f"{vision_maze[4][1]}", fg = "white")
        self.maze_label23.config(text = f"{vision_maze[4][2]}", fg = "white")
        self.maze_label24.config(text = f"{vision_maze[4][3]}", fg = "white")
        self.maze_label25.config(text = f"{vision_maze[4][4]}", fg = "white")
        if vision_maze[0][0] == self.maze.player_symbol:
            self.maze_label1.config(fg = "blue")
        elif vision_maze[0][0] == self.maze.treasure_symbol:
            self.maze_label1.config(fg = "yellow")
        elif vision_maze[0][0] == self.maze.boss_symbol:
            self.maze_label1.config(fg = "red")
        elif vision_maze[0][0] == self.maze.torch_symbol:
            self.maze_label1.config(fg = "orange")
        elif vision_maze[0][0] == self.maze.exit_symbol:
            self.maze_label1.config(fg = "green")
        if vision_maze[0][1] == self.maze.player_symbol:
            self.maze_label2.config(fg = "blue")
        elif vision_maze[0][1] == self.maze.treasure_symbol:
            self.maze_label2.config(fg = "yellow")
        elif vision_maze[0][1] == self.maze.boss_symbol:
            self.maze_label2.config(fg = "red")
        elif vision_maze[0][1] == self.maze.torch_symbol:
            self.maze_label2.config(fg = "orange")
        elif vision_maze[0][1] == self.maze.exit_symbol:
            self.maze_label2.config(fg = "green")
        if vision_maze[0][2] == self.maze.player_symbol:
            self.maze_label3.config(fg = "blue")
        elif vision_maze[0][2] == self.maze.treasure_symbol:
            self.maze_label3.config(fg = "yellow")
        elif vision_maze[0][2] == self.maze.boss_symbol:
            self.maze_label3.config(fg = "red")
        elif vision_maze[0][2] == self.maze.torch_symbol:
            self.maze_label3.config(fg = "orange")
        elif vision_maze[0][2] == self.maze.exit_symbol:
            self.maze_label3.config(fg = "green")
        if vision_maze[0][3] == self.maze.player_symbol:
            self.maze_label4.config(fg = "blue")
        elif vision_maze[0][3] == self.maze.treasure_symbol:
            self.maze_label4.config(fg = "yellow")
        elif vision_maze[0][3] == self.maze.boss_symbol:
            self.maze_label4.config(fg = "red")
        elif vision_maze[0][3] == self.maze.torch_symbol:
            self.maze_label4.config(fg = "orange")
        elif vision_maze[0][3] == self.maze.exit_symbol:
            self.maze_label4.config(fg = "green")
        if vision_maze[0][4] == self.maze.player_symbol:
            self.maze_label5.config(fg = "blue")
        elif vision_maze[0][4] == self.maze.treasure_symbol:
            self.maze_label5.config(fg = "yellow")
        elif vision_maze[0][4] == self.maze.boss_symbol:
            self.maze_label5.config(fg = "red")
        elif vision_maze[0][4] == self.maze.torch_symbol:
            self.maze_label5.config(fg = "orange")
        elif vision_maze[0][4] == self.maze.exit_symbol:
            self.maze_label5.config(fg = "green")
        if vision_maze[1][0] == self.maze.player_symbol:
            self.maze_label6.config(fg = "blue")
        elif vision_maze[1][0] == self.maze.treasure_symbol:
            self.maze_label6.config(fg = "yellow")
        elif vision_maze[1][0] == self.maze.boss_symbol:
            self.maze_label6.config(fg = "red")
        elif vision_maze[1][0] == self.maze.torch_symbol:
            self.maze_label6.config(fg = "orange")
        elif vision_maze[1][0] == self.maze.exit_symbol:
            self.maze_label6.config(fg = "green")
        if vision_maze[1][1] == self.maze.player_symbol:
            self.maze_label7.config(fg = "blue")
        elif vision_maze[1][1] == self.maze.treasure_symbol:
            self.maze_label7.config(fg = "yellow")
        elif vision_maze[1][1] == self.maze.boss_symbol:
            self.maze_label7.config(fg = "red")
        elif vision_maze[1][1] == self.maze.torch_symbol:
            self.maze_label7.config(fg = "orange")
        elif vision_maze[1][1] == self.maze.exit_symbol:
            self.maze_label7.config(fg = "green")
        if vision_maze[1][2] == self.maze.player_symbol:
            self.maze_label8.config(fg = "blue")
        elif vision_maze[1][2] == self.maze.treasure_symbol:
            self.maze_label8.config(fg = "yellow")
        elif vision_maze[1][2] == self.maze.boss_symbol:
            self.maze_label8.config(fg = "red")
        elif vision_maze[1][2] == self.maze.torch_symbol:
            self.maze_label8.config(fg = "orange")
        elif vision_maze[1][2] == self.maze.exit_symbol:
            self.maze_label8.config(fg = "green")
        if vision_maze[1][3] == self.maze.player_symbol:
            self.maze_label9.config(fg = "blue")
        elif vision_maze[1][3] == self.maze.treasure_symbol:
            self.maze_label9.config(fg = "yellow")
        elif vision_maze[1][3] == self.maze.boss_symbol:
            self.maze_label9.config(fg = "red")
        elif vision_maze[1][3] == self.maze.torch_symbol:
            self.maze_label9.config(fg = "orange")
        elif vision_maze[1][3] == self.maze.exit_symbol:
            self.maze_label9.config(fg = "green")
        if vision_maze[1][4] == self.maze.player_symbol:
            self.maze_label10.config(fg = "blue")
        elif vision_maze[1][4] == self.maze.treasure_symbol:
            self.maze_label10.config(fg = "yellow")
        elif vision_maze[1][4] == self.maze.boss_symbol:
            self.maze_label10.config(fg = "red")
        elif vision_maze[1][4] == self.maze.torch_symbol:
            self.maze_label10.config(fg = "orange")
        elif vision_maze[1][4] == self.maze.exit_symbol:
            self.maze_label10.config(fg = "green")
        if vision_maze[2][0] == self.maze.player_symbol:
            self.maze_label11.config(fg = "blue")
        elif vision_maze[2][0] == self.maze.treasure_symbol:
            self.maze_label11.config(fg = "yellow")
        elif vision_maze[2][0] == self.maze.boss_symbol:
            self.maze_label11.config(fg = "red")
        elif vision_maze[2][0] == self.maze.torch_symbol:
            self.maze_label11.config(fg = "orange")
        elif vision_maze[2][0] == self.maze.exit_symbol:
            self.maze_label11.config(fg = "green")
        if vision_maze[2][1] == self.maze.player_symbol:
            self.maze_label12.config(fg = "blue")
        elif vision_maze[2][1] == self.maze.treasure_symbol:
            self.maze_label12.config(fg = "yellow")
        elif vision_maze[2][1] == self.maze.boss_symbol:
            self.maze_label12.config(fg = "red")
        elif vision_maze[2][1] == self.maze.torch_symbol:
            self.maze_label12.config(fg = "orange")
        elif vision_maze[2][1] == self.maze.exit_symbol:
            self.maze_label12.config(fg = "green")
        if vision_maze[2][2] == self.maze.player_symbol:
            self.maze_label13.config(fg = "blue")
        elif vision_maze[2][2] == self.maze.treasure_symbol:
            self.maze_label13.config(fg = "yellow")
        elif vision_maze[2][2] == self.maze.boss_symbol:
            self.maze_label13.config(fg = "red")
        elif vision_maze[2][2] == self.maze.torch_symbol:
            self.maze_label13.config(fg = "orange")
        elif vision_maze[2][2] == self.maze.exit_symbol:
            self.maze_label13.config(fg = "green")
        if vision_maze[2][3] == self.maze.player_symbol:
            self.maze_label14.config(fg = "blue")
        elif vision_maze[2][3] == self.maze.treasure_symbol:
            self.maze_label14.config(fg = "yellow")
        elif vision_maze[2][3] == self.maze.boss_symbol:
            self.maze_label14.config(fg = "red")
        elif vision_maze[2][3] == self.maze.torch_symbol:
            self.maze_label14.config(fg = "orange")
        elif vision_maze[2][3] == self.maze.exit_symbol:
            self.maze_label14.config(fg = "green")
        if vision_maze[2][4] == self.maze.player_symbol:
            self.maze_label15.config(fg = "blue")
        elif vision_maze[2][4] == self.maze.treasure_symbol:
            self.maze_label15.config(fg = "yellow")
        elif vision_maze[2][4] == self.maze.boss_symbol:
            self.maze_label15.config(fg = "red")
        elif vision_maze[2][4] == self.maze.torch_symbol:
            self.maze_label15.config(fg = "orange")
        elif vision_maze[2][4] == self.maze.exit_symbol:
            self.maze_label15.config(fg = "green")
        if vision_maze[3][0] == self.maze.player_symbol:
            self.maze_label16.config(fg = "blue")
        elif vision_maze[3][0] == self.maze.treasure_symbol:
            self.maze_label16.config(fg = "yellow")
        elif vision_maze[3][0] == self.maze.boss_symbol:
            self.maze_label16.config(fg = "red")
        elif vision_maze[3][0] == self.maze.torch_symbol:
            self.maze_label16.config(fg = "orange")
        elif vision_maze[3][0] == self.maze.exit_symbol:
            self.maze_label16.config(fg = "green")
        if vision_maze[3][1] == self.maze.player_symbol:
            self.maze_label17.config(fg = "blue")
        elif vision_maze[3][1] == self.maze.treasure_symbol:
            self.maze_label17.config(fg = "yellow")
        elif vision_maze[3][1] == self.maze.boss_symbol:
            self.maze_label17.config(fg = "red")
        elif vision_maze[3][1] == self.maze.torch_symbol:
            self.maze_label17.config(fg = "orange")
        elif vision_maze[3][1] == self.maze.exit_symbol:
            self.maze_label17.config(fg = "green")
        if vision_maze[3][2] == self.maze.player_symbol:
            self.maze_label18.config(fg = "blue")
        elif vision_maze[3][2] == self.maze.treasure_symbol:
            self.maze_label18.config(fg = "yellow")
        elif vision_maze[3][2] == self.maze.boss_symbol:
            self.maze_label18.config(fg = "red")
        elif vision_maze[3][2] == self.maze.torch_symbol:
            self.maze_label18.config(fg = "orange")
        elif vision_maze[3][2] == self.maze.exit_symbol:
            self.maze_label18.config(fg = "green")
        if vision_maze[3][3] == self.maze.player_symbol:
            self.maze_label19.config(fg = "blue")
        elif vision_maze[3][3] == self.maze.treasure_symbol:
            self.maze_label19.config(fg = "yellow")
        elif vision_maze[3][3] == self.maze.boss_symbol:
            self.maze_label19.config(fg = "red")
        elif vision_maze[3][3] == self.maze.torch_symbol:
            self.maze_label19.config(fg = "orange")
        elif vision_maze[3][3] == self.maze.exit_symbol:
            self.maze_label19.config(fg = "green")
        if vision_maze[3][4] == self.maze.player_symbol:
            self.maze_label20.config(fg = "blue")
        elif vision_maze[3][4] == self.maze.treasure_symbol:
            self.maze_label20.config(fg = "yellow")
        elif vision_maze[3][4] == self.maze.boss_symbol:
            self.maze_label20.config(fg = "red")
        elif vision_maze[3][4] == self.maze.torch_symbol:
            self.maze_label20.config(fg = "orange")
        elif vision_maze[3][4] == self.maze.exit_symbol:
            self.maze_label20.config(fg = "green")
        if vision_maze[4][0] == self.maze.player_symbol:
            self.maze_label21.config(fg = "blue")
        elif vision_maze[4][0] == self.maze.treasure_symbol:
            self.maze_label21.config(fg = "yellow")
        elif vision_maze[4][0] == self.maze.boss_symbol:
            self.maze_label21.config(fg = "red")
        elif vision_maze[4][0] == self.maze.torch_symbol:
            self.maze_label21.config(fg = "orange")
        elif vision_maze[4][0] == self.maze.exit_symbol:
            self.maze_label21.config(fg = "green")
        if vision_maze[4][1] == self.maze.player_symbol:
            self.maze_label22.config(fg = "blue")
        elif vision_maze[4][1] == self.maze.treasure_symbol:
            self.maze_label22.config(fg = "yellow")
        elif vision_maze[4][1] == self.maze.boss_symbol:
            self.maze_label22.config(fg = "red")
        elif vision_maze[4][1] == self.maze.torch_symbol:
            self.maze_label22.config(fg = "orange")
        elif vision_maze[4][1] == self.maze.exit_symbol:
            self.maze_label22.config(fg = "green")
        if vision_maze[4][2] == self.maze.player_symbol:
            self.maze_label23.config(fg = "blue")
        elif vision_maze[4][2] == self.maze.treasure_symbol:
            self.maze_label23.config(fg = "yellow")
        elif vision_maze[4][2] == self.maze.boss_symbol:
            self.maze_label23.config(fg = "red")
        elif vision_maze[4][2] == self.maze.torch_symbol:
            self.maze_label23.config(fg = "orange")
        elif vision_maze[4][2] == self.maze.exit_symbol:
            self.maze_label23.config(fg = "green")
        if vision_maze[4][3] == self.maze.player_symbol:
            self.maze_label24.config(fg = "blue")
        elif vision_maze[4][3] == self.maze.treasure_symbol:
            self.maze_label24.config(fg = "yellow")
        elif vision_maze[4][3] == self.maze.boss_symbol:
            self.maze_label24.config(fg = "red")
        elif vision_maze[4][3] == self.maze.torch_symbol:
            self.maze_label24.config(fg = "orange")
        elif vision_maze[4][3] == self.maze.exit_symbol:
            self.maze_label24.config(fg = "green")
        if vision_maze[4][4] == self.maze.player_symbol:
            self.maze_label25.config(fg = "blue")
        elif vision_maze[4][4] == self.maze.treasure_symbol:
            self.maze_label25.config(fg = "yellow")
        elif vision_maze[4][4] == self.maze.boss_symbol:
            self.maze_label25.config(fg = "red")
        elif vision_maze[4][4] == self.maze.torch_symbol:
            self.maze_label25.config(fg = "orange")
        elif vision_maze[4][4] == self.maze.exit_symbol:
            self.maze_label25.config(fg = "green")

        self.root.update()
    
    
    