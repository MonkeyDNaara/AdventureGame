import tkinter as tk
from tkinter import messagebox
from maze import Maze


class MainWindow:
    def __init__(self, maze, char_name, hp, attack, defense, vision_range):
        self.initial_maze = maze
        self.char_name = char_name
        self.char_hp = hp
        self.char_attack = attack
        self.char_defense = defense
        self.vision_range = vision_range
        self.maze = Maze(self.initial_maze, self.vision_range)

        self.root = tk.Tk()
        self.root.title("Maze Runner")
        self.root.geometry("1200x800")

        self.header = tk.Label(self.root, text="Maze Runner", font=("Arial", 24), fg='red')
        self.header.pack(padx=20, pady=20)
        self.header.pack(fill="x")
        
        self.statsframe = tk.Frame(self.root)
        self.statsframe.columnconfigure(
            0, weight=1
        )
        self.statsframe.columnconfigure(
            1, weight=1)
        self.statsframe.rowconfigure(
            0, weight=1
        )
        self.statsframe.rowconfigure(
            1, weight=1)
        
        self.char_name_label = tk.Label(self.statsframe, text=f"Name: {self.char_name}", font=("Arial", 16))
        self.char_name_label.grid(row=0, column=0, sticky=tk.W + tk.E, padx=10, pady=10)

        self.char_hp_label = tk.Label(self.statsframe, text=f"HP: {self.char_hp}", font=("Arial", 16))
        self.char_hp_label.grid(row=1, column=0, sticky=tk.W + tk.E, padx=10, pady=10)

        self.char_attack_label = tk.Label(self.statsframe, text=f"Attack: {self.char_attack}", font=("Arial", 16))
        self.char_attack_label.grid(row=0, column=1, sticky=tk.W + tk.E, padx=10, pady=10)

        self.char_defense_label = tk.Label(self.statsframe, text=f"Defense: {self.char_defense}", font=("Arial", 16))
        self.char_defense_label.grid(row=1, column=1, sticky=tk.W + tk.E, padx=10, pady=10)

        self.statsframe.pack(fill="x", pady=10, padx=10)

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
        self.maze_label1 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[0][0]}", font=("Arial", 20))
        self.maze_label1.grid(row=0, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label2 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[0][1]}", font=("Arial", 20))
        self.maze_label2.grid(row=0, column=1, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label3 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[0][2]}", font=("Arial", 20))
        self.maze_label3.grid(row=0, column=2, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label4 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[0][3]}", font=("Arial", 20))
        self.maze_label4.grid(row=0, column=3, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label5 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[0][4]}", font=("Arial", 20))
        self.maze_label5.grid(row=0, column=4, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label6 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[1][0]}", font=("Arial", 20))
        self.maze_label6.grid(row=1, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label7 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[1][1]}", font=("Arial", 20))
        self.maze_label7.grid(row=1, column=1, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label8 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[1][2]}", font=("Arial", 20))
        self.maze_label8.grid(row=1, column=2, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label9 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[1][3]}", font=("Arial", 20))
        self.maze_label9.grid(row=1, column=3, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label10 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[1][4]}", font=("Arial", 20))
        self.maze_label10.grid(row=1, column=4, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label11 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[2][0]}", font=("Arial", 20))
        self.maze_label11.grid(row=2, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label12 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[2][1]}", font=("Arial", 20))
        self.maze_label12.grid(row=2, column=1, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label13 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[2][2]}", font=("Arial", 20))
        self.maze_label13.grid(row=2, column=2, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label14 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[2][3]}", font=("Arial", 20))
        self.maze_label14.grid(row=2, column=3, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label15 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[2][4]}", font=("Arial", 20))
        self.maze_label15.grid(row=2, column=4, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label16 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[3][0]}", font=("Arial", 20))
        self.maze_label16.grid(row=3, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label17 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[3][1]}", font=("Arial", 20))
        self.maze_label17.grid(row=3, column=1, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label18 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[3][2]}", font=("Arial", 20))
        self.maze_label18.grid(row=3, column=2, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label19 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[3][3]}", font=("Arial", 20))
        self.maze_label19.grid(row=3, column=3, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label20 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[3][4]}", font=("Arial", 20))
        self.maze_label20.grid(row=3, column=4, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label21 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[4][0]}", font=("Arial", 20))
        self.maze_label21.grid(row=4, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label22 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[4][1]}", font=("Arial", 20))
        self.maze_label22.grid(row=4, column=1, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label23 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[4][2]}", font=("Arial", 20))
        self.maze_label23.grid(row=4, column=2, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label24 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[4][3]}", font=("Arial", 20))
        self.maze_label24.grid(row=4, column=3, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_label25 = tk.Label(self.maze_frame, text=f"{self.maze.vision_maze[4][4]}", font=("Arial", 20))
        self.maze_label25.grid(row=4, column=4, sticky=tk.W + tk.E, padx=10, pady=10)
        self.maze_frame.pack(pady=10, padx=10)

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

        buttonframe.pack(fill="x", pady=10, padx=10)


        self.root.update()
        self.root.bind("<w>", self.key_event)
        self.root.bind("<a>", self.key_event)
        self.root.bind("<s>", self.key_event)
        self.root.bind("<d>", self.key_event)
        # self.root.bind("<Space>", maze.check_action)
        self.root.bind("<q>", self.key_event)

        self.root.mainloop()
    
    def key_event(self, event):
        actual_vision_maze = self.maze.check_action(event)
        self.update_label(actual_vision_maze)

    def update_label(self, vision_maze):
        self.maze_label1.config(text = f"{vision_maze[0][0]}")
        self.maze_label2.config(text = f"{vision_maze[0][1]}")
        self.maze_label3.config(text = f"{vision_maze[0][2]}")
        self.maze_label4.config(text = f"{vision_maze[0][3]}")
        self.maze_label5.config(text = f"{vision_maze[0][4]}")
        self.maze_label6.config(text = f"{vision_maze[1][0]}")
        self.maze_label7.config(text = f"{vision_maze[1][1]}")
        self.maze_label8.config(text = f"{vision_maze[1][2]}")
        self.maze_label9.config(text = f"{vision_maze[1][3]}")
        self.maze_label10.config(text = f"{vision_maze[1][4]}")
        self.maze_label11.config(text = f"{vision_maze[2][0]}")
        self.maze_label12.config(text = f"{vision_maze[2][1]}")
        self.maze_label13.config(text = f"{vision_maze[2][2]}")
        self.maze_label14.config(text = f"{vision_maze[2][3]}")
        self.maze_label15.config(text = f"{vision_maze[2][4]}")
        self.maze_label16.config(text = f"{vision_maze[3][0]}")
        self.maze_label17.config(text = f"{vision_maze[3][1]}")
        self.maze_label18.config(text = f"{vision_maze[3][2]}")
        self.maze_label19.config(text = f"{vision_maze[3][3]}")
        self.maze_label20.config(text = f"{vision_maze[3][4]}")
        self.maze_label21.config(text = f"{vision_maze[4][0]}")
        self.maze_label22.config(text = f"{vision_maze[4][1]}")
        self.maze_label23.config(text = f"{vision_maze[4][2]}")
        self.maze_label24.config(text = f"{vision_maze[4][3]}")
        self.maze_label25.config(text = f"{vision_maze[4][4]}")

        self.root.update()
    
    
    