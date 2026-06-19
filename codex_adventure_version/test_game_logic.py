import unittest

from game_logic import (
    EMPTY_DOT,
    FULL_DOT,
    collect_item,
    consume_messages,
    create_enemy,
    create_player,
    format_inventory,
    format_status,
    get_attack,
    make_dots,
    potions,
    use_potion,
    weapons,
)


class GameLogicTests(unittest.TestCase):
    def test_player_start_values_are_simple(self):
        player = create_player()

        self.assertEqual(player["name"], "Nyrik")
        self.assertEqual(player["level"], 1)
        self.assertEqual(player["xp_to_next_level"], 10)
        self.assertEqual(player["hp"], 30)
        self.assertEqual(player["max_hp"], 30)
        self.assertEqual(player["vision"], 0)

    def test_weapons_and_potions_keep_known_values(self):
        self.assertEqual(weapons["stick"]["attack_bonus"], 2)
        self.assertEqual(weapons["rusty_sword"]["attack_bonus"], 4)
        self.assertEqual(weapons["iron_sword"]["attack_bonus"], 7)
        self.assertEqual(potions["small_potion"]["heal"], 10)
        self.assertEqual(potions["big_potion"]["heal"], 20)

    def test_status_has_level_xp_and_hp_with_dots(self):
        player = create_player()
        player["xp"] = 5
        player["hp"] = 15

        status = format_status(player)

        self.assertIn("LVL 1", status)
        self.assertIn("XP  5/10", status)
        self.assertIn("HP  15/30", status)
        self.assertIn(FULL_DOT * 5 + EMPTY_DOT * 5, status)

    def test_make_dots_uses_same_style_for_xp_and_hp(self):
        self.assertEqual(make_dots(5, 10), FULL_DOT * 5 + EMPTY_DOT * 5)
        self.assertEqual(make_dots(0, 10), EMPTY_DOT * 10)
        self.assertEqual(make_dots(10, 10), FULL_DOT * 10)

    def test_collect_torch_sets_vision(self):
        player = create_player()

        collect_item(player, {"type": "torch"})

        self.assertTrue(player["has_torch"])
        self.assertEqual(player["vision"], 1)
        self.assertIn("torch", " ".join(consume_messages(player)).lower())

    def test_collect_sword_changes_attack(self):
        player = create_player()

        collect_item(player, {"type": "weapon", "name": "rusty_sword"})

        self.assertEqual(player["weapon"], "rusty_sword")
        self.assertEqual(get_attack(player), 9)

    def test_collect_key_adds_key_to_player(self):
        player = create_player()

        collect_item(player, {"type": "key", "key": "x"})

        self.assertIn("x", player["keys"])

    def test_use_potion_outside_combat(self):
        player = create_player()
        player["hp"] = 20
        player["inventory"].append("small_potion")

        used = use_potion(player, "small_potion")

        self.assertTrue(used)
        self.assertEqual(player["hp"], 30)
        self.assertEqual(player["inventory"], [])

    def test_create_enemy_reads_fixed_enemy_values(self):
        enemy = create_enemy(2)

        self.assertEqual(enemy["level"], 2)
        self.assertEqual(enemy["max_hp"], enemy["hp"])

    def test_inventory_counts_potions_keys_and_weapon(self):
        player = create_player()
        player["inventory"] = ["small_potion", "big_potion", "big_potion"]
        player["keys"] = ["x"]
        player["weapon"] = "rusty_sword"

        inventory_text = format_inventory(player)

        self.assertIn("Small Potion: 1", inventory_text)
        self.assertIn("Big Potion:   2", inventory_text)
        self.assertIn("Keys:         x", inventory_text)
        self.assertIn("Old Rusty Sword", inventory_text)


if __name__ == "__main__":
    unittest.main()
