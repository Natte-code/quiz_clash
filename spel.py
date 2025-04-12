import random
import curses
import time
import os
import threading
from typing import Union
from colorama   import Fore, Style


#Def av några sid funktioner som kallas på igenom spelet
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


#Denna ska ändras på om spelaren gör något med en lärare och ska då också kollas om den är 1 eller mer då kan spelaren får ett slut.
teacher_interaction = 0
#Också, kom på hela denna helt idén själv. fick ingen AI hjälp.



#Du glömde att sätta in den för minus epic potion 


#kod skaffad från Chatgpt och används för att insperara denna kod.
####################################################################################################
# Loggan definierad som en lista av strängar


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
                Öppna lådor för att få nya vapen och potions. (rummet finns i andra rummet till höger)
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
skibidi = Sword("Skibidi", 15230489572938759283750) #debug
träsvärd = Sword("Träsvärd", 10)

class Character:   
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.coins = 5 #debug
        self.totems = 0 #debug
        self.shields = 1
        self.antal_potion_vanlig = 2 #debug
        self.antal_potion_epic = 1 #debug
        self.inventory = {
            "swords": {sword.name: sword.damage for sword in [träsvärd,]},
            "potions": {
                "normal": self.antal_potion_vanlig,
                "epic": self.antal_potion_epic
            }
        }
        self.last_heal = 0

    def add_sword_to_inventory(self, sword):
        if sword.name not in self.inventory["swords"]:
            self.inventory["swords"][sword.name] = sword.damage
            print_success(f"Du har låst upp {sword.name.capitalize()}!")
        else:
            print_error(f"Du har redan {sword.name.capitalize()} i inventoryt.")



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


        


    def add_coins(self, amount): #Vart används ens denna? - nathaniel
        self.coins += amount
        print(f"Earned {amount} coins! Total: {self.coins}")



    def add_coins_random(self, amount):
        random.randint(amount)
        player.coins += amount
        print(f"Du fick {amount} coins")
 


class Boss:
    def __init__(self, name, health, min_damage, max_damage, regen):
        self.name = name
        self.health = health
        self.max_health = health
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.regen = regen
        self.is_regen = False
        self.regen_thread = None  # Track the thread

    def start_regen(self):
        if not self.is_regen:
            self.is_regen = True
            self.regen_thread = threading.Thread(target=self.regenerate_health, daemon=True)
            self.regen_thread.start()

    def regenerate_health(self):
        while self.is_regen and self.health > 0:
            time.sleep(17.5)
            self.health = min(self.max_health, self.health + self.regen)
            print(f"\nBOSS REGENERATES +{self.regen} HP!")

    def stop_regen(self):
        self.is_regen = False
        if self.regen_thread:
            self.regen_thread.join()  # Ensure thread cleanup

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

#Union är OR-gate bassicly -Felix söndag 2025-02-16 21:39 
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
            print("Tip: Go and open a chest in the chest room. \n Normal chests: 5 coins. Epic 15.")
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
            end1()
            return False

        time.sleep(2)



teacher1 = Teacher(name="johanna", health=100, min_damage=1, max_damage=10)
teacher2 = Teacher(name="Ronja", health=110, min_damage=5, max_damage=15)
teacher3 = Teacher(name="Henrik", health=125, min_damage=8, max_damage=18)
teacher4 = Teacher(name="Victor", health=135, min_damage=1, max_damage=13)
teacher5 = Teacher(name="David", health=150, min_damage=9, max_damage=20)
teacher6 = Teacher(name="Mirrela", health=200, min_damage=11, max_damage=25)

final_boss = Boss("Lars", 500, 20, 50, 20)
player = Character(player_name, 100)

# combat_loop(player, final_boss )


#Bugg 1, Lars kan regena efter han är död, Hur fan. #löst
#Bugg 2, Input saken av spelaren kan brytas när lars får en regen. Texten överskriver spelarens input, Men spelaren kan fortfarande skriva in


#Kod optimized av Deepseek r1. 
#--------------------------------------------------------------------------



# Anta att Player-klassen och Sword-klassen redan finns



