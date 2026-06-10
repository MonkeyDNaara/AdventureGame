class Maze:
    def __init__(self, maze):
        self.DirDict = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        self.symbol = "O"
        self.maze = maze

    def check_position(self, array, symbol):
        for entry in array:
            if symbol in entry:
                y = array.index(entry)
                x = entry.index(symbol)
                return (y, x)

    def move(self, direction):
        actual_pos = self.check_position(self.maze, self.symbol)
        move_dir = self.DirDict[direction]
        self.maze[actual_pos[0]][actual_pos[1]] = self.maze[
            actual_pos[0] + move_dir[0]
        ][actual_pos[1] + move_dir[1]]
        self.maze[actual_pos[0] + move_dir[0]][
            actual_pos[1] + move_dir[1]
        ] = self.symbol
        return self.maze

    def print_maze(self):
        print("")
        for i in self.maze:
            print("".join(i))
