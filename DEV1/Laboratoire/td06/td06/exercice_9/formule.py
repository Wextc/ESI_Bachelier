from jour_mois import suite_numeros_jours, nbre_jour
from  exercice_9  import suite_numeros_jours
import textwrap  # pour formater le calendrier (retours à la ligne automatiques)

   # pour formater le calendrier (retours à la ligne automatiques)

def main(mois, annee):
    # 1) Quel jour de la semaine est le 1er du mois ?
    #    (0 = lundi, 1 = mardi, ..., 6 = dimanche)
    decalage = numero_jour(1, mois, annee)

    # 2) Tous les jours du mois sous forme "01 02 03 ... 31"
    jours = suite_numeros_jours(mois, annee)

    # 3) On ajoute les espaces avant "01"
    # Chaque "case jour" prend 3 caractères ("dd ")
    espaces_avant = "   " * decalage

    # 4) Chaîne linéaire avec les bons espaces + les numéros du mois
    suite_numeros = espaces_avant + jours

    # 5) On coupe cette chaîne en semaines (7 colonnes * 3 caractères = 21 caractères)
    calendrier_formate = textwrap.fill(suite_numeros, width=21)

    # 6) Affichage final
    print("lu ma me je ve sa di")
    print(calendrier_formate)


if __name__ == "__main__":
    main(3, 2018)  # exemple : mars 2018