from game_logic import collect_item, create_enemy, has_key, item_info


UNKNOWN_SYMBOL = "□"
TORCH_LIGHT_RADIUS = 1


DEFAULT_MAZE = [
    "IIIIIIIIIIIIIIIIIIII",     #0
    "IX  I I     I S I  I",     #1
    "Ip    I IIIII   I II",     #2
    "I   I I     I   I II",     #3
    "IIIII IIIII III I II",     #4
    "I     I     I      I",     #5
    "I IIIII II IIIIIII I",     #6
    "I        I         I",     #7
    "IIIIIIII IIII III II",     #8
    "I      I  I I I I  I",     #9
    "I II I II I I I    I",     #10
    "I  I I  I I I IIII I",     #11
    "IIII II I          I",     #12
    "I     I I III IIII I",     #13
    "IFIII III I I   I  I",     #14
    "I   I     I   I I  I",     #15
    "I I I I IIIIIII I  I",     #16
    "I I I I IE      II I",     #17
    "I●I!I I  IBI   I   I",     #18
    "IIIIIIIIIIAIIIIIIIII",     #19
]


HIDDEN_ROOM = [
    "IIIIIIIIII",   #0
    "I●  I   !I",   #1
    "III I IIII",   #2
    "I   I    I",   #3
    "I IIII I I",   #4
    "I      I I",   #5
    "I IIIIII I",   #6
    "I M  XII I",   #7
    "IIIIIIx  I",   #8
    "IIIIIIIIII",   #9
]


DIRECTIONS = {
    "w": (-1, 0),
    "s": (1, 0),
    "a": (0, -1),
    "d": (0, 1),
}


ITEM_TILES = {
    "F": {"type": "torch"},
    "p": {"type": "potion", "name": "small_potion"},
    "P": {"type": "potion", "name": "big_potion"},
    "S": {"type": "weapon", "name": "rusty_sword"},
    "x": {"type": "key", "key": "x"},
}


ENEMY_TILES = {
    "e": 1,
    "E": 2,
    "m": 3,
    "M": 4,
    "B": 10,
}


class Maze:
    def __init__(self):
        self.maps = {
            "main": [list(row) for row in DEFAULT_MAZE],
            "hidden": [list(row) for row in HIDDEN_ROOM],
        }
        self.current_map = "main"
        self.maze = self.maps[self.current_map]
        self.player_symbol = "●"
        self.wall_symbol = "I"
        self.positions = {
            "main": self.find_and_remove_player("main"),
            "hidden": self.find_and_remove_player("hidden"),
        }
        self.player_position = self.positions["main"]

    def find_and_remove_player(self, map_name):
        maze = self.maps[map_name]

        for row in range(len(maze)):
            for col in range(len(maze[row])):
                if maze[row][col] == self.player_symbol:
                    maze[row][col] = " "
                    return (row, col)

        raise ValueError("Map needs a player symbol: ●")

    def tile_at(self, position):
        row, col = position
        return self.maze[row][col]

    def set_tile(self, position, symbol):
        row, col = position
        self.maze[row][col] = symbol

    def get_tile_info(self, position):
        symbol = self.tile_at(position)

        if symbol in ITEM_TILES:
            return ITEM_TILES[symbol].copy()

        if symbol in ENEMY_TILES:
            return {"type": "enemy", "level": ENEMY_TILES[symbol]}

        if symbol == "X":
            return {"type": "chest"}

        if symbol == "!":
            return {"type": "door"}

        if symbol == "A":
            return {"type": "exit"}

        return {"type": "empty"}

    # One simple move: calculate target, check tile, then decide what happens.
    def move_player(self, direction):
        if direction not in DIRECTIONS:
            return {"outcome": "invalid", "message": "Use W A S D to move."}

        row, col = self.player_position
        row_change, col_change = DIRECTIONS[direction]
        target = (row + row_change, col + col_change)

        if self.tile_at(target) == self.wall_symbol:
            return {"outcome": "wall", "message": "A wall blocks the way."}

        tile = self.get_tile_info(target)

        if tile["type"] == "enemy":
            enemy = create_enemy(tile["level"])
            return {"outcome": "enemy", "message": f"A {enemy['name']} blocks the way."}

        self.player_position = target

        if tile["type"] == "door":
            self.change_map()
            return {"outcome": "door", "message": "You found a hidden room."}

        if tile["type"] == "exit":
            return {"outcome": "win", "message": "You escaped the maze."}

        return {"outcome": "moved", "message": "Moved."}

    # Space uses this function. It only collects/open things under the player.
    def collect_current_item(self, player):
        tile = self.get_tile_info(self.player_position)

        if tile["type"] == "chest":
            return self.open_chest(player)

        if tile["type"] not in ["torch", "potion", "weapon", "key"]:
            return {"outcome": "nothing", "message": "There is nothing to pick up."}

        collect_item(player, tile)
        self.set_tile(self.player_position, " ")
        return {"outcome": "collected", "message": "Item collected."}

    def open_chest(self, player):
        if not has_key(player, "x"):
            return {"outcome": "locked", "message": "The chest is locked. You need key x."}

        player["keys"].remove("x")
        player["weapon"] = "iron_sword"
        player["inventory"].append("big_potion")
        player["inventory"].append("big_potion")
        player["inventory"].append("big_potion")
        self.set_tile(self.player_position, " ")
        return {"outcome": "chest_opened", "message": "You opened the chest and found an Iron Sword and 3 Big Potions."}

    def get_current_item_prompt(self):
        tile = self.get_tile_info(self.player_position)

        if tile["type"] == "torch":
            return "Torch\nPress Space to take it from the wall."

        if tile["type"] in ["potion", "weapon", "key"]:
            return f"{item_info(tile)}\nPress Space to pick it up."

        if tile["type"] == "chest":
            return "Chest\nPress Space to open it with key x."

        return ""

    def change_map(self):
        self.positions[self.current_map] = self.player_position

        if self.current_map == "main":
            self.current_map = "hidden"
        else:
            self.current_map = "main"

        self.maze = self.maps[self.current_map]
        self.player_position = self.positions[self.current_map]

    def render(self, player):
        rows = []

        for row in range(len(self.maze)):
            visible_row = ""
            for col in range(len(self.maze[row])):
                position = (row, col)

                if position == self.player_position:
                    visible_row += self.player_symbol
                elif self.is_visible(position, player):
                    visible_row += self.tile_at(position)
                else:
                    visible_row += UNKNOWN_SYMBOL

            rows.append(visible_row)

        return "\n".join(rows)

    def is_visible(self, position, player):
        if self.is_lit_by_torch(position):
            return True

        if player["vision"] <= 0:
            return False

        row_distance = abs(position[0] - self.player_position[0])
        col_distance = abs(position[1] - self.player_position[1])
        return max(row_distance, col_distance) <= player["vision"]

    def is_lit_by_torch(self, position):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == "F":
                    row_distance = abs(position[0] - row)
                    col_distance = abs(position[1] - col)

                    if max(row_distance, col_distance) <= TORCH_LIGHT_RADIUS:
                        return True

        return False
