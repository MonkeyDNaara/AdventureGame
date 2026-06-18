import random

from game_logic import get_item_display_name, handle_tile


TORCH_LIGHT_RADIUS = 1
COLLECTABLE_TYPES = {"torch", "potion", "weapon", "key"}


DEFAULT_MAZE = [
    "IIIIIIIIIIIIIIIIIIII",
    "I   I I     I W I  I",
    "IP    I IIIII   I II",
    "I   I I     I   I II",
    "IIIII IIIII III I II",
    "I     I     I      I",
    "I IIIII II IIIIIII I",
    "I        I         I",
    "IIIIIIII IIII III II",
    "I      I  I I I I  I",
    "I II I II I I I    I",
    "I  I I  I I I IIII I",
    "IIII II I    P     I",
    "I  S  I I III IIIIII",
    "I III III I I  EI  I",
    "I   I  S EI   I I  I",
    "I I I IIIIIIIII I  I",
    "IFI I    IE  S  II I",
    "IOI I II IBI  I    I",
    "IIIIIIIIIIIIIIIIIIII",
]


SPECIAL_TILES = {
    (1, 14): {"type": "weapon", "name": "iron_sword"},
    (2, 1): {"type": "potion", "name": "small_potion"},
    (12, 13): {"type": "potion", "name": "big_potion"},
    (13, 3): {"type": "spawn", "enemy_level": 1, "spawn_chance": 0.75},
    (15, 7): {"type": "spawn", "enemy_level": 2, "spawn_chance": 0.75},
    (17, 13): {"type": "spawn", "enemy_level": 3, "spawn_chance": 0.75},
    (14, 15): {"type": "enemy", "enemy_level": 2},
    (15, 9): {"type": "enemy", "enemy_level": 2},
    (17, 10): {"type": "enemy", "enemy_level": 3},
}


SYMBOL_TILES = {
    " ": {"type": "empty"},
    "F": {"type": "torch"},
    "P": {"type": "potion", "name": "small_potion"},
    "W": {"type": "weapon", "name": "rusty_sword"},
    "E": {"type": "enemy", "enemy_level": 1},
    "S": {"type": "spawn", "enemy_level": 1, "spawn_chance": 0.75},
    "B": {"type": "boss"},
    "A": {"type": "exit"},
}


