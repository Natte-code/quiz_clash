import time
import random
import curses
import os
import threading



#Def av några sid funktioner som kallas på igenom spelet
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



#Du glömde att sätta in den för minus epic potion 


#kod skaffad från Chatgpt och används för att insperara denna kod.
####################################################################################################
# Loggan definierad som en lista av strängar
import time

#Här skrivs funktioner som man ska gömma från main koden

# Loggan definierad som en lista av strängar
logo = [
    " ________  ___  ___  ___  ________                    ",
    "|\\   __  \\|\\  \\|\\  \\|\\  \\|\\_____  \\                   ",
    "\\ \\  \\|\\  \\ \\  \\\\\\  \\ \\  \\\\|___/  /|                  ",
    " \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\  \\   /  / /                  ",
    "  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\  \\ /  /_/__                 ",
    "   \\ \\_____  \\ \\_______\\ \\__\\\\________\\               ",
    "    \\|___| \\__\\|_______|\\|__|\\|_______|              ",
    "          \\|__|                                       ",
    "                                                     ",
    " ________  ___       ________  ________  ___  ___    ",
    "|\\   ____\\|\\  \\     |\\   __  \\|\\   ____\\|\\  \\|\\  \\   ",
    "\\ \\  \\___|\\ \\  \\    \\ \\  \\|\\  \\ \\  \\___|\\ \\  \\\\\\  \\  ",
    " \\ \\  \\    \\ \\  \\    \\ \\   __  \\ \\_____  \\ \\   __  \\ ",
    "  \\ \\  \\____\\ \\  \\____\\ \\  \\ \\  \\|____|\\  \\ \\  \\ \\  \\",
    "   \\ \\_______\\ \\_______\\ \\__\\ \\__\\____\\_\\  \\ \\__\\ \\__\\",
    "    \\|_______|\\|_______|\\|__|\\|__|\\_________\\|__|\\|__|",
    "                                 \\|_________|         "
]

def logo_print(logo, delay=0.15):
    for line in logo:
      print(line)
      time.sleep(delay) 
#funktionen skriver ut loggan rad för rad med tiden 0.2 s per rad.



def start_screen(): #startar start skärmen, förklarar hur man spelar och visar loggan
   print("")
   print("\n" * 100)
   print("")
   print("välkommen till ♦Quiz Clash♦")
   time.sleep(1)
   print("")
   print("....")
   print("")
   time.sleep(1)
   logo_print(logo)
   time.sleep(1)
   print("")
   print("""Hur man spelar:
                Rör dig med WASD
                Samla mynt, öppna lådor och upptäck klassrum. 
                Svara på lärarens frågor. Fel svar leder till turordningsbaserade strider.
                Håll terminalen i FULL SCREEN (Och zooma ut om spelet krashar (med hjälp av att trycka CTRL och - ))!!
                Håll årdning på ditt inventory (går ej att släppa saker, så använd varsamt!)
                Lycka till!!
         """)
   print("")

   print("\nTryck på ENTER knappen för att starta spelet!")
   input()

start_screen()
player_name = input("Ange ditt namn: ")






###########################################################################

#classes för allt i spelet
#altså där vi lagrar all info om alla saker som kan förändras

#koden skrivs av nathaniel och eliot

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
skibidi = Sword("Skibidi", 1005745283746239746295786395876395876349857365873465927648972364924)


def add_sword_to_inventory(self, sword: Sword):
    category = "swords"
    if category not in self.inventory:
        self.inventory[category] = {}
    self.inventory[category][sword.name] = sword.damage
    print(f"Added {sword.name} with damage {sword.damage} to inventory.")



class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.coins = 5
        self.totems = 1
        self.shields = 1
        self.antal_potion_vanlig = 5 # Här behövs tänkas på ifall något blir fel med potions och om dessa nummer ska ändras. Det ät satt på 5 för DEMO just nu.-
        self.antal_potion_epic = 5
        self.inventory = {
            "swords": {"träsvärd": 10, "järnsvärd": 20},  # Ifall vi ska lägga till fler
            "potions": {"normal": 2, "epic": 1}          
        }
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
        
def is_critical_hit(self):
    return random.random() < 0.15 #15 % chans att göra kritisk träff
    

def attack(self, weapon):
    # Om vapnet finns i inventoryt, använd dess skada; annars använd händerna
    """Beräknar skada baserat på vapen och kritisk chans."""
    base_damage = self.inventory["swords"].get(weapon, random.randint(5, 10))
    if self.is_critical_hit():
        crit_damage = int(base_damage * 2.5)
        print(f"KRITISK TRÄFF! Du gör {crit_damage} skada!\n------------")
        return crit_damage
    return base_damage


def heal(self, potion_type):
    if potion_type == "normal" and self.antal_potion_vanlig > 0:
        self.antal_potion_vanlig -= 1
        return 50
    elif potion_type == "epic" and self.antal_potion_epic > 0:
        self.antal_potion_epic -= 1
        return 100
    return 0 #koden för att heala--

                                                                ## Nu Får vi fan se om denna bootleg ändring funkar
                                                                    # Modifierade koden bara rakt av utav huvudet
                                                                    #(om något inte funkar så är det mitt fel - Nathaniel)

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


    
# Definerar Spelaren
player = Character(name=player_name, health=100)

class boss:
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
        while self.isregen: True
        time.sleep(10)
        if self.health < self.max_health:
            self.health = min(self.max_health, self.health + self.regen)
            print(f"+15 HP: {self.health}")

    def stop_regen(self):
        self.isregen = False

    def attack(self):
        return random.randint(self.min_damage, self.max_damage)

#Klassen för teacher
class Teacher:
    def __init__(self, name, health, min_damage, max_damage):
        self.name = name
        self.health = health
        self.min_damage = min_damage
        self.max_damage = max_damage

    def attack(self):
        return random.randint(self.min_damage, self.max_damage) #Slumpar skadan teacher gör mot spelaren. för att definera max och min dmg så gör man det när man definerar läraren
#definerar Lärararna osv

bos = boss(name="Lars", health=450, min_damage=10, max_damage=95, regen=15)

teacher1 = Teacher(name="johanna", health=100, min_damage=1, max_damage=10) #klassrumm 1
teacher2 = Teacher(name="Ronja", health=110, min_damage=5, max_damage=15)
teacher3 = Teacher(name="Henrik", health=125, min_damage=8, max_damage=18)
teacher4 = Teacher(name="Victor", health=135, min_damage=1, max_damage=13)
teacher5 = Teacher(name="David", health=150, min_damage=9, max_damage=20)
teacher6 = Teacher(name="Mirrela", health=200, min_damage=11, max_damage=25) #klassrumm 6


#######################################################################################################################

def combat_loop(player, teacher): #combat loopen1
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
                print(f"Du har nu {player.health}HP!")
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
            
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        
            
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
            end1()
        if teacher.health <= 0:
            break
    # print(f"{teacher.name} är besegrad! Du vann!\n------------")
    # player.coins += 10  # Reward coins
    # print(f"Du fick 10 mynt! Du har nu {player.coins} mynt.")
    # defeated_teachers.append(teacher.name)



