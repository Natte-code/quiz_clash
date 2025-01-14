import random


# Loot-pool enligt specifikationen
loot_pool = {
    "normal": [
        ("Pie", "swords", 3.14),  # 20% chans
        ("järnsvärd", "swords", 20),      # 20% chans
        ("katana", "swords", 15),         # 15% chans
        ("Dagger", "swords", 10),         # 10% chans
        ("Pinne", "swords", 5),           # 5% chans
        ("low_potion", "potions", 25),    # 20% chans
        ("medium_potion", "potions", 50), # 10% chans
    ],
    "epic": [
        ("Kukri", "swords", 25),          # 25% chans
        ("battle axe", "swords", 20),     # 20% chans
        ("lightsaber", "swords", 35),     # 15% chans
        ("stekpanna", "swords", 55),      # 5% chans
        ("epic_potion", "potions", 100),  # 10% chans
        ("legendary_potion", "potions", 200), # 5% chans
        ("totem", "special"),             # 25% chans
    ],
}


# Representerar en spelare
class Character:
    def __init__(self, name, health, coins):
        self.name = name
        self.health = health
        self.max_health = health
        self.coins = coins
        self.inventory = {
            "swords": [],   # Svärd med namn och skada
            "potions": [],  # Potions med namn och healing
            "special": [],  # Specialföremål som totems
        }

    def add_to_inventory(self, item):
        """Lägger till föremål i rätt kategori."""
        if item[1] == "swords":
            self.inventory["swords"].append((item[0], item[2]))  # (Name, Damage)
        elif item[1] == "potions":
            self.inventory["potions"].append((item[0], item[2]))  # (Name, Healing)
        elif item[1] == "special":
            self.inventory["special"].append(item[0])  # (Name)
        print(f"Du har fått: {item[0]}!")

    def use_potion(self, potion_name):
        """Använd en potion för att heala."""
        for potion in self.inventory["potions"]:
            if potion[0] == potion_name:
                self.inventory["potions"].remove(potion)
                heal_amount = potion[1]
                self.health = min(self.max_health, self.health + heal_amount)
                print(f"Du använde en {potion_name} och helade {heal_amount} HP!")
                return
        print(f"Du har ingen {potion_name} potion!")

    def attack(self, weapon_name):
        """Attackerar med ett svärd och returnerar skada."""
        for sword in self.inventory["swords"]:
            if sword[0] == weapon_name:
                damage = sword[1]
                print(f"Du attackerade med {weapon_name} och gjorde {damage} skada!")
                return damage
        print(f"Du har inte {weapon_name}, så du använder händerna!")
        return random.randint(5, 10)

    def show_inventory(self):
        print("\nSpelarens Inventory:")
        print(f"- Svärd: {self.inventory['swords']}")
        print(f"- Potions: {self.inventory['potions']}")
        print(f"- Special: {self.inventory['special']}")
        print("\n")


# Chest-klassen
class Chest:
    def __init__(self, rarity, cost):
        self.rarity = rarity
        self.cost = cost

    def open(self, player):
        """Öppnar kistan och lägger till slumpat föremål till spelarens inventory."""
        if player.coins < self.cost:
            print("Du har inte tillräckligt med coins för att öppna denna kista!")
            return

        # Dra av kostnaden
        player.coins -= self.cost
        print(f"\nDu öppnade en {self.rarity.capitalize()} Chest för {self.cost} coins!")

        # Välj föremål baserat på loot-poolen
        pool = loot_pool[self.rarity]
        weights = [25 if item[1] == "special" else 20 if item[1] == "potions" else 15 for item in pool]
        chosen_item = random.choices(pool, weights=weights, k=1)[0]

        # Lägg till föremålet i spelarens inventory
        player.add_to_inventory(chosen_item)


# Combat-loop
def combat_loop(player, opponent):
    """Simpel stridsloop mellan spelare och motståndare."""
    while player.health > 0 and opponent.health > 0:
        print(f"\n{player.name}: {player.health} HP")
        print(f"{opponent['name']}: {opponent['health']} HP\n")
        action = input("Välj handling (attack, heal, stand): ").strip().lower()

        if action == "attack":
            weapon_name = input("Välj vapen (eller tryck ENTER för att använda händerna): ").strip()
            damage = player.attack(weapon_name)
            opponent["health"] -= damage
        elif action == "heal":
            potion_name = input("Välj potion att använda: ").strip()
            player.use_potion(potion_name)
        elif action == "stand":
            print("Du väntar på din nästa tur...")
        else:
            print("Ogiltigt val!")

        if opponent["health"] <= 0:
            print(f"{opponent['name']} är besegrad! Du vann!")
            return

        # Motståndaren attackerar
        damage = random.randint(opponent["min_damage"], opponent["max_damage"])
        print(f"{opponent['name']} attackerar och gör {damage} skada!")
        player.health -= damage

        if player.health <= 0:
            print("Du förlorade kampen! Bättre lycka nästa gång!")
            return


# Testa spelet
def test_game():
    # Skapa spelaren
    player = Character(name="Hjälte", health=100, coins=50)

    # Skapa en motståndare
    opponent = {"name": "Henrik", "health": 120, "min_damage": 8, "max_damage": 18}

    # Skapa kistor
    normal_chest = Chest(rarity="normal", cost=10)
    epic_chest = Chest(rarity="epic", cost=25)

    # Testa loot och strid
    player.show_inventory()
    normal_chest.open(player)
    epic_chest.open(player)
    player.show_inventory()

    # Starta en strid
    combat_loop(player, opponent)


if __name__ == "__main__":
    test_game()
