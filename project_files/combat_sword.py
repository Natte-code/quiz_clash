import time
import random


class Sword:
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage

    def __repr__(self):
        return f"Sword(name='{self.name}', damage={self.damage})"

    def get_stats(self):
        return {"name": self.name, "damage": self.damage}
    
#-------------(Normal)-----------------
Pie = Sword("Pie", 3.14)
järnsvärd = Sword("järnsvärd", 20)
katana = Sword("katana", 15)
Dagger = Sword("Dagger", 17)
Pinne = Sword("Pinne", 9.86960440052517106225)
#-------------(Epic)-----------------
Kukri = Sword("Kukri", 25)
battle_axe = Sword("battle_axe", 35)
lightsaber = Sword("lightsaber", 50)
stekpanna = Sword("stekpanna", 69)



class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.coins = 5
        self.totems = 1
        self.shields = 1
        # Inventory med Sword-objekt
        self.inventory = {
            "swords": {
                "träsvärd": Sword("Träsvärd", 10),
                "järnsvärd": Sword("Järnsvärd", 20),
                "stekpanna": Sword("stekpanna", 69),
                "Pie": Sword("Pie", 3.14),
                "lightsaber": Sword("lightsaber", 50)


            },
            "potions": {"normal": 2, "epic": 1}
        }

    def is_critical_hit(self):
        return random.random() < 0.15  # 15 % chans att göra kritisk träff

    def attack(self, weapon_name):
        """Beräknar skada baserat på vapen och kritisk chans."""
        weapon = self.inventory["swords"].get(weapon_name)
        if weapon:
            base_damage = weapon.damage
        else:
            # Standard skada med händerna
            base_damage = random.randint(5, 10)
        
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
        return random.random() < 0.3  # 30% chans att blockera en attack

    def totem(self):
        """Använd totem automatiskt när HP når 0."""
        if self.totems > 0:
            self.totems -= 1
            self.health = 100
            print(f"------------\nDu använde en totem! {self.name} är återupplivad med 100 HP!\n------------")
            input("Tryck ENTER för att fortsätta...")
            return True
        return False


class Teacher:
    def __init__(self, name, health, min_damage, max_damage):
        self.name = name
        self.health = health
        self.min_damage = min_damage
        self.max_damage = max_damage

    def attack(self):
        return random.randint(self.min_damage, self.max_damage)


# Definiera lärare
teacher1 = Teacher(name="Johanna", health=100, min_damage=1, max_damage=10)
teacher2 = Teacher(name="Ronja", health=110, min_damage=5, max_damage=15)
teacher3 = Teacher(name="Henrik", health=125, min_damage=8, max_damage=18)
teacher4 = Teacher(name="Victor", health=135, min_damage=1, max_damage=13)
teacher5 = Teacher(name="David", health=150, min_damage=9, max_damage=20)
teacher6 = Teacher(name="Mirrela", health=200, min_damage=11, max_damage=25)


def combat_loop(player, teacher):
    while player.health > 0 and teacher.health > 0:
        # Visa UI
        print(f"\n{player.name}'s tur\n------------")
        print(f"Inventarie:")
        print(f"- Svärd: {list(player.inventory['swords'].keys())}")
        print(f"- Potions: {player.inventory['potions']}")
        print(f"- Totems: {player.totems}")
        print(f"- Sköldar: {player.shields}")
        print(f"HP: {player.health}\n------------")
        print(f"{teacher.name}s HP: {teacher.health}\n------------")

        action = input("Välj handling (attack, heal, stand): ").strip().lower()
        print("------------")

        if action == "attack":
            weapon_name = input("Välj svärd (eller tryck ENTER för att använda händerna): ").strip().lower()
            print("------------")
            damage = player.attack(weapon_name)
            teacher.health = max(0, teacher.health - damage)
            print(f"Du attackerade {teacher.name} med {weapon_name if weapon_name else 'händerna'} och gjorde {damage} skada!")

        elif action == "heal":
            potion = input("Välj potion (normal/epic): ").strip().lower()
            heal_amount = player.heal(potion)
            if heal_amount > 0:
                player.health = min(100, player.health + heal_amount)
                print(f"Du använde en {potion}-potion och helade {heal_amount} HP! Nuvarande HP: {player.health}.")
            else:
                print("Ogiltig potion eller slut!")

        elif action == "stand":
            print("Du valde att vänta. Nästa tur!\n------------")

        else:
            print("Ogiltig handling!\n------------")

        if teacher.health <= 0:
            print(f"{teacher.name} är besegrad! Du vann!\n------------")
            break

        # Lärarens tur
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
            print("Du förlorade kampen! Bättre lycka nästa gång.\n------------")
            break


# Exempel: Starta strid
player_name = "Spelaren"
player = Character(name=player_name, health=100)
combat_loop(player, teacher1)