#combat_loop(player, MOTSTONDARE) #kallning på funktion med vilken lärare när strid ska starta


#--------------------------------------------------------------------------


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

    if player.coins >= 15:
        
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


















###########################################################################
#där skrivs alla frågor för lärare
#alla lärare har sin egen definition med 20 frågor, bara 5 av de är plockad för varje lärare
#den kod är skriven av eliot


# starta frågorna

#johanna
def johannaquestion():
    global input_j
    os.system('cls' if os.name == 'nt' else 'clear')
    # Olika frågor och rätta svar
    input_j = 1 # Gör så att man vet när den har frågat fem frågor
    q_and_a_johanna = [
        ("Vad är 15 + 27?", "42"),
        ("Vad är 12 × 9?", "108"),
        ("Lös ekvationen: ? + 7 = 20", "13"),
        ("Vad är arean av en rektangel med längd 5 cm och bredd 3 cm?", "15 cm2"),
        ("Vad är medelvärdet av 5, 8, 12 och 20?", "11,25"),
        ("Om en triangel har basen 6 cm och höjden 4 cm, vad är dess area?", "12 cm2"),
        ("Beräkna: 3 + 2 x 5", "13"),
        ("Vad är volymen av en kub med sidan 4 cm?", "64 cm3"),
        ("Om en cirkels radie är 3 cm, vad är dess omkrets?", "18,84 cm"),
        ("Vad är 15% av 200?", "30"),
        ("Lös ekvationen: (2 x ?) = 10", "5"),
        ("Vad är 5^2?", "25"),
        ("Om ett pris ökar med 10%, vad blir det nya priset på 50 kr?", "55kr"),
        ("Vad är 3/4 + 1/4?", "1"),
        ("Om y = 4, vad är värdet av 2 + 3 x y? (Endast svar)", "14"),
        ("Vad är 9 x 8 ?", "72"),
        ("Om du delar 45 med 5, vad får du då?", "9"),
        ("Vad är 1/5 av 50?", "10"),
        ("Vad är: 7 x 3 - 3", "18"),
        ("Vad är medelvärdet av 3, 6, 9 och 12?", "7,5")
    ]

    # Välj slumpmässigt 5 frågor
    selected_questions = random.sample(q_and_a_johanna, 5)

    for i, (question, correct_answer) in enumerate(selected_questions, start=1):
        print(f"Fråga {i}: {question}")
        answer = input("Ditt svar: ").strip().lower()

        if answer == correct_answer.lower():
            print("Rätt!\n")
            input_j =  input_j + 1

        else:
            # Spelaren går in i fight
            print(f"Fel!")
            time.sleep(1)
            print("Nu du ska vi slåss >:)")
            time.sleep(5)
            combat_loop(player, teacher1)

    if input_j == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        curses.initscr()
        return input_j
        
#ronja
def ronjaquestion():
    global input_r
    os.system('cls' if os.name == 'nt' else 'clear')
    input_r = 1
    # Olika frågor och rätta svar
    q_and_a_ronja = [
    ("What is the capital of the United Kingdom?", "London"),
    ("Who wrote the play 'Romeo and Juliet'?", "William Shakespeare"),
    ("Which word is a synonym for 'happy'?", "joyful"),
    ("What is the opposite of 'increase'?", "decrease"),
    ("What is the past tense of 'run'?", "ran"),
    ("What is the plural form of 'child'?", "children"),
    ("How do you spell the color of the sky?", "blue"),
    ("Which of these is a noun: 'quickly', 'dog', or 'happy'?", "dog"),
    ("What is the superlative form of 'good'?", "best"),
    ("What does the word 'benevolent' mean?", "kind or charitable"),
    ("What is the past participle of 'eat'?", "eaten"),
    ("What is the meaning of 'metaphor'?", "a figure of speech comparing two things without using 'like' or 'as'"),
    ("Which of these is a verb: 'sing', 'yellow', or 'cat'?", "sing"),
    ("What is the opposite of 'inside'?", "outside"),
    ("What type of word is 'quickly'?", "adverb"),
    ("What does the word 'audible' mean?", "able to be heard"),
    ("What is the plural of 'mouse'?", "mice"),
    ("Which is the correct form: 'She don't like ice cream' or 'She doesn't like ice cream'?", "She doesn't like ice cream"),
    ("What is the comparative form of 'big'?", "bigger"),
    ("Which is a compound word: 'sunshine', 'happy', or 'book'?", "sunshine")
]

    # Välj slumpmässigt 5 frågor
    selected_questions = random.sample(q_and_a_ronja, 5)

    for i, (question, correct_answer) in enumerate(selected_questions, start=1):
        print(f"Fråga {i}: {question}")
        answer = input("Ditt svar: ").strip().lower()

        if answer == correct_answer.lower():
            print("Rätt!\n")
            input_r = input_r + 1
        else:
            # Spelaren går in i fight
            print(f"Fel!")
            combat_loop(player, teacher2)
            break
    if input_r == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        curses.initscr()
        return input_r

#henrik
def henrikquestion():
    global input_h
    os.system('cls' if os.name == 'nt' else 'clear')
    input_h = 1
    # Olika frågor och rätta svar
    q_and_a_henrik = [
    ("Är solen en stjärna?", "Ja"),
    ("Har alla föremål med massa också gravitation?", "Ja"),
    ("Kan ljud färdas i rymden?", "Nej"),
    ("Är ljus snabbare än ljud?", "Ja"),
    ("Är vatten en bra ledare för elektricitet?", "Ja"),
    ("Är en Newton en enhet för kraft?", "Ja"),
    ("Är temperaturen alltid högre än 0°C på jorden?", "Nej"),
    ("Kan energi förstöras?", "Nej"),
    ("Är tyngdkraften svagare på månen än på jorden?", "Ja"),
    ("Kan du se infrarött ljus med blotta ögat?", "Nej"),
    ("Är elektricitet och magnetism relaterade?", "Ja"),
    ("Kan en kompass peka mot söder?", "Nej"),
    ("Är metaller bra ledare för värme?", "Ja"),
    ("Kan en kraft ändra riktningen på ett föremål?", "Ja"),
    ("Är atomkärnan större än atomen?", "Nej"),
    ("Är en blixt ett exempel på statisk elektricitet?", "Ja"),
    ("Är gravitationskraften starkare på jorden än på Jupiter?", "Nej"),
    ("Kan ett föremål flyta om dess densitet är högre än vattnets?", "Nej"),
    ("Är ljus både en våg och en partikel?", "Ja"),
    ("Är värme en form av energi?", "Ja")
]


    # Välj slumpmässigt 5 frågor
    selected_questions = random.sample(q_and_a_henrik, 5)

    for i, (question, correct_answer) in enumerate(selected_questions, start=1):
        print(f"Fråga {i}: {question}")
        answer = input("Ditt svar: ").strip().lower()

        if answer == correct_answer.lower():
            print("Rätt!\n")
            input_h = input_h + 1
        else:
            # Spelaren går in i fight
            print(f"Fel!")
            combat_loop(player, teacher3)
            break

    if input_h == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        curses.initscr()
        return input_h

