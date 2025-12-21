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




