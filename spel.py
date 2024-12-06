import time
import random
import curses

#alternativt: koden ska göra terminalen i fullscreen

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



###########################################################################
#koden för rörelse i spelet och att skapa spelkartan
#Denna kod är skaffad av ChatGPT och lite modifierad av Felix
    name = input("innan spelet börjar helt... Ange ditt namn: ")
def main(stdscr):
    # Initiera curses
    curses.curs_set(0)  # Dölj markören
    stdscr.nodelay(1)   # Gör getch icke-blockerande
    stdscr.timeout(2000) # Ställ in en timeout för getch (ms)
    
    # Spelvariabler
    rows, cols = 30, 60  # Storlek på spelplanen
    player_pos = [15, 30]  # Startposition för spelaren (centrerad)
    key = None            # Håller koll på vilken knapp som trycks
    
    while True:
        # Ritning av spelplanen
        stdscr.clear()
        for r in range(rows):
            for c in range(cols):
                # Rita väggar på kanterna
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    stdscr.addch(r, c, '#')  # Vägg
                elif [r, c] == player_pos:
                    stdscr.addch(r, c, 'O')  # Placera spelaren
                else:
                    stdscr.addch(r, c, ' ')  # Ritning av spelplanen
        
        stdscr.refresh()

        # Hantera användarinput
        key = stdscr.getch()
        new_pos = player_pos.copy()
        if key == ord('q'):  # Avsluta spelet
            break
        elif key == ord('w'):  # Upp
            new_pos[0] -= 1
        elif key == ord('s'):  # Ner
            new_pos[0] += 1
        elif key == ord('a'):  # Vänster
            new_pos[1] -= 1
        elif key == ord('d'):  # Höger
            new_pos[1] += 1

        # Kontrollera om spelaren försöker gå in i en vägg
        if not (new_pos[0] == 0 or new_pos[0] == rows - 1 or 
                new_pos[1] == 0 or new_pos[1] == cols - 1):
            player_pos = new_pos

if __name__ == "__main__":
    curses.wrapper(main)

###########################################################################




###########################################################################

#classes för allt i spelet
#altså där vi lagrar all info om alla saker som kan förändras

#koden skrivs av nathaniel och eliot
class Charecter: #classen för 
   def __init__(self, health, base_damage):
    self.base_damage = base_damage
    self.health = health
    self.inventory = {"swords": {}, "potions": {}, "shields": {}, "totems": 0}
    self.coins = 0
    self.revive_used = False

    def add_item(self, item_type, item_name, value):
        #lägger till föremål i inventory eller coins i inventory.
        if item_type =="coins":
            self.coins += value
        elif item_type in self.inventory:
            if item_type == "totems":
                self.inventory["totems"] += value
            else:
                self.inventory[item_type][item_name] = value
 
      
class Teacher:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage


#koden för combat systemet
#--------------------------------------------------------------------------
def combat_round(player, teacher):
    #spelarens tur (spelaren börjar alltid)
    print(f"\n{player.name}'s turn!")
    print(f"\n ditt Inventory: {player.inventory} ")

    if player.inventory["potions"]:
        action = input("Välj en attack").strip().lower()
    else:
        action = "attack" #Använder attack om det inte finns några potions

    if action == "attack":
        print("tillgängliga svärd: ", list(player.inventory["swords"].keys())) 
        sword = input("Välj svärd (eller tryck ENTER om du inte har några / vill slå med handen): ").strip().lower()
        damage = player.attack(sword)
        teacher.health -= damage
        print(f"du attackerade {teacher.name} med {"Dina händer" if sword =="" else sword}, som gjorde {damage} skada!")
        



#--------------------------------------------------------------------------