#Victor
def vicorquestion():
    global input_v
    os.system('cls' if os.name == 'nt' else 'clear')
    input_v = 1
    # Olika frågor och rätta svar
    q_and_a_victor = [
    ("Vilket tal saknas i serien: 2, 4, 8, 16, ?", "32"),
    ("En trappstege är 6 steg hög. Om du går upp 3 steg och ner 2 steg, hur många steg är du totalt uppförd?", "1"),
    ("Om du har 4 olika färger av marker och du ska välja 2 marker att ta, hur många olika kombinationer kan du göra?", "6"),
    ("Vad är det största talet som är delbart med både 12 och 18?", "36"),
    ("Om en bok kostar 100 kronor och den är nedsatt med 25%, vad kostar boken?", "75 kronor"),
    ("Om du har en korg med 5 röda äpplen, 7 gröna och 3 gula, hur många äpplen är det i korgen totalt?", "15 äpplen"),
    ("Om en rektangel har en längd på 12 cm och en bredd på 4 cm, vad är dess omkrets?", "32 cm"),
    ("Om en tårta är delad i 10 bitar och du äter 3, hur många bitar är kvar?", "7 bitar"),
    ("Vilken ordning kommer bokstäverna A, C, B i när man ordnar dem alfabetiskt?", "A B C"),
    ("Vad är det största gemensamma delare av 24 och 36?", "12"),
    ("Om en person kör 60 km på 1 timme, hur långt skulle personen köra på 4 timmar?", "240 km"),
    ("Hur många olika sätt kan du ordna tre böcker på en hylla?", "6 sätt"),
    ("Felix ålder är dubbelt så stor som Marcus. Om Felix är 12 år, hur gammal är Marcus?", "6 år"),
    ("Om du går 5 steg framåt och 2 steg bakåt, hur många steg framåt är du från startpunkten?", "3 "),
    ("En fisk simmar 30 meter varje minut. Hur långt simmar den på 10 minuter?", "300 meter"),
    ("Om en bok har 250 sidor och du har läst 150 sidor, hur många sidor är kvar?", "100 sidor"),
    ("Vad är nästa tal i serien: 1, 4, 9, 16, ?", "25"),
    ("Vad är medianen i följande tal: 5, 8, 10, 2, 7?", "7"),
    ("En veckodag infaller var sjunde dag. Om det är en tisdag idag, vilken veckodag är det om 28 dagar?", "Tisdag"),
    ("Om du har 5 bilar och varje bil kan ta 4 passagerare, hur många passagerare kan totalt åka i alla bilar?", "20 passagerare"),
    ("Vad är nästa tal i serien: 1, 1, 2, 3, 5, 8, ?", "13")
]



    # Välj slumpmässigt 5 frågor
    selected_questions = random.sample(q_and_a_victor, 5)

    for i, (question, correct_answer) in enumerate(selected_questions, start=1):
        print(f"Fråga {i}: {question}")
        answer = input("Ditt svar: ").strip().lower()

        if answer == correct_answer.lower():
            print("Rätt!\n")
            input_v = input_v + 1
        else:
            # Spelaren går in i fight
            print(f"Fel!")
            combat_loop(player, teacher4)
            break
    if input_v == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        curses.initscr()
        return input_v

#David
def davidquestion():
    global input_d
    os.system('cls' if os.name == 'nt' else 'clear')
    input_d = 1
    # Olika frågor och rätta svar
    q_and_a_david = [
    ("Hur många spelare finns det i ett fotbollslag?", "11"),
    ("Vad är längden på ett standard maratonlopp?", "42,195 km"),
    ("I basket, hur många poäng är ett tvåpoängsskott värt?", "2 poäng"),
    ("Vad är det högsta möjliga poängantalet i en bowlingmatch?", "300"),
    ("Hur många minuter är en standard ishockeymatch?", "60 minuter"),
    ("Vad kallas ett resultat av noll i tennis?", "love"),
    ("Vilken sport spelas på Wimbledon?", "Tennis"),
    ("Hur många yards är det i en mile?", "1 760 yards"),
    ("I vilken sport använder man en spjut?", "Friidrott"),
    ("Vad är högsta möjliga poäng i en gymnastikövning?", "10.0"),
    ("Vad är avståndet mellan baserna i baseball?", "90 fot"),
    ("Hur lång är en olympisk simbassäng?", "50 meter"),
    ("Vilken typ av lopp är 100 meter?", "Sprint"),
    ("I vilken sport gör man en layup?", "Basketboll"),
    ("Vad heter trofén som delas ut till vinnaren av Super Bowl?", "Vince Lombardi Trophy"),
    ("I vilken sport tävlar man i tiokamp?", "Friidrott"),
    ("Hur lång är en standard rugbymatch?", "80 minuter"),
    ("Vad heter fotbollstävlingen som spelas mellan de bästa lagen i Europa?", "UEFA Champions League"),
    ("Hur många set måste en spelare vinna för att vinna en match i volleyboll?", "3")
]




    # Välj slumpmässigt 5 frågor
    selected_questions = random.sample(q_and_a_david, 5)

    for i, (question, correct_answer) in enumerate(selected_questions, start=1):
        print(f"Fråga {i}: {question}")
        answer = input("Ditt svar: ").strip().lower()

        if answer == correct_answer.lower():
            print("Rätt!\n")
            input_d = input_d + 1
        else:
            # Spelaren går in i fight
            print(f"Fel!")
            break
        combat_loop(player, teacher5)
    if input_d == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        curses.initscr()
        return input_d
            
#Mirrela
def mirrelaquestion():
    global input_m
    os.system('cls' if os.name == 'nt' else 'clear')
    input_m = 1
    # Olika frågor och rätta svar
    q_and_a_mirrela = [
    ("Är CPU detsamma som datorns hjärna?", "Ja"),
    ("Kan du surfa på internet utan en webbläsare?", "Nej"),
    ("Är en hårddisk till för att lagra data?", "Ja"),
    ("Är en IP-adress alltid synlig för användaren?", "Nej"),
    ("Kan en router ge internetanslutning trådlöst?", "Ja"),
    ("Är USB ett sätt att överföra data mellan enheter?", "Ja"),
    ("Är www en förkortning för Wide World Web?", "Nej"),
    ("Kan datorvirus spridas genom e-postbilagor?", "Ja"),
    ("Är Wi-Fi detsamma som en nätverkskabel?", "Nej"),
    ("Är RAM ett permanent lagringsutrymme?", "Nej"),
    ("Kan du skriva ut en fil utan att en skrivare är ansluten?", "Nej"),
    ("Är en server en dator som delar resurser i ett nätverk?", "Ja"),
    ("Behöver du en nätverkskabel för att ansluta till internet via Wi-Fi?", "Nej"),
    ("Kan en bit bara ha värdena 0 eller 1?", "Ja"),
    ("Är en molntjänst fysisk hårdvara i ditt hem?", "Nej"),
    ("Är en webbsida en del av internet?", "Ja"),
    ("Är antivirusprogram alltid gratis?", "Nej"),
    ("Kan en nätverksswitch koppla ihop flera datorer?", "Ja"),
    ("Är Windows ett exempel på ett operativsystem?", "Ja"),
    ("Kan du ladda ner en fil utan en internetanslutning?", "Nej")
]


    # Välj slumpmässigt 5 frågor
    selected_questions = random.sample(q_and_a_mirrela, 5)

    for i, (question, correct_answer) in enumerate(selected_questions, start=1):
        print(f"Fråga {i}: {question}")
        answer = input("Ditt svar: ").strip().lower()

        if answer == correct_answer.lower():
            print("Rätt!\n")
            input_m = input_m + 1
        
            
        else:
            # Spelaren går in i fight
            print(f"Fel!")
            combat_loop(player, teacher6)
            break
    if input_m == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        curses.initscr()
        return input_m


