import random
import time
import os

player_name = input("Innan spelet börjar helt... Ange ditt namn: ")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Loot-pool
loot_pool = {
    "normal": [
        #Namn, class, chans i % att få.
        ("Pie", "swords", 20),           # 20% chans
        ("järnsvärd", "swords", 20),     # 20% chans
        ("katana", "swords", 15),        # 15% chans
        ("Dagger", "swords", 10),        # 10% chans
        ("Pinne", "swords", 5),          # 5% chans
        ("low_potion", "potions", 20),   # 20% chans
        ("medium_potion", "potions", 10) # 10% chans
    ],
    "epic": [
        ("Kukri", "swords", 25),         # 25% chans
        ("battle_axe", "swords", 20),    # 20% chans
        ("kukri", "swords", 15),         # 15% chans
        ("stekpanna", "swords", 5),      # 5% chans
        ("epic_potion", "potions", 10),  # 10% chans
        ("legendary_potion", "potions", 5), # 5% chans
        ("totem", "special", 10)         # 10% chans
    ]
}

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.coins = 5
        self.totems = 4
        self.shields = 1
        # Förenklat inventory
        self.inventory = {
            "swords": {"träsvärd": 10, "järnsvärd": 20},
            "potions": {"normal": 5, "epic": 3}          
        }

    def attack(self, weapon):
        """Beräknar skada baserat på vapen och kritisk chans."""
        base_damage = self.inventory["swords"].get(weapon, random.randint(5, 10))
        if self.is_critical_hit():
            crit_damage = int(base_damage * 2.5)
            print(f"KRITISK TRÄFF! Du gör {crit_damage} skada!\n------------")
            return crit_damage
        return base_damage

    def heal(self, potion_type):
        if potion_type == "normal" and self.inventory["potions"].get("normal", 0) > 0:
            self.inventory["potions"]["normal"] -= 1
            return 50
        elif potion_type == "epic" and self.inventory["potions"].get("epic", 0) > 0:
            self.inventory["potions"]["epic"] -= 1
            return 100
        return 0

    def block(self):
        return random.random() < 0.3

    def totem(self):
        if self.totems > 0:
            self.totems -= 1
            self.health = 100
            print(f"------------\nDu använde en totem! {self.name} är återupplivad med 100 HP!\n------------")
            input("Tryck ENTER för att fortsätta...")
            return True
        return False

    def is_critical_hit(self):
        return random.random() < 0.15

    def open_chest(self, chest_type):
        """Öppna en kista och få ett slumpmässigt föremål."""
        cost = 5 if chest_type == "normal" else 15

        if self.coins < cost:
            print(f"Du har inte tillräckligt med coins för att öppna en {chest_type} chest.")
            return

        self.coins -= cost
        print(f"Du öppnade en {chest_type} chest! ({cost} coins)")

        loot = self._get_random_loot(loot_pool[chest_type])
        item, category = loot[:2]
        self.inventory[category][item] = self.inventory[category].get(item, 0) + 1
        print(f"Du fick en {item}!")

    def _get_random_loot(self, pool):
        """Slumpar en item från loot-poolen baserat på vikt."""
        total_weight = sum(item[2] for item in pool)
        rand = random.uniform(0, total_weight)
        cumulative = 0
        for item in pool:
            cumulative += item[2]
            if rand < cumulative:
                return item

class Teacher:
    def __init__(self, name, health, min_damage, max_damage):
        self.name = name
        self.health = health
        self.min_damage = min_damage
        self.max_damage = max_damage

    def attack(self):
        return random.randint(self.min_damage, self.max_damage)

def combat_loop(player, teacher):
    while player.health > 0 and teacher.health > 0:
        clear_screen()
        print(f"{player.name}'s tur\n------------")
        print(f"Inventarie:\n")
        print(f"- Svärd: {list(player.inventory['swords'].keys())}")
        print(f"- Potions: {player.inventory['potions']}")
        print(f"- Totems: {player.totems}")
        print(f"- Sköldar: {player.shields}")
        print(f"HP: {player.health}\n------------")
        print(f"{teacher.name}s HP: {teacher.health}\n------------")

        action = input("Välj handling (attack, heal, chest, stand): ").strip().lower()
        print("------------")

        if action == "attack":
            weapon = input("Välj svärd: ").strip().lower()
            if weapon in player.inventory["swords"]:
                damage = player.attack(weapon)
                teacher.health = max(0, teacher.health - damage)
                print(f"Du attackerade {teacher.name} med {weapon} och gjorde {damage} skada!")
            else:
                print("Ogiltigt vapen!")

        elif action == "heal":
            potion = input("Välj potion (normal/epic): ").strip().lower()
            heal_amount = player.heal(potion)
            if heal_amount > 0:
                player.health = min(100, player.health + heal_amount)
                print(f"Du använde en {potion}-potion och helade {heal_amount} HP!")
            else:
                print("Ogiltig potion eller slut!")

        elif action == "chest":
            chest_type = input("Vilken chest vill du öppna? (normal/epic): ").strip().lower()
            if chest_type in ["normal", "epic"]:
                player.open_chest(chest_type)
            else:
                print("Ogiltig kisttyp!")

        elif action == "stand":
            print("Du valde att vänta.")

        else:
            print("Ogiltig handling!")

        if teacher.health <= 0:
            print(f"{teacher.name} är besegrad! Du vann!\n------------")
            break

        input("Tryck ENTER för att fortsätta...")
        print(f"{teacher.name}s tur!\n------------")
        time.sleep(2)
        damage = teacher.attack()
        if player.block():
            print("Din sköld blockerade attacken!")
        else:
            player.health = max(0, player.health - damage)
            print(f"{teacher.name} attackerade och gjorde {damage} skada!")
            if player.health == 0 and player.totem():
                continue

        if player.health <= 0:
            print("Du förlorade kampen! Bättre lycka nästa gång.")
            break

player = Character(name=player_name, health=100)
teacher1 = Teacher(name="Johanna", health=100, min_damage=5, max_damage=15)
#combat_loop(player, teacher1)
