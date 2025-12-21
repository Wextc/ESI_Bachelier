import textwrap  # Exercice 9 : module pour formater le texte
# On suppose que les fonctions ci-dessous sont dans le même fichier
# ou importées depuis un module `jour_mois`

def est_bissextile(annee):
    """Retourne True si l'année est bissextile, False sinon."""
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)


def nbre_jour(premier, dernier):
    """Retourne une chaîne avec les jours du mois formatés sur deux chiffres."""
    res = []
    for i in range(premier, dernier + 1):
        if i < 10:
            res.append("0" + str(i))
        else:
            res.append(str(i))
    return " ".join(res)


def suite_numeros_jours(mois, annee):
    """Retourne la suite des numéros de jours du mois/année donné."""
    if 1 <= mois <= 12:
        if mois in [1, 3, 5, 7, 8, 10, 12]:
            return nbre_jour(1, 31)
        elif mois in [4, 6, 9, 11]:
            return nbre_jour(1, 30)
        elif mois == 2:
            if est_bissextile(annee):
                return nbre_jour(1, 29)
            else:
                return nbre_jour(1, 28)
    else:
        return "Mois doit être compris entre 1 et 12"


def numero_jour(jour, mois, annee):
    """Retourne le jour de la semaine pour la date donnée
    (0 = lundi, 1 = mardi, ..., 6 = dimanche) basé sur la congruence de Zeller.
    """
    # Ajustement : janvier et février deviennent mois 13 et 14 de l’année précédente
    if mois == 1:
        mois = 13
        annee -= 1
    elif mois == 2:
        mois = 14
        annee -= 1

    q = jour                  # jour du mois
    m = mois                  # mois ajusté
    K = annee % 100           # année du siècle (00-99)
    J = annee // 100          # siècle

    # Formule de Zeller
    h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

    # Adapter pour que 0 = lundi ... 6 = dimanche
    h = (h + 5) % 7

    return h


def afficher_calendrier(mois, annee):
    # 1) Trouver le jour de la semaine du 1er du mois
    #    (0=lundi, 1=mardi, ..., 6=dimanche)
    decalage = numero_jour(1, mois, annee)

    # 2) Générer "01 02 03 ... 30/31/28/29"
    jours = suite_numeros_jours(mois, annee)

    # 3) Ajouter des "cases vides" avant le 1er jour
    # Chaque jour prend 3 caractères ("dd "), donc on met 3 espaces par case vide
    espaces_avant = "   " * decalage

    # 4) Construire la grande ligne complète du mois
    suite_numeros = espaces_avant + jours

    # 5) Exercice 9/10 : utiliser textwrap.fill pour couper en semaines
    # Largeur d'une semaine = 7 jours * 3 caractères = 21
    calendrier_formate = textwrap.fill(suite_numeros, width=21)

    # 6) Affichage final
    print("lu ma me je ve sa di")
    print(calendrier_formate)


# -----------------
# TEST demandé par l'énoncé
# -----------------
afficher_calendrier(2, 2021)   