# -----------------------------------------------------------------------------
# Hjälpfunktioner för färger och bekräftelse
# -----------------------------------------------------------------------------
def print_success(message):
    print(Fore.GREEN + "★ " + message + " ★" + Style.RESET_ALL)

def print_error(message):
    print(Fore.RED + "✘ " + message + " ✘" + Style.RESET_ALL)

def confirm_purchase(cost, box_type):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Vill du öppna en {box_type} lootbox för {cost} coins? (ja/nej)")
    choice = input("> ").lower()
    return choice == "ja"

# -----------------------------------------------------------------------------
# Lootbox-systemet
# -----------------------------------------------------------------------------
def open_lootbox(lootpool, cost, box_type):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if player.coins < cost:
        print_error(f"Du behöver {cost} coins för en {box_type} lootbox!")
        time.sleep(2)
        return

    player.coins -= cost
    chosen_item = random.choice(list(lootpool.keys()))
    lootpool[chosen_item]()  # Kör funktionen för det valda itemet

    # Hantera utskrift
    if "_potion" in chosen_item:
        potion_type = chosen_item.split("_")[0]
        print_success(f"Du fick 1 {potion_type} potion! Totalt: {getattr(player, f'antal_potion_{potion_type}')}")
    else:
        print_success(f"Du fick {chosen_item.capitalize()}!")
    
    time.sleep(2)

# ----------------------------------------------------------------------------- ######INTE KLAR##########
# Definiera lootpools och Sword-instanser
# -----------------------------------------------------------------------------
# Skapa Sword-instanser (exempel, justera efter ditt spel)

lootpool_normal = {
    "kukri": lambda: player.add_sword_to_inventory(Kukri),
    "järnsvärd": lambda: player.add_sword_to_inventory(järnsvärd),
    "normal_potion": lambda: setattr(player, 'antal_potion_vanlig', player.antal_potion_vanlig + 1),
    "katana": lambda: player.add_sword_to_inventory(katana),
    "dagger": lambda: player.add_sword_to_inventory(Dagger),
    "pinne": lambda: player.add_sword_to_inventory(Pinne),
}

lootpool_epic = {
    "epic_potion": lambda: setattr(player, 'antal_potion_epic', player.antal_potion_epic + 1),
    "battle_axe": lambda: player.add_sword_to_inventory(battle_axe),
    "totem": lambda: setattr(player, 'totems', player.totems + 1),
    "lightsaber": lambda: player.add_sword_to_inventory(lightsaber),
    "stekpanna": lambda: player.add_sword_to_inventory(stekpanna),
}

# -----------------------------------------------------------------------------
# Exempel på användning
# -----------------------------------------------------------------------------



###########################################################################
#där skrivs alla frågor för lärare
#alla lärare har sin egen definition med 20 frågor, bara 5 av de är plockad för varje lärare
#den kod är skriven av eliot


# starta frågorna

#johanna
def johannaquestion():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Hur bra är du på matte då?")
    time.sleep(2)

    os.system('cls' if os.name == 'nt' else 'clear')
    # Olika frågor och rätta svar
    global input_j
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
    teacher_interaction += 1
    if teacher1.health >= 0:  # Prevent infinite loop by checking if health is greater than 0
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
                time.sleep(1)
                combat_loop(player, teacher1)
                break

        if input_j == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Du va bra på matte, kull för dig")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            player.add_coins_random(15)
            teacher1.health == 0
            curses.initscr()
     
        
#ronja
def ronjaquestion():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("How god in english?")
    time.sleep(2)

    os.system('cls' if os.name == 'nt' else 'clear')

    global input_r
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
    teacher_interaction += 1
    if teacher2.health >= 0:  # Prevent infinite loop by checking if health is greater than 0
        for i, (question, correct_answer) in enumerate(selected_questions, start=1):
            print(f"Fråga {i}: {question}")
            answer = input("Ditt svar: ").strip().lower()

            if answer == correct_answer.lower():
                print("Rätt!\n")
                input_r = input_r + 1
            else:
                # Spelaren går in i fight
                print(f"Wrong!")
                print("Thats the wrong anser, now DIE")
                time.sleep(2)
                combat_loop(player, teacher2)
                break
        if input_r == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Wow, Your english is impressive. Move on")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            player.add_coins_random(15)
            teacher2.health == 0
            curses.initscr()


