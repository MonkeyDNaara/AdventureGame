import contextlib
import io
import unittest

from game_logic import consume_messages, create_player
from maze import Maze


class MazeTests(unittest.TestCase):
    def test_starting_vision_shows_player_and_torch_light(self):
        player = create_player()
        maze = Maze()

        rendered = maze.render(player)

        self.assertIn("O", rendered)
        self.assertIn("F", rendered)
        self.assertIn("?", rendered)

    def test_moving_onto_torch_does_not_auto_collect(self):
        player = create_player()
        maze = Maze()

        result = maze.move_player(player, "w")

        self.assertTrue(result["moved"])
        self.assertEqual(result["outcome"], "standing_on_item")
        self.assertFalse(player["has_torch"])
        self.assertEqual(maze.tile_symbol((17, 1)), "F")
        self.assertIn("Torch", maze.get_current_item_prompt())

    def test_space_pickup_collects_torch_removes_symbol_and_expands_vision(self):
        player = create_player()
        maze = Maze()
        maze.move_player(player, "w")

        with contextlib.redirect_stdout(io.StringIO()):
            result = maze.pickup_current_item(player)

        self.assertTrue(result["moved"])
        self.assertEqual(result["outcome"], "collected")
        self.assertTrue(player["has_torch"])
        self.assertGreater(player["vision"], 0)
        self.assertEqual(maze.tile_symbol((17, 1)), " ")
        self.assertNotIn("F", maze.render(player, reveal_all=True))
        self.assertIn("torch", " ".join(consume_messages(player)).lower())

    def test_item_prompt_names_potions(self):
        maze = Maze()
        maze.player_position = (2, 1)

        prompt = maze.get_current_item_prompt()

        self.assertIn("Small Potion", prompt)
        self.assertIn("Space", prompt)

    def test_wasd_directions_are_supported(self):
        maze = Maze()

        self.assertEqual(maze.normalize_direction("w"), "up")
        self.assertEqual(maze.normalize_direction("a"), "left")
        self.assertEqual(maze.normalize_direction("s"), "down")
        self.assertEqual(maze.normalize_direction("d"), "right")

    def test_walls_block_line_of_sight(self):
        player = create_player()
        player["vision"] = 5
        maze = Maze()

        self.assertTrue(maze.is_visible((17, 1), player))
        self.assertFalse(maze.is_visible((18, 3), player))

    def test_spawn_room_can_be_farmed(self):
        player = create_player()
        player["strength"] = 99
        maze = Maze()
        maze.player_position = (13, 2)

        with contextlib.redirect_stdout(io.StringIO()):
            result = maze.move_player(
                player,
                "d",
                input_func=lambda prompt: "fight",
                spawn_roll=0,
            )

        self.assertEqual(result["outcome"], "enemy_defeated")
        self.assertEqual(maze.tile_symbol((13, 3)), "S")

    def test_fleeing_enemy_keeps_player_in_place(self):
        player = create_player()
        maze = Maze()
        maze.player_position = (15, 8)

        with contextlib.redirect_stdout(io.StringIO()):
            result = maze.move_player(player, "d", input_func=lambda prompt: "flee")

        self.assertFalse(result["moved"])
        self.assertEqual(result["outcome"], "fled")
        self.assertEqual(maze.player_position, (15, 8))


if __name__ == "__main__":
    unittest.main()
