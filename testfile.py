import time
import os

class Player:
    def __init__(self, name, health, inventory):
        self.name = name
        self.health = health
        self.inventory = inventory

    def attack(self, weapon):
        if weapon in self.inventory["swords"]:
            damage = 50 + self.inventory["swords"][weapon]
        else:
            damage = 5  # Base damage for unarmed attack
        return damage

    def heal(self, potion):
        if potion in self.inventory["potions"]:
            if potion == "normal":
                heal_amount = 20
            elif potion == "epic":
                heal_amount = 50
            self.inventory["potions"][potion] -= 1
            return heal_amount
        return 0

    def block(self):
        return False  # Simplified block mechanic


class Teacher:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        return 15


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def combat_loop(player, teacher):
    while player.health > 0 and teacher.health > 0:
        clear_screen()
        
        # Display UI
        print(f"{player.name}'s Turn\n")
        print(f"\nditt Inventory: {player.inventory} ")
        print(f"HP: {player.health}")
        print(f"Lärarens HP: {teacher.health}\n")

        action = input("Välj attack (attack, heal, stand): ").strip().lower()
   
        # Player's turn
        if action == "attack":
            weapon = input("Välj svärd (eller tryck ENTER för att använda händerna): ").strip().lower()
            print("-------------------------------------")
            if weapon in player.inventory["swords"] or weapon == "":
                damage = player.attack(weapon)
                teacher.health = max(0, teacher.health - damage)
                print("-------------------------------------")
                print(f"Du attackerade {teacher.name} med {'Dina händer' if weapon == '' else weapon}, som gjorde {damage} skada!")
            else:
                print("\nOgiltigt vapen!")
            
        elif action == "heal":
            potion = input("Välj potion (normal/epic): ").strip().lower()
            if potion in player.inventory["potions"] and player.inventory["potions"][potion] > 0:
                heal_amount = player.heal(potion)
                player.health = min(100, player.health + heal_amount)
                print(f"\nDu använde {potion}-potion och helade dig själv med {heal_amount} HP!")
                print(f"HP: {player.health}")
            else:
                print("\nOgiltig eller slut potion!")

        elif action == "stand":
            print("\nDu stog ditt kast. Nästa tur!")

        else:
            print("\nOgiltig handling!")

        # Check teacher's health
        if teacher.health == 0:
            print(f"\n{teacher.name} är besegrad! Du vann!")
            break

        input("-----------tryck ENTER för att fortsätta-----------")  # Pause to show action results
        
        # Teacher's turn
        print(f"{teacher.name}s tur!")
        
        time.sleep(2)
        damage = teacher.attack()
        if player.block():
            print("Din sköld blockerade attacken!")
        else:
            player.health = max(0, player.health - damage)
            print(f"{teacher.name} attackerade och gjorde {damage} skada!")
        print(f"\n{teacher.name}s HP: {teacher.health}")
        print(f"{player.name}s HP efter attack: {player.health}")

        # Check player's health
        if player.health == 0:
            print("\nDu förlorade kampen! Bättre lycka nästa gång.")
            break

        input("-----------tryck ENTER för att fortsätta-----------")

# Setup
player_inventory = {
    "swords": {"wooden sword": 5, "iron sword": 10},
    "potions": {"normal": 2, "epic": 1}
}
player = Player("Hjälte", 100, player_inventory)
teacher = Teacher("Läraren", 100)

# Start combat
combat_loop(player, teacher)
