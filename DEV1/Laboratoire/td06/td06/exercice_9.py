def main():
    # Choisis le mois et l'année que tu veux afficher :
    mois = 3
    annee = 2008

    # 1) Quel jour de la semaine est le 1er du mois ?
    #    (0 = lundi, 1 = mardi, ..., 6 = dimanche)
    decalage = numero_jour(1, mois, annee)

    # 2) Tous les jours du mois sous forme "01 02 03 ... 31"
    jours = suite_numeros_jours(mois, annee)

    # 3) On ajoute les espaces avant le "01"
    # Chaque "case jour" prend 3 caractères ("dd ")
    espaces_avant = "   " * decalage

    # 4) Chaîne linéaire avec décalage + jours
    suite_numeros = espaces_avant + jours

    # ---- Exercice 10 : affichage calendrier lisible ----
    # On veut que chaque semaine tienne sur une ligne.
    # Une "semaine" = 7 colonnes, chaque colonne fait 3 caractères → largeur 21.
    calendrier_formate = textwrap.fill(suite_numeros, width=21)

    # Affichage final :
    print("lu ma me je ve sa di")  # En-tête (optionnel mais joli)
    print(calendrier_formate)

if __name__ == "__main__":
    main()
 

