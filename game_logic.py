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
    
    def use_potion(self):
        if potions[0] not in self.inventory:
            print("You don't have a potion.")
            return
        self.actual_hp += potions[0].heal
        self.inventory.remove(potions[0])
        if self.actual_hp > self.hp:
            self.actual_hp = self.hp
        print(f"You used {potions[0].name} and restored {potions[0].heal} HP.\nHP: {self.actual_hp}/{self.hp}")


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
    
    def fight(self, enemy):
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
        enemy.actual_hp = enemy.hp
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
potions = [Item("Small Potion", "potion", heal = 10)]

enemies = [Character("Boss", hp = 30, attack = 7, defense = 5, exp_on_kill = 30), Character("Goblin", hp = 10, attack = 7, defense = 3, exp_on_kill = 10)]

