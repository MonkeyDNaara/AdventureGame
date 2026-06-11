class Maze:
    def __init__(self, maze):
        self.DirDict = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        self.player_symbol = "O"
        self.wall_symbol = "I"
        self.treasure_symbol = "X"
        self.boss_symbol = "B"
        self.maze = maze

    def check_position(self, array, symbol):
        for entry in array:
            if symbol in entry:
                y = array.index(entry)
                x = entry.index(symbol)
                return (y, x)

    def check_action(self, direction):
        actual_pos = self.check_position(self.maze, self.player_symbol)
        move_dir = self.DirDict[direction]
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
