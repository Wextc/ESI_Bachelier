#Ex 1
def nom_du_mois(index):
    mois = [
        "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ]
    return mois[index - 1]

#print(nom_du_mois(4))

def afficher_titre(mois, annee):
    mois = nom_du_mois(mois)
    ligne = "=" * 26
    print(ligne)
    print(f"{mois} {annee}")
    print(ligne)

#afficher_titre(4,2018)
    
    
