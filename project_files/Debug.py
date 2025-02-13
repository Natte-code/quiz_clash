import random
import time
import os
import threading
from typing import Union

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Sword:
    def __init__(self, name: str, damage: int):
        self.name = name.lower()  # Store weapon names in lowercase
        self.damage = damage

    def __repr__(self):
        return f"Sword(name='{self.name}', damage={self.damage})"

#-------------(Swords)-----------------
Pie = Sword("Pie", 3.14)
järnsvärd = Sword("järnsvärd", 20)
katana = Sword("katana", 15)
Dagger = Sword("Dagger", 17)
Pinne = Sword("Pinne", 10)
Kukri = Sword("Kukri", 25)
battle_axe = Sword("battle_axe", 35)
lightsaber = Sword("lightsaber", 50)
stekpanna = Sword("stekpanna", 69)
skibidi = Sword("Skibidi", 150)

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.coins = 5
        self.totems = 1
        self.shields = 1
        self.antal_potion_vanlig = 5
        self.antal_potion_epic = 3
        self.inventory = {
            "swords": {sword.name: sword.damage for sword in [skibidi, Pie, järnsvärd, katana, stekpanna]},
            "potions": {
                "normal": self.antal_potion_vanlig,
                "epic": self.antal_potion_epic
            }
        }
        self.last_heal = 0

    def is_critical_hit(self):
        return random.random() < 0.15

    def attack(self, weapon_name: str):
        """Handles weapon selection with case-insensitive checks."""
        weapon_name = weapon_name.lower().strip()
        
        if weapon_name not in self.inventory["swords"]:
            available = list(self.inventory["swords"].keys())
            raise ValueError(
                f"Invalid weapon: '{weapon_name}'. "
                f"Available swords: {', '.join(available)}"
            )
        
        base_damage = self.inventory["swords"][weapon_name]
        if self.is_critical_hit():
            crit_damage = int(base_damage * 2.5)
            print(f"\nCRITICAL HIT! {crit_damage} damage!")
            return crit_damage
        return base_damage

    def heal(self, potion_type):
        current_time = time.time()
        if current_time - self.last_heal < 5:
            print("Wait 5 seconds between potions!")
            return 0
            
        if potion_type == "normal" and self.antal_potion_vanlig > 0:
            self.antal_potion_vanlig -= 1
            self.last_heal = current_time
            return 50
        elif potion_type == "epic" and self.antal_potion_epic > 0:
            self.antal_potion_epic -= 1
            self.last_heal = current_time
            return 100
        print("No potions left!")
        return 0

    def block(self):
        return random.random() < 0.3

    def use_totem(self):
        if self.totems > 0:
            self.totems -= 1
            self.health = 100
            print("\n=== TOTEM USED! HP RESTORED TO 100 ===")
            return True
        return False

    def add_coins(self, amount):
        self.coins += amount
        print(f"Earned {amount} coins! Total: {self.coins}")

class Boss:
    def __init__(self, name, health, min_damage, max_damage, regen):
        self.name = name
        self.health = health
        self.max_health = health
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.regen = regen
        self.is_regen = False

    def start_regen(self):
        if not self.is_regen:
            self.is_regen = True
            threading.Thread(target=self.regenerate_health, daemon=True).start()

    def regenerate_health(self):
        while self.is_regen and self.health > 0:
            time.sleep(10)
            self.health = min(self.max_health, self.health + self.regen)
            print(f"\nBOSS REGENERATES +{self.regen} HP!")

    def stop_regen(self):
        self.is_regen = False

    def attack(self):
        return random.randint(self.min_damage, self.max_damage)

class Teacher:
    def __init__(self, name, health, min_damage, max_damage):
        self.name = name
        self.health = health
        self.min_damage = min_damage
        self.max_damage = max_damage

    def attack(self):
        return random.randint(self.min_damage, self.max_damage)

