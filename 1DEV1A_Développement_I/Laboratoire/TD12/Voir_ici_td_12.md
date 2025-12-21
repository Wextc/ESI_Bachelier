### Dictionnaire

<b>Qu’est-ce qu’un dictionnaire ?</b>

Un dictionnaire est une structure de données qui stocke des informations sous forme de clé → valeur.

Dictionnaire contient donc des paires clef-valeur.

```
# cle = valeur

```

<b>Caractéristiques</b>

À chaque clef du dictionnaire, il y a exactement une valeur associée.

```
d = {
    "a": 1,
    "b": 2
}

## L'exemple suivant est incorrect.
d = {
    "a","c": 1,     # Ceci est interdit car il y a 2 clef pour la valeur 1.
    "b": 2
}

```

Les clefs doivent être hachables.

Une clef doit être immuable (ne change pas).

```
# Les clefs qui sont autorisé
d = {
    1: "entier",
    3.14: "flottant",
    "nom": "texte",
    (1, 2): "tuple"
}

# La clefs qui sont interdites

d = {
    [1, 2]      # liste
    {"a": 1}    # dictionnaire
}

```

Les valeurs peuvent être de n’importe quel type

```
d = {
    "notes": [12, 15, 18],   # liste
    "age": 15,              # entier
    "actif": True,          # booléen
    "profil": {"ville": "Paris"}  # dictionnaire
}


```

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1DEV1A_Développement_I/Laboratoire/TD12/img/1.2.png)

<b>Création littérale</b>

Créer un dictionnaire directement avec des accolades {}.

```
eleve = {"nom": "Sara", "age": 14, "classe": "3e"}

```

<b>Création en compréhension</b>

Créer un dictionnaire à partir d’un itérable (comme une liste).

```
carres = {x: x*x for x in range(5)}
print(carres)

# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

lettres = {c: ord(c) for c in "abcde"}
print(lettres)

# {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101}

```

<b>Dictionnaire vide</b>

```
d1 = {}

d2 = dict()

```

<b>Dictionnaire vide</b>

```
d1 = {}

d2 = dict()

```

<b>Accès via []</b>

Permet d’obtenir la valeur associée à une clé.

```
print(eleve["nom"])

```

<b>Modifier ou ajouter une paire</b>

```
print("age" in eleve)      # True

print("note" in eleve)     # False

```

<b>Tester l’existence d’une clé</b>

```
print("age" in eleve)      # True

print("note" in eleve)     # False

```

<b>Parcourir les clés</b>

```
for key in eleve:
    print(key)

```

<b>Parcourir les paires clé / valeur</b>

```
for key, value in eleve.items():
    print(key, value)

```

<b>1.2.2 D’autres opérations utiles</b>

<b>Accès via .get()</b>

```
print(eleve.get("note", 0))

```

<b>Nombre de clés</b>

```
print(len(eleve))

```

<b>Liste des clés</b>

```
print(list(eleve))

```

<b>Supprimer une clé</b>

```
del eleve["classe"]

```

<b>Récupérer et supprimer une valeur (pop)</b>

```
age = eleve.pop("age", None)
print(age)

```

<b>Supprimer tout le contenu</b>

```
eleve.clear()

```

<b>Copier un dictionnaire</b>

```
copie = eleve.copy()

```

<b>Résumé rapide</b>

```
{} → créer

[] / .get() → accéder

in → tester

items() → parcourir

pop() / del → supprimer

copy() → copier

```

###1.3 Usages idiomatiques

« Idiomatique » = faire les choses à la façon du langage, de manière simple et lisible, pas forcément de la manière “brute” ou trop longue.

```

# C’est un dictionnaire simple : une clé → une valeur.
profs_dev1 = {
    "A111": "bej", "A112": "mbr", "A121": "sre", "A122": "dbo", "A131": "abe",
    "A132": "clg", "A211": "bej", "A212": "cuv", "A221": "sre", "A222": "sdr",
    "A231": "hal", "A232": "nri", "A311": "bis", "A312": "clg", "A321": "cuv",
    "A322": "hal", "A331": "srv", "A332": "gba", "A341": "pbt", "A342": "tni"
    }


# Compter les occurrences d’une valeur
# compter.py
groupes_par_prof = {
    "abe": 1, "bej": 2, "bis": 1, "clg": 2, "cuv": 2,
    "dbo": 1, "gba": 1, "hal": 2, "mbr": 1, "nri": 1,
    "pbt": 1, "sdr": 1, "sre": 2, "srv": 1, "tni": 1
}


#  Créer un "objet" avec des propriétés. Par exemple
une_personne = {
    "prénom": "Guillaume",
    "nom": "Apollinaire",
    "naissance": (26, 8, 1880)  # jour, mois, année
}

autre_personne = {
    "prénom": "Jean-Jacques",
    "nom": "Goldmann",
    "naissance": (11, 10, 1951)
}

# On peut combiner les deux idées : chaque étudiant a un matricule unique → dictionnaire d’informations.

# bdd.py
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

# Accès aux données

print(etudiants[52104]["nom"])  # Apollinaire


# Ajouter un étudiant
etudiants[67890] = {
    "prénom": "Alice",
    "nom": "Dupont",
    "groupe": "A111"
}

# Parcourir tous les étudiants

for matricule, info in etudiants.items():
    print(matricule, info["prénom"], info["groupe"])



```

### 2 Découverte

#### Exercice 2:

<b>Obtenir le prof du groupe A311</b>

```
profs_dev1 = {
    "A111": "bej", "A112": "mbr", "A121": "sre", "A122": "dbo", "A131": "abe",
    "A132": "clg", "A211": "bej", "A212": "cuv", "A221": "sre", "A222": "sdr",
    "A231": "hal", "A232": "nri", "A311": "bis", "A312": "clg", "A321": "cuv",
    "A322": "hal", "A331": "srv", "A332": "gba", "A341": "pbt", "A342": "tni"
}

prof_A311 = profs_dev1["A311"]
print(prof_A311)

```

<b> Obtenir le nombre de groupes de Mme Cuvelier (cuv).</b>

```
groupes_par_prof = {
    "abe": 1, "bej": 2, "bis": 1, "clg": 2, "cuv": 2,
    "dbo": 1, "gba": 1, "hal": 2, "mbr": 1, "nri": 1,
    "pbt": 1, "sdr": 1, "sre": 2, "srv": 1, "tni": 1
}
nombre_groupes_cuv = groupes_par_prof["cuv"]
# Obtenir le nombre de groupes de Mme Cuvelier (cuv).
print("Le nombre de groupes de Mme Cuvelier (cuv) ",nombre_groupes_cuv)

```

<b>Obtenir le groupe de l’étudiant ayant le matricule 52104</b>

```
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

print(groupe_52104)


```

<b>Afficher tou·tes les enseignant·es de dev1 (sans doublons)</b>

```# Afficher tou·tes les enseignant·es de dev1 (sans doublons)
profs_dev1 = {
    "A111": "bej", "A112": "mbr", "A121": "sre", "A122": "dbo", "A131": "abe",
    "A132": "clg", "A211": "bej", "A212": "cuv", "A221": "sre", "A222": "sdr",
    "A231": "hal", "A232": "nri", "A311": "bis", "A312": "clg", "A321": "cuv",
    "A322": "hal", "A331": "srv", "A332": "gba", "A341": "pbt", "A342": "tni"
}

enseignants_sans_doublon = set(profs_dev1.values())
print("Tous les groupes des prof sans doublons est ", enseignants_sans_doublon)

```

#### Exercice 3:
