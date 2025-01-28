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
        category = "swords"
        if category not in self.inventory:
            self.inventory[category] = {}
        self.inventory[category][sword.name] = sword.damage
        print(f"Added {sword.name} with damage {sword.damage} to inventory.")
                                                                                                            ############################################## ADDED TO SPEL.PY
# Skapa spelaren
player = Character(name=player_name, health=100)

# Lägg till svärden direkt från Sword-klassen
# player.add_sword_to_inventory(katana)
# player.add_sword_to_inventory(lightsaber)
# player.add_sword_to_inventory(Pie)

# Visa uppdaterat inventory


#jag vill här nu testa så jag kan få fram sakerna i inventoriet och ska sen implementera det.

#Svärden behöver bara hanteras som föremål allt annat kan vi göra som en siffra i en variabel
#så tex när den ska dra en potion så drar den och bara ändrar Potion = 2 tex istället för att ha det som ett föremål så får combat systemet hantera healing systemet
#samma med totem systemet.



#min förösk här 
antal_potion_vanlig = 0
antal_potion_epic = 0

def potion_inventory_vissa():
    print(f'Du har {antal_potion_vanlig} vanliga potion')
    print(f"Du har {antal_potion_epic} epic potion")

def potion_inventory_plus_vanlig():
    global antal_potion_vanlig
    antal_potion_vanlig = antal_potion_vanlig + 1
    print(f'Du har nu {antal_potion_vanlig} vanliga potion')

def potion_inventory_plus_epic():
    global antal_potion_epic
    antal_potion_epic = antal_potion_epic + 1
    print(f'Du har nu {antal_potion_epic} epic potion')

def potion_inventory_minus_vanlig():
    global antal_potion_vanlig
    if antal_potion_vanlig >= 1:
        antal_potion_vanlig = antal_potion_vanlig - 1
        print(f'Du har nu {antal_potion_vanlig} vanliga potion')
    else:
        print("Redan 0 potion vanlig")

def potion_inventory_minus_epic():
    global antal_potion_epic
    if antal_potion_epic >= 1:
        antal_potion_epic = antal_potion_epic - 1
        print(f'Du har nu {antal_potion_epic} epic potion')
    else:
        print("Redan 0 potion epic")



def lootbox_normal():

    if player.coins >= 5:
        
        lootpool_normal = ["Kukri", "Järnsvärd", "normal_potion", "katana", "Dagger", "Pinne"]
        chosen_item = random.choice(lootpool_normal)

        if chosen_item == "normal_potion":
            potion_inventory_plus_vanlig()
            print(antal_potion_vanlig)   
        elif chosen_item == "Pie":
            player.add_sword_to_inventory(Pie)
        elif chosen_item == "järnsvärd":
            player.add_sword_to_inventory(järnsvärd)
        elif chosen_item == "katana":
            player.add_sword_to_inventory(katana)
        elif chosen_item == "Dagger":
            player.add_sword_to_inventory(Dagger)
        elif chosen_item == "Pinne":
            player.add_sword_to_inventory(Pinne)
        else:
            print("Du har inte nog med coins!")


def lootbox_epic():

    if player.coins >= 5:
        
        lootpool_epic = ["Epic_potion", "battle_axe", "totem", "lightsaber", "stekpanna"]
        chosen_item = random.choice(lootpool_epic)

        if chosen_item == "Epic_potion":
            potion_inventory_plus_vanlig()
            print(antal_potion_vanlig)   
        elif chosen_item == "battle_axe":
            player.add_sword_to_inventory(battle_axe)
        elif chosen_item == "totem":
            print("totem")
            # player.add_sword_to_inventory(totem)
        elif chosen_item == "lightsaber":
            player.add_sword_to_inventory(lightsaber)
        elif chosen_item == "stekpanna":
            player.add_sword_to_inventory(stekpanna)
        
            print("Du har inte nog med coins!")



    #Lootbox_epic
        #liten chan för normal items men större chans för epic item



#funktionen ska först kolla om spelaren har nog med mynt
#sen ta bort X mängd mynt och sen ge spelaren vad dem förtjänar


jonathan = int(input(""))

if jonathan == 0:
    lootbox_normal()

else:
    lootbox_epic()


print(player.inventory)

















    # def heal(self, potion_type):
    #     if potion_type == "normal" and self.inventory["potions"].get("normal", 0) > 0:
    #         self.inventory["potions"]["normal"] -= 1
    #         return 50
    #     elif potion_type == "epic" and self.inventory["potions"].get("epic", 0) > 0:
    #         self.inventory["potions"]["epic"] -= 1
    #         return 100
    #     return 0 #koden för att heala
