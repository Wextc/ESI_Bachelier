chaine=input("Entrez un mot : ")
premiere_lettre = chaine[0]
derniere_lettre = chaine[len(chaine)-1]

if chaine == 0:
    print("Vous n'avez rien entré.")
else:
    if  premiere_lettre == derniere_lettre:
        print("La première et la dernière lettre sont les mêmes.")
    else:
        print("La première et la dernière lettre ne sont pas les mêmes.")