#henrik
def henrikquestion():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Hur bra på fysik är du?")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    global input_h
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
    teacher_interaction += 1
    if teacher3.health >= 0:  # Prevent infinite loop by checking if health is greater than 0
        for i, (question, correct_answer) in enumerate(selected_questions, start=1):
            print(f"Fråga {i}: {question}")
            answer = input("Ditt svar: ").strip().lower()

            if answer == correct_answer.lower():
                print("Rätt!\n")
                input_h = input_h + 1
            else:
                # Spelaren går in i fight
                print(f"Fel!")
                print("sämst, va dålig du va på fysik då, Nu ska du dö för det!")
                time.sleep(2)
                combat_loop(player, teacher3)
                break

        if input_h == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Du kunde fysik asså, bra gjort!")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            player.add_coins_random(15)
            teacher3.health == 0
            curses.initscr()
        

#Victor
def vicorquestion():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Kan du svara på mina matte frågor?")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    global input_v
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
    teacher_interaction += 1
    if teacher4.health >= 0:  # Prevent infinite loop by checking if health is greater than 0
        for i, (question, correct_answer) in enumerate(selected_questions, start=1):
            print(f"Fråga {i}: {question}")
            answer = input("Ditt svar: ").strip().lower()

            if answer == correct_answer.lower():
                print("Rätt!\n")
                input_v = input_v + 1
            else:
                # Spelaren går in i fight
                print(f"Fel!")
                print("Så du är dålig på matte, det var dåligt för dig då! >:)")
                time.sleep(2)
                combat_loop(player, teacher4)
                break
        if input_v == 5:
            print("jäklar, du var bra på matte då. aja du besegrade mig. ha det bra unge man.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            player.add_coins_random(15)
            teacher4.health == 0
            curses.initscr()
            

#David
def davidquestion():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Tjena, kan du svara rätt på mina idrotts frågot?")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    global input_d
    input_d = 1 #Denna ska användas för att kolla om spelaren har interactat, men när den kallas på är den inte definerad än?
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
    teacher_interaction += 1
    if teacher5.health >= 0:  # Prevent infinite loop by checking if health is greater than 0
        for i, (question, correct_answer) in enumerate(selected_questions, start=1):
            print(f"Fråga {i}: {question}")
            answer = input("Ditt svar: ").strip().lower()

            if answer == correct_answer.lower():
                print("Rätt!\n")
                input_d = input_d + 1
            else:
                # Spelaren går in i fight
                print(f"Fel!")
                print("Men ojojoj, Du hade fel. Du vet nog vad som händer nu.")
                time.sleep(2)
                combat_loop(player, teacher5)
                break
        if input_d == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Du är bra på idrott, det ger dig ett sort A min unge gosse. Ha det bra nu :)")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            player.add_coins_random(15)
            teacher5.health == 0
            curses.initscr()
        
            
#Mirrela
def mirrelaquestion():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Hur bra är du på datorer?")
    time.sleep(2) 
    os.system('cls' if os.name == 'nt' else 'clear')
    
    global input_m
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
    teacher_interaction += 1
    if teacher6.health >= 0:  # Prevent infinite loop by checking if health is greater than 0, FÖR FAN ANVÄND >= ISTÄLLET FÖR >
        for i, (question, correct_answer) in enumerate(selected_questions, start=1):
            print(f"Fråga {i}: {question}")
            answer = input("Ditt svar: ").strip().lower()

            if answer == correct_answer.lower():
                print("Rätt!\n")
                input_m = input_m + 1
            else:
                # Spelaren går in i fight
                print(f"Fel!")
                print("Du hade fel, nu ska vi slås!")
                time.sleep(2)
                combat_loop(player, teacher6)
                break
        if input_m == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Du kan dina datorer du, gå vidare nu med din kunskap.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            player.add_coins_random(15)
            teacher6.health == 0
            curses.initscr()


