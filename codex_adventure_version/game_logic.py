import math


MAX_STAT_DOTS = 10
XP_BAR_WIDTH = 12
BASE_MAX_HP = 60
BASE_STRENGTH = 5
BASE_ARMOR = 1
LEVEL_HP_BONUS = 8
LEVEL_STRENGTH_BONUS = 1
TORCH_VISION = 4

FULL_DOT = "●"
EMPTY_DOT = "○"


weapons = {
    "stick": {
        "name": "Wooden Stick",
        "attack_bonus": 2,
    },
    "rusty_sword": {
        "name": "Old Rusty Sword",
        "attack_bonus": 4,
    },
    "iron_sword": {
        "name": "Iron Sword",
        "attack_bonus": 7,
    },
}


potions = {
    "small_potion": {
        "name": "Small Potion",
        "heal": 15,
    },
    "big_potion": {
        "name": "Big Potion",
        "heal": 30,
    },
}


def get_item_display_name(item):
    item_type = item["type"]

    if item_type == "torch":
        return "Torch"

    if item_type == "potion":
        return potions[item["name"]]["name"]

    if item_type == "weapon":
        return weapons[item["name"]]["name"]

    if item_type == "key":
        return f"{item['color'].title()} Key"

    return "Item"


def create_player(name="Nyrik"):
    return {
        "name": name,
        "level": 1,
        "xp": 0,
        "xp_to_next_level": 12,
        "max_hp": BASE_MAX_HP,
        "hp": BASE_MAX_HP,
        "strength": BASE_STRENGTH,
        "armor": BASE_ARMOR,
        "weapon": None,
        "inventory": [],
        "keys": [],
        "has_torch": False,
        "vision": 0,
        "alive": True,
        "boss_defeated": False,
        "messages": [],
    }


def add_message(player, message):
    player.setdefault("messages", []).append(message)


def consume_messages(player):
    messages = player.get("messages", [])
    player["messages"] = []
    return messages


def format_progress_bar(current, maximum, width=XP_BAR_WIDTH):
    if maximum <= 0:
        filled = width
    else:
        filled = math.floor((current / maximum) * width)

    filled = max(0, min(filled, width))
    return "[" + "#" * filled + "-" * (width - filled) + "]"


def format_stat_dots(label, value, maximum=MAX_STAT_DOTS):
    visible_value = max(0, min(value, maximum))
    return f"{label:<5} {value:<7} " + (FULL_DOT * visible_value) + (EMPTY_DOT * (maximum - visible_value))


def format_hp_dots(player):
    if player["max_hp"] <= 0 or player["hp"] <= 0:
        full_count = 0
    else:
        full_count = math.ceil((player["hp"] / player["max_hp"]) * MAX_STAT_DOTS)

    full_count = max(0, min(full_count, MAX_STAT_DOTS))
    return FULL_DOT * full_count + EMPTY_DOT * (MAX_STAT_DOTS - full_count)


def format_status(player):
    xp_bar = format_progress_bar(player["xp"], player["xp_to_next_level"])
    return "\n".join(
        [
            f"LVL   {player['level']:<7} XP {xp_bar} {player['xp']}/{player['xp_to_next_level']}",
            f"HP    {str(player['hp']) + '/' + str(player['max_hp']):<7} {format_hp_dots(player)}",
            format_stat_dots("STR", player["strength"]),
            format_stat_dots("ARMOR", player["armor"]),
        ]
    )


def count_inventory(player):
    return {
        "small_potion": player["inventory"].count("small_potion"),
        "big_potion": player["inventory"].count("big_potion"),
    }


def format_inventory(player):
    counts = count_inventory(player)
    return "\n".join(
        [
            "Inventory",
            f"Small Potion: {counts['small_potion']}",
            f"Big Potion:   {counts['big_potion']}",
        ]
    )


def get_player_attack(player):
    weapon_bonus = 0

    if player["weapon"] is not None:
        weapon_bonus = weapons[player["weapon"]]["attack_bonus"]

    return player["strength"] + weapon_bonus


def calculate_incoming_damage(player, raw_damage):
    return max(1, raw_damage - player["armor"])


def create_enemy(level, name=None):
    strength = 3 + level * 2
    hp = 12 + level * 8
    return {
        "name": name or "Shadow Creature",
        "level": level,
        "hp": hp,
        "max_hp": hp,
        "strength": strength,
        "attack": strength,
        "xp_reward": 8 + level * 6,
    }


def create_boss():
    return {
        "name": "Maze Guardian",
        "level": 5,
        "hp": 95,
        "max_hp": 95,
        "strength": 12,
        "attack": 12,
        "xp_reward": 75,
        "is_boss": True,
    }


def format_enemy_status(enemy):
    return "\n".join(
        [
            enemy["name"],
            f"LVL   {enemy['level']}",
            f"HP    {enemy['hp']}/{enemy['max_hp']}",
            f"STR   {enemy['strength']}",
        ]
    )


def format_encounter_prompt(enemy):
    return "\n".join(
        [
            f"A {enemy['name']} blocks your way.",
            f"Enemy level: {enemy['level']} | HP: {enemy['hp']}/{enemy['max_hp']} | STR: {enemy['strength']}",
        ]
    )


