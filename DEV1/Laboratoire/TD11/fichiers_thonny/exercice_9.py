def suppression_occurrences(ma_liste, mot):
    compteur = 0

    while mot in ma_liste:
        ma_liste.remove(mot)
        compteur += 1

    return compteur
liste = ["a","v","r","v","r"]
nb = suppression_occurrences(liste, "r")

print("Nombre de suppressions :", nb)
print("Liste après suppression :", liste)