import random
import threading
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Karaktärsklassen
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.coins = 5
        self.totems = 1
        self.shields = 1
        self.inventory = {
            "swords": {"träsvärd": 10, "järnsvärd": 20},
            "potions": {"normal": 2, "epic": 1}
        }

    def is_critical_hit(self):
        return random.random() < 0.15

    def attack(self, weapon):
        base_damage = self.inventory["swords"].get(weapon, random.randint(5, 10))
        if self.is_critical_hit():
            crit_damage = int(base_damage * 2.5)
            print(f"\nKRITISK TRÄFF! Du gör {crit_damage} skada!\n")
            return crit_damage
        return base_damage

    def heal(self, potion_type):
        if potion_type in self.inventory["potions"] and self.inventory["potions"][potion_type] > 0:
            self.inventory["potions"][potion_type] -= 1
            return 50 if potion_type == "normal" else 100
        return 0

    def block(self):
        return random.random() < 0.3

    def totem(self):
        if self.totems > 0:
            self.totems -= 1
            self.health = 100
            print(f"\n------------\nDu använde en totem! {self.name} är återupplivad med 100 HP!\n------------")
            input("Tryck ENTER för att fortsätta...")
            return True
        return False

# Bossklassen
class Boss:
    def __init__(self, name, health, min_damage, max_damage, regen):
        self.name = name
        self.health = health
        self.max_health = health
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.regen = regen
        self.isregen = False

    def start_regen(self):
        if not self.isregen:
            self.isregen = True
            threading.Thread(target=self.regenerate_health, daemon=True).start()

    def regenerate_health(self):
        while self.isregen:
            time.sleep(15)
            if self.health < self.max_health:
                self.health = min(self.max_health, self.health + self.regen)
                print(f"\nLars Helade +{self.regen} HP: {self.health}\n (Tryck ENTER efter detta, eller fortsätt med HANDLINGEN)")

    def stop_regen(self):
        self.isregen = False

    def attack(self):
        return random.randint(self.min_damage, self.max_damage)

# Teacher-klassen
class Teacher:
    def __init__(self, name, health, min_damage, max_damage):
        self.name = name
        self.health = health
        self.min_damage = min_damage
        self.max_damage = max_damage

    def attack(self):
        return random.randint(self.min_damage, self.max_damage)

# Stridsloopen
def combat_loop(player, opponent):
    if isinstance(opponent, Boss):
        opponent.start_regen()

    while player.health > 0 and opponent.health > 0:
        clear_screen()

        # Visa status
        print(f"\n{player.name}'s tur\n------------")
        print(f"HP: {player.health} | Potions: {player.inventory['potions']} | Totems: {player.totems} | Shields: {player.shields}")
        print(f"{opponent.name}'s HP: {opponent.health}\n------------")

        # Spelarens val
        action = input("Välj handling (attack, heal, stand): ").strip().lower()
        if action == "attack":
            weapon = input("Välj vapen (träsvärd/järnsvärd eller lämna tomt för händer): ").strip().lower()
            if weapon in player.inventory["swords"] or not weapon:
                damage = player.attack(weapon)
                opponent.health = max(0, opponent.health - damage)
                print(f"\nDu attackerade {opponent.name} med {'händerna' if not weapon else weapon} och gjorde {damage} skada!\n")
            else:
                print("\nOgiltigt vapen!\n")
                continue

        elif action == "heal":
            potion = input("Välj potion (normal/epic): ").strip().lower()
            heal_amount = player.heal(potion)
            if heal_amount:
                player.health = min(100, player.health + heal_amount)
                print(f"\nDu använde en {potion}-potion och helade {heal_amount} HP!\n")
            else:
                print("\nOgiltig potion eller slut!\n")
                continue

        elif action == "stand":
            print("\nDu valde att vänta.\n")

        else:
            print("\nOgiltig handling! Försök igen.\n")
            continue

        # Kontrollera om motståndaren är besegrad
        if opponent.health <= 0:
            print(f"\n------------\n{opponent.name} är besegrad! Du vann striden!\n------------")
            input("Tryck ENTER för att avsluta striden...")
            if isinstance(opponent, Boss):
                opponent.stop_regen()
            return

        input("Tryck ENTER för att fortsätta till motståndarens tur...")

        # Motståndarens tur
        print(f"\n{opponent.name}s tur!\n------------")
        time.sleep(1)  # Skapar en paus för dramatik
        damage = opponent.attack()
        if player.block():
            print(f"\nDin sköld blockerade {opponent.name}s attack!\n")
        else:
            player.health = max(0, player.health - damage)
            print(f"\n{opponent.name} attackerade och gjorde {damage} skada!\n")

        # Visa motståndarens handling och resultat innan skärmen rensas
        input("Tryck ENTER för att fortsätta...")

        # Kontrollera om spelaren är död och om totem används
        if player.health <= 0:
            if player.totem():
                continue
            print("\nDu förlorade kampen!\n")
            break

# Skapa en spelare och boss för test
player = Character(name="Spelare", health=100)
boss = Boss(name="Lars", health=450, min_damage=20, max_damage=50, regen=10)

# Testa stridsloopen
combat_loop(player, boss)