#Lars boss
def larsquestion(): 
    inputl = 1
    # Olika frågor och rätta svar
    q_and_a_boss = [
        #omöjlig att svara rätt på
        ("Är det möjligt att svara nej på denna fråga och ändå ha rätt?", "dnjgfj28736t542iuyfh2iuf8888888888888888888888888888888888888888888888UHIFOI"),
        ("Vad är 1/100 av 50?", "0,5"),
        ("Är en hårddisk till för att lagra data", "ja"),
        ("Kan ett föremål flyta om dess densitet är högre än vattnets?", "nej"),
        ("Beräkna: 1 x 3 + 2 x 3 + 3 x 3", "18"),
    ]

    # Välj slumpmässigt 5 frågor
    selected_questions = random.sample(q_and_a_boss, 5)

    for i, (question, correct_answer) in enumerate(selected_questions, start=1):
        print(f"Fråga {i}: {question}")
        answer = input("Ditt svar: ").strip().lower()

        if answer == correct_answer.lower():
            print("Rätt!\n")
            inputl = inputl + 1
        else:
            print("Fel!")
            combat_loop(player, boss)
            break
    if inputl == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        curses.initscr()
        

# ändrade så att status saken funkade bättre med hjälp av AI
def status():
    
    teachers = [teacher1, teacher2, teacher3, teacher4, teacher5, teacher6]
    
    if all(t.health == 0 for t in teachers) and bos.health == 0:
        return "Alla lärare och Lars är besegrade!"
    elif all(t.health == 0 for t in teachers):
        return "Du har bara Lars kvar nu!"
    else:
        status_msg = "Lärare hälsostatus:\n"
        for t in teachers:
            status_msg += f"{t.name}: {'Besegrad' if t.health == 0 else 'Levande'}\n"
        status_msg += f"Lars: {'Besegrad' if bos.health == 0 else 'Levande'}"
        return status_msg
    
