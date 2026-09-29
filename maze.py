import copy
import random

import game_logic


def load_maze(path):
    with open(path, encoding="utf-8") as file:
        return [list(line.rstrip("\n")) for line in file if line.strip()]


class Maze:
    directions = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
    player_symbol = "O"
    wall_symbol = "I"
    treasure_symbol = "X"
    boss_symbol = "B"
    torch_symbol = "F"
    exit_symbol = "A"
    goblin_symbol = "G"
    potion_symbol = "P"
    empty_symbol = " "
    enemy_symbols = {goblin_symbol: "goblin", boss_symbol: "boss"}
    torch_vision_range = 2

    def __init__(self, maze, vision_range=2):
        # deepcopy so a new game always starts with the original layout
        self.maze = copy.deepcopy(maze)
        self.vision_range = vision_range
        self.character = game_logic.Character("Nyrik")
        self.player_pos = self.check_position(self.player_symbol)
        self.reached_exit = False
        # enemies are created on first contact and remembered by position,
        # so an enemy you fled from keeps its damage
        self.enemies = {}

    def check_position(self, symbol):
        for y, row in enumerate(self.maze):
            if symbol in row:
                return (y, row.index(symbol))
        return None

    def is_inside(self, y, x):
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[y])

    def check_action(self, key):
        """Moves the player. Returns the enemy if the player ran into one."""
        move_y, move_x = self.directions[key]
        target_pos = (self.player_pos[0] + move_y, self.player_pos[1] + move_x)
        if not self.is_inside(*target_pos):
            return
        target = self.maze[target_pos[0]][target_pos[1]]
        if target == self.wall_symbol:
            return
        if target in self.enemy_symbols:
            if target_pos not in self.enemies:
                self.enemies[target_pos] = game_logic.create_enemy(self.enemy_symbols[target])
            return self.enemies[target_pos]

        if target == self.treasure_symbol:
            self.open_chest()
        elif target == self.torch_symbol:
            self.character.pick_up_item(game_logic.useful_items[0])
            self.character.vision_range = self.torch_vision_range
        elif target == self.potion_symbol:
            self.character.pick_up_item(random.choice(game_logic.potions))
        elif target == self.exit_symbol:
            self.reached_exit = True
        self.move(target_pos)

    def remove_enemy(self, enemy):
        for pos, maze_enemy in list(self.enemies.items()):
            if maze_enemy is enemy:
                self.maze[pos[0]][pos[1]] = self.empty_symbol
                del self.enemies[pos]

    def open_chest(self):
        missing_items = [
            item for item in game_logic.weapons + game_logic.armors
            if item not in self.character.inventory
        ]
        if missing_items:
            self.character.pick_up_item(random.choice(missing_items))

    def move(self, target_pos):
        self.maze[self.player_pos[0]][self.player_pos[1]] = self.empty_symbol
        self.maze[target_pos[0]][target_pos[1]] = self.player_symbol
        self.player_pos = target_pos

    def show_vision_maze(self):
        player_y, player_x = self.player_pos
        # without the torch you only see the tiles right next to you
        sight = self.character.vision_range
        vision_maze = []
        for i in range(-self.vision_range, self.vision_range + 1):
            vision_maze_row = ""
            for j in range(-self.vision_range, self.vision_range + 1):
                vision_y = player_y + i
                vision_x = player_x + j
                in_sight = abs(i) <= sight and abs(j) <= sight
                if in_sight and self.is_inside(vision_y, vision_x):
                    vision_maze_row += self.maze[vision_y][vision_x]
                else:
                    vision_maze_row += self.empty_symbol
            vision_maze.append(vision_maze_row)
        return vision_maze
