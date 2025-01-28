#Koden för status

class boss:
    def __init__(self, name, health, min_damage, max_damage, regen):
        self.name = name
        self.health = health
        self.max_health = health
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.regen = regen
        self.isregen = False





class Teacher:
    def __init__(self, name, health, min_damage, max_damage):
        self.name = name
        self.health = health
        self.min_damage = min_damage
        self.max_damage = max_damage


teacher1 = Teacher(name="johanna", health=100, min_damage=1, max_damage=10) 
teacher2 = Teacher(name="Ronja", health=110, min_damage=5, max_damage=15)
teacher3 = Teacher(name="Henrik", health=125, min_damage=8, max_damage=18)
teacher4 = Teacher(name="Victor", health=135, min_damage=1, max_damage=13)
teacher5 = Teacher(name="David", health=150, min_damage=9, max_damage=20)
teacher6 = Teacher(name="Mirrela", health=200, min_damage=11, max_damage=25)


def statu_player():
    if teacher1.health == 0:
        print("Johanna är besegrad \n")
    else:
        print("Du måste fortfarande göra Johanna \n")


    if teacher2.health == 0:
        print("Ronja är besegrad \n")
    else:
        print("Du måste fortfarande göra Ronja \n")


    if teacher3.health == 0:
        print("henrik är besegrad \n")
    else:
        print("Du måste fortfarande göra Henrik \n")


    if teacher4.health == 0:
        print("Victor är besegrad \n")
    else:
        print("Du måste fortfarande göra Victor \n")


    if teacher5.health == 0:
        print("David är besegrad \n")
    else:
        print("Du måste fortfarande göra David \n")


    if teacher6.health == 0:
        print("Mirella är besegrad \n")
    else:
        print("Du måste fortfarande göra Mirella \n")


    if teacher1.health == 0 and teacher2.health == 0 and teacher3.health == 0 and teacher4.health == 0 and teacher5.health == 0 and teacher6.health == 0 and boss.health == 0:
        print("Du dödade alla")
 # Där ska man har end2() som säger du vann spelet

statu_player()