#Lars boss
def larsquestion():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("""Så du har besegrat alla andra lärare. Men du kommer att in se att jag inte är lätt att slå.
    Jag är nog du kommer ha svårats för att möta. Så nu ska vi se om du kan svara på mina frågor! >:)""")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
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
            print("""HAHAHHAHAHA, jag viste att du inte skulle kunna svara på mina frågor. Nu vet du nog vad som händer.
            Du kommer alrdig att vinna min fight! 
            SÅ DÖ!!! >:)""")
            time.sleep(3)
            combat_loop(player, final_boss)
            break
    if inputl == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Hur kunde du svara på alla mina frågor. Ingen har någonsin kunnat göra det.")
        time.sleep(2)
        print("Aja, du ska dö ändå din homosexuela jävel! >:)")
        time.sleep(2)
        combat_loop(player, final_boss)
        

# ändrade så att status saken funkade bättre med hjälp av AI

def status():
    
    teachers = [teacher1, teacher2, teacher3, teacher4, teacher5, teacher6]
    
    if all(t.health <= 0 for t in teachers) and final_boss.health <= 0:
        return "Alla lärare och Lars är besegrade!"
    elif all(t.health <= 0 for t in teachers):
        return "Du har bara Lars kvar nu!"
    else:
        
        status_msg = "Lärare hälsostatus:\n"
        for t in teachers:
            status_msg += f"{t.name}: {'Besegrad' if t.health <= 0 else 'Levande'}\n"
        status_msg += f"Lars: {'Besegrad' if final_boss.health <= 0 else 'Levande'}"
        return status_msg



def inventorystats():
    return (f"""Player: {player_name}\nHealth: {player.health}\nCoins: {player.coins}\n"""
            f"""Totems: {player.totems}\nInventory: {player.inventory}\n""")   

#lars.skibidi


