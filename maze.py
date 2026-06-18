class Maze:
    def __init__(self, maze, vision_range):
        self.DirDict = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
        self.player_symbol = "O"
        self.wall_symbol = "I"
        self.treasure_symbol = "X"
        self.boss_symbol = "B"
        self.maze = maze
        self.vision_range = vision_range

    def check_position(self, array, symbol):
        for entry in array:
            if symbol in entry:
                y = array.index(entry)
                x = entry.index(symbol)
                return (y, x)

    def check_action(self, event):
        actual_pos = self.check_position(self.maze, self.player_symbol)
        move_dir = self.DirDict[event.keysym]
        target_pos = self.maze[actual_pos[0] + move_dir[0]][actual_pos[1] + move_dir[1]]
        if target_pos == self.wall_symbol:
            pass
        elif target_pos == self.treasure_symbol:
            self.move(actual_pos, move_dir)
            self.maze[actual_pos[0]][actual_pos[1]] = " "
        elif target_pos == self.boss_symbol:
            self.move(actual_pos, move_dir)
            self.maze[actual_pos[0]][actual_pos[1]] = " "
            print("You won.")
        else:
            self.move(actual_pos, move_dir)
        self.show_vision_maze(self.vision_range)
        

    def move(self, actual_pos, move_dir):
        self.maze[actual_pos[0]][actual_pos[1]] = self.maze[
            actual_pos[0] + move_dir[0]
        ][actual_pos[1] + move_dir[1]]
        self.maze[actual_pos[0] + move_dir[0]][
            actual_pos[1] + move_dir[1]
        ] = self.player_symbol
        return self.maze

    def print_maze(self):
        print("")
        for i in self.maze:
            print("".join(i))

    def show_vision_maze(self, vision_range):
        actual_pos = self.check_position(self.maze, self.player_symbol)
        vision_maze = []
        print("")
        for i in range(-1 * vision_range, vision_range + 1, 1):
            vision_maze = []
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
                vision_maze.append(self.maze[vision_y][vision_x])
            print("".join(vision_maze))
