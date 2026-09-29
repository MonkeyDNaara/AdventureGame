import unittest

from maze import Maze

TEST_MAZE = [
    list("IIIII"),
    list("IO GI"),
    list("I IPI"),
    list("IFIAI"),
    list("IIIII"),
]


class TestMaze(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(TEST_MAZE)

    def test_wall_blocks_movement(self):
        self.maze.check_action("w")
        self.assertEqual(self.maze.player_pos, (1, 1))

    def test_move_and_pick_up_torch(self):
        self.maze.check_action("s")
        self.maze.check_action("s")
        self.assertEqual(self.maze.player_pos, (3, 1))
        self.assertEqual(self.maze.character.vision_range, 2)

    def test_running_into_enemy_starts_fight(self):
        self.maze.check_action("d")
        enemy = self.maze.check_action("d")
        self.assertEqual(enemy.name, "Goblin")
        self.assertEqual(self.maze.player_pos, (1, 2))
        # same enemy again if you walk into it again
        self.assertIs(self.maze.check_action("d"), enemy)

    def test_remove_enemy_clears_tile(self):
        self.maze.check_action("d")
        enemy = self.maze.check_action("d")
        self.maze.remove_enemy(enemy)
        self.assertEqual(self.maze.maze[1][3], " ")

    def test_vision_is_limited_without_torch(self):
        vision = self.maze.show_vision_maze()
        self.assertEqual(len(vision), 5)
        # the outer ring stays dark until the torch is picked up
        self.assertEqual(vision[0], "     ")
        self.assertEqual(vision[2][2], "O")

    def test_new_maze_does_not_change_the_layout(self):
        self.maze.check_action("d")
        self.assertEqual(TEST_MAZE[1][1], "O")


if __name__ == "__main__":
    unittest.main()