# Denna göra så att man inte kan komma in i lars rum om lärare lever
def lars_door(transition_to, stdscr):
    os.system('cls' if os.name == 'nt' else 'clear')
    if all(teacher.health <= 0 for teacher in [teacher1, teacher2, teacher3, teacher4, teacher5, teacher6]):
        os.system('cls' if os.name == 'nt' else 'clear')
        curses.initscr()
        Larsboss(stdscr, transition_to)
    else:
        print("Dörren till Lars rum är stängd.")
        print("Besegra alla lärare innan du kan komma igenom!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        curses.initscr()

#spelaren ska få coins av att defeata läraren


#kod skaffad från Chatgpt och används för att insperara denna kod.
####################################################################################################


##################################
def end1():
    clear_screen()
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
    clear_screen()
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
    clear_screen()
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
    clear_screen()
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
    input("Press ENTER to exit...")
    exit()
#------------------------------------------------------------------------





#pangs baguette kod

# #Ska göra kod här som kollar om spelaren ens har gjort något med läraren eller inte, om dem inte har ska han inte kunna få något av dessa
# def val_av_end():
    
#     if all(teacher.health <= 0 for teacher in [teacher1, teacher2, teacher3, teacher4, teacher5, teacher6]) and final_boss.health > 0:
#         end3()  # Afraid ending
#     elif all(teacher.health == 100 for teacher in [teacher1, teacher2, teacher3, teacher4, teacher5, teacher6]) and final_boss.health == 500:
#         end4()  # Pacifist ending
#     elif all(teacher.health <= 0 for teacher in [teacher1, teacher2, teacher3, teacher4, teacher5, teacher6]) and final_boss.health <= 0:
#         end2()  # Good ending

    #används ju för fan inte ens. Då försvinner ännu mer av pang pangs kod. Förlåt men skriv bättre kod pls



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
    message = '''
        Johannas rum

        Hej, jag heter Johanna och jag är en matte lärare.

        Jag kommer ställa dig 5 olika frågor, om du svarar rätt på alla då får du gå iväg.
        Om du gör ett ända fel då kommer det blir kaos för dig.

        Hehe
        '''

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
        stats = inventorystats()
        stats_lines = stats.strip().split('\n')  # Split stats into lines
        for i, line in enumerate(stats_lines):
            stdscr.addstr(i, cols + 2, line) 
        # Display the message
        stdscr.addstr(rows, 0, f"Message: {message}")
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
            if teacher1.health <= 0:
                player_pos = [12, 37]
                message = ("Johanna är besegrad")
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
    message ='''
        Ronja rum

        Hi my name is Ronja, I am a english/swedish teatcher.

        I am going to ask you 5 question, if you answer correct to all of them you can leave.
        If you do one single mistake this is going to be really bad for you.

        Let's go!
        '''

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

        stats = inventorystats()
        stats_lines = stats.strip().split('\n')  # Split stats into lines
        for i, line in enumerate(stats_lines):
            stdscr.addstr(i, cols + 2, line) 
        # Display the message
        stdscr.addstr(rows, 0, f"Message: {message}")
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
            if teacher2.health <= 0:
                player_pos = [12, 37]
                message = ("Ronja är besegrad")
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
    message = '''
        Henrik rum

        Hej, jag heter Henrik och jag är en matte och fysik lärare.

        Jag kommer ställa dig 5 olika frågor, om du svarar rätt på alla då får du gå iväg.
        Om du gör ett ända fel då kommer det blir  för dig.

        Hehe
        '''

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

        stats = inventorystats()
        stats_lines = stats.strip().split('\n')  # Split stats into lines
        for i, line in enumerate(stats_lines):
            stdscr.addstr(i, cols + 2, line)
        # Display the message
        stdscr.addstr(rows, 0, f"Message: {message}")
        
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
            if teacher3.health <= 0:
                player_pos = [12, 37]
                message = ("Henrik är besegrad")
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
    message = '''
        Victor rum

        Hej, jag heter Victor och jag är en matte lärare.

        Jag kommer ställa dig 5 olika frågor om logisk tänkande, om du svarar rätt på alla då får du gå iväg.
        Om du gör ett ända fel då kommer det blir.... du vill inte veta hehehe.

        '''

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

        stats = inventorystats()
        stats_lines = stats.strip().split('\n')  # Split stats into lines
        for i, line in enumerate(stats_lines):
            stdscr.addstr(i, cols + 2, line) 
        # Display the message
        stdscr.addstr(rows, 0, f"Message: {message}")
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
            if teacher4.health <= 0:
                player_pos = [12, 7]
                message = ("Victor är besegrad")
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
    message = '''
        David rum

        Hej, jag heter David och jag är idrotts läraren.

        Jag kommer ställa dig 5 olika frågor om idrott, om du svarar rätt på alla då får du gå iväg.
        Om du gör ett ända fel då måste kommer det blir riktgit dåligt för dig...

        '''

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


        stats = inventorystats()
        stats_lines = stats.strip().split('\n')  # Split stats into lines
        for i, line in enumerate(stats_lines):
            stdscr.addstr(i, cols + 2, line) 
        # Display the message
        stdscr.addstr(rows, 0, f"Message: {message}")
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
            if teacher5.health <= 0:

                player_pos = [12, 7]
                message = ("David är besegrad")
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
    curses.curs_set(0)
    stdscr.nodelay(1)   
    stdscr.timeout(100) # Reduced from 20000 to 100ms for more responsive input
    stdscr.keypad(1)    # Enable keypad for arrow keys

    # Game variables
    rows, cols = 25, 45  # Game board dimensions
    player_pos = [21, 20]  # Player's starting position
    block_pos = []   # Block positions
    Lärar_pos = [3, 20]      # Goal position
    door_pos = [[23, 17], [23, 18], [23, 19], [23, 20], [23, 21], [23, 22], [23, 23]]

    key = None           # Key press tracker
    message = '''
        Mirella rum

        Hej, jag heter Mirella och jag är en dator och nätverks teknik lärare.

        Jag kommer ställa dig 5 olika frågor, om du svarar rätt på alla då får du gå iväg.
        Om du gör ett ända fel då ska jag krasha din dator. 
        '''

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
                    stdscr.addch(r, c, 'B')  # Block
                elif [r, c] == Lärar_pos:
                    stdscr.addch(r, c, 'X')  # Goal
                elif [r, c] == player_pos:
                    stdscr.addch(r, c, 'O')  # Player
                else:
                    stdscr.addch(r, c, ' ')  # Empty space


        stats = inventorystats()
        stats_lines = stats.strip().split('\n')  # Split stats into lines
        for i, line in enumerate(stats_lines):
            stdscr.addstr(i, cols + 2, line) 
        # Display the message
        stdscr.addstr(rows, 0, f"Message: {message}")
        stdscr.refresh()

        # Handle user input
        try:
            key = stdscr.getch()
            new_pos = player_pos.copy()

            if key == ord('q'):
                break
            elif key in [ord('w'), curses.KEY_UP]:
                new_pos[0] -= 1
            elif key in [ord('s'), curses.KEY_DOWN]:
                new_pos[0] += 1
            elif key in [ord('a'), curses.KEY_LEFT]:
                new_pos[1] -= 1
            elif key in [ord('d'), curses.KEY_RIGHT]:
                new_pos[1] += 1

            # Validate movement
            if (0 < new_pos[0] < rows-1 and 
                0 < new_pos[1] < cols-1 and 
                new_pos not in block_pos):
                player_pos = new_pos

        except curses.error:
            continue

        # Check for goal and special positions
        if player_pos == Lärar_pos:
            if teacher6.health <= 0:
                player_pos = [12, 37]
                message = ("Mirrela är besegrad")
            else:
                stdscr.clear()
                os.system('cls' if os.name == 'nt' else 'clear')
                curses.endwin()
                player_pos = [21, 20]
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


        stats = inventorystats()
        stats_lines = stats.strip().split('\n')  # Split stats into lines
        for i, line in enumerate(stats_lines):
            stdscr.addstr(i, cols + 2, line) 
        # Display the message
        message = 'ChestRoom'

        stdscr.addstr(0, cols+2, f"Message: {message}")
        
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
            open_lootbox(cost=5, box_type=lootpool_normal, lootpool=lootpool_normal)
            
            
        elif player_pos == Chest_pos2:
            stdscr.clear()
            os.system('cls' if os.name == 'nt' else 'clear')
            curses.endwin()
            player_pos = [2, 22]
            open_lootbox(cost=15, box_type=lootpool_epic, lootpool=lootpool_epic)
            
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
    message = '''
        Lars boss rum

        Hello there, jag heter Lars men folk brukar kalla mig Mr aura eller Albert Einstein

        Jag är den bästa läraren någonsin, min kunskapnivå är obeskrivligt och jag har mystiskt aura.
        Min skalle är så slät att de reflekterar allt som matte, fysik och mycket mer.
        Jag kommer ställa dig fem frågor också fast denna gången du kan inte åka iväg så lätt.

        Det kommer blir roligt hehe...

        '''

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


        stats = inventorystats()
        stats_lines = stats.strip().split('\n')  # Split stats into lines
        for i, line in enumerate(stats_lines):
            stdscr.addstr(i, cols + 2, line) 
        # Display the message
        stdscr.addstr(rows, 0, f"Message: {message}")
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
            if final_boss.health == 0:
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
#Fan vad jag hatar pythons läsa rad för rad stil. FUCK
def exit_door():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
            print("""Vill du lämna skolan eller stanna kvar?:
1. Lämna
2. Stanna
""")
            try:
                svar = int(input("1 eller 2: "))
                if svar == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if teacher_interaction == 0: #Koden ska nu kolla om du ens har gjort något innan den låter dig gå ut.
                        print("Du måste interagera med minst en lärare innan du kan avsluta spelet!")
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        curses.initscr()
                        break
                    elif all(teacher.health > 0 for teacher in [teacher1, teacher2, teacher3, teacher4, teacher5, teacher6]) and final_boss.health == 500:
                        end4()  # Pacifist ending: No fights, all questions answered correctly
                    elif all(teacher.health <= 0 for teacher in [teacher1, teacher2, teacher3, teacher4, teacher5, teacher6]) and final_boss.health == 500:
                        end3()  # Afraid ending: Flee without fighting Lars
                    else:
                        end1()  # Bad ending: You die
                    break
                elif svar == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    curses.initscr()
                    break
                else:
                    print("Ogiltigt val! Vänligen välj 1 eller 2.")
            except ValueError:
                print("Ogiltig inmatning! Vänligen skriv en siffra (1 eller 2).")
                time.sleep(1)





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
        stats = inventorystats()
        stats_lines = stats.strip().split('\n')  # Split stats into lines
        for i, line in enumerate(stats_lines):
            stdscr.addstr(i, cols + 2, line) 
        # Display the message
       
        stdscr.addstr(rows, 0, f"{status()}", curses.A_BOLD)
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
            lars_door(transition_to, stdscr)
            
        
###############################################################################
#Hallway 1
def main(stdscr, transiton_to):
        # Check terminal size
    max_y, max_x = stdscr.getmaxyx()
    required_y, required_x = 35, 65  # Minimum terminal size
    if max_y < required_y or max_x < required_x:
        stdscr.addstr(0, 0, "Terminal fönstret är för litet! gör det till big screen")
        stdscr.refresh()
        stdscr.getch()
        return
    # Initialize curses
    curses.initscr()
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking getch
    stdscr.timeout(20000) # Input timeout (ms)

    # Game variables
    rows, cols = 35, 35  # Game board dimensions
    player_pos = [31, 16]  # Player's starting positio      
    door_pos = [[11, 1], [9, 3]]
    door_pos2 = [[1, 19], [1, 18], [1, 17], [1, 16], [1, 15], [1, 14], [1, 13]]
    door_pos3 = [[27, 1], [25, 3]]
    door_pos4 = [[11, 31], [9, 33]]
    door_pos5 = [[27, 31],  [25, 33]]
    secret_pos = [[1, 1]] 
    one = [26, 2]
    two = [10, 2]
    tre = [10, 32]
    foure = [26, 32]
    key = None           # Key press tracker

    while True:
        # Draw game board
        stdscr.clear()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    stdscr.addch(r, c, '#')  # Wall
                elif [r, c] in door_pos:
                    stdscr.addch(r, c, '/')
                elif [r, c] == one:
                    stdscr.addch(r, c, '1')
                elif [r, c] in door_pos2:
                    stdscr.addch(r, c, '-')
                elif [r, c] == two:
                    stdscr.addch(r, c, '2')
                elif [r, c] in door_pos3:
                    stdscr.addch(r, c, '/')
                elif [r, c] == tre:
                    stdscr.addch(r, c, '3')
                elif [r, c] in door_pos4:
                    stdscr.addch(r, c, '/')
                elif [r, c] == foure:
                    stdscr.addch(r, c, '4')
                elif [r, c] in door_pos5:
                    stdscr.addch(r, c, '/')
                elif [r, c] == player_pos:
                    stdscr.addch(r, c, 'O')  # Player
                elif [r, c] in secret_pos:  
                    stdscr.addch(r, c, ' ')
                else:
                    stdscr.addch(r, c, ' ')  # Empty space

        # Display inventory stats
        stats = inventorystats()
        stats_lines = stats.strip().split('\n')  # Split stats into lines
        for i, line in enumerate(stats_lines):
            stdscr.addstr(i, cols + 2, line) 
        # Display the message
       
        stdscr.addstr(rows, 0, f"{status()}", curses.A_BOLD)
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
        elif player_pos in secret_pos:  # Check if player_pos matches any position in secret_pos
            player.health += 10  # Fix typo from 'heath' to 'health'
            try:
                os.startfile("lars.jpg")  # Ensure the file exists
            except FileNotFoundError:
                print("Secret image 'lars.jpg' not found.")
            os.system('cls' if os.name == 'nt' else 'clear')
            curses.endwin()

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

#9/11

if __name__ == "__main__":
    curses.wrapper(entry_point)


#Buggar som jag hittar nu

        #2 Buggar som är relaterade till lars-regen funktion (Non-Issue)
        #Bugg med kartan och combat systemet - Fixad??
        #Overlapp med statusen i spelet och kartan och skärmen är för inzoomad

        #samma med henrik och troligen alla lärare (vad fan är detta för spagheti kod)

        
        


#todo: lägg till coins efter alla rätt svar på frågor vid läraren (gjord)

#pang pangs kod är nu helt bortplockad från koden, den är bra nog. ;-;

#Fortfarande lite cred för att han försökte, koden är bara bort kommenterad inte bortplockad (vad jag vet iallafal.)


#felix för fan gör färdigt allt, du glömdee ändra siffrorna i sal 2 på dörrarna i tur ordning