antal_potion_vanlig = 0
antal_potion_epic = 0

print('''
1. Vissa inventory
2. Lägg till potion vanlig
3. Lägg till potion epic
4. Tar bort potion  vanlig
5. Tar bort potion epic  
       ''')
fraga_potion_inventory = str(input())

if fraga_potion_inventory == "1":
    print (f'Du har {antal_potion_vanlig} vanliga potion')
    print (f"Du har {antal_potion_epic} epic potion")

elif fraga_potion_inventory == "2":
    antal_potion_vanlig = antal_potion_vanlig + 1
    print (f'Du har nu {antal_potion_vanlig} vanliga potion')

elif fraga_potion_inventory == "3":
    antal_potion_epic = antal_potion_epic + 1
    print (f'Du har nu {antal_potion_epic} epic potion')

elif fraga_potion_inventory == "4":
    antal_potion_vanlig = antal_potion_vanlig - 1
    print (f'Du har nu {antal_potion_vanlig} vanliga potion')


elif fraga_potion_inventory == "5":
    antal_potion_epic = antal_potion_epic - 1
    print (f'Du har nu {antal_potion_epic} epic potion')

else:
    print ("Ogiltlig svar")