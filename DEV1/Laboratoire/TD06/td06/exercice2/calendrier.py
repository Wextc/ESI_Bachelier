def nom_du_mois(index):
    arr = [
        "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ]
    # On vérifie que l’index est valide (1 à 12)
    if 1 <= index <= 12:
        return arr[index - 1]
    else:
        return "Mois invalide"


def afficher_titre(mois, annee):
    print("=" * 25)
    print(f"{nom_du_mois(mois)} {annee}")
    print("=" * 25)