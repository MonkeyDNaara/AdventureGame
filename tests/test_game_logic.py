import random
import unittest

from game_logic import Character, Fight, Item, create_enemy


class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.player = Character("Tester")

    def test_best_weapon_counts(self):
        self.player.pick_up_item(Item("Stick", "weapon", attack=2))
        self.player.pick_up_item(Item("Sword", "weapon", attack=7))
        self.assertEqual(self.player.attack, 12)

    def test_level_up_keeps_item_bonus(self):
        self.player.pick_up_item(Item("Chainmail", "armor", defense=4))
        messages = self.player.gain_exp(10)
        self.assertEqual(self.player.level, 2)
        self.assertEqual(self.player.defense, 10)
        self.assertIn("Level up! You are now LVL 2.", messages)

    def test_potion_heals_but_not_over_max(self):
        self.player.pick_up_item(Item("Small Potion", "potion", heal=10))
        self.player.take_damage(4)
        used, _ = self.player.use_potion()
        self.assertTrue(used)
        self.assertEqual(self.player.actual_hp, self.player.hp)
        self.assertEqual(self.player.inventory, [])

    def test_potion_not_used_at_full_hp(self):
        self.player.pick_up_item(Item("Small Potion", "potion", heal=10))
        used, _ = self.player.use_potion()
        self.assertFalse(used)
        self.assertEqual(len(self.player.inventory), 1)


class TestFight(unittest.TestCase):
    def setUp(self):
        random.seed(1)
        self.player = Character("Tester")
        self.goblin = create_enemy("goblin")
        self.fight = Fight(self.player, self.goblin)

    def test_attack_round_damages_both(self):
        self.fight.player_attack()
        self.assertLess(self.goblin.actual_hp, self.goblin.hp)
        self.assertLess(self.player.actual_hp, self.player.hp)
        self.assertEqual(self.fight.round, 2)

    def test_defend_takes_less_damage(self):
        self.fight.player_defend()
        self.assertGreaterEqual(self.player.actual_hp, self.player.hp - 1)

    def test_fight_until_win_gives_exp(self):
        self.player.pick_up_item(Item("Sword", "weapon", attack=7))
        while not self.fight.is_over:
            self.fight.player_attack()
        self.assertTrue(self.fight.player_won())
        self.assertEqual(self.player.level, 2)

    def test_player_can_lose(self):
        self.player.actual_hp = 1
        self.fight.player_attack()
        self.assertFalse(self.player.is_alive())
        self.assertTrue(self.fight.is_over)
        self.assertFalse(self.fight.player_won())

    def test_potion_without_potion_costs_no_turn(self):
        self.fight.player_use_potion()
        self.assertEqual(self.player.actual_hp, self.player.hp)
        self.assertEqual(self.fight.round, 1)


if __name__ == "__main__":
    unittest.main()
