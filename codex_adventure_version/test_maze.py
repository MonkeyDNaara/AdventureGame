import unittest

from game_logic import create_player
from maze import DEFAULT_MAZE, HIDDEN_ROOM, UNKNOWN_SYMBOL, Maze


class MazeTests(unittest.TestCase):
    def test_maps_have_expected_size(self):
        self.assertEqual(len(DEFAULT_MAZE), 20)
        self.assertEqual({len(row) for row in DEFAULT_MAZE}, {20})
        self.assertEqual(len(HIDDEN_ROOM), 10)
        self.assertEqual({len(row) for row in HIDDEN_ROOM}, {10})

    def test_player_symbol_is_dot(self):
        maze = Maze()

        self.assertEqual(maze.player_symbol, "●")

    def test_unknown_tiles_use_block_symbol(self):
        player = create_player()
        maze = Maze()

        rendered = maze.render(player)

        self.assertIn(UNKNOWN_SYMBOL, rendered)
        self.assertNotIn("?", rendered)

    def test_torch_is_visible_before_player_has_vision(self):
        player = create_player()
        maze = Maze()

        rendered = maze.render(player)

        self.assertIn("F", rendered)
        self.assertEqual(player["vision"], 0)

    def test_move_is_simple_and_moves_to_empty_tile(self):
        maze = Maze()
        result = maze.move_player("w")

        self.assertEqual(result["outcome"], "moved")
        self.assertEqual(maze.player_position, (17, 1))

    def test_wall_blocks_movement(self):
        maze = Maze()
        result = maze.move_player("d")

        self.assertEqual(result["outcome"], "wall")
        self.assertEqual(maze.player_position, (18, 1))

    def test_collect_torch_after_standing_on_it(self):
        player = create_player()
        maze = Maze()
        maze.player_position = (14, 1)

        prompt = maze.get_current_item_prompt()
        result = maze.collect_current_item(player)

        self.assertIn("Torch", prompt)
        self.assertEqual(result["outcome"], "collected")
        self.assertTrue(player["has_torch"])
        self.assertEqual(maze.tile_at((14, 1)), " ")

    def test_potion_prompt_shows_name(self):
        maze = Maze()
        maze.player_position = (2, 1)

        prompt = maze.get_current_item_prompt()

        self.assertIn("Small Potion", prompt)
        self.assertIn("Press Space", prompt)

    def test_enemy_blocks_the_way_while_fights_are_disabled(self):
        maze = Maze()
        maze.player_position = (17, 8)

        result = maze.move_player("d")

        self.assertEqual(result["outcome"], "enemy")
        self.assertEqual(maze.player_position, (17, 8))
        self.assertEqual(maze.tile_at((17, 9)), "E")

    def test_chest_requires_key(self):
        player = create_player()
        maze = Maze()
        maze.player_position = (1, 1)

        result = maze.collect_current_item(player)

        self.assertEqual(result["outcome"], "locked")

    def test_chest_uses_key_and_gives_rewards(self):
        player = create_player()
        player["keys"].append("x")
        maze = Maze()
        maze.player_position = (1, 1)

        result = maze.collect_current_item(player)

        self.assertEqual(result["outcome"], "chest_opened")
        self.assertEqual(player["weapon"], "iron_sword")
        self.assertEqual(player["inventory"].count("big_potion"), 3)
        self.assertNotIn("x", player["keys"])
        self.assertEqual(maze.tile_at((1, 1)), " ")

    def test_secret_door_changes_map(self):
        maze = Maze()
        maze.player_position = (18, 2)

        result = maze.move_player("d")

        self.assertEqual(result["outcome"], "door")
        self.assertEqual(maze.current_map, "hidden")


if __name__ == "__main__":
    unittest.main()
