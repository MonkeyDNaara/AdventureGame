import math


FULL_DOT = "●"
EMPTY_DOT = "○"
DOT_COUNT = 10


class Character():
    def __init__(self, name, level = 1, exp = 0, hp = 20, attack = 5, defense = 5, vision_range = 2, exp_on_kill = 10):
        self.name = name
        self.level = level
        self.exp = exp
        self.exp_on_kill = exp_on_kill
        self.hp = hp
        self.actual_hp = hp
        self.attack = attack
        self.base_attack = attack
        self.defense = defense
        self.base_defense = defense
        self.vision_range = vision_range
        self.be_infight = False
        self.inventory = []
        self.experience_to_next_level = [10, 20, 30, 50, 80, 130, 210, 340, 550, 890]

    def level_up(self):
        self.level += 1
        self.hp += 5
        self.actual_hp += 5
        self.base_attack += 1
        self.base_defense += 1
        self.attack = self.base_attack + self.attack_bonus
        self.defense = self.base_defense + self.defense_bonus
        print(f"Level up! You are now LVL {self.level}.")
    
    def pick_up_item(self, item):
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.inventory.append(item)
        self.attack_bonus, self.defense_bonus = self.calc_stats()
        self.attack += self.attack_bonus
        self.defense += self.defense_bonus

    def calc_stats(self):
        attack_bonus_items = []
        defense_bonus_items = []
        for item in self.inventory:
            if item.type == "weapon":
                attack_bonus_items.append(item.attack)
            elif item.type == "armor":
                defense_bonus_items.append(item.defense)
        attack_bonus = max(attack_bonus_items) if attack_bonus_items else 0
        defense_bonus = max(defense_bonus_items) if defense_bonus_items else 0
        return attack_bonus, defense_bonus
    
    def fight(self, enemy, key):
        while self.actual_hp > 0 and enemy.actual_hp > 0:
            self.be_infight = True
            damage_to_enemy = max(0, self.attack - enemy.defense)
            print(f"You dealt {damage_to_enemy} damage to the {enemy.name}. Enemy HP: {enemy.actual_hp}/{enemy.hp}")
            enemy.actual_hp -= damage_to_enemy
            if enemy.actual_hp <= 0:
                print(f"You defeated the {enemy.name}!")
                self.exp += enemy.exp_on_kill
                print(f"You gained {enemy.exp_on_kill} EXP. Total EXP: {self.exp}")
                break
            damage_to_self = max(0, enemy.attack - self.defense)
            print(f"{enemy.name} dealt {damage_to_self} damage to you. Your HP: {self.actual_hp}/{self.hp}")
            self.actual_hp -= damage_to_self
        self.be_infight = False
        while self.exp >= self.experience_to_next_level[self.level - 1]:
            self.exp -= self.experience_to_next_level[self.level - 1]
            self.level_up()
        return 


class Item():
    def __init__(self, name, item_type, attack = 0, defense = 0, heal = 0):
        self.name = name
        self.type = item_type
        self.attack = attack
        self.defense = defense
        self.heal = heal

weapons = [Item("Wooden Stick", "weapon", attack = 2), Item("Old Rusty Sword", "weapon", attack = 4), Item("Iron Sword", "weapon", attack = 7)]
armors = [Item("Leather Armor", "armor", defense = 2), Item("Chainmail", "armor", defense = 4), Item("Plate Armor", "armor", defense = 7)]
useful_items = [Item("Torch", "util")]
potions = [Item("Small Potion", "potion", heal = 10), Item("Big Potion", "potion", heal = 20)]

enemies = [Character("Boss", hp = 30, attack = 7, defense = 5, exp_on_kill = 30), Character("Goblin", hp = 10, attack = 3, defense = 2, exp_on_kill = 10)]

# Fixed enemy values. Fights are disabled for now, but the map can already read enemy tiles.
# enemies = {
#     1: {"name": "Enemy Level 1", "level": 1, "hp": 20, "attack": 5, "xp_reward": 10},
#     2: {"name": "Enemy Level 2", "level": 2, "hp": 30, "attack": 7, "xp_reward": 15},
#     3: {"name": "Enemy Level 3", "level": 3, "hp": 40, "attack": 9, "xp_reward": 20},
#     4: {"name": "Enemy Level 4", "level": 4, "hp": 50, "attack": 11, "xp_reward": 25},
#     10: {"name": "The Maze Guardian", "level": 10, "hp": 80, "attack": 15, "xp_reward": 50},
# }


