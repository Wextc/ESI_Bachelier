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

<b> Que se passe-t-il si on essaye de</b>

<b> donner deux valeurs à une même clef ?</b>

```

```

<b> donner la même valeur à deux clefs différentes ?</b>

Le dictionnaire ne peut pas avoir deux valeurs pour la même clé.

Python garde seulement la dernière valeur.

Ici, d["a"] vaudra 2, pas 1.

La première valeur est écrasée.

```
d = {"a": 1, "a": 2}

```

<b> accéder (par exemple afficher) à une clef qui n’existe pas dans le dictionnaire ?</b>

C’est parfaitement autorisé.

Chaque clé est unique, donc Python accepte.

Les deux clés a et b pointent vers la même valeur 1

- utiliser une liste comme clef ?

```
d = {"a": 1, "b": 1}

```

#### Exercice 4:

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1DEV1A_Développement_I/Laboratoire/TD12/img/exercice_04.png)

```
jours = {
    "lundi": "Monday",
    "mardi": "Tuesday",
    "mercredi": "Wednesday",
    "jeudi": "Thursday",
    "vendredi": "Friday",
    "samedi": "Saturday",
    "dimanche": "Sunday"
}

```

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1DEV1A_Développement_I/Laboratoire/TD12/img/exercice_05.png)

```
profs_dev1 = [
"bej", "mbr", "sre", "dbo", "abe",
"clg", "bej", "cuv", "sre", "sdr",
"hal", "nri", "bis", "clg", "cuv",
"hal", "srv", "gba", "pbt", "tni"
]

def compte_repetition(liste):
    resultat = {}
    for item in liste:
        if item in resultat:
            resultat[item] += 1
        else:
            resultat[item] = 1

    return resultat



print(compte_repetition(profs_dev1))

```

La fonction compte_repetition prend en paramètre une liste d’éléments. Elle a pour objectif de compter combien de fois chaque élément apparaît dans cette liste.

Au début de la fonction, on crée un dictionnaire vide appelé resultat. Ce dictionnaire servira à stocker les éléments de la liste comme clés, et leur nombre d’apparitions comme valeurs.

Ensuite, la fonction parcourt la liste élément par élément à l’aide d’une boucle for. À chaque passage dans la boucle, l’élément courant est stocké dans la variable item.

Pour chaque élément, la fonction vérifie s’il est déjà présent comme clé dans le dictionnaire resultat.

Si c’est le cas, cela signifie que l’élément a déjà été rencontré auparavant. On augmente donc la valeur associée à cette clé de 1 pour compter une apparition supplémentaire.

Si ce n’est pas le cas, cela signifie que l’élément apparaît pour la première fois. On l’ajoute alors au dictionnaire avec la valeur 1, indiquant une première occurrence.

Une fois que tous les éléments de la liste ont été parcourus et comptés, la fonction retourne le dictionnaire resultat. Celui-ci contient, pour chaque élément de la liste, le nombre total de fois où il apparaît.

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1DEV1A_Développement_I/Laboratoire/TD12/img/exercice_06.png)

```
data = {
"abe": 1, "bej": 2, "bis": 1, "clg": 2, "cuv": 2,
"dbo": 1, "gba": 1, "hal": 2, "mbr": 1, "nri": 1,
"pbt": 1, "sdr": 1, "sre": 2, "srv": 1, "tni": 1
}



```

<b>Remarque :</b>

```
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

```

On a un dictionnaire data où chaque clé est un nom et chaque valeur un nombre. La fonction cles_valeur_max sert à trouver toutes les clés dont la valeur est la plus grande. Elle commence par créer une liste vide res pour stocker les résultats. Ensuite, elle vérifie si le dictionnaire est vide avec if not d: ; si c’est le cas, elle retourne directement la liste vide. Sinon, elle calcule la valeur maximale du dictionnaire avec maximum = max(d.values()). Puis, elle parcourt toutes les paires clé-valeur du dictionnaire avec for clef, valeur in d.items(): et, à chaque itération, elle compare la valeur actuelle avec le maximum. Si elles sont égales, la clé correspondante est ajoutée à la liste res. Enfin, la fonction retourne cette liste. Pour le dictionnaire donné, la liste finale contient toutes les clés dont la valeur est 2 : ['bej', 'clg', 'cuv', 'hal', 'sre'].

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1DEV1A_Développement_I/Laboratoire/TD12/img/exercice_07.png)

```

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


```

Ce programme sert à demander à l’utilisateur de saisir des mots, puis à afficher le ou les mots les plus souvent saisis.

La fonction mots() crée une liste vide appelée resultat et utilise une boucle infinie while True pour demander à l’utilisateur de taper des mots un par un. À chaque itération, le programme lit l’entrée avec input("Choisissez les mots :"). Si l’utilisateur appuie sur Entrée sans rien taper, la boucle se termine grâce à break. Sinon, le mot saisi est ajouté à la liste resultat. Quand la boucle se termine, la fonction retourne la liste complète des mots saisis.

La variable data stocke le résultat de la fonction mots(), c’est-à-dire la liste de tous les mots que l’utilisateur a entrés.

La fonction compter_occurrence(data) analyse cette liste pour déterminer quels mots apparaissent le plus souvent. Elle crée d’abord un dictionnaire obj pour compter les occurrences de chaque mot. Pour chaque mot dans la liste data, si le mot est déjà présent dans le dictionnaire, son compteur est augmenté de 1 ; sinon, il est ajouté avec une valeur de 1.

Ensuite, la fonction cherche la fréquence maximale avec maximum = max(obj.values()). Elle parcourt à nouveau le dictionnaire et ajoute dans la liste resultat tous les mots dont la fréquence est égale à cette valeur maximale.

Enfin, la fonction retourne la liste des mots les plus fréquents.

Le programme principal affiche le résultat avec print(compter_occurrence(data)).

Ainsi, après que l’utilisateur a saisi ses mots, le programme renvoie la ou les clés qui ont été tapées le plus souvent.
