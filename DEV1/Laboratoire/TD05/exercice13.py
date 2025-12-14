def afficher_boite(n):
    # Cas invalides
    if n <= 0:
        print("Largeur invalide !")
        return
    
    # Ligne du haut
    print("*" * n)
    
    # Lignes du milieu (intérieur vide)
    # On doit afficher 4 lignes au total, donc 2 du milieu (4 - 2 = 2)
    for _ in range(4 - 2):
        if n == 1:
            print("*")  # une seule étoile, pas de vide possible
        elif n == 2:
            print("**")  # juste deux étoiles collées
        else:
            print("*" + " " * (n - 2) + "*")
    
    # Ligne du bas
    print("*" * n)
    
afficher_boite(123)