# def create_player():
#     return {
#         "name": "Nyrik",
#         "level": 1,
#         "xp": 0,
#         "xp_to_next_level": 10,
#         "max_hp": 30,
#         "hp": 30,
#         "base_attack": 5,
#         "weapon": None,
#         "inventory": [],
#         "keys": [],
#         "has_torch": False,
#         "vision": 0,
#         "messages": [],
#     }


# def add_message(player, text):
#     player["messages"].append(text)


# def consume_messages(player):
#     messages = player["messages"]
#     player["messages"] = []
#     return messages


# def make_dots(current, maximum):
#     if maximum <= 0:
#         filled = 0
#     else:
#         filled = round((current / maximum) * DOT_COUNT)

#     filled = max(0, min(filled, DOT_COUNT))
#     empty = DOT_COUNT - filled
#     return FULL_DOT * filled + EMPTY_DOT * empty


# def format_status(player):
#     return "\n".join(
#         [
#             f"LVL {player['level']}",
#             f"XP  {player['xp']}/{player['xp_to_next_level']} {make_dots(player['xp'], player['xp_to_next_level'])}",
#             f"HP  {player['hp']}/{player['max_hp']} {make_dots(player['hp'], player['max_hp'])}",
#         ]
#     )


# def create_enemy(level):
#     enemy = enemies[level].copy()
#     enemy["max_hp"] = enemy["hp"]
#     return enemy


# def level_up(player):
#     player["level"] += 1
#     player["max_hp"] += 5
#     player["hp"] += 5
#     player["base_attack"] += 1
#     player["xp_to_next_level"] = math.ceil(player["xp_to_next_level"] * 1.3)
#     add_message(player, f"Level up! You are now LVL {player['level']}.")


# def gain_xp(player, amount):
#     player["xp"] += amount
#     add_message(player, f"You gained {amount} XP.")

#     while player["xp"] >= player["xp_to_next_level"]:
#         player["xp"] -= player["xp_to_next_level"]
#         level_up(player)


# def add_key(player, key):
#     player["keys"].append(key)
#     add_message(player, f"You found key {key}.")


# def has_key(player, key):
#     return key in player["keys"]


# def get_attack(player):
#     attack = player["base_attack"]

#     if player["weapon"] is not None:
#         attack += weapons[player["weapon"]]["attack_bonus"]

#     return attack


# def item_name(item):
#     if item["type"] == "torch":
#         return "Torch"

#     if item["type"] == "potion":
#         return potions[item["name"]]["name"]

#     if item["type"] == "weapon":
#         return weapons[item["name"]]["name"]

#     if item["type"] == "key":
#         return f"Key {item['key']}"

#     if item["type"] == "chest":
#         return "Chest"

#     return "Item"


# def item_info(item):
#     if item["type"] == "weapon":
#         weapon = weapons[item["name"]]
#         return f"{weapon['name']} (Attack +{weapon['attack_bonus']})"

#     return item_name(item)


# def collect_item(player, item):
#     item_type = item["type"]

#     if item_type == "potion":
#         potion_name = item["name"]
#         player["inventory"].append(potion_name)
#         add_message(player, f"You found a {potions[potion_name]['name']}.")
#         return True

#     if item_type == "weapon":
#         weapon_name = item["name"]
#         player["weapon"] = weapon_name
#         add_message(player, f"You equipped {weapons[weapon_name]['name']}.")
#         return True

#     if item_type == "key":
#         add_key(player, item["key"])
#         return True

#     if item_type == "torch":
#         player["has_torch"] = True
#         player["vision"] = 1
#         add_message(player, "You picked up the torch.")
#         add_message(player, "You can now see around you. What a relief.")
#         return True

#     return False


# def use_potion(player, potion_name):
#     if potion_name not in player["inventory"]:
#         add_message(player, "You don't have this potion.")
#         return False

#     heal_amount = potions[potion_name]["heal"]
#     player["hp"] += heal_amount

#     if player["hp"] > player["max_hp"]:
#         player["hp"] = player["max_hp"]

#     player["inventory"].remove(potion_name)
#     add_message(player, f"You used {potions[potion_name]['name']}.")
#     add_message(player, f"HP: {player['hp']}/{player['max_hp']}")
#     return True


# def format_inventory(player):
#     small_count = player["inventory"].count("small_potion")
#     big_count = player["inventory"].count("big_potion")
#     keys = ", ".join(player["keys"]) if player["keys"] else "none"

#     if player["weapon"] is None:
#         weapon = "None"
#     else:
#         weapon = weapons[player["weapon"]]["name"]

#     return "\n".join(
#         [
#             "Inventory",
#             f"Small Potion: {small_count}",
#             f"Big Potion:   {big_count}",
#             f"Keys:         {keys}",
#             f"Weapon:       {weapon}",
#         ]
#     )
