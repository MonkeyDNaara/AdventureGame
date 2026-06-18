import contextlib
import io
import unittest

from game_logic import (
    EMPTY_DOT,
    FULL_DOT,
    calculate_incoming_damage,
    collect_item,
    consume_messages,
    create_boss,
    create_player,
    fight,
    format_combat_view,
    format_encounter_prompt,
    format_hp_dots,
    format_status,
    handle_tile,
)


class GameLogicTests(unittest.TestCase):
    def test_player_starts_without_torch_or_vision(self):
        player = create_player()

        self.assertFalse(player["has_torch"])
        self.assertEqual(player["vision"], 0)

    def test_player_has_fixed_starting_stats(self):
        player = create_player()

        self.assertEqual(player["strength"], 5)
        self.assertEqual(player["armor"], 1)
        self.assertEqual(player["hp"], 60)
        self.assertNotIn("unspent_stat_points", player)

    def test_status_uses_hp_dots_and_xp_bar(self):
        player = create_player()
        player["hp"] = 30
        status = format_status(player)

        self.assertIn("LVL   1", status)
        self.assertIn("XP [", status)
        self.assertIn("HP    30/60", status)
        self.assertEqual(format_hp_dots(player), FULL_DOT * 5 + EMPTY_DOT * 5)

    def test_torch_expands_vision_and_adds_message(self):
        player = create_player()
        collect_item(player, {"type": "torch"})

        self.assertTrue(player["has_torch"])
        self.assertGreater(player["vision"], 0)
        self.assertIn("torch", " ".join(consume_messages(player)).lower())

    def test_armor_reduces_incoming_damage(self):
        player = create_player()

        self.assertEqual(calculate_incoming_damage(player, 8), 7)

    def test_encounter_prompt_shows_enemy_stats_once(self):
        prompt = format_encounter_prompt({
            "name": "Shadow Creature",
            "level": 1,
            "hp": 20,
            "max_hp": 20,
            "strength": 5,
        })

        self.assertIn("Enemy level: 1", prompt)
        self.assertIn("HP: 20/20", prompt)
        self.assertIn("STR: 5", prompt)

    def test_combat_view_shows_monster_player_and_inventory(self):
        player = create_player()
        player["inventory"].append("big_potion")
        boss = create_boss()
        view = format_combat_view(player, boss)

        self.assertIn("MONSTER", view)
        self.assertIn("PLAYER", view)
        self.assertIn("Small Potion: 0", view)
        self.assertIn("Big Potion:   1", view)

    def test_player_can_flee_before_fight_starts(self):
        player = create_player()

        with contextlib.redirect_stdout(io.StringIO()):
            outcome = handle_tile(
                player,
                {"type": "enemy", "enemy_level": 1},
                input_func=lambda prompt: "flee",
            )

        self.assertEqual(outcome, "fled")
        self.assertEqual(player["hp"], player["max_hp"])

    def test_unprepared_player_can_die_against_boss(self):
        player = create_player()

        with contextlib.redirect_stdout(io.StringIO()):
            survived = fight(player, create_boss())

        self.assertFalse(survived)
        self.assertFalse(player["alive"])

    def test_winning_fight_logs_combined_xp_message(self):
        player = create_player()
        enemy = {"name": "Test", "level": 1, "hp": 1, "max_hp": 1, "strength": 1, "attack": 1, "xp_reward": 3}

        fight(player, enemy)
        messages = consume_messages(player)

        self.assertIn("You won the fight! You gained 3 XP.", messages)


if __name__ == "__main__":
    unittest.main()
