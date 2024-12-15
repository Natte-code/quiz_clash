import random
import time
import os

# Loot-pool
loot_pool = {
    "normal": [
        ("Pie", "swords", 20),           # 20% chans
        ("järnsvärd", "swords", 20),     # 20% chans
        ("katana", "swords", 15),        # 15% chans
        ("Dagger", "swords", 10),        # 10% chans
        ("Pinne", "swords", 5),          # 5% chans
        ("low_potion", "potions", 20),   # 20% chans
        ("medium_potion", "potions", 10) # 10% chans
    ],
    "epic": [
        ("Kukri", "swords", 25),         # 25% chans
        ("battle_axe", "swords", 20),    # 20% chans
        ("kukri", "swords", 15),         # 15% chans
        ("stekpanna", "swords", 5),      # 5% chans
        ("epic_potion", "potions", 10),  # 10% chans
        ("legendary_potion", "potions", 5), # 5% chans
        ("totem", "special", 10)         # 10% chans
    ]
}

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.coins = 25
        self.totems = 4
        self.shields = 1
        # Förenklat inventory
        self.inventory = {
            "swords": {"träsvärd": 10, "järnsvärd": 20},
            "potions": {"normal": 5, "epic": 3}          
        }

    def open_chest(self, chest_type):
        """Öppna en kista och få ett slumpmässigt föremål."""
        cost = 5 if chest_type == "normal" else 15

        if self.coins < cost:
            print(f"Du har inte tillräckligt med coins för att öppna en {chest_type} chest.")
            return

        self.coins -= cost
        print(f"Du öppnade en {chest_type} chest! ({cost} coins)")

        loot = self.get_random_loot(loot_pool[chest_type])
        item, category = loot[:2]
        self.inventory[category][item] = self.inventory[category].get(item, 0) + 1
        print(f"Du fick en {item}!")

    def get_random_loot(self, pool):
#Slumpar en item från loot-poolen
        total_weight = sum(item[2] for item in pool)
        rand = random.uniform(0, total_weight)
        cumulative = 0
        for item in pool:
            cumulative += item[2]
            if rand < cumulative:
                return item


# Testa koden
if __name__ == "__main__":
    # Skapa en karaktär
    player = Character(name="Testkaraktär", health=100)
    
    # Visa initial status
    print(f"Initial coins: {player.coins}")
    print(f"Inventory: {player.inventory}")
    
    # Öppna en "normal" kista
    player.open_chest("normal")
    
    # Visa uppdaterad status
    print(f"Remaining coins: {player.coins}")
    print(f"Updated inventory: {player.inventory}")
    
    # Försök öppna en "epic" kista
    player.open_chest("epic")


#vad jag behöver ändra - gör så när man öppnar låda man får veta vilken rarity man får på sin item
#att inventoryt updateras med rätt stats att dagger ska visa sin damage när den är i inventoryt

#tex om jag får dagger ska den visa "dagger": 20 dmg (ex)i inventoryt istället för "dagger": 1 för att visa att jag har 1 av den.
#lägg block så man max kan ha 10 saker i inventoryt av svärd
#och visa alla stats av saker man får och vilken rarit20,1