# Denna hindra en från att gå ut ur dörren innan alla lärare och boss är döda
def exit_door():
    os.system('cls' if os.name == 'nt' else 'clear')
    if teacher1.health == 0 and teacher2.health == 0 and teacher3.health == 0 and teacher4.health == 0 and teacher5.health == 0 and teacher6.health == 0 and bos.health == 0:
        end2()
    else:
        print("Nope, Exit dörren är stängd,")
        print("Besegra alla lärare och Lars först innan du kan komma igenom!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        curses.initscr()


# Denna göra så att man inte kan komma in i lars rum om lärare lever
def lars_door():
    os.system('cls' if os.name == 'nt' else 'clear')
    if teacher1.health == 0 and teacher2.health == 0 and teacher3.health == 0 and teacher4.health == 0 and teacher5.health == 0 and teacher6.health == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        curses.initscr()
        Larsboss()
    else:
        print("Nope, Dörren till Lars rum är stängt,")
        print("Besegra alla lärare inna du kan komma igenom!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        curses.initscr()

#spelaren ska få coins av att defeata läraren


#kod skaffad från Chatgpt och används för att insperara denna kod.
####################################################################################################
def clear_terminal_visual():
    os.system('cls' if os.name == 'nt' else 'clear')

##################################
def end1():
    clear_terminal_visual()
    print(""" 
 __   __            ____  _          _   _ 
 \ \ / /__  _   _  |  _ \(_) ___  __| | | |
  \ V / _ \| | | | | | | | |/ _ \/ _` | | |
   | | (_) | |_| | | |_| | |  __/ (_| | |_|
   |_|\___/ \__,_| |____/|_|\___|\__,_| (_)


    --Tack för du har spelat Quiz Clash--
    --Spela igen för hela slutet--
    --Slut 1 av 4, (Bad ending)--
    
    """)
    exit()

def end2():
    clear_terminal_visual()
    print("""
__   __                     _       _ 
\ \ / /__  _   _  __      _(_)_ __ | |
 \ V / _ \| | | | \ \ /\ / / | '_ \| |
  | | (_) | |_| |  \ V  V /| | | | |_|
  |_|\___/ \__,_|   \_/\_/ |_|_| |_(_)

    --Tack för du har spelat Quiz Clash--
    --Gjord av Nathaniel, Felix och Elliot--
    --Slut 2 av 4, (Good ending)--""")
    exit()

def end3():
    clear_terminal_visual()
    print("""
    _     __           _     _       
   / \   / _|_ __ __ _(_) __| |      
  / _ \ | |_| '__/ _` | |/ _` |      
 / ___ \|  _| | | (_| | | (_| |_ _ _ 
/_/   \_\_| |_|  \__,_|_|\__,_(_|_|_)

    --Tack för du har spelat Quiz Clash--
    --Spela igen för hela slutet--
    --Slut 3 av 4, (afraid ending)--""")
    exit()

def end4():
    clear_terminal_visual()
    print("""
                        _    __   _         _   
 _ __     __ _    ___  (_)  / _| (_)  ___  | |_ 
| '_ \   / _` |  / __| | | | |_  | | / __| | __|
| |_) | | (_| | | (__  | | |  _| | | \__ \ | |_ 
| .__/   \__,_|  \___| |_| |_|   |_| |___/  \__|
|_|                                             
    --Tack för du har spelat Quiz Clash--
    --Spela igen för hela slutet--
    --Slut 4 av 4, (pacifist ending)--""")
    exit()
    
#--------------------------------------------------------------------------


def val_av_end():
    if teacher1.health == 0 and teacher2.health == 0 and teacher3.health == 0 and teacher4.health == 0 and teacher5.health == 0 and teacher6.health == 0 and bos.health == 0:
        end2()
    
    if teacher1.health == 0 and teacher2.health == 0 and teacher3.health == 0 and teacher4.health == 0 and teacher5.health == 0 and teacher6.health == 0 and bos.health == 450:
        end3()
    
    if teacher1.health == 100 and teacher2.health == 110 and teacher3.health == 125 and teacher4.health == 135 and teacher5.health == 150 and teacher6.health == 200 and bos.health == 450:
        end4()



###########################################################################
#koden för rörelse i spelet och att skapa spelkartan
#bas kod är skapad av ChatGPT och modifierad av Felix


def room1(stdscr, transition_to):
    
    # Initialize curses
    curses.initscr()
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking getch
    stdscr.timeout(20000) # Input timeout (ms)

    # Game variables
    rows, cols = 25, 45  # Game board dimensions
    player_pos = [12, 37]  # Player's starting position
    block_pos = []   # Block positions
    Lärar_pos = [12, 3]      # Goal position
    door_pos = [[13, 41], [12, 42], [11, 43]]

    key = None           # Key press tracker
    message = ""

    while True:
        # Draw game board
        stdscr.clear()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    stdscr.addch(r, c, '#')  # Wall
                elif [r, c] in door_pos:
                    stdscr.addch(r, c, '/')
                elif [r, c] in block_pos:
                    stdscr.addch(r, c, 'B')  # Block
                elif [r, c] == Lärar_pos:
                    stdscr.addch(r, c, 'X')  # Goal
                elif [r, c] == player_pos:
                    stdscr.addch(r, c, 'O')  # Player
                else:
                    stdscr.addch(r, c, ' ')  # Empty space

        # Display the message
        stdscr.addstr(rows, 0, f"Message: {message}")
        message = '''
        Johannas rum

        Hej, jag heter Johanna och jag är en matte lärare.

        Jag kommer ställa dig 5 olika frågor, om du svarar rätt på alla då får du gå iväg.
        Om du gör ett ända fel då kommer det blir kaos för dig.

        Hehe
        '''
        stdscr.refresh()

        # Handle user input
        key = stdscr.getch()
        new_pos = player_pos.copy()

        if key == ord('q'):  # Quit the game
            break
        elif key == ord('w'):  # Move up
            new_pos[0] -= 1
        elif key == ord('s'):  # Move down
            new_pos[0] += 1
        elif key == ord('a'):  # Move left
            new_pos[1] -= 1
        elif key == ord('d'):  # Move right
            new_pos[1] += 1
        elif key == ord('i'):
            break
        
        # Validate movement
        if not (new_pos[0] == 0 or new_pos[0] == rows - 1 or 
                 new_pos[1] == 0 or new_pos[1] == cols - 1) and new_pos not in block_pos:
            player_pos = new_pos

        # Check for goal and special positions
        if player_pos == Lärar_pos:
            if teacher1.health == 0 or input_j == 5:
                player_pos = [12, 37]
                message = ("Johanna är död")
            else:
                stdscr.clear()
                os.system('cls' if os.name == 'nt' else 'clear')
                curses.endwin()
                player_pos = [12, 37]
                johannaquestion()
            
        elif player_pos in door_pos:
            transition_to("main")
            break

###############################################################################
#Room 2
def room2(stdscr, transition_to):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking getch
    stdscr.timeout(20000) # Input timeout (ms)

    # Game variables
    rows, cols = 25, 45  # Game board dimensions
    player_pos = [12, 37]  # Player's starting position
    block_pos = []   # Block positions
    Lärar_pos = [12, 3]      # Goal position
    door_pos = [[13, 41], [12, 42], [11, 43]]

    key = None           # Key press tracker
    message = ""

    while True:
        # Draw game board
        stdscr.clear()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    stdscr.addch(r, c, '#')  # Wall
                elif [r, c] in door_pos:
                    stdscr.addch(r, c, '/')
                elif [r, c] in block_pos:
                    stdscr.addch(r, c, 'B')  # Block
                elif [r, c] == Lärar_pos:
                    stdscr.addch(r, c, 'X')  # Goal
                elif [r, c] == player_pos:
                    stdscr.addch(r, c, 'O')  # Player
                else:
                    stdscr.addch(r, c, ' ')  # Empty space

        # Display the message
        stdscr.addstr(rows, 0, f"Message: {message}")
        message ='''
        Ronja rum

        Hi my name is Ronja, I am a english/swedish teatcher.

        I am going to ask you 5 question, if you answer correct to all of them you can leave.
        If you do one single mistake this is going to be really bad for you.

        Let's go!
        '''
        stdscr.refresh()

        # Handle user input
        key = stdscr.getch()
        new_pos = player_pos.copy()

        if key == ord('q'):  # Quit the game
            break
        elif key == ord('w'):  # Move up
            new_pos[0] -= 1
        elif key == ord('s'):  # Move down
            new_pos[0] += 1
        elif key == ord('a'):  # Move left
            new_pos[1] -= 1
        elif key == ord('d'):  # Move right
            new_pos[1] += 1
        elif key == ord('i'):
            break
        
        # Validate movement
        if not (new_pos[0] == 0 or new_pos[0] == rows - 1 or 
                 new_pos[1] == 0 or new_pos[1] == cols - 1) and new_pos not in block_pos:
            player_pos = new_pos

        # Check for goal and special positions
        if player_pos == Lärar_pos:
            if teacher2.health == 0 or input_r == 5:
                player_pos = [12, 37]
                message = ("Ronja är död")
            else:
                stdscr.clear()
                os.system('cls' if os.name == 'nt' else 'clear')
                curses.endwin()
                player_pos = [12, 37]
                ronjaquestion()
            
        elif player_pos in door_pos:
            transition_to("main")
            break

###############################################################################
#Room 3
def room3(stdscr, transition_to):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking getch
    stdscr.timeout(20000) # Input timeout (ms)

    # Game variables
    rows, cols = 25, 45  # Game board dimensions
    player_pos = [12, 7]  # Player's starting position
    block_pos = []   # Block positions
    Lärar_pos = [12, 40]      # Goal position
    door_pos = [[13, 1], [12, 2], [11, 3]]

    key = None           # Key press tracker
    message = ""

    while True:
        # Draw game board
        stdscr.clear()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    stdscr.addch(r, c, '#')  # Wall
                elif [r, c] in door_pos:
                    stdscr.addch(r, c, '/')
                elif [r, c] in block_pos:
                    stdscr.addch(r, c, 'B')  # Block
                elif [r, c] == Lärar_pos:
                    stdscr.addch(r, c, 'X')  # Goal
                elif [r, c] == player_pos:
                    stdscr.addch(r, c, 'O')  # Player
                else:
                    stdscr.addch(r, c, ' ')  # Empty space

        # Display the message
        stdscr.addstr(rows, 0, f"Message: {message}")
        message = '''
        Henrik rum

        Hej, jag heter Henrik och jag är en matte och fysik lärare.

        Jag kommer ställa dig 5 olika frågor, om du svarar rätt på alla då får du gå iväg.
        Om du gör ett ända fel då kommer det blir  för dig.

        Hehe
        '''
        stdscr.refresh()

        # Handle user input
        key = stdscr.getch()
        new_pos = player_pos.copy()

        if key == ord('q'):  # Quit the game
            break
        elif key == ord('w'):  # Move up
            new_pos[0] -= 1
        elif key == ord('s'):  # Move down
            new_pos[0] += 1
        elif key == ord('a'):  # Move left
            new_pos[1] -= 1
        elif key == ord('d'):  # Move right
            new_pos[1] += 1
        elif key == ord('i'):
            break
        
        # Validate movement
        if not (new_pos[0] == 0 or new_pos[0] == rows - 1 or 
                 new_pos[1] == 0 or new_pos[1] == cols - 1) and new_pos not in block_pos:
            player_pos = new_pos

        # Check for goal and special positions
        if player_pos == Lärar_pos:
            if teacher3.health == 0 or input_h == 5:
                player_pos = [12, 37]
                message = ("Henrik är död")
            else:
                stdscr.clear()
                os.system('cls' if os.name == 'nt' else 'clear')
                curses.endwin()
                player_pos = [12, 7]
                henrikquestion()
            
        elif player_pos in door_pos:
            transition_to("main")
            break

###############################################################################
#Room 4
def room4(stdscr, transition_to):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking getch
    stdscr.timeout(20000) # Input timeout (ms)

    # Game variables
    rows, cols = 25, 45  # Game board dimensions
    player_pos = [12, 7]  # Player's starting position
    block_pos = []   # Block positions
    Lärar_pos = [12, 40]      # Goal position
    door_pos = [[13, 1], [12, 2], [11, 3]]

    key = None           # Key press tracker
    message = ""

    while True:
        # Draw game board
        stdscr.clear()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    stdscr.addch(r, c, '#')  # Wall
                elif [r, c] in door_pos:
                    stdscr.addch(r, c, '/')
                elif [r, c] in block_pos:
                    stdscr.addch(r, c, 'B')  # Block
                elif [r, c] == Lärar_pos:
                    stdscr.addch(r, c, 'X')  # Goal
                elif [r, c] == player_pos:
                    stdscr.addch(r, c, 'O')  # Player
                else:
                    stdscr.addch(r, c, ' ')  # Empty space

        # Display the message
        stdscr.addstr(rows, 0, f"Message: {message}")
        message = '''
        Victor rum

        Hej, jag heter Victor och jag är en matte lärare.

        Jag kommer ställa dig 5 olika frågor om logisk tänkande, om du svarar rätt på alla då får du gå iväg.
        Om du gör ett ända fel då kommer det blir.... du vill inte veta hehehe.

        '''
        stdscr.refresh()

        # Handle user input
        key = stdscr.getch()
        new_pos = player_pos.copy()

        if key == ord('q'):  # Quit the game
            break
        elif key == ord('w'):  # Move up
            new_pos[0] -= 1
        elif key == ord('s'):  # Move down
            new_pos[0] += 1
        elif key == ord('a'):  # Move left
            new_pos[1] -= 1
        elif key == ord('d'):  # Move right
            new_pos[1] += 1
        elif key == ord('i'):
            break
        
        # Validate movement
        if not (new_pos[0] == 0 or new_pos[0] == rows - 1 or 
                 new_pos[1] == 0 or new_pos[1] == cols - 1) and new_pos not in block_pos:
            player_pos = new_pos

        # Check for goal and special positions
        if player_pos == Lärar_pos:
            if teacher4.health == 0 or input_v == 5:
                player_pos = [12, 7]
                message = ("Victor är död")
            else:
                stdscr.clear()
                os.system('cls' if os.name == 'nt' else 'clear')
                curses.endwin()
                player_pos = [12, 7]
                vicorquestion()
            
        elif player_pos in door_pos:
            transition_to("main")
            break

###############################################################################
#Room 5
def room5(stdscr, transition_to):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking getch
    stdscr.timeout(20000) # Input timeout (ms)

    # Game variables
    rows, cols = 25, 45  # Game board dimensions
    player_pos = [12, 7]  # Player's starting position
    block_pos = []   # Block positions
    Lärar_pos = [12, 40]      # Goal position
    door_pos = [[13, 1], [12, 2], [11, 3]]

    key = None           # Key press tracker
    message = ""

    while True:
        # Draw game board
        stdscr.clear()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    stdscr.addch(r, c, '#')  # Wall
                elif [r, c] in door_pos:
                    stdscr.addch(r, c, '/')
                elif [r, c] in block_pos:
                    stdscr.addch(r, c, 'B')  # Block
                elif [r, c] == Lärar_pos:
                    stdscr.addch(r, c, 'X')  # Goal
                elif [r, c] == player_pos:
                    stdscr.addch(r, c, 'O')  # Player
                else:
                    stdscr.addch(r, c, ' ')  # Empty space

        # Display the message
        stdscr.addstr(rows, 0, f"Message: {message}")
        message = '''
        David rum

        Hej, jag heter David och jag är idrotts läraren.

        Jag kommer ställa dig 5 olika frågor om idrott, om du svarar rätt på alla då får du gå iväg.
        Om du gör ett ända fel då måste kommer det blir riktgit dåligt för dig...

        '''
        stdscr.refresh()

        # Handle user input
        key = stdscr.getch()
        new_pos = player_pos.copy()

        if key == ord('q'):  # Quit the game
            break
        elif key == ord('w'):  # Move up
            new_pos[0] -= 1
        elif key == ord('s'):  # Move down
            new_pos[0] += 1
        elif key == ord('a'):  # Move left
            new_pos[1] -= 1
        elif key == ord('d'):  # Move right
            new_pos[1] += 1
        elif key == ord('i'):
            break
        
        # Validate movement
        if not (new_pos[0] == 0 or new_pos[0] == rows - 1 or 
                 new_pos[1] == 0 or new_pos[1] == cols - 1) and new_pos not in block_pos:
            player_pos = new_pos

        # Check for goal and special positions
        if player_pos == Lärar_pos:
            if teacher5.health == 0 or input_d == 5:
                player_pos = [12, 7]
                message = ("David är död")
            else:
                stdscr.clear()
                os.system('cls' if os.name == 'nt' else 'clear')
                curses.endwin()
                player_pos = [12, 7]
                davidquestion()
            
        elif player_pos in door_pos:
            transition_to("hallway2")
            break

###############################################################################
#Room 6
def room6(stdscr, transition_to):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking getch
    stdscr.timeout(20000) # Input timeout (ms)

    # Game variables
    rows, cols = 25, 45  # Game board dimensions
    player_pos = [12, 37]  # Player's starting position
    block_pos = []   # Block positions
    Lärar_pos = [12, 3]      # Goal position
    door_pos = [[13, 41], [12, 42], [11, 43]]

    key = None           # Key press tracker
    message = ""

    while True:
        # Draw game board
        stdscr.clear()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    stdscr.addch(r, c, '#')  # Wall
                elif [r, c] in door_pos:
                    stdscr.addch(r, c, '/')
                elif [r, c] in block_pos:
                    stdscr.addch(r, c, 'B')  # Block
                elif [r, c] == Lärar_pos:
                    stdscr.addch(r, c, 'X')  # Goal
                elif [r, c] == player_pos:
                    stdscr.addch(r, c, 'O')  # Player
                else:
                    stdscr.addch(r, c, ' ')  # Empty space

        # Display the message
        stdscr.addstr(rows, 0, f"Message: {message}")
        message = '''
        Mirella rum

        Hej, jag heter Mirella och jag är en dator och nätwerks teknik lärare.

        Jag kommer ställa dig 5 olika frågor, om du svarar rätt på alla då får du gå iväg.
        Om du gör ett ända fel då ska jag krasha din dator. 
        '''
        stdscr.refresh()

        # Handle user input
        key = stdscr.getch()
        new_pos = player_pos.copy()

        if key == ord('q'):  # Quit the game
            break
        elif key == ord('w'):  # Move up
            new_pos[0] -= 1
        elif key == ord('s'):  # Move down
            new_pos[0] += 1
        elif key == ord('a'):  # Move left
            new_pos[1] -= 1
        elif key == ord('d'):  # Move right
            new_pos[1] += 1
        elif key == ord('i'):
            break
        
        # Validate movement
        if not (new_pos[0] == 0 or new_pos[0] == rows - 1 or 
                 new_pos[1] == 0 or new_pos[1] == cols - 1) and new_pos not in block_pos:
            player_pos = new_pos

        # Check for goal and special positions
        if player_pos == Lärar_pos:
            if teacher6.health == 0 or input_m == 5:
                player_pos = [12, 37]
                message = ("Mirrela är död")
            else:
                stdscr.clear()
                os.system('cls' if os.name == 'nt' else 'clear')
                curses.endwin()
                player_pos = [12, 37]
                mirrelaquestion()
        elif player_pos in door_pos:
            transition_to("hallway2")
            break

###############################################################################
#Chest Room
def Chestroom(stdscr, transition_to):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking getch
    stdscr.timeout(20000) # Input timeout (ms)

    # Game variables
    rows, cols = 25, 45  # Game board dimensions
    player_pos = [2, 22]  # Player's starting position
    block_pos = [[23, 21], [22, 21], [21, 21], [12, 43], [12, 42], [12, 41], [12, 40], [12, 39], [12, 1], [12, 2], [12, 3], [12, 4], [12, 5]]   # Block positions
    Chest_pos1 = [21, 11] # Chest position
    Chest_pos2 = [21, 33]
    door_pos = [[1, 19], [1, 20], [1, 21], [1, 22], [1, 23], [1, 24], [1, 25]]

    key = None           # Key press tracker
    

    while True:
        # Draw game board
        stdscr.clear()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    stdscr.addch(r, c, '#')  # Wall
                elif [r, c] in door_pos:
                    stdscr.addch(r, c, '-')
                elif [r, c] in block_pos:
                    stdscr.addch(r, c, '#')  # Block
                elif [r, c] == Chest_pos1:
                    stdscr.addch(r, c, 'N')  # normal chest
                elif [r, c] == Chest_pos2:
                    stdscr.addch(r, c, 'E')  # Epic chest
                elif [r, c] == player_pos:
                    stdscr.addch(r, c, 'O')  # Player
                else:
                    stdscr.addch(r, c, ' ')  # Empty space

        # Display the message
        message = 'ChestRoom'
        stdscr.addstr(0, cols, f"Message: {message}")
        
        stdscr.refresh()

        stdscr.addstr(rows, 0, 'Normal chest')
        stdscr.addstr(rows, 21, 'Epic chest')
        # Handle user input
        key = stdscr.getch()
        new_pos = player_pos.copy()

        if key == ord('q'):  # Quit the game
            break
        elif key == ord('w'):  # Move up
            new_pos[0] -= 1
        elif key == ord('s'):  # Move down
            new_pos[0] += 1
        elif key == ord('a'):  # Move left
            new_pos[1] -= 1
        elif key == ord('d'):  # Move right
            new_pos[1] += 1
        elif key == ord('i'):
            break
        
        # Validate movement
        if not (new_pos[0] == 0 or new_pos[0] == rows - 1 or 
                 new_pos[1] == 0 or new_pos[1] == cols - 1) and new_pos not in block_pos:
            player_pos = new_pos

        # Check for goal and special positions
        if player_pos == Chest_pos1:
            stdscr.clear()
            os.system('cls' if os.name == 'nt' else 'clear')
            curses.endwin()
            player_pos = [2, 22]
            lootbox_normal()
            
            
        elif player_pos == Chest_pos2:
            stdscr.clear()
            os.system('cls' if os.name == 'nt' else 'clear')
            curses.endwin()
            player_pos = [2, 22]
            lootbox_epic()
            
        elif player_pos in door_pos:
            transition_to("hallway2")
            
        
###############################################################################
#Lars Boss Room
def Larsboss(stdscr, transition_to):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking getch
    stdscr.timeout(20000) # Input timeout (ms)

    # Game variables
    rows, cols = 25, 45  # Game board dimensions
    player_pos = [12, 37]  # Player's starting position
    block_pos = []   # Block positions
    Lärar_pos = [12, 3]      # Goal position
    door_pos = [[13, 41], [12, 42], [11, 43]]

    key = None           # Key press tracker
    message = ""

    while True:
        # Draw game board
        stdscr.clear()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    stdscr.addch(r, c, '#')  # Wall
                elif [r, c] in door_pos:
                    stdscr.addch(r, c, '/')
                elif [r, c] in block_pos:
                    stdscr.addch(r, c, 'B')  # Block
                elif [r, c] == Lärar_pos:
                    stdscr.addch(r, c, 'X')  # Goal
                elif [r, c] == player_pos:
                    stdscr.addch(r, c, 'O')  # Player
                else:
                    stdscr.addch(r, c, ' ')  # Empty space

        # Display the message
        stdscr.addstr(rows, 0, f"Message: {message}")
        message = '''
        Lars boss rum

        Hello there, jag heter Lars men folk brukar kalla mig Mr aura eller Albert Einstein

        Jag är den bästa läraren någonsin, min kunskapnivå är obeskrivligt och jag har mystiskt aura.
        Min skalle är så slät att de reflekterar allt som matte, fysik och mycket mer.
        Jag kommer ställa dig fem frågor också fast denna gången du kan inte åka iväg så lätt.

        Det kommer blir roligt hehe...

        '''
        stdscr.refresh()

        # Handle user input
        key = stdscr.getch()
        new_pos = player_pos.copy()

        if key == ord('q'):  # Quit the game
            break
        elif key == ord('w'):  # Move up
            new_pos[0] -= 1
        elif key == ord('s'):  # Move down
            new_pos[0] += 1
        elif key == ord('a'):  # Move left
            new_pos[1] -= 1
        elif key == ord('d'):  # Move right
            new_pos[1] += 1
        elif key == ord('i'):
            break
        
        # Validate movement
        if not (new_pos[0] == 0 or new_pos[0] == rows - 1 or 
                 new_pos[1] == 0 or new_pos[1] == cols - 1) and new_pos not in block_pos:
            player_pos = new_pos

        # Check for goal and special positions
        if player_pos == Lärar_pos:
            if boss.health == 0:
                player_pos = [12, 37]
                message = ("Lars är död")
            else:
                stdscr.clear()
                os.system('cls' if os.name == 'nt' else 'clear')
                curses.endwin()
                player_pos = [12, 37]
                larsquestion()
        elif player_pos in door_pos:
            transition_to("hallway2")
            break
        
###############################################################################
#Hallway 2
def Hallway2(stdscr, transition_to):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking getch
    stdscr.timeout(20000) # Input timeout (ms)

    # Game variables
    rows, cols = 15, 100  # Game board dimensions
    player_pos = [12, 23]  # Player's starting position
    block_pos = []   # Block positions
    door_pos = [[13, 20], [13, 21], [13, 22], [13, 23], [13, 24], [13, 25], [13, 26]]
    door_pos2 = [[7, 97], [8, 96], [6, 98]]
    door_pos3 = [[13, 80], [13, 79], [13, 78], [13, 77], [13, 76], [13, 75], [13, 74]]
    door_pos4 = [[1, 80], [1, 79], [1, 78], [1, 77], [1, 76], [1, 75], [1, 74]]
    door_pos5 = [[1, 20], [1, 21], [1, 22], [1, 23], [1, 23], [1, 24], [1, 25], [1, 26]]
    Larsboss_pos =[[7, 2], [8, 1], [6, 3]]
    key = None           # Key press tracker
    message = 'Hallway2'

    while True:
        # Draw game board
        stdscr.clear()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    stdscr.addch(r, c, '#')  # Wall
                elif [r, c] in door_pos:
                    stdscr.addch(r, c, '-')
                elif [r, c] in door_pos2:
                    stdscr.addch(r, c, '/')
                elif [r, c] in door_pos3:
                    stdscr.addch(r, c, '-')
                elif [r, c] in door_pos4:
                    stdscr.addch(r, c, '-')
                elif [r, c] in door_pos5:
                    stdscr.addch(r, c, '-')
                elif [r, c] in Larsboss_pos:
                    stdscr.addch(r, c, '/')
                elif [r, c] in block_pos:
                    stdscr.addch(r, c, 'B')  # Block
                elif [r, c] == player_pos:
                    stdscr.addch(r, c, 'O')  # Player
                else:
                    stdscr.addch(r, c, ' ')  # Empty space

        # Display the message
        stdscr.addstr(rows, 0, f"Room: {message}")
        stdscr.addstr(rows, 0, f"status: {status()}", curses.A_BOLD)
        stdscr.refresh()

        # Handle user input
        key = stdscr.getch()
        new_pos = player_pos.copy()

        if key == ord('q'):  # Quit the game
            break
        elif key == ord('w'):  # Move up
            new_pos[0] -= 1
        elif key == ord('s'):  # Move down
            new_pos[0] += 1
        elif key == ord('a'):  # Move left
            new_pos[1] -= 1
        elif key == ord('d'):  # Move right
            new_pos[1] += 1
        elif key == ord('i'):
            break
        
        # Validate movement
        if not (new_pos[0] == 0 or new_pos[0] == rows - 1 or 
                 new_pos[1] == 0 or new_pos[1] == cols - 1) and new_pos not in block_pos:
            player_pos = new_pos

        # Check for goal and special positions
        if player_pos in door_pos:
            transition_to('main')
            break
        elif player_pos in door_pos2:
            transition_to('room5')
            break
        elif player_pos in door_pos3:
            transition_to('Chestroom')
            break
        elif player_pos in door_pos4:
            transition_to('room6')
            break
        elif player_pos in door_pos5:
            stdscr.clear()
            os.system('cls' if os.name == 'nt' else 'clear')
            curses.endwin()
            player_pos = [12, 23]
            exit_door()
        elif player_pos in Larsboss_pos:
            stdscr.clear()
            os.system('cls' if os.name == 'nt' else 'clear')
            curses.endwin()
            player_pos = [12, 23]
            lars_door()
            
        
###############################################################################
#Hallway 1
def main(stdscr, transiton_to):
    # Initialize curses
    curses.initscr()
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking getch
    stdscr.timeout(20000) # Input timeout (ms)

    # Game variables
    rows, cols = 35, 35  # Game board dimensions
    player_pos = [31, 16]  # Player's starting positio      
    door_pos = [[11, 1], [10, 2], [9, 3]]
    door_pos2 = [[1, 19], [1, 18], [1, 17], [1, 16], [1, 15], [1, 14], [1, 13]]
    door_pos3 = [[27, 1], [26, 2], [25, 3]]
    door_pos4 = [[11, 31], [10, 32], [9, 33]]
    door_pos5 = [[27, 31], [26, 32], [25, 33]]
    key = None           # Key press tracker
    message = 'Main room'

    while True:
        # Draw game board
        stdscr.clear()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    stdscr.addch(r, c, '#')  # Wall
                elif [r, c] in door_pos:
                    stdscr.addch(r, c, '/')
                elif [r, c] in door_pos2:
                    stdscr.addch(r, c, '-')
                elif [r, c] in door_pos3:
                    stdscr.addch(r, c, '/')
                elif [r, c] in door_pos4:
                    stdscr.addch(r, c, '/')
                elif [r, c] in door_pos5:
                    stdscr.addch(r, c, '/')
                elif [r, c] == player_pos:
                    stdscr.addch(r, c, 'O')  # Player
                else:
                    stdscr.addch(r, c, ' ')  # Empty space

        # Display the message
        stdscr.addstr(0, cols, f"Room: {message}")
        stdscr.addstr(rows, 0, f"status: {status()}", curses.A_BOLD)
        stdscr.refresh()


        # Handle user input
        key = stdscr.getch()
        new_pos = player_pos.copy()

        if key == ord('q'):  # Quit the game
            break
        elif key == ord('w'):  # Move up
            new_pos[0] -= 1
        elif key == ord('s'):  # Move down
            new_pos[0] += 1
        elif key == ord('a'):  # Move left
            new_pos[1] -= 1
        elif key == ord('d'):  # Move right
            new_pos[1] += 1
        elif key == ord('i'): # inventory
            break #ta bork break och lägg in befinitionen för inventory
        
        # Validate movement
        if not (new_pos[0] == 0 or new_pos[0] == rows - 1 or 
                 new_pos[1] == 0 or new_pos[1] == cols - 1):
            player_pos = new_pos

        # Check for goal and special position
        if player_pos in door_pos:
            transiton_to('room2')  #room 2
            break
        elif player_pos in door_pos2:
            transiton_to('hallway2') #Halway
            break
        elif player_pos in door_pos3:
            transiton_to("room1") #room 1
            break
        elif player_pos in door_pos4:
            transiton_to('room4') #room 4
            break
        elif player_pos in door_pos5:
            transiton_to('room3') #room 3
            break

###############################################################################
#def libriary

def entry_point(stdscr):

    ROOMS = {
        'main': main,
        'room1': room1,
        'room2': room2,
        'room3': room3,
        'room4': room4,
        'room5': room5,
        'room6': room6,
        'Larsboss': Larsboss,
        'Chestroom': Chestroom,
        'hallway2': Hallway2,
        
        
    }

    def transition_to(room_name):
        if room_name in ROOMS:
            ROOMS[room_name](stdscr, transition_to)

    # Start the game in the main room
    transition_to('main')


if __name__ == "__main__":
    curses.wrapper(entry_point)