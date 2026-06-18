import tkinter as tk
from tkinter import messagebox
from maze import Maze


class MainWindow:
    def __init__(self, maze, char_name, hp, attack, defense, vision_range):
        self.maze = maze
        self.char_name = char_name
        self.char_hp = hp
        self.char_attack = attack
        self.char_defense = defense
        self.vision_range = vision_range
        maze = Maze(self.maze, self.vision_range)

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

        self.textbox = tk.Text(self.root, height=5, font=("Arial", 12))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()  # erstellt eine Int Variable
        self.check = tk.Checkbutton(
            self.root,
            text="Show Messagebox",
            font=("Arial", 12),
            variable=self.check_state,  # weise der CHeckbox die Variabe check_state zu
        )
        self.check.pack(padx=10, pady=10)

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
            font=("Arial", 16),
            command=self.action,  # dem command (wenn der Button geclicked wird) wird die Funktion show message zugewiesen (darum ohne Klammern, mit Klammern würde die Funktion ausgeführt werden)
        )
        self.attack_button.grid(row=0, column=0, sticky=tk.W + tk.E, padx=10, pady=10)

        self.defend_button = tk.Button(
            buttonframe,
            text="Defend",
            font=("Arial", 16),
            command=self.action,  # dem command (wenn der Button geclicked wird) wird die Funktion show message zugewiesen (darum ohne Klammern, mit Klammern würde die Funktion ausgeführt werden)
        )
        self.defend_button.grid(row=0, column=1, sticky=tk.W + tk.E, padx=10, pady=10)

        self.potion_button = tk.Button(
            buttonframe,
            text="Potion",
            font=("Arial", 16),
            command=self.action,  # dem command (wenn der Button geclicked wird) wird die Funktion show message zugewiesen (darum ohne Klammern, mit Klammern würde die Funktion ausgeführt werden)
        )
        self.potion_button.grid(row=0, column=2, sticky=tk.W + tk.E, padx=10, pady=10)

        buttonframe.pack(fill="x", pady=10, padx=10)


        self.root.update()
        self.root.bind("<w>", maze.check_action)
        self.root.bind("<a>", maze.check_action)
        self.root.bind("<s>", maze.check_action)
        self.root.bind("<d>", maze.check_action)
        # self.root.bind("<Space>", maze.check_action)
        self.root.bind("<q>", maze.check_action)
        
        self.root.mainloop()

    def action(self):
        if (
            self.check_state.get() == 0
        ):  # gettet (holt) den Status der Variable check_state, da diese von einer Checkbox gesetzt wird, kann diese nur 0 oder 1 sein
            print(
                self.textbox.get("1.0", tk.END)
            )  # gettet den Inhalt der Textbox "textbox" von Anfang ("1.0" bedeutet Anfang) bis Ende (tk.END bedeutet bis zum Ende der Textbox)
        else:
            messagebox.showinfo(
                title="Messagebox", message=self.textbox.get("1.0", tk.END)
            )
    
    def doSomething(self, event):
        print(f"Button {event.keysym} pressed.")
        # mit label.config(text=...) kann das Label immer wieder verändert werden -> für Maze merken
        
    



