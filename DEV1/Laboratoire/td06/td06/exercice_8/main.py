from jour_mois import suite_numeros_jours
import textwrap  # Exercice 9-10 : pour le retour à la ligne automatique
def numero_jour(jour, mois, annee):
    """Retourne la valeur de la congruence de Zeller (0 = lundi, 1 = mardi, ..., 6 = dimanche)"""

    # Ajustement : janvier et février comptent comme les mois 13 et 14 de l’année précédente
    if mois == 1:
        mois = 13
        annee -= 1
    elif mois == 2:
        mois = 14
        annee -= 1

    q = jour                  # jour du mois
    m = mois                  # mois ajusté
    K = annee % 100           # année du siècle
    J = annee // 100          # siècle

    # Formule de Zeller
    h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

    # Ajustement pour que 0 = lundi, ..., 6 = dimanche
    h = (h + 5) % 7

    return h
print(numero_jour(, 3, 2008))
