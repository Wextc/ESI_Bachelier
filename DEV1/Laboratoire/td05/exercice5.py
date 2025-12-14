import random

def tirer_carte():
    les_valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'valet', 'dame', 'roi', 'as']
    les_couleurs = ['pique', 'trèfle', 'cœur', 'carreau']
    la_carte = random.choice(les_valeurs)
    la_couleur = random.choice(les_couleurs)
    resultat = [la_carte, la_couleur]
    return resultat

print(tirer_carte())