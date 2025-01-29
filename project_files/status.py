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


teacher1 = Teacher(name="johanna", health=0, min_damage=1, max_damage=10) 
teacher2 = Teacher(name="Ronja", health=0, min_damage=5, max_damage=15)
teacher3 = Teacher(name="Henrik", health=0, min_damage=8, max_damage=18)
teacher4 = Teacher(name="Victor", health=0, min_damage=1, max_damage=13)
teacher5 = Teacher(name="David", health=0, min_damage=9, max_damage=20)
teacher6 = Teacher(name="Mirrela", health=1, min_damage=11, max_damage=25)

lars = boss(name="Lars", health=0, min_damage=0, max_damage=0, regen=0)


def status_player():
    if teacher1.health == 0 and teacher2.health == 0 and teacher3.health == 0 and teacher4.health == 0 and teacher5.health == 0 and teacher6.health == 0 and lars.health == 0:
        print("Du dödade alla")
    else:
        if teacher1.health == 0:
            print("Johanna är besegrad")
        else:
            print("Du har kvar Johanna att slåss mot\n")


        if teacher2.health == 0:
            print("Ronja är besegrad")
        else:
            print("Du har kvar Ronja att slåss mot\n")


        if teacher3.health == 0:
            print("Henrik är besegrad")
        else:
            print("Du har kvar Henrik att slåss mot\n")


        if teacher4.health == 0:
            print("Victor är besegrad")
        else:
            print("Du har kvar Victor att slåss mot\n")


        if teacher5.health == 0:
            print("David är besegrad")
        else:
            print("Du har kvar David att slåss mot\n")


        if teacher6.health == 0:
            print("Mirella är besegrad")
        else:
            print("Du har kvar Mirella att slåss mot \n")
    
    


status_player()
