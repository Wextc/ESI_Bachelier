
#Input => reçoit en paramètre d'entier avec des doublons
# Supprime les doublons
# Output => donne une liste d'entier sans doublons

def suppression_doublons(ma_liste):
    
    for i in ma_liste:
        ma_liste.remove(i)
        print(ma_liste)

suppression_doublons([7, 3, 3, 8, 8, 8, 7])

"""
Attention 

for i in ma_liste:
    ma_liste.remove(i)
    Quand tu supprimes un élément :

la liste change de taille

Python “saute” des éléments

le résultat devient incorrect


"""


#### Code correcte

def suppression_doublons(ma_liste):
    resultat = []
    for i in ma_liste:
        if i not in resultat:
            resultat.append(i)
    return resultat

print(suppression_doublons([7, 3, 3, 8, 8, 8, 7]))


