import math


weapons = {
    "stick": {
        "name": "Wooden Stick",
        "attack_bonus": 2
    },
    "rusty_sword": {
        "name": "Old Rusty Sword",
        "attack_bonus": 4
    },
    "iron_sword": {
        "name": "Iron Sword",
        "attack_bonus": 7
    }
}


potions = {
    "small_potion": {
        "name": "Small Potion",
        "heal": 10
    },
    "big_potion": {
        "name": "Big Potion",
        "heal": 20
    }
}


def create_player():
    return {
        "name": "Nyrik",
        "level": 1,
        "xp": 0,
        "xp_to_next_level": 10,
        "max_hp": 30,
        "hp": 30,
        "base_attack": 5,
        "weapon": None,
        "inventory": [],
        "keys": [], 
        "has_torch": False, 
        "vision": 0
    }


def get_player_attack(player):
    attack = player["base_attack"]

    if player["weapon"] is not None:
        weapon_name = player["weapon"]
        attack += weapons[weapon_name]["attack_bonus"]

    return attack


def create_enemy(level):
    return {
        "name": f"Shadow Creature Level {level}",
        "level": level,
        "hp": 10 + level * 5,
        "attack": 3 + level * 2,
        "xp_reward": 5 + level * 5
    }


def level_up(player):
    player["level"] += 1
    player["max_hp"] += 10
    player["hp"] = player["max_hp"]
    player["base_attack"] += 2

    player["xp_to_next_level"] = math.ceil(
        player["xp_to_next_level"] * 1.25
    )

    print(f"Level up! You are now level {player['level']}.")
    print(f"HP: {player['hp']}/{player['max_hp']}")
    print(f"Attack: {player['base_attack']}")
    print(f"XP needed for next level: {player['xp_to_next_level']}")


def gain_xp(player, amount):
    player["xp"] += amount
    print(f"You gained {amount} XP.")

    while player["xp"] >= player["xp_to_next_level"]:
        player["xp"] -= player["xp_to_next_level"]
        level_up(player)


def add_key(player, color):
    player["keys"].append(color)
    print(f"You found a {color} key.")


def has_key(player, color):
    return color in player["keys"]


def open_door(player, color):
    if has_key(player, color):
        print(f"You opened the {color} door.")
        return True

    print(f"The {color} door is locked. You need a {color} key.")
    return False


def collect_item(player, item):
    item_type = item["type"]

    if item_type == "potion":
        potion_name = item["name"]
        player["inventory"].append(potion_name)
        print(f"You found a {potions[potion_name]['name']}.")

    elif item_type == "weapon":
        weapon_name = item["name"]
        player["weapon"] = weapon_name
        print(f"You equipped {weapons[weapon_name]['name']}.")

    elif item_type == "key":
        add_key(player, item["color"])

    elif item_type == "torch":
        player["has_torch"] = True
        player["vision"] = 1
        print("You picked up the torch.")
        print("You can now the around you. What a relief.")

def use_potion(player, potion_name):
    if potion_name not in player["inventory"]:
        print("You don't have this potion.")
        return

    heal_amount = potions[potion_name]["heal"]
    player["hp"] += heal_amount

    if player["hp"] > player["max_hp"]:
        player["hp"] = player["max_hp"]

    player["inventory"].remove(potion_name)

    print(f"You used {potions[potion_name]['name']}.")
    print(f"HP: {player['hp']}/{player['max_hp']}")


def fight(player, enemy):
    print(f"A {enemy['name']} appears!")

    while player["hp"] > 0 and enemy["hp"] > 0:
        player_damage = get_player_attack(player)
        enemy["hp"] -= player_damage

        print(f"You hit the enemy for {player_damage} damage.")

        if enemy["hp"] <= 0:
            print(f"You defeated {enemy['name']}!")
            gain_xp(player, enemy["xp_reward"])
            return True

        player["hp"] -= enemy["attack"]

        print(f"The enemy hits you for {enemy['attack']} damage.")
        print(f"Your HP: {player['hp']}/{player['max_hp']}")

    print("You died.")
    return False


def handle_tile(player, tile):
    if tile["type"] == "empty":
        print("There is nothing here.")

    elif tile["type"] == "enemy":
        enemy = create_enemy(tile["enemy_level"])
        return fight(player, enemy)

    elif tile["type"] == "boss":
        boss = {
            "name": "The Maze Guardian",
            "level": 5,
            "hp": 60,
            "attack": 12,
            "xp_reward": 50
        }
        return fight(player, boss)

    elif tile["type"] == "potion":
        collect_item(player, tile)

    elif tile["type"] == "weapon":
        collect_item(player, tile)

    elif tile["type"] == "key":
        collect_item(player, tile)

    elif tile["type"] == "door":
        return open_door(player, tile["color"])

    elif tile["type"] == "exit":
        print("You found the exit.")
        print("You escaped the maze.")
        return "win"
    
    elif tile["type"] == "torch":
        collect_item(player, tile)

    else:
        print("Unknown tile type.")