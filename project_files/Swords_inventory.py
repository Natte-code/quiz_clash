import random
import time

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

player_name = "test"

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.coins = 5
        self.totems = 1
        self.shields = 1
        # Simpelt inventory
        self.inventory = {
            "swords": {"träsvärd": 10, "järnsvärd": 20},  # Ifall vi ska lägga till fler
            "potions": {"normal": 2, "epic": 1}          
        }

    def add_sword_to_inventory(self, sword: Sword):
        """
        Lägger till ett Sword-objekt i spelarens inventory i kategorin "swords".
        
        :param sword: Ett Sword-objekt som ska läggas till.
        """
        category = "swords"
        if category not in self.inventory:
            self.inventory[category] = {}
        self.inventory[category][sword.name] = sword.damage
        print(f"Added {sword.name} with damage {sword.damage} to inventory.")

# Skapa spelaren
player = Character(name=player_name, health=100)

# Lägg till svärden direkt från Sword-klassen
player.add_sword_to_inventory(katana)
player.add_sword_to_inventory(lightsaber)
player.add_sword_to_inventory(Pie)

# Visa uppdaterat inventory
print(player.inventory)

#jag vill här nu testa så jag kan få fram sakerna i inventoriet och ska sen implementera det.

#Svärden behöver bara hanteras som föremål allt annat kan vi göra som en siffra i en variabel
#så tex när den ska dra en potion så drar den och bara ändrar Potion = 2 tex istället för att ha det som ett föremål så får combat systemet hantera healing systemet
#samma med totem systemet.
