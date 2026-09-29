import random


class Item:
    def __init__(self, name, item_type, attack=0, defense=0, heal=0):
        self.name = name
        self.type = item_type
        self.attack = attack
        self.defense = defense
        self.heal = heal

    def describe(self):
        if self.type == "weapon":
            return f"{self.name} (+{self.attack} attack)"
        if self.type == "armor":
            return f"{self.name} (+{self.defense} defense)"
        if self.type == "potion":
            return f"{self.name} (+{self.heal} HP)"
        return self.name


class Character:
    experience_to_next_level = [10, 20, 30, 50, 80, 130, 210, 340, 550, 890]

    def __init__(self, name, level=1, exp=0, hp=20, attack=5, defense=5, vision_range=1):
        self.name = name
        self.level = level
        self.exp = exp
        self.hp = hp
        self.actual_hp = hp
        self.base_attack = attack
        self.base_defense = defense
        self.attack_bonus = 0
        self.defense_bonus = 0
        self.attack = attack
        self.defense = defense
        self.vision_range = vision_range
        self.inventory = []

    def is_alive(self):
        return self.actual_hp > 0

    def take_damage(self, damage):
        self.actual_hp = max(0, self.actual_hp - damage)

    def heal(self, amount):
        healed = min(amount, self.hp - self.actual_hp)
        self.actual_hp += healed
        return healed

    def calc_damage(self, target):
        # a little randomness so fights don't always play out the same way
        return max(1, self.attack - target.defense + random.randint(-1, 1))

    def exp_needed(self):
        index = min(self.level - 1, len(self.experience_to_next_level) - 1)
        return self.experience_to_next_level[index]

    def gain_exp(self, amount):
        self.exp += amount
        messages = [f"You gained {amount} EXP."]
        while self.exp >= self.exp_needed():
            self.exp -= self.exp_needed()
            self.level_up()
            messages.append(f"Level up! You are now LVL {self.level}.")
        return messages

    def level_up(self):
        self.level += 1
        self.hp += 5
        self.actual_hp += 5
        self.base_attack += 1
        self.base_defense += 1
        self.update_stats()

    def pick_up_item(self, item):
        self.inventory.append(item)
        self.update_stats()

    def update_stats(self):
        self.attack_bonus, self.defense_bonus = self.calc_stats()
        self.attack = self.base_attack + self.attack_bonus
        self.defense = self.base_defense + self.defense_bonus

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

    def find_potion(self):
        for item in self.inventory:
            if item.type == "potion":
                return item
        return None

    def use_potion(self):
        potion = self.find_potion()
        if potion is None:
            return False, "You don't have a potion."
        if self.actual_hp == self.hp:
            return False, "Your HP is already full."
        self.inventory.remove(potion)
        healed = self.heal(potion.heal)
        return True, f"You used a {potion.name} and restored {healed} HP."


class Enemy(Character):
    def __init__(self, name, hp, attack, defense, exp_on_kill):
        super().__init__(name, hp=hp, attack=attack, defense=defense)
        self.exp_on_kill = exp_on_kill


class Fight:
    flee_chance = 0.5

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.round = 1
        self.is_over = False
        self.player_fled = False

    def player_won(self):
        return self.is_over and not self.enemy.is_alive()

    def player_attack(self):
        damage = self.player.calc_damage(self.enemy)
        self.enemy.take_damage(damage)
        log = [f"You hit the {self.enemy.name} for {damage} damage."]
        if not self.enemy.is_alive():
            return log + self.win()
        return log + self.enemy_turn()

    def player_defend(self):
        return ["You raise your guard."] + self.enemy_turn(defending=True)

    def player_use_potion(self):
        used, message = self.player.use_potion()
        if not used:
            # no potion or full HP -> the turn isn't wasted
            return [message]
        return [message] + self.enemy_turn()

    def player_flee(self):
        if random.random() < self.flee_chance:
            self.is_over = True
            self.player_fled = True
            return [f"You escaped from the {self.enemy.name}!"]
        return [f"You try to run, but the {self.enemy.name} blocks your way!"] + self.enemy_turn()

    def enemy_turn(self, defending=False):
        damage = self.enemy.calc_damage(self.player)
        if defending:
            damage //= 2
        self.player.take_damage(damage)
        self.round += 1
        log = [f"The {self.enemy.name} hits you for {damage} damage."]
        if not self.player.is_alive():
            self.is_over = True
            log.append(f"You were defeated by the {self.enemy.name}...")
        return log

    def win(self):
        self.is_over = True
        return [f"You defeated the {self.enemy.name}!"] + self.player.gain_exp(self.enemy.exp_on_kill)


weapons = [Item("Wooden Stick", "weapon", attack=2), Item("Old Rusty Sword", "weapon", attack=4), Item("Iron Sword", "weapon", attack=7)]
armors = [Item("Leather Armor", "armor", defense=2), Item("Chainmail", "armor", defense=4), Item("Plate Armor", "armor", defense=7)]
useful_items = [Item("Torch", "util")]
potions = [Item("Small Potion", "potion", heal=10)]

enemy_types = {
    "boss": {"name": "Boss", "hp": 30, "attack": 7, "defense": 5, "exp_on_kill": 30},
    "goblin": {"name": "Goblin", "hp": 10, "attack": 7, "defense": 3, "exp_on_kill": 10},
}


def create_enemy(enemy_type):
    return Enemy(**enemy_types[enemy_type])


def clean_player_name(name, default="Nyrik", max_length=15):
    name = " ".join(name.split())
    if not name:
        return default
    return name[:max_length]
