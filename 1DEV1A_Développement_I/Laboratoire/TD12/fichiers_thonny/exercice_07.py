
def mots():
    resultat = []
    while True:
        choix = str(input("Choisissez les mots :"))
        if choix == "":
            break
        resultat.append(choix)
    return resultat

data = mots()
def compter_occurrence(data):
    obj = {}
    resultat = []
    for item in data:
        if item in obj:
            obj[item] += 1
        else:
            obj[item] = 1
    maximum = max(obj.values())
    for clef, valeur in obj.items():
        if valeur == maximum:
            resultat.append(clef)
    return resultat
        
        
print(compter_occurrence(data))
