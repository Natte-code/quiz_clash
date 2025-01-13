import time
import random
import curses
import os
import threading

#Def av några sid funktioner som kallas på igenom spelet
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



#kod skaffad från Chatgpt och används för att insperara denna kod.
####################################################################################################
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



def start_screen(name): #startar start skärmen, förklarar hur man spelar och visar loggan
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
                Rör dig med WASD eller PILLAR-tangenterna. 
                Samla mynt, öppna lådor och upptäck klassrum. 
                Svara på lärarens frågor. Fel svar leder till turordningsbaserade strider.
                Håll terminalen i FULL SCREEN!!
                Tryck "i" för att öppna ditt inventory (går ej att släppa saker, så använd varsamt!)
                Lycka till!!
         """)
   print("")
   print("\nTryck på ENTER knappen för att starta spelet!")
   input()


if __name__ == "__main__":
    start_screen(NameError)
#Kontrollerar om filen körs direkt (inte importeras som en modul).

player_name = input("innan spelet börjar helt... Ange ditt namn: ")






###########################################################################

#classes för allt i spelet
#altså där vi lagrar all info om alla saker som kan förändras

#koden skrivs av nathaniel och eliot

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

        
    def is_critical_hit(self):
        return random.random() < 0.15 #15 % chans att göra kritisk träff
    

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
boss = boss(name="Lars", health=450, min_damage=10, max_damage=95)

teacher1 = Teacher(name="johanna", health=100, min_damage=1, max_damage=10)
teacher2 = Teacher(name="Ronja", health=110, min_damage=5, max_damage=15)
teacher3 = Teacher(name="Henrik", health=125, min_damage=8, max_damage=18)
teacher4 = Teacher(name="Victor", health=135, min_damage=1, max_damage=13)
teacher5 = Teacher(name="David", health=150, min_damage=9, max_damage=20)
teacher6 = Teacher(name="Mirrela", health=200, min_damage=11, max_damage=25)

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




#combat_loop(player, MOTSTONDARE) #kallning på funktion med vilken lärare när strid ska starta


#--------------------------------------------------------------------------



#koden är skriven helt av nathaniel och skrivet HELT från scratch. inga idér från intenet utan helt från grunden upp.
#koden ska trigga när dem olika sluta ska triggas
#--------------------------------------------------------------------------

####################################
#importerad från chatgpt för att tömma terminalen
def clear_terminal_visual():
    print("\n" * 1000)

# Använder funktionen


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


###########################################################################
#koden för rörelse i spelet och att skapa spelkartan
#bas kod är skaffad av ChatGPT och modifierad av Felix
#Hallway 1

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking getch
    stdscr.timeout(20000) # Input timeout (ms)

    # Game variables
    rows, cols = 35, 35  # Game board dimensions
    player_pos = [31, 16]  # Player's starting position
    block_pos = [[3, 3]]   # Block positions
    goal_pos = [2, 2]      # Goal position
    door_pos = [[11, 1], [10, 2], [9, 3]]
    door_pos2 = [[1, 19], [1, 18], [1, 17], [1, 16], [1, 15], [1, 14], [1, 13]]
    door_pos3 = [[27, 1], [26, 2], [25, 3]]
    door_pos4 = [[11, 31], [10, 32], [9, 33]]
    door_pos5 = [[27, 31], [26, 32], [25, 33]]
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
                elif [r, c] in door_pos2:
                    stdscr.addch(r, c, '-')
                elif [r, c] in door_pos3:
                    stdscr.addch(r, c, '/')
                elif [r, c] in door_pos4:
                    stdscr.addch(r, c, '/')
                elif [r, c] in door_pos5:
                    stdscr.addch(r, c, '/')
                elif [r, c] in block_pos:
                    stdscr.addch(r, c, 'B')  # Block
                elif [r, c] == goal_pos:
                    stdscr.addch(r, c, 'X')  # Goal
                elif [r, c] == player_pos:
                    stdscr.addch(r, c, 'O')  # Player
                else:
                    stdscr.addch(r, c, ' ')  # Empty space

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
        elif key == ord('i'): # inventory
            break #ta bork break och lägg in befinitionen för inventory
        
        # Validate movement
        if not (new_pos[0] == 0 or new_pos[0] == rows - 1 or 
                 new_pos[1] == 0 or new_pos[1] == cols - 1) and new_pos not in block_pos:
            player_pos = new_pos

        # Check for goal and special positions
        if player_pos == goal_pos:
            message = "You reached the goal!" #test sak
            break
        elif player_pos in door_pos:
            message = "You encountered a door!"  #room 2
        elif player_pos in door_pos2:
            message = "You found a secret!" #Halway
        elif player_pos in door_pos3:
            message = "You found a secret!3" #room 1
        elif player_pos in door_pos4:
            message = "You found a secret!4" #chest room
        elif player_pos in door_pos5:
            message = "You found a secret!5" #room 3

if __name__ == "__main__":
    curses.wrapper(main)

###########################################################################
#Hallway 2


###########################################################################
#Room 1

###########################################################################
#Room 2

###########################################################################
#Room 3

###########################################################################
#Room 4

###########################################################################
#Room 5

###########################################################################
#Room 6

###########################################################################
#Chest Room