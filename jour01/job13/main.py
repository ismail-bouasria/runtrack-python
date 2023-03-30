#job13

nomber1 = input("Entrer le nombre 1: ")
nomber2 = input("Entrer le nombre 2: ")
nomber3 = input("Entrer le nombre 3: ")
nomber4 = input("Entrer le nombre 4: ")
nomber5 = input("Entrer le nombre 5: ")

liste = [nomber1,
         nomber2,
         nomber3,
         nomber4,
         nomber5]

def tri_liste(liste):
    liste.sort()
    return liste

print(tri_liste(liste))
    