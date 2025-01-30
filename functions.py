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
                Rör dig med WASD, inte med PILL-tagneter
                Samla mynt, öppna lådor och upptäck klassrum. 
                Svara på lärarens frågor. Fel svar leder till turordningsbaserade strider.
                Håll terminalen i FULL SCREEN!!
                Tryck "i" för att öppna ditt inventory (går ej att släppa saker, så använd varsamt!)
                Lycka till!!
         """)
   print("")
   print("\nTryck på ENTER knappen för att starta spelet!")
   input()




player_name = input("innan spelet börjar helt... Ange ditt namn: ")