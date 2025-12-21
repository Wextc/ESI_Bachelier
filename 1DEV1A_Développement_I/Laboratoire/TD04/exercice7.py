# Liste des voyelles
voyelles = "aeiouyAEIOUY"

# Demande à l'utilisateur un mot
chaine = input("Entrez un mot : ")

# Vérifie d'abord que l'utilisateur n'a pas laissé la chaîne vide
if len(chaine) == 0:
    print("Vous n’avez rien saisi.")
else:
    # Vérifie si la première lettre est une voyelle
    if chaine[0] in voyelles:
        print("La première lettre est une voyelle.")
    else:
        print("La première lettre n’est pas une voyelle.")