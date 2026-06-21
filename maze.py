import game_logic
import random

class Maze:
    def __init__(self, maze, vision_range):
        self.DirDict = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1), " ": (0, 0)}
        self.player_symbol = "O"
        self.wall_symbol = "I"
        self.treasure_symbol = "X"
        self.boss_symbol = "B"
        self.torch_symbol = "F"
        self.exit_symbol = "A"
        self.goblin_symbol = "G"
        self.potion_symbol = "P"
        self.maze = maze
        self.vision_range = vision_range
        self.vision_maze = self.show_vision_maze(self.vision_range)
        self.character = game_logic.Character("Nyrik")

    def check_position(self, array, symbol):
        for entry in array:
            if symbol in entry:
                y = array.index(entry)
                x = entry.index(symbol)
                return (y, x)

    def check_action(self, key = " "):
        actual_pos = self.check_position(self.maze, self.player_symbol)
        move_dir = self.DirDict[key]
        target_pos = self.maze[actual_pos[0] + move_dir[0]][actual_pos[1] + move_dir[1]]
        if target_pos == self.wall_symbol:
            pass
        elif target_pos == self.treasure_symbol:
            self.move(actual_pos, move_dir)
            self.maze[actual_pos[0]][actual_pos[1]] = " "
            while True and len(self.character.inventory) < len(game_logic.weapons) + len(game_logic.armors):
                random_weapon = game_logic.weapons[random.randint(0, len(game_logic.weapons) - 1)]
                random_armor = game_logic.armors[random.randint(0, len(game_logic.armors) - 1)]
                random_number = random.randint(0, 1)
                if random_number == 0:
                    if random_weapon not in self.character.inventory:
                        self.character.pick_up_item(random_weapon)
                        break
                else:
                    if random_armor not in self.character.inventory:
                        self.character.pick_up_item(random_armor)
                        break
        elif target_pos == self.torch_symbol:
            self.move(actual_pos, move_dir)
            self.maze[actual_pos[0]][actual_pos[1]] = " "
            self.character.pick_up_item(game_logic.useful_items[0])
        elif target_pos == self.exit_symbol:
            self.move(actual_pos, move_dir)
            self.maze[actual_pos[0]][actual_pos[1]] = " "
        elif target_pos == self.boss_symbol:
            self.move(actual_pos, move_dir)
            self.maze[actual_pos[0]][actual_pos[1]] = " "
            self.character.fight(game_logic.enemies[0])
        elif target_pos == self.goblin_symbol:
            self.move(actual_pos, move_dir)
            self.maze[actual_pos[0]][actual_pos[1]] = " "
            self.character.fight(game_logic.enemies[1])
        elif target_pos == self.potion_symbol:
            self.move(actual_pos, move_dir)
            self.maze[actual_pos[0]][actual_pos[1]] = " "
            random_potion = game_logic.potions[random.randint(0, len(game_logic.potions) - 1)]
            self.character.pick_up_item(random_potion)
        else:
            self.move(actual_pos, move_dir)
        actual_vision_maze = self.show_vision_maze(self.vision_range)
        return actual_vision_maze

    def move(self, actual_pos, move_dir):
        self.maze[actual_pos[0]][actual_pos[1]] = self.maze[
            actual_pos[0] + move_dir[0]
        ][actual_pos[1] + move_dir[1]]
        self.maze[actual_pos[0] + move_dir[0]][
            actual_pos[1] + move_dir[1]
        ] = self.player_symbol
        return self.maze

    def show_vision_maze(self, vision_range):
        actual_pos = self.check_position(self.maze, self.player_symbol)
        vision_maze = []
        # print("")
        for i in range(-1 * vision_range, vision_range + 1, 1):
            vision_maze_row = ""
            for j in range(-1 * vision_range, vision_range + 1, 1):
                vision_y = actual_pos[0] + i
                vision_x = actual_pos[1] + j
                if vision_y < 0:
                    continue
                elif vision_y >= len(self.maze):
                    continue
                if vision_x < 0:
                    continue
                elif vision_x >= len(self.maze[0]):
                    continue
                vision_maze_row += self.maze[vision_y][vision_x]
            while len(vision_maze_row) < vision_range * 2 + 1:
                vision_maze_row += " "
            # print(vision_maze_row)
            vision_maze.append(vision_maze_row)
        while len(vision_maze) < vision_range * 2 + 1:
            empty_string = ""
            for i in range(vision_range * 2 + 1):
                empty_string += " "
            vision_maze.append(empty_string)
        return vision_maze