class Maze:
    def __init__(self, maze=None):
        self.DirDict = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }
        self.aliases = {
            "w": "up",
            "s": "down",
            "a": "left",
            "d": "right",
        }
        self.player_symbol = "O"
        self.wall_symbol = "I"
        self.torch_symbol = "F"
        self.spawn_symbol = "S"
        self.boss_symbol = "B"
        self.maze = [list(row) for row in (maze or DEFAULT_MAZE)]
        self.player_position = self.check_position(self.maze, self.player_symbol)

        if self.player_position is None:
            raise ValueError("Maze needs one player start symbol 'O'.")

        self.maze[self.player_position[0]][self.player_position[1]] = " "

    def check_position(self, array, symbol):
        if symbol == self.player_symbol and hasattr(self, "player_position"):
            return self.player_position

        for y, row in enumerate(array):
            if symbol in row:
                return (y, row.index(symbol))

        return None

    def normalize_direction(self, direction):
        direction = direction.lower()
        return self.aliases.get(direction, direction)

    def is_inside(self, position):
        y, x = position
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[y])

    def tile_symbol(self, position):
        y, x = position
        return self.maze[y][x]

    def set_tile_symbol(self, position, symbol):
        y, x = position
        self.maze[y][x] = symbol

    def get_tile(self, position):
        symbol = self.tile_symbol(position)
        tile = dict(SYMBOL_TILES.get(symbol, {"type": "empty"}))
        tile.update(SPECIAL_TILES.get(position, {}))
        return tile

    def get_current_item(self):
        tile = self.get_tile(self.player_position)

        if tile["type"] in COLLECTABLE_TYPES:
            return tile

        return None

    def get_current_item_prompt(self):
        item = self.get_current_item()

        if item is None:
            return ""

        return f"{get_item_display_name(item)}\nZum Aufnehmen press Space."

    def pickup_current_item(self, player):
        item = self.get_current_item()

        if item is None:
            return self._result(False, "nothing_to_pick_up", "There is nothing here to pick up.")

        outcome = handle_tile(player, item)

        if outcome == "collected":
            self.set_tile_symbol(self.player_position, " ")

        return self._result(True, outcome, "Picked up item.")

    def check_action(self, direction):
        return self.move_player(None, direction, reveal_result=True)

    def move(self, actual_pos, move_dir):
        target = (actual_pos[0] + move_dir[0], actual_pos[1] + move_dir[1])

        if self.is_inside(target) and self.tile_symbol(target) != self.wall_symbol:
            self.player_position = target

        return self.render_grid(reveal_all=True)

    def move_player(
        self,
        player,
        direction,
        input_func=input,
        combat_action_provider=None,
        reveal_result=False,
        spawn_roll=None,
    ):
        direction = self.normalize_direction(direction)

        if direction not in self.DirDict:
            return self._result(False, "invalid", "Unknown direction.")

        dy, dx = self.DirDict[direction]
        target = (self.player_position[0] + dy, self.player_position[1] + dx)

        if not self.is_inside(target) or self.tile_symbol(target) == self.wall_symbol:
            return self._result(False, "blocked", "A wall blocks the way.")

        if player is None:
            self.player_position = target
            if reveal_result:
                self.print_maze(reveal_all=True)
            return self._result(True, "moved", "Moved.")

        tile = self.get_tile(target)

        if tile["type"] in COLLECTABLE_TYPES:
            self.player_position = target
            return self._result(True, "standing_on_item", "Moved.")

        if tile["type"] == "spawn":
            roll = random.random() if spawn_roll is None else spawn_roll
            if roll <= tile.get("spawn_chance", 1):
                tile = {"type": "enemy", "enemy_level": tile["enemy_level"]}
            else:
                tile = {"type": "empty"}
                print("The shadows move, but nothing attacks.")

        outcome = handle_tile(player, tile, input_func, combat_action_provider)

        if outcome in {"fled", "locked", "dead"}:
            return self._result(False, outcome, "You stay where you are.")

        self.player_position = target

        if outcome == "enemy_defeated" and self.tile_symbol(target) != self.spawn_symbol:
            self.set_tile_symbol(target, " ")

        if outcome == "win":
            self.set_tile_symbol(target, "A")
            return self._result(True, "win", "The maze releases you.")

        return self._result(True, outcome, "Moved.")

    def _result(self, moved, outcome, message):
        return {
            "moved": moved,
            "outcome": outcome,
            "message": message,
            "position": self.player_position,
        }

    def render_grid(self, player=None, reveal_all=False):
        lines = []

        for y, row in enumerate(self.maze):
            visible_row = []
            for x, symbol in enumerate(row):
                position = (y, x)

                if position == self.player_position:
                    visible_row.append(self.player_symbol)
                elif reveal_all or self.is_visible(position, player):
                    visible_row.append(symbol)
                else:
                    visible_row.append("?")

            lines.append(visible_row)

        return lines

    def render(self, player=None, reveal_all=False):
        return "\n".join("".join(row) for row in self.render_grid(player, reveal_all))

    def print_maze(self, player=None, reveal_all=False):
        print("")
        print(self.render(player, reveal_all))

    def is_visible(self, position, player):
        if position == self.player_position:
            return True

        if self.is_lit_by_torch(position):
            return True

        if player is None:
            return False

        vision = player.get("vision", 0)
        if vision <= 0:
            return False

        dy = abs(position[0] - self.player_position[0])
        dx = abs(position[1] - self.player_position[1])

        if max(dy, dx) > vision:
            return False

        return self.has_line_of_sight(self.player_position, position)

    def is_lit_by_torch(self, position):
        for y, row in enumerate(self.maze):
            for x, symbol in enumerate(row):
                if symbol != self.torch_symbol:
                    continue

                if max(abs(position[0] - y), abs(position[1] - x)) <= TORCH_LIGHT_RADIUS:
                    return True

        return False

    def has_line_of_sight(self, start, end):
        for point in self._line_between(start, end)[1:-1]:
            if self.tile_symbol(point) == self.wall_symbol:
                return False

        return True

    def _line_between(self, start, end):
        y0, x0 = start
        y1, x1 = end
        points = []
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        error = dx + dy

        while True:
            points.append((y0, x0))

            if (y0, x0) == (y1, x1):
                return points

            doubled_error = 2 * error

            if doubled_error >= dy:
                error += dy
                x0 += sx

            if doubled_error <= dx:
                error += dx
                y0 += sy
