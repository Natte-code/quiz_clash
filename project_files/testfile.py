import random
import time
import os

player_name = input("Innan spelet börjar helt... Ange ditt namn: ")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.coins = 5
        self.totems = 1
        self.shields = 1
        # Förenklat inventory
        self.inventory = {
            "swords": {"träsvärd": 10, "järnsvärd": 20},  # Ifall vi ska lägga till fler
            "potions": {"normal": 2, "epic": 1}          
        }

    def attack(self, weapon):
        """Beräknar skada baserat på vapen och kritisk chans."""
        # Om vapnet finns i inventoryt, använd dess skada; annars använd händerna
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
        return 0 #koden för att heala

    def block(self):
        return random.random() < 0.3 #30% chans att blockera en attack

    def totem(self):
        """Använd totem automatiskt när HP når 0."""
        if self.totems > 0:
            self.totems -= 1
            self.health = 100
            print(f"------------\nDu använde en totem! {self.name} är återupplivad med 100 HP!\n------------")
            input("Tryck ENTER för att fortsätta...")
            return True #Använder en totem om spelaren har en och ger spelaren 100 hp
        return False #om spelaren inte har totem så dör spelaren här.

    def is_critical_hit(self):
        return random.random() < 0.15 #15 % chans att göra kritisk träff

#Klassen för teacher
class Teacher:
    def __init__(self, name, health, min_damage, max_damage):
        self.name = name
        self.health = health
        self.min_damage = min_damage
        self.max_damage = max_damage

    def attack(self):
        return random.randint(self.min_damage, self.max_damage) #Slumpar skadan teacher gör mot spelaren. för att definera max och min dmg så gör man det när man definerar läraren

def combat_loop(player, teacher): #combat loopen
    while player.health > 0 and teacher.health > 0:
        clear_screen()
        
        # Visa UI
        print(f"{player.name}'s tur\n------------")
        print(f"Inventarie:\n")
        print(f"- Svärd: {list(player.inventory['swords'].keys())}")  # Lista svärden
        print(f"- Potions: {player.inventory['potions']}")           # Lista potions
        print(f"- Totems: {player.totems}")                        # Visa antal totems
        print(f"- Sköldar: {player.shields}")                      # Visa sköld
        print(f"HP: {player.health}\n------------")
        print(f"{teacher.name}s HP: {teacher.health}\n------------")

        action = input("Välj handling (attack, heal, stand): ").strip().lower()
        print("------------")

        # Spelarens tur
        if action == "attack":
            weapon = input("Välj svärd (eller tryck ENTER för att använda händerna): ").strip().lower()
            print("------------")
            if weapon in player.inventory["swords"] or weapon == "":
                damage = player.attack(weapon)
                teacher.health = max(0, teacher.health - damage)
                print(f"Du attackerade {teacher.name} med {'händerna' if weapon == '' else weapon} och gjorde {damage} skada!")
            else:
                print("Ogiltigt vapen!")
            print("------------")

#heal
        elif action == "heal":
            potion = input("Välj potion (normal/epic): ").strip().lower()
            print("------------")
            heal_amount = player.heal(potion)
            if heal_amount > 0:
                player.health = min(100, player.health + heal_amount)
                print(f"Du använde en {potion}-potion och helade {heal_amount} HP!")
            else:
                print("Ogiltig potion eller slut!")
            print("------------") 

#stand
        elif action == "stand":
            print("Du valde att vänta. Nästa tur!\n------------")

        else:
            print("Ogiltig handling!\n------------")

        # Kontrollera om teacher hp = 0
        if teacher.health <= 0:
            print(f"{teacher.name} är besegrad! Du vann!\n------------")
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!lägg till vad som ska hända här när teacher är död

        input("Tryck ENTER för att fortsätta...")

        # Lärarens tur
        print(f"{teacher.name}s tur!\n------------")
        time.sleep(2)
        damage = teacher.attack()
        if player.block():
            print("Din sköld blockerade attacken!\n------------") #Vad som händer när teachers attack blir blockerad. #se def block
        else:
            player.health = max(0, player.health - damage)
            print(f"{teacher.name} attackerade och gjorde {damage} skada!\n------------")
            # Kontrollera om spelaren ska använda totem
            if player.health == 0 and player.totem():
                continue  # Fortsätt spelet efter användning av totem

        print(f"{teacher.name}s HP: {teacher.health}\n------------")
        print(f"{player.name}s HP: {player.health}\n------------")

        # Kontrollera om player är död
        if player.health <= 0:
            print("Du förlorade kampen! Bättre lycka nästa gång.\n------------")
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Lägg till end1() här

        input("Tryck ENTER för att fortsätta...")

# Definerar alla olika charecters // lärare osv
player = Character(name=player_name, health=100)

boss = Teacher(name="Lars", health=450, min_damage=10, max_damage=95)


#combat_loop(player, MOTSTONDARE) #kallning på funktion med vilken lärare när strid ska starta
