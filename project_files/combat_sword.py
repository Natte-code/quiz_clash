import random
import time
import threading
import os

# Utility function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Sword:
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage

    def __repr__(self):
        return f"Sword(name='{self.name}', damage={self.damage})"

    def get_stats(self):
        return {"name": self.name, "damage": self.damage}

# Define the swords
#-------------(Normal)-----------------
Pie = Sword("Pie", 3)
jarnsvard = Sword("järnsvärd", 20)
katana = Sword("katana", 15)
dagger = Sword("Dagger", 17)
pinne = Sword("Pinne", 9)
#-------------(Epic)-----------------
kukri = Sword("Kukri", 25)
battle_axe = Sword("battle_axe", 35)
lightsaber = Sword("lightsaber", 50)
stekpanna = Sword("stekpanna", 69)
skibidi = Sword("Skibidi", 100)

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.coins = 5
        self.totems = 1
        self.shields = 1
        self.antal_potion_vanlig = 5  # Number of normal potions
        self.antal_potion_epic = 5    # Number of epic potions
        self.inventory = {
            "swords": {},  # Start with no swords
            "potions": {"normal": self.antal_potion_vanlig, "epic": self.antal_potion_epic}          
        }

    def add_sword_to_inventory(self, sword: Sword):
        self.inventory["swords"][sword.name] = sword.damage
        print(f"Added {sword.name} with damage {sword.damage} to inventory.")

    def is_critical_hit(self):
        return random.random() < 0.15  # 15% chance for a critical hit

    def attack(self, weapon_name):
        """Calculates damage based on weapon and critical chance."""
        if weapon_name == "":
            # Use hands if no weapon is specified
            base_damage = random.randint(5, 10)
        elif weapon_name in self.inventory["swords"]:
            base_damage = self.inventory["swords"][weapon_name]
        else:
            print("Invalid weapon! Using hands instead.")
            base_damage = random.randint(5, 10)

        if self.is_critical_hit():
            crit_damage = int(base_damage * 2.5)
            print(f"CRITICAL HIT! You deal {crit_damage} damage!\n------------")
            return crit_damage
        return base_damage

    def heal(self, potion_type):
        if potion_type == "normal" and self.antal_potion_vanlig > 0:
            self.antal_potion_vanlig -= 1
            heal_amount = 50
            print(f"You used a normal potion and healed {heal_amount} HP!")
            return heal_amount
        elif potion_type == "epic" and self.antal_potion_epic > 0:
            self.antal_potion_epic -= 1
            heal_amount = 100
            print(f"You used an epic potion and healed {heal_amount} HP!")
            return heal_amount
        else:
            print("Invalid potion or none left!")
            return 0

    def block(self):
        return random.random() < 0.3  # 30% chance to block an attack

    def totem(self):
        """Automatically uses a totem when HP reaches 0."""
        if self.totems > 0:
            self.totems -= 1
            self.health = 100
            print(f"------------\nYou used a totem! {self.name} is revived with 100 HP!\n------------")
            input("Press ENTER to continue...")
            return True
        return False

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
        while self.is_regen:
            time.sleep(10)
            if self.health < self.max_health:
                self.health = min(self.max_health, self.health + self.regen)
                print(f"+{self.regen} HP: {self.health}")

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

# Define Teachers
teacher1 = Teacher(name="Johanna", health=100, min_damage=1, max_damage=10)
teacher2 = Teacher(name="Ronja", health=110, min_damage=5, max_damage=15)
teacher3 = Teacher(name="Henrik", health=125, min_damage=8, max_damage=18)
teacher4 = Teacher(name="Victor", health=135, min_damage=1, max_damage=13)
teacher5 = Teacher(name="David", health=150, min_damage=9, max_damage=20)
teacher6 = Teacher(name="Mirella", health=200, min_damage=11, max_damage=25)

# Define Boss
boss = Boss(name="Lars", health=450, min_damage=10, max_damage=95, regen=15)

def combat_loop(player, opponent):
    while player.health > 0 and opponent.health > 0:
        clear_screen()

        # Display UI
        print(f"{player.name}'s Turn\n------------")
        print(f"Inventory:")
        print(f"- Swords: {list(player.inventory['swords'].keys())}")
        print(f"- Potions: Normal({player.antal_potion_vanlig}), Epic({player.antal_potion_epic})")
        print(f"- Totems: {player.totems}")
        print(f"- Shields: {player.shields}")
        print(f"HP: {player.health}\n------------")
        print(f"{opponent.name}'s HP: {opponent.health}\n------------")

        action = input("Choose action (attack, heal, stand): ").strip().lower()
        print("------------")

        # Player's turn
        if action == "attack":
            weapon = input("Choose sword (or press ENTER to use hands): ").strip()
            print("------------")
            damage = player.attack(weapon)
            opponent.health = max(0, opponent.health - damage)
            print(f"You attacked {opponent.name} with {'your hands' if weapon == '' else weapon} and dealt {damage} damage!")

        elif action == "heal":
            potion = input("Choose potion (normal/epic): ").strip().lower()
            print("------------")
            heal_amount = player.heal(potion)
            if heal_amount > 0:
                player.health = min(100, player.health + heal_amount)
                print(f"You now have {player.health} HP!")

        elif action == "stand":
            print("You chose to wait. Next turn!\n------------")

        else:
            print("Invalid action!\n------------")

        # Check if opponent is defeated
        if opponent.health <= 0:
            print(f"{opponent.name} is defeated! You won!\n------------")
            break

        input("Press ENTER to continue...")

        # Opponent's turn
        print(f"{opponent.name}'s Turn!\n------------")
        time.sleep(2)
        damage = opponent.attack()
        if player.block():
            print("Your shield blocked the attack!\n------------")
        else:
            player.health = max(0, player.health - damage)
            print(f"{opponent.name} attacked and dealt {damage} damage!\n------------")
            # Check if player should use totem
            if player.health == 0 and player.totem():
                continue  # Continue the game after using totem

        print(f"{opponent.name}'s HP: {opponent.health}\n------------")
        print(f"{player.name}'s HP: {player.health}\n------------")

        # Check if player is dead
        if player.health <= 0:
            print("You lost the battle! Better luck next time.\n------------")
            # You can add game over logic here
            break

        input("Press ENTER to continue...")

# Sample Game Start
if __name__ == "__main__":
    player_name = input("Enter your character's name: ")
    player = Character(name=player_name, health=100)

    # Add swords to player's inventory
    player.add_sword_to_inventory(Pie)
    player.add_sword_to_inventory(jarnsvard)
    player.add_sword_to_inventory(katana)
    player.add_sword_to_inventory(dagger)
    player.add_sword_to_inventory(pinne)
    # Add epic swords if desired
    # player.add_sword_to_inventory(kukri)
    # player.add_sword_to_inventory(battle_axe)
    # etc.

    # Start combat with a teacher for example
    combat_loop(player, teacher1)