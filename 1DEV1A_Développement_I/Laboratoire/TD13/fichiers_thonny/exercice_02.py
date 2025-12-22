
inventaire = {
    "potirons": 15,
    "courgettes": 20,
    "poireaux": 17,
    "brocolis": 23,
    "oignons": 32
    }

def choix_utilisateur():
    resultat = {}
    while True:
        legume = str(input("Veuillez entrer votre choix : potirons, courgettes, poireaux, brocolis et oignons."))
        unite = input("Combient en voulez-vous?")
        if legume == "":
            break
        resultat[legume] = unite
        inventaire[legume] -= int(unite)
    return resultat
        


def stock(data):
    reslutat = {}
    print(inventaire)

data = choix_utilisateur()
print(stock(data))


"""
 print("Il a aujourd’hui", inventaire["potirons"], "potirons,", 
          inventaire["courgettes"], "courgettes,", 
          inventaire["poireaux"], "poireaux,", 
          inventaire["brocolis"], "brocolis et", 
          inventaire["oignons"], "oignons")

"""