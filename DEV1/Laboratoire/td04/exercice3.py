# Demande d'un nombre entier à l'utilisateur
nbre = int(input("Entrez un nombre entier : "))

# Vérification de la parité
if nbre % 2 == 0:
    print(nbre, "est pair.")
else:
    print(nbre, "est impair.")