def format_combat_view(player, enemy):
    left_lines = format_enemy_status(enemy).splitlines()
    right_lines = format_status(player).splitlines() + ["", *format_inventory(player).splitlines()]
    height = max(len(left_lines), len(right_lines))
    left_lines += [""] * (height - len(left_lines))
    right_lines += [""] * (height - len(right_lines))

    lines = ["MONSTER".ljust(34) + "PLAYER"]
    lines.append("-" * 26 + "        " + "-" * 34)

    for left, right in zip(left_lines, right_lines):
        lines.append(left.ljust(34) + right)

    return "\n".join(lines)


def level_up(player):
    player["level"] += 1
    player["max_hp"] += LEVEL_HP_BONUS
    player["hp"] = player["max_hp"]
    player["strength"] += LEVEL_STRENGTH_BONUS

    if player["level"] % 3 == 0:
        player["armor"] += 1

    player["xp_to_next_level"] = math.ceil(player["xp_to_next_level"] * 1.35)
    add_message(player, f"Level up! You are now LVL {player['level']}.")


def gain_xp(player, amount, announce=True):
    player["xp"] += amount

    if announce:
        add_message(player, f"You gained {amount} XP.")

    while player["xp"] >= player["xp_to_next_level"]:
        player["xp"] -= player["xp_to_next_level"]
        level_up(player)


def add_key(player, color):
    player["keys"].append(color)
    add_message(player, f"You found a {color} key.")


def has_key(player, color):
    return color in player["keys"]


def open_door(player, color):
    if has_key(player, color):
        add_message(player, f"You opened the {color} door.")
        return True

    add_message(player, f"The {color} door is locked. You need a {color} key.")
    return False


def collect_item(player, item):
    item_type = item["type"]

    if item_type == "potion":
        potion_name = item["name"]
        player["inventory"].append(potion_name)
        add_message(player, f"You found a {potions[potion_name]['name']}.")

    elif item_type == "weapon":
        weapon_name = item["name"]
        player["weapon"] = weapon_name
        add_message(player, f"You equipped {weapons[weapon_name]['name']}.")

    elif item_type == "key":
        add_key(player, item["color"])

    elif item_type == "torch":
        player["has_torch"] = True
        player["vision"] = max(player["vision"], TORCH_VISION)
        add_message(player, "You take the torch. The maze finally has edges.")


def use_potion(player, potion_name):
    if potion_name not in player["inventory"]:
        add_message(player, "You don't have this potion.")
        return False

    heal_amount = potions[potion_name]["heal"]
    player["hp"] = min(player["max_hp"], player["hp"] + heal_amount)
    player["inventory"].remove(potion_name)

    add_message(player, f"You used {potions[potion_name]['name']}.")
    add_message(player, f"HP: {player['hp']}/{player['max_hp']}")
    return True


def choose_fight_or_flee(enemy, input_func=input):
    print(format_encounter_prompt(enemy))

    while True:
        choice = input_func("\nFight or flee? ").strip().lower()

        if choice in {"fight", "f"}:
            return "fight"

        if choice in {"flee", "run", "r"}:
            return "flee"

        print("Please choose 'fight' or 'flee'.")


def default_combat_action(player, enemy):
    return "attack"


def fight(player, enemy, combat_action_provider=None):
    action_provider = combat_action_provider or default_combat_action

    while player["hp"] > 0 and enemy["hp"] > 0:
        action = action_provider(player, enemy)

        if action in potions:
            if not use_potion(player, action):
                continue
        else:
            player_damage = get_player_attack(player)
            enemy["hp"] -= player_damage
            add_message(player, f"You hit the enemy for {player_damage} damage.")

        if enemy["hp"] <= 0:
            xp_reward = enemy["xp_reward"]
            add_message(player, f"You won the fight! You gained {xp_reward} XP.")
            gain_xp(player, xp_reward, announce=False)

            if enemy.get("is_boss"):
                player["boss_defeated"] = True

            return True

        damage = calculate_incoming_damage(player, enemy["attack"])
        player["hp"] -= damage
        add_message(player, f"The enemy hits you for {damage} damage.")
        add_message(player, f"Your HP: {player['hp']}/{player['max_hp']}")

    player["alive"] = False
    add_message(player, "You died.")
    return False


def handle_tile(player, tile, input_func=input, combat_action_provider=None):
    tile_type = tile["type"]

    if tile_type == "empty":
        return "empty"

    if tile_type == "torch":
        collect_item(player, tile)
        return "collected"

    if tile_type == "enemy":
        enemy = create_enemy(tile["enemy_level"])
        choice = choose_fight_or_flee(enemy, input_func)

        if choice == "flee":
            add_message(player, "You step back and keep breathing.")
            return "fled"

        return "enemy_defeated" if fight(player, enemy, combat_action_provider) else "dead"

    if tile_type == "boss":
        boss = create_boss()
        choice = choose_fight_or_flee(boss, input_func)

        if choice == "flee":
            add_message(player, "The guardian waits. It knows you will have to return.")
            return "fled"

        return "win" if fight(player, boss, combat_action_provider) else "dead"

    if tile_type in {"potion", "weapon", "key"}:
        collect_item(player, tile)
        return "collected"

    if tile_type == "door":
        return "opened" if open_door(player, tile["color"]) else "locked"

    if tile_type == "exit":
        add_message(player, "You found the exit.")
        add_message(player, "You escaped the maze.")
        return "win"

    add_message(player, "Unknown tile type.")
    return "unknown"
