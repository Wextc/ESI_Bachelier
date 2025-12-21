profs_dev1 = [
"bej", "mbr", "sre", "dbo", "abe",
"clg", "bej", "cuv", "sre", "sdr",
"hal", "nri", "bis", "clg", "cuv",
"hal", "srv", "gba", "pbt", "tni"
]

 # résultat attendu:

{
"abe": 1, "bej": 2, "bis": 1, "clg": 2, "cuv": 2,
"dbo": 1, "gba": 1, "hal": 2, "mbr": 1, "nri": 1,
"pbt": 1, "sdr": 1, "sre": 2, "srv": 1, "tni": 1
}


# Input list - Output dictionnaire.



def compte_repetition(liste):
    resultat = {}
    for item in liste:
        if item in resultat:
            resultat[item] += 1
        else:
            resultat[item] = 1
        
    return resultat
    
 

print(compte_repetition(profs_dev1))

