profs_dev1 = {
    "A111": "bej", "A112": "mbr", "A121": "sre", "A122": "dbo", "A131": "abe",
    "A132": "clg", "A211": "bej", "A212": "cuv", "A221": "sre", "A222": "sdr",
    "A231": "hal", "A232": "nri", "A311": "bis", "A312": "clg", "A321": "cuv",
    "A322": "hal", "A331": "srv", "A332": "gba", "A341": "pbt", "A342": "tni"
}

prof_A311 = profs_dev1["A311"]
# Obtenir le prof du groupe A311
print("Le prof du groupe A311 est ",prof_A311)
groupes_par_prof = {
    "abe": 1, "bej": 2, "bis": 1, "clg": 2, "cuv": 2,
    "dbo": 1, "gba": 1, "hal": 2, "mbr": 1, "nri": 1,
    "pbt": 1, "sdr": 1, "sre": 2, "srv": 1, "tni": 1
}
nombre_groupes_cuv = groupes_par_prof["cuv"]
# Obtenir le nombre de groupes de Mme Cuvelier (cuv).
print("Le nombre de groupes de Mme Cuvelier (cuv) ",nombre_groupes_cuv)

# Obtenir le groupe de l’étudiant ayant le matricule 52104
etudiants = {
    52104: {
        "prénom": "Guillaume",
        "nom": "Apollinaire",
        "groupe": "A321"
    },
    45371: {
        "prénom": "Jean-Jacques",
        "nom": "Goldmann",
        "groupe": "A123"
    }
}
groupe_52104 = etudiants[52104]["groupe"]
print("Le groupe de l'’étudiant ayant le matricule 52104 est ",groupe_52104)

# Afficher tou·tes les enseignant·es de dev1 (sans doublons)
profs_dev1 = {
    "A111": "bej", "A112": "mbr", "A121": "sre", "A122": "dbo", "A131": "abe",
    "A132": "clg", "A211": "bej", "A212": "cuv", "A221": "sre", "A222": "sdr",
    "A231": "hal", "A232": "nri", "A311": "bis", "A312": "clg", "A321": "cuv",
    "A322": "hal", "A331": "srv", "A332": "gba", "A341": "pbt", "A342": "tni"
}

enseignants_sans_doublon = set(profs_dev1.values())
print("Tous les groupes des prof sans doublons est ", enseignants_sans_doublon)

