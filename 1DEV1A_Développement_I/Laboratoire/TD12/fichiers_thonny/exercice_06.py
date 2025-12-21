data = {
"abe": 1, "bej": 2, "bis": 1, "clg": 2, "cuv": 2,
"dbo": 1, "gba": 1, "hal": 2, "mbr": 1, "nri": 1,
"pbt": 1, "sdr": 1, "sre": 2, "srv": 1, "tni": 1
}


def cles_valeur_max(d):
    res = []
    if not d:
        return res
    maximum = max(d.values())
    for clef, valeur in d.items():
        if valeur == maximum:
            res.append(clef)
    return res

print(cles_valeur_max(data))


"""

Si je veux sélectionner en fonction des clés-valeurs j'utilise items()

items() → clés + valeurs
for clef, valeur in data.items():
    print(valeur)
    print(clef)
Si je veux sélectionner en fonction des clés j'utilise keys()
keys() → seulement clés
for clef in data.keys():
    print(clef)

Si je veux sélectionner en fonction des values j'utilise values
values() → seulement valeurs
for valeur in data.values():
    print(valeur)

"""