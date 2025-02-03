import time
import random
import curses
import os
import threading

# Loggan
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

# Helper Functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo_print(logo, delay=0.15):
    for line in logo:
        print(line)
        time.sleep(delay)

def start_screen():
    print("\n" * 100)
    print("Välkommen till ♦Quiz Clash♦")
    time.sleep(1)
    print("....")
    time.sleep(1)
    logo_print(logo)
    time.sleep(1)
    print("""
Hur man spelar:
    Rör dig med WASD
    Samla mynt, öppna lådor och upptäck klassrum.
    Svara på lärarens frågor. Fel svar leder till turordningsbaserade strider.
    Håll terminalen i FULL SCREEN (Och zooma ut om spelet krashar (med hjälp av att trycka CTRL och - ))!!
    Håll årdning på ditt inventory (går ej att släppa saker, så använd varsamt!)
    Lycka till!!
    """)
    input("\nTryck på ENTER knappen för att starta spelet!")

# Classes
class Sword:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __repr__(self):
        return f"Sword(name='{self.name}', damage={self.damage})"

class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.coins = 5
        self.totems = 1
        self.shields = 1
        self.inventory = {
            "swords": {"träsvärd": 10, "järnsvärd": 20},
            "potions": {"normal": 5, "epic": 5}
        }

    def is_critical_hit(self):
        return random.random() < 0.15  # 15% chance for critical hit

    def attack(self, weapon):
        base_damage = self.inventory["swords"].get(weapon, random.randint(5, 10))
        if self.is_critical_hit():
            crit_damage = int(base_damage * 2.5)
            print(f"KRITISK TRÄFF! Du gör {crit_damage} skada!\n------------")
            return crit_damage
        return base_damage

    def heal(self, potion_type):
        if potion_type in self.inventory["potions"] and self.inventory["potions"][potion_type] > 0:
            self.inventory["potions"][potion_type] -= 1
            return 50 if potion_type == "normal" else 100
        return 0

    def block(self):
        return random.random() < 0.3  # 30% chance to block

    def use_totem(self):
        if self.totems > 0:
            self.totems -= 1
            self.health = 100
            print(f"------------\nDu använde en totem! {self.name} är återupplivad med 100 HP!\n------------")
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

class Boss(Teacher):
    def __init__(self, name, health, min_damage, max_damage, regen):
        super().__init__(name, health, min_damage, max_damage)
        self.regen = regen
        self.is_regen = False

    def start_regen(self):
        if not self.is_regen:
            self.is_regen = True
            threading.Thread(target=self.regenerate_health, daemon=True).start()

    def regenerate_health(self):
        while self.is_regen:
            time.sleep(10)
            if self.health < self.max_health:
                self.health = min(self.max_health, self.health + self.regen)
                print(f"+15 HP: {self.health}")

    def stop_regen(self):
        self.is_regen = False

# Game Logic
def combat_loop(player, opponent):
    while player.health > 0 and opponent.health > 0:
        clear_screen()
        print(f"{player.name}'s tur\n------------")
        print(f"Inventarie:\n- Svärd: {list(player.inventory['swords'].keys())}")
        print(f"- Potions: {player.inventory['potions']}")
        print(f"- Totems: {player.totems}")
        print(f"- Sköldar: {player.shields}")
        print(f"HP: {player.health}\n------------")
        print(f"{opponent.name}s HP: {opponent.health}\n------------")

        action = input("Välj handling (attack, heal, stand): ").strip().lower()
        print("------------")

        if action == "attack":
            weapon = input("Välj svärd (eller tryck ENTER för att använda händerna): ").strip().lower()
            if weapon in player.inventory["swords"] or weapon == "":
                damage = player.attack(weapon)
                opponent.health = max(0, opponent.health - damage)
                print(f"Du attackerade {opponent.name} med {'händerna' if weapon == '' else weapon} och gjorde {damage} skada!")
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
        elif action == "stand":
            print("Du valde att vänta. Nästa tur!\n------------")
        else:
            print("Ogiltig handling!\n------------")

        if opponent.health <= 0:
            print(f"{opponent.name} är besegrad! Du vann!\n------------")
            break

        time.sleep(2)
        clear_screen()
        input("Tryck ENTER för att fortsätta...")

        # Opponent's turn
        print(f"{opponent.name}s tur!\n------------")
        time.sleep(2)
        damage = opponent.attack()
        if player.block():
            print("Din sköld blockerade attacken!\n------------")
        else:
            player.health = max(0, player.health - damage)
            print(f"{opponent.name} attackerade och gjorde {damage} skada!\n------------")
            if player.health == 0 and player.use_totem():
                continue

        print(f"{opponent.name}s HP: {opponent.health}\n------------")
        print(f"{player.name}s HP: {player.health}\n------------")

        if player.health <= 0:
            print("Du förlorade kampen! Bättre lycka nästa gång.\n------------")
            end1()
            break

# Map System
def draw_map(stdscr, player_pos, room_layout):
    stdscr.clear()
    for y, row in enumerate(room_layout):
        for x, char in enumerate(row):
            if [y, x] == player_pos:
                stdscr.addch(y, x, 'O')  # Player
            else:
                stdscr.addch(y, x, char)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100) # Refresh rate

    # Room layout
    room_layout = [
        "####################",
        "#..................#",
        "#..................#",
        "#..................#",
        "#..................#",
        "#..................#",
        "####################"
    ]

    player_pos = [3, 3]  # Starting position

    while True:
        draw_map(stdscr, player_pos, room_layout)
        key = stdscr.getch()

        # Movement
        if key == ord('w'):
            player_pos[0] -= 1
        elif key == ord('s'):
            player_pos[0] += 1
        elif key == ord('a'):
            player_pos[1] -= 1
        elif key == ord('d'):
            player_pos[1] += 1
        elif key == ord('q'):  # Quit
            break

# Main Game
def start_game():
    start_screen()
    player_name = input("Ange ditt namn: ")
    player = Character(player_name)

    # Example combat
    teacher = Teacher("Johanna", 100, 1, 10)
    combat_loop(player, teacher)

if __name__ == "__main__":
    curses.wrapper(main)  # Start curses-based map system
    start_game()          # Start the game