# Enemy instances
teacher1 = Teacher(name="johanna", health=100, min_damage=1, max_damage=10) #klassrumm 1
teacher2 = Teacher(name="Ronja", health=110, min_damage=5, max_damage=15)
teacher3 = Teacher(name="Henrik", health=125, min_damage=8, max_damage=18)
teacher4 = Teacher(name="Victor", health=135, min_damage=1, max_damage=13)
teacher5 = Teacher(name="David", health=150, min_damage=9, max_damage=20)
teacher6 = Teacher(name="Mirrela", health=200, min_damage=11, max_damage=25)

final_boss = Boss("Lars", 500, 20, 50, 20)

def combat_loop(player: Character, enemy: Union[Teacher, Boss]) -> bool:
    """
    Starts a combat loop between the player and an enemy.

    Usage:
    combat_loop(player, teacher1)  # Start fight against a teacher
    combat_loop(player, final_boss)  # Start boss fight

    Returns:
    True if the player wins, False if they lose.
    """
    if isinstance(enemy, Boss):
        enemy.start_regen()

    while player.health > 0 and enemy.health > 0:
        clear_screen()
        print(f"=== {enemy.name} === HP: {enemy.health}\n")
        print(f"{player.name}: HP: {player.health} | Coins: {player.coins}")
        print(f"Potions: Normal({player.antal_potion_vanlig}) Epic({player.antal_potion_epic})")
        print(f"Totems: {player.totems}")
        
        # Show available swords
        available_weapons = list(player.inventory["swords"].keys())
        print(f"\nAvailable swords: {', '.join(available_weapons)}")
        
        print("\nChoose action:")
        print("1. Attack\n2. Heal\n3. Wait")

        choice = input("\nYour choice: ").lower()

        if choice in ("1", "attack"):
            clear_screen()
            print(f"=== {enemy.name} === HP: {enemy.health}")
            print(f"Your swords: {', '.join(available_weapons)}")
            weapon = input("\nChoose weapon: ").lower().strip()
            
            try:
                damage = player.attack(weapon)
                enemy.health -= damage
                print(f"\nYou attack with {weapon} and deal {damage} damage!")
            except ValueError as e:
                print(f"\n{e}")
                input("Press ENTER to continue...")
                continue

        elif choice in ("2", "heal"):
            clear_screen()
            print(f"=== {enemy.name} === HP: {enemy.health}")
            heal_type = input("Choose potion type (normal/epic): ").lower()
            heal_amount = player.heal(heal_type)
            if heal_amount > 0:
                player.health = min(100, player.health + heal_amount)
                print(f"\n✓ Healed {heal_amount} HP!")

        elif choice in ("3", "wait"):
            print("\nYou wait and gather your strength...")

        else:
            print("\nInvalid choice! You lose your turn...")

        time.sleep(1.5)
        
        if enemy.health <= 0:
            reward = random.randint(10, 20)
            player.add_coins(reward)
            print(f"\n★ {enemy.name} defeated! ★")
            input("Press ENTER to continue...")
            return True

        # Enemy's attack
        enemy_damage = enemy.attack()
        if player.block():
            print("\n⚔️ You blocked the attack! ⚔️")
        else:
            player.health -= enemy_damage
            print(f"\n⚔️ {enemy.name} attacks and deals {enemy_damage} damage! ⚔️")

        if player.health <= 0:
            if player.use_totem():
                continue
            print("\n☠️ GAME OVER! ☠️")
            input("Press ENTER to exit...")
            return False

        time.sleep(2)



player_name = input("What is your hero's name? ")
player = Character(player_name, 100)

combat_loop(player, final_boss )


#Bugg 1, Lars kan regena efter han är död, Hur fan.
#Bugg 2, Input saken av spelaren kan brytas när lars får en regen. Texten överskriver spelarens input, Men spelaren kan fortfarande skriva in


# combat_loop(player, teacher1)
# Starta en strid när du vill
# combat_loop(player, teacher1)  # Strid mot Johanna
# combat_loop(player, boss)       # Strid mot bossen