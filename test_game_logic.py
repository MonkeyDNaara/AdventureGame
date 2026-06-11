from game_logic import create_player, handle_tile, use_potion

player = create_player()

print(player)

handle_tile(player, {"type": "weapon", "name": "rusty_sword"})
handle_tile(player, {"type": "potion", "name": "small_potion"})
handle_tile(player, {"type": "key", "color": "blue"})
handle_tile(player, {"type": "door", "color": "blue"})
handle_tile(player, {"type": "enemy", "enemy_level": 1})

use_potion(player, "small_potion")

print(player)