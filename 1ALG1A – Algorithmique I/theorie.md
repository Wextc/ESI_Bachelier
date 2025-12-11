## Chapitre 2

### Algorithmes séquentiels

- Algorithme séquentiel

Un algorithme séquentiel (ou linéaire) exécute une suite d’instructions dans l’ordre, une seule fois, sans alternatives ni boucles.

Données

Les algorithmes manipulent différents types de données selon le contexte (ingrédients, briques, rues…).
En informatique, les données de base sont :

Nombres

Booléens

Chaînes de caractères

- Variables

Les variables stockent des valeurs en mémoire et peuvent changer pendant l’exécution de l’algorithme.

Chaque variable a un type, qui détermine la nature des données qu’elle peut contenir.

- Types principaux

| Type    | Contenu possible | Remarques                           |
| ------- | ---------------- | ----------------------------------- |
| Entier  | 0, 5, 42, …      | Éléments de ℤ                       |
| Réel    | 2,5, 0,333…      | Peut aussi contenir des entiers     |
| Booléen | vrai / faux      | Deux seules valeurs possibles       |
| Chaîne  | "texte", "x", "" | Suite de caractères, peut être vide |

- Types et langages

Les types peuvent varier selon les langages (ex. Java : byte, short, int, long).

Les nombres réels sont souvent tronqués à cause de la capacité mémoire.

Certains langages (ex. Python) déterminent le type d’une variable automatiquement à partir de son contenu.

En algorithmique, on utilise des types simples et généraux pour la pédagogie, avant de les adapter dans un langage spécifique.

- Forme générale d’un algorithme

Forme générale d’un algorithme

Un algorithme suit généralement la structure suivante :

```
algorithme [nom]
    // déclaration des données
    // lecture des données
    // instructions agissant sur les données
    // écriture du résultat
fin
```

algorithme [nom] : ligne introductive (en-tête) qui donne un nom à l’algorithme.

Déclaration des données : section où l’on définit les variables qui seront utilisées.

Lecture des données : section où l’on récupère les valeurs fournies par l’utilisateur (Lire).

Instructions agissant sur les données : section où l’on effectue les calculs ou traitements nécessaires.

Écriture du résultat : section où l’on affiche les résultats (Écrire).

fin : ligne finale qui indique la fin de l’algorithme.

- Déclaration des données

La déclaration des données liste les variables utilisées dans l’algorithme.

Elle résulte de la compréhension du problème et de l’identification des données nécessaires pour obtenir le résultat attendu.

La forme générale d’une déclaration est :

nom_de_variable : type

Le nom de variable doit être clair et refléter son rôle.

Les noms peuvent être composés de plusieurs mots, mais sans espaces, par exemple :

nombreSpectateurs, prix_beurre, plaqueImmatriculation

Plusieurs variables peuvent être déclarées sur une seule ligne :

```
nombre1, nombre2, nombre3 : entier

```

Les noms peuvent contenir des chiffres, mais pas au début.

Il est conseillé d’éviter des variables différant uniquement par la casse (nombrePersonnes ≠ NombrePersonnes).

Bien que facultative dans certains langages (comme Python), la déclaration des données est utile à titre pédagogique pour structurer l’algorithme.

Exemples de types de variables :

```
quantité : entier

prix : réel

adresse : chaîne

exact : booléen

```

- Lecture des données

La lecture des données permet à l’ordinateur de connaître les valeurs des variables déclarées.

Au départ, les variables sont vides ou non définies, il faut leur attribuer une valeur pour pouvoir les utiliser.

L’utilisateur fournit ces valeurs via l’instruction :

```
lire variable

```

Cette instruction demande à l’utilisateur d’entrer une valeur (ex. clavier ou clic), qui est affectée à la variable.

On parle aussi d’affectation externe.

Il est possible de lire plusieurs variables à la fois :

```
Lire variable1, variable2, variable3, ...

```

Cela équivaut à plusieurs instructions de lecture successives.

Dans un programme réel, la lecture peut être plus complexe : interface graphique, messages explicatifs, vérification de la validité des valeurs… Mais pour l’algorithmique, la lecture reste simple et directe.

- Instructions agissant sur les données

Cette section transforme les données, calcule de nouvelles valeurs et les stocke éventuellement dans de nouvelles variables.

Les instructions principales sont les affectations internes, de la forme :

variable ← expression

Une expression peut être :

Une formule mathématique avec opérateurs et variables

Une seule variable

Une valeur numérique

Principaux opérateurs arithmétiques :

```
+ : addition

- : soustraction

* : multiplication

/ : division réelle

DIV : division entière

MOD : reste de la division entière

Exemples d’affectation :

a ← b + 2*c

x ← y

delta ← b*b – 4*a*c

prixAvecTVA ← prixHorsTVA*1,21

unité ← nombre MOD 10


siècle ← année DIV 100 + 1


```

Les règles de priorité des opérations doivent être respectées, avec usage possible de parenthèses pour lever les ambiguïtés.

Le type de l’expression doit correspondre au type de la variable à gauche.

On peut utiliser des fonctions mathématiques classiques :

```
sin(x), cos(x), log(x), exp(x), sqrt(x)

Exposant : x\*\*y (x élevé à la puissance y)

```

- Écriture du résultat

Une fois les variables calculées, il faut communiquer le(s) résultat(s) à l’utilisateur.

L’instruction utilisée est :

Écrire variable

Elle affiche le contenu de la variable à l’écran.

En algorithmique, le format d’affichage n’est pas pris en compte : seul le contenu logique importe.

Dans un programme réel, le programmeur peut améliorer l’affichage (emplacement à l’écran, mise en forme, couleur, cadre explicatif…), mais ce n’est pas l’objet de l’algorithme.

- Commentaires

Les commentaires permettent d’ajouter des remarques ou explications pour le lecteur ou le programmeur.

Ils ne sont pas exécutés par l’algorithme.

Syntaxes possibles :

// ceci est un commentaire

# ceci est un commentaire

/_ ceci est un commentaire _/

Exemples

Somme de deux entiers :

```
algorithme somme
x, y, somme : entier
lire x, y
somme ← x + y
écrire somme
fin
```

Prix total à payer :

```
algorithme prixTotal
prixUnité, prixTotal : réel
quantité : entier
lire prixUnité
lire quantité
prixTotal ← prixUnité * quantité
écrire "Le prix total à payer est : ", prixTotal
fin

```

- Traçage d’algorithme

Traçage : suivre l’évolution des variables pas à pas pour comprendre ou vérifier un algorithme.

Utile pour :

Valider que l’algorithme produit le résultat attendu

Repérer les erreurs logiques

Méthode :

On utilise un tableau :

Colonnes : une par variable

Lignes : chaque modification d’une variable dans l’ordre d’exécution

Une colonne peut indiquer le numéro de ligne concerné

Exemple pour l’algorithme somme avec x=18 et y=24 :

```
Ligne	x	y	somme
2
3	18	24
4	18	24	42


```

- Mots réservés

Certains mots ont une signification spéciale dans l’algorithmique :

algorithme, lire, écrire, fin, si, pour, tant que, etc.

Ces mots-clés ne doivent pas être utilisés comme noms de variables ou d’algorithmes.

Qualité d’un algorithme

Un bon algorithme doit répondre à trois critères principaux :

Validité :

Fournir le résultat attendu pour toutes les situations prévues

Vérifiable par des tests couvrant différents cas

Lisibilité :

Compréhensible dès la lecture

Facilite la correction et la modification

Bonnes pratiques : noms de variables pertinents, indentation correcte, commentaires utiles

Performance :

Résolution rapide et efficace du problème

Optimisation possible en limitant le nombre d’étapes ou de variables

Liée à la complexité (étudiée plus tard)

Exemple : calcul de l’âge du capitaine

ageCapitaine1 : variables claires et lisibles, algorithme valide.

ageCapitaine2 : très concis mais moins lisible (x n’indique pas son rôle).

ageCapitaine3 : lisible et valide, commentaires utiles.

ageCapitaine4 : noms de variables humoristiques (haddock, tintin), valide mais peu clair.

Conclusion : un algorithme doit être valide, lisible et compréhensible, pas seulement fonctionner.

Exemples:

Voici une série d’algorithmes qui calculent chacun l’âge du capitaine. La plupart ont
des qualités et des défauts, pouvez-vous les identifier ? Sont-ils tous valides ?
Quelles pratiques vous semblent « bonnes » ou « mauvaises » ? Tous les
commentaires sont-ils utiles ? Quel est selon vous le meilleur algorithme des 4 ?

```
algorithme ageCapitaine1
    age : entier
    année : entier
    lire année // année de naissance du capitaine
    age <- 2025 – année // cette instruction calcule son âge
écrire "L’âge du capitaine est : ", age // affichage de l’âge
fin

```

```
algorithme ageCapitaine2
    x : entier
    lire x
    écrire "L’âge du capitaine est : ", 2025 – x
fin

```

```
algorithme ageCapitaine3
    // N.B. l’algorithme ne tient pas compte des jours et des mois,
    // à améliorer quand on aura vu les alternatives...
    ageCapitaine : entier
    annéeNaissance : entier
    lire annéeNaissance
    ageCapitaine <- 2025 – annéeNaissance
    écrire "L’âge du capitaine est : ", ageCapitaine
fin

```

```
algorithme ageCapitaine4
    haddock : entier
    tintin : entier
    lire tintin
    haddock <- 2025 – tintin
    écrire "L’âge du capitaine est : ", haddock
fin

```

## Exercices

<b>Exercice 1</b>

Quel type de variable, parmi les 4 types présentés dans ce chapitre, choisiriez-vous
pour stocker les types de données suivants ?
o l’age d’une personne
o le poids d’une personne
o le nom d’une personne
o un code postal belge
o un numéro de maison
o une adresse email

| Donnée               | Type   |
| -------------------- | ------ |
| Âge d’une personne   | Entier |
| Poids d’une personne | Réel   |
| Nom d’une personne   | Chaîne |
| Code postal belge    | Entier |
| Numéro de maison     | Entier |
| Adresse email        | Chaîne |

---

<b>Exercice 2</b>

Tracer l’algorithme suivant, dans le cas où les nombres lus sont 4 et 10.

| Ligne | Instruction    | a   | b   | c   | Explication                          |
| ----- | -------------- | --- | --- | --- | ------------------------------------ |
| 3     | lire a, b      | 4   | 10  | —   | On lit a=4 et b=10                   |
| 4     | c ← a + 2\*b   | 4   | 10  | 24  | c = 4 + 2×10 = 24                    |
| 5     | a ← c DIV b    | 2   | 10  | 24  | a = 24 DIV 10 = 2 (division entière) |
| 6     | b ← b MOD a    | 2   | 0   | 24  | b = 10 MOD 2 = 0                     |
| 7     | écrire a, b, c | 2   | 0   | 24  | Résultat final                       |

<b>Exercice 3</b>

Tracer l’algorithme suivant, en supposant que les nombres lus sont 2 et 3.

```
algorithme bizarre
    x, y : entier
    lire x
    x <- 2*x
    y <- 3*x
    lire y
    y <- 3*y
    écrire y MOD x
fin
```

| Étape          | x   | y   | Commentaire         |
| -------------- | --- | --- | ------------------- |
| lire x (=2)    | 2   | ?   |                     |
| x ← 2\*x       | 4   | ?   | 2×2 = 4             |
| y ← 3\*x       | 4   | 12  | 3×4 = 12            |
| lire y (=3)    | 4   | 3   | Remplace l'ancien y |
| y ← 3\*y       | 4   | 9   | 3×3 = 9             |
| écrire y MOD x | 4   | 9   | 9 mod 4 = 1         |

<b>Exercice 4</b>

On voudrait dans l’algorithme suivant échanger le contenu des variables x et y de
sorte qu’à la ligne 7, les nombres s’affichent dans l’ordre inverse de leur lecture (par
exemple, si on lit 30 et 40, les nombres affichés seront – dans l’ordre – 40 et 30).
Compléter le code pour obtenir le résultat voulu. Aide : il faudra peut-être introduire
une variable supplémentaire pour réaliser cet exercice.

```
algorithme échange
    x, y : entier
    lire x, y
    ...
    ...
    ...
    écrire x, y
fin

```

```
algorithme échange
    x, y, t : entier
    lire x, y
    t ← x
    x ← y
    y ← t
    écrire x, y
fin

```

<b>Exercice 5</b>

Ecrire un algorithme qui calcule la surface d’un
triangle à partir des mesures de sa base et de
sa hauteur.
Par exemple, si la base mesure 6 cm et la
hauteur 4 cm, l’algorithme affichera 12 cm2.

```
algorithme surface_triangle:
    base, hauteur, surface : entier
    lire base, hauteur
    surface ← (base * hauteur) / 2
    écrire surface
fin


```

<b>Exercice 6</b>

Ecrire un algorithme qui calcule la vitesse d’un
véhicule en km/h, connaissant la distance qu’il
a parcourue en kilomètres et le temps du trajet
en minutes.
Attention aux unités, cet algorithme nécessite
une petite conversion de données...

La distance est en km.
Le temps est en minutes.
Pour obtenir la vitesse en km/h, on utilise :
vitesse = distance / (tempsMin / 60)
ce qui revient à :
vitesse = distance \* 60 / tempsMin

```
algorithme vitesse_vehicule
    distance, tempsMin, vitesse : entier
    lire distance, tempsMin
    vitesse ← distance * 60 / tempsMin
    écrire vitesse
fin

```

<b>Exercice 7</b>

Ecrire un algorithme qui lit un nombre entier de 3 chiffres, et affiche ensuite
séparément les chiffres des centaines, dizaines et unités.
Exemple : si le nombre lu est 723, l’algorithme affichera par exemple :
• le chiffre des centaines est 7
• le chiffre des dizaines est 2
• le chiffre des unités est 3

```
algorithme decomposition_nombre:
    n, centaines, dizaines, unites : entier
    lire n
    centaines ← n DIV 100
    dizaines ← (n MOD 100) DIV 10 //
    unites ← n MOD 10
    écrire centaines, dizaines, unites
fin

```

Si n=723 alors n MOD 100 veut dire 7 × 100 + 23.
Si n=723 alors n MOD 10 veut dire 72 × 10 + 3.
Si n=723 alors n DIV 100 veut dire qu'on prend la division entière. => 7

<b>Exercice 8</b>

Le miroir d’un nombre entier est ce nombre
écrit en inversant l’ordre de ses chiffres. Par
exemple, le miroir de 189 est 981, et celui de
752 est 257.
Ecrire un algorithme qui lit un nombre entier de
3 chiffres, et affiche ensuite le miroir de ce
nombre. Vérifiez si votre algorithme fonctionne
aussi lorsque le nombre se termine par 1 ou 2
zéros.

```
algorithme miroir_nbre:
    n, centaine, dizaine, unités: entier
    lire n
    centaine ← n DIV 100
    dizaine ← (n MOD 100) DIV 10
    unité ← n MOD 10
    écrire unité, dizaine, centaine
fin
```

<b>Exercice 9</b>

Ecrire un algorithme qui convertit une durée
exprimée sous la forme de trois nombres
(heure, minute, seconde) en nombre total de
secondes.
Par exemple, pour 12h 3’ 40’’, l’algorithme
affichera 43420 secondes.

```
algorithme conversion_HMS:
    heures, minutes, secondes, total:entier
    lire heures, minutes, secondes
    total ← heures * 3 600 + minutes * 60 + secondes
    écrire total
fin
```

<b>Exercice 10</b>

On fait ici l'inverse. On part du nombre pour trouver les heures.

La mainière inverse.

```
algorithme inverse:
    heures, minutesn secondes, total: entier
    lire total

    heures ← total DIV 3600
    total ←  total MOD 3600
    minutes ←  total  DIV 60
    secondes ←  total DIV 60
    écrire heures, mintes, secondes
fin
```

Exemple : 43420 secondes

heures ← 43420 DIV 3600 = 12

total ← 43420 MOD 3600 = 220

minutes ← 220 DIV 60 = 3

secondes ← 220 MOD 60 = 40

→ Résultat affiché : 12 h 3 min 40 s

## Chapitre 3

<b>Les structures alternatives et les conditions</b>

- Définition :

Une condition est une expression qui a une valeur booléenne (vrai ou faux).

Elle peut être une variable booléenne ou une expression calculée à partir des variables de l’algorithme.

- Fonctionnement :

Si la condition est vraie, le premier bloc d’instructions s’exécute et le second est ignoré.

Si la condition est fausse, le deuxième bloc d’instructions s’exécute et le premier est ignoré.

Exemple pratique :

    Lecture de deux nombres x = 4 et y = 1.

    Condition : x > y → vraie → variable max = x = 4.

    Le bloc “sinon” n’est pas exécuté.

    Lecture de x = 4 et y = 6.

- Condition : x > y → fausse → variable max = y = 6.

Le bloc “si” n’est pas exécuté.

Réflexion :

Si x et y sont égaux, que se passe-t-il ?

L’algorithme reste valide, mais si la condition est modifiée en x ≥ y, le bloc “si” sera exécuté lorsque les deux nombres sont égaux, ce qui peut changer le comportement.

<b>Alternative sans alternative</b>

Alternative sans alternative
Parfois, une action ne doit être réalisée que si une condition est vraie, et rien n’est prévu si elle est fausse. On parle alors de structure “si… alors” sans sinon. Par exemple, on peut écrire “si la personne est mineure, afficher ‘trop jeune’”. Si elle n’est pas mineure, aucune instruction n’est exécutée. Cette forme est simple et permet de gérer des situations où on ne souhaite agir que dans un seul cas particulier.

```
algorithme casino
    age : entier
    lire age
    si age < 18 alors
        écrire "trop jeune pour entrer au casino !"
    fin si
fin
```

<b>Alternatives multiples</b>

Dans certaines situations, plusieurs cas possibles doivent être distingués, mais un seul d’entre eux sera exécuté. C’est le cas des alternatives multiples. On utilise alors des structures en cascade : “si… alors”, “sinon si… alors”, et éventuellement un “sinon” final. Les conditions sont testées dans l’ordre, et dès qu’une condition est vraie, le bloc correspondant est exécuté, et les autres blocs sont ignorés. Par exemple, on peut classifier une personne en “mineur”, “majeur” ou “senior” selon son âge.

```
algorithme catégorie
    age : entier
    lire age
    si age ≥ 60 alors
        écrire "La personne est un senior"
    sinon si age ≥ 18
        écrire "La personne est majeure"
    sinon
        écrire "La personne est mineure"
    fin si
fin
```

<b>Structure « selon que »</b>

Cette structure est une variante des alternatives multiples, utilisée pour choisir parmi plusieurs valeurs possibles d’une même variable. Elle permet d’exécuter différents blocs d’instructions selon que la variable prend telle ou telle valeur. C’est souvent une alternative plus lisible et concise que de multiplier les “si… alors” pour chaque valeur.

```
algorithme localExamen
    groupe : entier
    local : chaîne
    lire groupe
    selon que groupe vaut
        111, 112, 121, 122 : local  "004"
        131, 132 : local  "003"
        211, 212 : local  "101"
        221, 222 : local  "102"
        231, 232 : local  "103"
        autre : local  "105"
    fin selon
    écrire "L’examen a lieu au local", local
fin
```

<b>Les varirables booléennes</b>

Ces variables n’ont que 2 possibilités de contenu : vrai ou faux.

Il n’est pas d’usage de leur donner un contenu par une affectation externe (lire),
mais plutôt par une affectation interne, via une expression qui a elle-même une
valeur booléenne (par ex. en utilisant les opérateurs de comparaison =, <, >,...).

```
algorithme parité
   nombre : entier
   estPair : booléen
   lire nombre
       estPair <- nombre MOD 2 = 0
   si estPair alors
       écrire "Le nombre est pair "
   sinon
       écrire "Le nombre est impair "
   fin si
fin

```

<b>La booléenne</b>

En algorithmique, un opérateur booléen est un outil qui permet de combiner une ou plusieurs conditions (ou expressions booléennes) pour obtenir une nouvelle condition, elle aussi vraie ou fausse. Les trois principaux opérateurs sont :

ET (conjonction) : l’expression p ET q est vraie seulement si p et q sont toutes les deux vraies. Dans tous les autres cas, elle est fausse.

OU (disjonction inclusive) : l’expression p OU q est vraie si au moins une des deux conditions est vraie ; elle est fausse seulement si les deux conditions sont fausses.

NON (négation) : l’expression NON p inverse la valeur de p : si p est vrai, NON p sera faux, et inversement.

Lorsque plusieurs opérateurs apparaissent dans une même expression, il est conseillé d’utiliser des parenthèses pour préciser l’ordre des calculs. Par exemple :

p ET (q OU r) n’est pas équivalent à (p ET q) OU r. Les parenthèses permettent de lever toute ambiguïté et d’éviter des résultats erronés.

En informatique, il existe également un concept appelé évaluation court-circuitée. Cela signifie que, dans certaines expressions, il n’est pas nécessaire d’évaluer toutes les conditions pour connaître le résultat final :

Pour p ET q : si p est faux, le résultat est forcément faux, et q n’est même pas évalué.

Pour p OU q : si p est vrai, le résultat est forcément vrai, et q n’est pas évalué.

Cette technique peut améliorer la rapidité d’exécution d’un algorithme et peut avoir un impact si l’évaluation de q est coûteuse ou comporte des effets secondaires.

![algo](https://github.com/Wextc/ESI_Bachelier/blob/main/1ALG1A%20%E2%80%93%20Algorithmique%20I/img/algo.png)

## Exercices

<b>Exercice 1</b>

Qu’affichent les algorithmes ci-dessous si les nombres lus au départ sont
successivement 2 et 3 ? Même question avec 4 et 1.

```
algorithme exercice1a
    a, b : entier
    lire a, b
    si a > b alors
        a <- a+2*b
    fin si
écrire a
fin

```

| Étape | Instruction                       | a   | b   | Condition a > b | Action exécutée  |
| ----- | --------------------------------- | --- | --- | --------------- | ---------------- |
| 1     | lire a, b                         | 2   | 3   | -               | -                |
| 2     | si a > b alors                    | 2   | 3   | 2 > 3 → faux    | Bloc non exécuté |
| 3     | a ← a + 2\*b (si condition vraie) | 2   | 3   | -               | Non exécuté      |
| 4     | écrire a                          | 2   | 3   | -               | Affiche 2        |

| Étape | Instruction    | a   | b   | Condition a > b | Action exécutée  |
| ----- | -------------- | --- | --- | --------------- | ---------------- |
| 1     | lire a, b      | 4   | 1   | -               | -                |
| 2     | si a > b alors | 4   | 1   | 4 > 1 → vrai    | Bloc exécuté     |
| 3     | a ← a + 2\*b   | 4   | 1   | -               | a = 4 + 2\*1 = 6 |
| 4     | écrire a       | 6   | 1   | -               | Affiche 6        |

```
algorithme exercice1b
    a, b, c : entier
    lire b, a // attention, piège !
    si a > b alors
        c <- a DIV b
    sinon
    c <- b MOD a
    fin si
    écrire c
fin

```

- Cas 1 : a = 2, b = 3

  Attention : les valeurs sont lues dans l’ordre b, a !

| Étape | Instruction               | a   | b   | Condition a > b | Action exécutée           |
| ----- | ------------------------- | --- | --- | --------------- | ------------------------- |
| 1     | lire b, a                 | 2   | 3   | -               | -                         |
| 2     | si a > b alors            | 2   | 3   | 2 > 3 → faux    | Bloc sinon exécuté        |
| 3     | c ← a DIV b / c ← b MOD a | 2   | 3   | -               | c ← b MOD a = 3 MOD 2 = 1 |
| 4     | écrire c                  | 2   | 3   | -               | Affiche 1                 |

Résultat affiché : 1

- Cas 2 : a = 4, b = 1

| Étape | Instruction    | a   | b   | Condition a > b | Action exécutée |
| ----- | -------------- | --- | --- | --------------- | --------------- |
| 1     | lire b, a      | 4   | 1   | -               | -               |
| 2     | si a > b alors | 4   | 1   | 4 > 1 → vrai    | Bloc si exécuté |
| 3     | c ← a DIV b    | 4   | 1   | -               | c = 4 DIV 1 = 4 |
| 4     | écrire c       | 4   | 1   | -               | Affiche 4       |

Résultat affiché : 4

```
algorithme exercice1c
    x1, x2 : entier
    ok : booléen
    lire x1, x2
    ok <- x1 > x2
    si ok alors
        ok <- ok ET x1 = 4
    sinon
        ok <- ok OU x2 = 3
    finsi
    si ok alors
        x1 <- x1 * 100
    fin si
    écrire x1 + x2
fin

```

- Exemples d'exécution

- Cas 1 : x1 = 2, x2 = 3

| Étape | Instruction           | x1  | x2  | ok   | Action exécutée                                                 |
| ----- | --------------------- | --- | --- | ---- | --------------------------------------------------------------- |
| 1     | lire x1, x2           | 2   | 3   | -    | -                                                               |
| 2     | ok ← x1 > x2          | 2   | 3   | faux | 2 > 3 → faux                                                    |
| 3     | si ok alors … sinon … | 2   | 3   | faux | Bloc sinon exécuté : ok ← ok OU x2=3 → ok = faux OU vrai = vrai |
| 4     | si ok alors …         | 2   | 3   | vrai | Bloc exécuté : x1 ← x1 \* 100 → x1 = 200                        |
| 5     | écrire x1 + x2        | 200 | 3   | vrai | Affiche 200 + 3 = 203                                           |

Résultat affiché : 203

- Cas 2 : x1 = 4, x2 = 1

| Étape | Instruction    | x1  | x2  | ok   | Action exécutée                                         |
| ----- | -------------- | --- | --- | ---- | ------------------------------------------------------- |
| 1     | lire x1, x2    | 4   | 1   | -    | -                                                       |
| 2     | ok ← x1 > x2   | 4   | 1   | vrai | 4 > 1 → vrai                                            |
| 3     | si ok alors …  | 4   | 1   | vrai | Bloc si exécuté : ok ← ok ET x1=4 → vrai ET vrai = vrai |
| 4     | si ok alors …  | 4   | 1   | vrai | Bloc exécuté : x1 ← x1 \* 100 → x1 = 400                |
| 5     | écrire x1 + x2 | 400 | 1   | vrai | Affiche 400 + 1 = 401                                   |

Résultat affiché : 401

Exemples d'exécution

- Cas 1 : x = 1, y = 3

| Étape | Instruction       | x   | y   | z   | ok   | Action exécutée                               |
| ----- | ----------------- | --- | --- | --- | ---- | --------------------------------------------- |
| 1     | lire x, y         | 1   | 3   | -   | -    | -                                             |
| 2     | z ← 10\*x + y + 1 | 1   | 3   | 14  | -    | Calcul z = 10\*1 + 3 + 1 = 14                 |
| 3     | selon que z vaut  | 1   | 3   | 14  | -    | Cas z=14 : ok ← z MOD 6 = 14 MOD 6 = 2 → faux |
| 4     | si ok alors       | 1   | 3   | 14  | faux | Bloc non exécuté                              |
| 5     | écrire z          | 1   | 3   | 14  | faux | Affiche 14                                    |

Résultat affiché : 14

- Cas 2 : x = 2, y = 3

| Étape | Instruction       | x   | y   | z   | ok   | Action exécutée                               |
| ----- | ----------------- | --- | --- | --- | ---- | --------------------------------------------- |
| 1     | lire x, y         | 2   | 3   | -   | -    | -                                             |
| 2     | z ← 10\*x + y + 1 | 2   | 3   | 24  | -    | Calcul z = 10\*2 + 3 + 1 = 24                 |
| 3     | selon que z vaut  | 2   | 3   | 24  | -    | Cas z=24 : ok ← z MOD 6 = 24 MOD 6 = 0 → vrai |
| 4     | si ok alors       | 2   | 3   | 24  | vrai | Bloc exécuté : z ← 2\*z → z = 48              |
| 5     | écrire z          | 2   | 3   | 48  | vrai | Affiche 48                                    |

Résultat affiché : 48

- Cas 3 : x = 3, y = 2

| Étape | Instruction       | x   | y   | z   | ok   | Action exécutée                                |
| ----- | ----------------- | --- | --- | --- | ---- | ---------------------------------------------- |
| 1     | lire x, y         | 3   | 2   | -   | -    | -                                              |
| 2     | z ← 10\*x + y + 1 | 3   | 2   | 33  | -    | Calcul z = 10\*3 + 2 + 1 = 33                  |
| 3     | selon que z vaut  | 3   | 2   | 33  | -    | Cas autre : ok ← z MOD 7 = 33 MOD 7 = 5 → faux |
| 4     | si ok alors       | 3   | 2   | 33  | faux | Bloc non ex                                    |

<b>Exercice 2</b>

1.Original :

```
si ok = vrai alors
    écrire nombre
fin si

```

Version concise :

```
si ok alors
    écrire nombre
fin si

```

On supprime = vrai, car ok est déjà un booléen.

2.Original :

```
si ok = faux alors
    écrire nombre
fin si
```

Version concise :

```
si NON ok alors
    écrire nombre
fin si

```

On utilise directement la négation pour tester faux.

3.Original :

```
si nerveux alors
    cool ← faux
sinon
    cool ← vrai
fin si
```

Version concise :

```
cool ← NON nerveux

```

Transformation en affectation directe avec négation.

```
si a > b alors
    ok <- faux
    sinon si a ≤ b alors
        ok <- vrai
fin si
```

A faire ...

```
si ok1 = faux alors
    ok2 <- faux
fin si

```

```
si ok1 = vrai alors
    si ok2 = faux alors
        ok3 <- ok1 ET ok2
    fin si
fin si

```

<b>Exercice 3</b>

Ecrire un algorithme qui indique si une personne est mineure ou majeure en fonction
de son âge.

```
algorithme age:
    si age < 18 alors:
        écrire "N'est majeur!"
    sinon age > 18:
        écrire "Est majeur!"
    fin si
fin

```

<b>Exercice 4</b>

Écrire un algorithme qui lit un nombre réel et affiche un message indiquant s'il est
strictement négatif, strictement positif ou nul.

```
algorithme AfficherSigne
    nombres:réel
    si réel > 0 alors:
        écrire "Le nombre est strictement positif."
    sinon réel < 0:
        écrire "Le nombre est strictement négatif."
    fin si
fin

```

<b>Exercice 5</b>

Écrire un algorithme qui résout une équation du second degré, déterminée par le
coefficient de x2, le coefficient de x et le terme indépendant. L’algorithme affichera la
ou les racine(s) de l’équation, ou un message adéquat si elle ne possède pas de
solution réelle.

ax² + bx + c

```
algorithme équation:
    a,b,c, x, x1, x2, delta :réels
    lire a,b,c
    si a = 0 alors:
        si b=0 alors:
            si c=0 alors:
                écrire "L'équation a une infinité de réponses."
            sinon:
                écrire "L'équation n'a pas de solution."
            fin si
        sinon:
            x <- -c / b
            écrire l'équation est du premier degré. x vaut", x
        fin si
    sinon:
        delta < b² - 4 * a * c
        si delta == 0:
            x1 = -b / 2*a*c
        si delta > O alors:
            x1 <- -b + sqrt(delta) / 2 * a
        sinon:
            x2 <- -b - sqrt(delta) / 2 * a
        fin si
    fin si
fin

```

<b> Exercice 6 </b>

Ecrire un algorithme qui lit 3 nombres et affiche la valeur du plus grand des trois.

```
algorithme comparaison:
    nombre_1, nombre_2, nombre_3, maximum: réels

    lire nombre_1, nombre_2, nombre_3

    maximum ← nombre_1

    si nombre_2 > maximum alors:
        maximum ← nombre_2
    fin si

    si nombre_3 > maximum alors:
        maximum ← nombre_3
    fin si

fin

```

<b> Exercice 7 </b>

Une personne est du signe astrologique des Poissons si elle
est née entre le 19 février et le 20 mars inclus. Ecrire un
algorithme qui indique si une personne possède ce signe ou
non à partir de sa date d’anniversaire (communiquée sous la
forme de 2 entiers jour et mois).

```
algorithme poisson
    année, mois, jours:entier
    lire jours, mois
    si (mois = 2 et jour = 19) ou (mois = 3 et jour = 20) alors:
        écrire "La personnes a le signe poisson."
    sinon:
        "La personne n'a pas le signe poisson."

```

<b> Exercice 8 </b>

Ecrire un algorithme qui affiche le nom du jour d’un jour du mois de novembre 2025,
donné par son numéro.
Par exemple, si on entre 6, l’ordinateur affichera « jeudi ».

```
algorithme jour_novembre:
    tableau_jours:chaine
    nombre_jour,i: entier
    i <- (nombre_jour-1) MOD 7
    tableau_jours <- ["samedi", "dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi"]
    jours_mois <- tableau_jours[i]
    écrire "Le jour du mois est pour ", nombre_jour, " est ",jours_mois.
fin
```

<b> Exercice 9 </b>

Ecrire un algorithme qui indique le nombre de jours qu’il y aura dans un mois de
l’année 2028. Le mois est donné sous forme d’un entier entre 1 et 12
Exemples :
• si mois = 1, l’algorithme affichera 31
• si mois = 2, l’algorithme affichera 29

```
algorithme jour_mois_2028:
    mois: entier
    lire mois
    si mois = 1 OU mois = 3 OU mois = 5 OU mois = 7 OU mois = 8 OU mois = 10 OU mois = 12 alors:
        écrire "Le nombre de jours de ce mois est ", mois
    fin si
fin

```

<b> Exercice 10 </b>

Ecrire un algorithme qui indique si une année est bissextile ou non.
Pour rappel, les années bissextiles on un numéro divisible par 4. Font exception à la
règle, les années multiples de 100, sauf les multiples de 400 qui eux sont bien
bissextiles ! Ainsi :

    2022 n'est pas bissextile
    2024 est bissextile
    2100 n'est pas bissextile
    2400 est bissextile

```
algorithme année_bissextile:
    année: entier
    lire année
    si (année mod4 = 0 ET année mod 100 !=0)  OU (année mod400 =0) alors:
        écrire année, "est bissextile"
    sinon
        écrire année, " n 'est pas bissextile."
    fin is
fin

```

<b> Exercice 11 </b>

Problème....

<b> Exercice 12 </b>

Dans une rue où se pratique le stationnement alterné, du 1 au 15 du mois, on se gare du côté des maisons ayant un numéro impair, et le reste du mois, on se gare de l'autre côté. Écrire un algorithme qui, sur base de la date du jour et du numéro de maison devant laquelle vous vous êtes arrêté, indique si vous êtes bien stationné ou non.

```
algorithme stationnement_alterné:
    jour, maison: entier
    lire jour, maison
    si (1 <= jour ET  15 >= jour) ET (maison mod2 != 0) alors:
        écrire  "Vous êtes bien stationné."
    sinon
        écrire "Vous êtes mal stationné."
    fin si
    si (16 <= jour ET  31 >= jour) ET (maison mod2 = 0) alors:
        écrire  "Vous êtes bien stationné."
    sinon "Vous êtes mal stationné."
    fin si
fin

```

<b> Exercice 13 </b>

Cet algorithme est destiné à prédire l’avenir, et il doit être infaillible ! Il lira au clavier les heures et les minutes, et il affichera l’heure qu’il sera une minute plus tard !

Par exemple, si l’utilisateur entre 21 puis 32,l’algorithme doit répondre « Dans une minute, il sera 21h 33 ».

```
Algorithme voir_futur:
    heure, minute : entier
    Lire heure, minute

    Si (minute >= 0 ET minute < 59) ET (heure >= 0 ET heure < 24) alors:
        minute <- minute + 1
        Écrire "Dans une minute, il sera ", heure, " h ", minute

    Sinon si minute = 59 alors:
        minute <- 0

        Si heure = 23 alors
            heure <- 0
        Sinon
            heure <- heure + 1
        Fin Si

        Écrire "Dans une minute, il sera ", heure, " h ", minute
    Fin Si
Fin


```

<b> Exercice 14 </b>

Ecrire un algorithme qui convertit un moment de la journée donnée au format HM (heure- minute) dans le format anglais.
Exemples :

• 3h10 devient 3:10 AM

• 12h25 devient 12:25 PM

• 15h21 devient 3:21 PM

```
algorithme HM:
    heure, minute: entier
    lire heure, minute
    si (heure >= 0 ET heure <= 11 ) ET (minute >= 0 ET minute <= 59) alors:
        si heure = 0 alors:
            heure <- 12
        sinon
            heure <- heure
        écrire heure, ":", minute "AM"
    sinon si (heure >= 12 ET heure <= 23) ET (minute >= 0 ET minute <= 59) alors:
        si heure = 12 alors;
            heure <- 12
        sinon
            heure <- heure - 12
        fin si
        écrire heure, ":", minute "PM"
    fin si
fin

```

<b> Exercice 15 </b>

Chez Happy Copy, le tarif affiché est le suivant :

    moins de 10 copies : 0.10 € la copie

    à partir de 10 copies : 0.07 € par copie

    à partir de 100 copies : 0.05 € par copie

    à partir de 1000 copies : 0.04 € par copie

Ecrire un algorithme qui affiche le prix à payer connaissant le nombre de copies effectuées.

```
algorithme copie:
    copies            : entier
    prix , prix_total :  réel
    lire copies
    si copies < 10 alors:
        prix_total <- copies * 0.1
        écrire  "Le prix total est ", prix_total, " euros".
    sinon si copies > 10 ET copies < 100 alors:
        prix_total <- copies * 0.07
        écrire  "Le prix total est ", prix_total, " euros".
    sinon si copies < 1000 alors:
        prix_total <- copies * 0.04
        écrire  "Le prix total est ", prix_total, " euros".
    fin si
fin
```

<b> Exercice 16 </b>

Un triangle est isocèle s’il possède 2 côtés de même longueur, ou de façon équivalentes, s’il possède 2 angles égaux. Ecrire un algorithme qui reçoit en paramètres 2 des angles de ce triangle, et affiche un message indiquant si le triangle est isocèle ou non.

N.B. : les données se limitent ici à 2 angles du triangle...
si cela vous perturbe, rappelez vous que la somme des angles d’un triangle vaut toujours 180°...

```
algorithme triangle_isocèle
    angle1, angle2 : entier
    lire angle1, angle2

    si angle1 = angle2 alors:
        Écrire "Le triangle est isocèle."
    sinon:
        Écrire "Le triangle n'est pas isocèle."
    fin si
fin

```

<b> Exercice 18</b>

Un magasin a décidé d’une campagne promotionnelle pour ses clients : plus grande est la quantité achetée pour un produit,plus grande est la remise (ristourne) sur le prix normal du produit.

il n’y a pas de remise pour moins de 5 fois le même produit

il y a une remise de 5% pour une quantité minimale de 5 et inférieure à 10 fois le même produit

il y a une remise de 10% pour une quantité minimale de 10 et inférieure à 50 fois le même produit

il y a une remise de 15% pour une quantité minimale de 50 fois le même produit

Ecrivez un algorithme qui calcule et affiche le prix à payer par le client à partir du prix unitaire et de la quantité achetée du même produit.

```
algorithme remise:
    quantité                   :entier
    prix_unitaire, prix_total  :réel
    lire quantité, prix_unitaire
    si quantité < 5 alors:
        prix_total <- prix_untitaire * quantié
    si quantité >= 5 ET quantité < 10 alors:
        prix_total <- prix_unitaire * (1 - 0, 05)
    sinon quantité >= 10 ET quantité < 50 alors:
        prix_total <- prix_unitaire *(1 -0,10)
    sinon quantité >= 50 alors:
        prix_total <- prix_unitaire * (1- 0,15)
    fin si
fin

```

<b> Exercice 19</b>

Le volume d’un téléviseur est mesuré sur une échelle de nombres entiers entre 0 et 20. Il est modifié par le bouton ‘+’ de la télécommande, qui augmente le volume d’une unité (sauf s’il est au maximum) ou par le bouton ‘–’ qui descend le volume d’une unité (sauf s’il est au minimum).

Ecrire un algorithme qui simule le fonctionnement du réglage du volume. Cet algorithme lira la valeur du volume actuel ainsi qu’un caractère qui peut valoir ‘p’ (pour le bouton ‘+’) ou ‘m’ (pour le bouton ‘–’) et affichera la nouvelle valeur du volume.

```
Algorithme volume:

    volume   : entier
    commande : caractère

    lire volume
    lire commande

    Si commande = "p" ET volume < 20 alors:
        volume <- volume + 1
    fin si

    Si commande = "m" ET volume > 0 alors:
        volume <- volume - 1
    fin si

    Écrire "Nouveau volume : ", volume
Fin

```

## Chapitre 4

<b> Algorithme avec paramètres </b>

Dans un algorithme, au lieu de lire les valeurs avec :

```
lire x
lire y

```

on peut faire en sorte que ces valeurs soient fournies directement lors de l’appel de l’algorithme.
Pour cela, on utilise des paramètres en entrée, écrits dans l’en-tête :

algorithme maximum(x, y : entier)

Cela signifie que x et y recevront leurs valeurs au moment où l’algorithme est appelé, par exemple :

```
maximum(5, 12)

```

Ainsi :

On ne lit plus x et y dans l’algorithme.

On ne redéclare pas x et y à l’intérieur (sinon on efface leur valeur).

L’algorithme ne pourra fonctionner que si les paramètres ont été fournis lors de l’appel.

Une fois les paramètres reçus, l’algorithme peut s’exécuter normalement, comme ici :

```
si x > y alors
    max ← x
sinon
    max ← y
fin si

```

<b>Appel d’un algorithme par un autre algorithme</b>

Pour appeler un algorithme qui possède des paramètres, il suffit d’écrire son nom suivi de valeurs entre parenthèses.
Ces valeurs doivent correspondre aux paramètres indiqués dans l’en-tête : même nombre, même ordre et même type.

Exemple : si maximum(x, y) est un algorithme qui affiche le plus grand des deux nombres, on peut l’appeler ainsi :

avec des variables : maximum(a, b)

avec des valeurs : maximum(10, 20)

avec un mélange : maximum(10, b)

avec des expressions : maximum(a + b, a - b)

Si l’utilisateur a donné a = 3 et b = 4, alors :

maximum(a, b) affiche 4

maximum(10, b) affiche 10

maximum(10, 20) affiche 20

Lorsqu’on écrit maximum(expr1, expr2), cela revient à ce que l’algorithme reçoive automatiquement :

```
x ← expr1
y ← expr2

```

Puis il s’exécute avec ces valeurs.

<b>Valeur de retour </b>

Après avoir appris à passer des valeurs à un algorithme grâce aux paramètres, la deuxième étape consiste à éviter d’y faire directement un affichage. En effet, un algorithme ne sert pas toujours à afficher un résultat : parfois, on veut simplement récupérer une valeur pour l’utiliser ailleurs. Pour cela, on introduit la notion de valeur de retour.

Un algorithme qui renvoie une valeur indique dans son en-tête, après une flèche, le type de cette valeur. À l’intérieur, une instruction spéciale — retourner — envoie la valeur calculée à l’endroit où l’algorithme a été appelé. Ainsi, l’algorithme maximum(x, y) peut renvoyer le plus grand des deux nombres sans rien afficher lui-même.

L’appel d’un algorithme avec valeur de retour se comporte comme une expression. On peut donc écrire par exemple :

```
écrire maximum(a, b)

```

ou même utiliser le résultat pour d'autres calculs. Contrairement à un algorithme sans valeur de retour, on n’appelle plus l’algorithme comme une simple instruction, mais comme une fonction qui produit un résultat.

Deux règles importantes accompagnent cela :

l’instruction retourner doit se trouver en fin d’algorithme, sinon tout ce qui est écrit ensuite serait ignoré (on parle de code mort) ;

il ne peut y avoir qu’un seul retourner, car le premier rencontré termine l’algorithme.

Par ailleurs, toutes les variables d’un algorithme sont locales, c’est-à-dire qu’elles ne sont connues que dans cet algorithme. Ainsi, x et y n’existent que dans maximum, tandis que a, b et c appartiennent uniquement à l’algorithme qui les utilise. Cela évite toute confusion entre les noms de variables dans différents sous-algorithmes.

L’intérêt de découper un problème en sous-algorithmes est d’organiser clairement le travail : l’algorithme appelant s’occupe de la lecture et de l’affichage, tandis que le sous-algorithme maximum se charge uniquement du calcul du maximum.

On peut ensuite réutiliser facilement cet algorithme. Par exemple, pour trouver le maximum de trois nombres, on appelle deux fois l’algorithme maximum : d’abord sur les deux premiers nombres, puis sur le résultat et le troisième nombre. On peut même écrire cette opération en une seule ligne, même si cela peut réduire la lisibilité.

### Exercice 1

Dans le code ci-dessous, l’algorithme principal fait appel à l’algorithme somme, mais parfois de façon erronée. Quels sont les appels corrects ? Quels sont les lignes incorrectes, et pourquoi ? Après avoir éliminé les lignes incorrectes, tracer l’algorithme en prenant 5 et 10 comme valeurs lues.

```
algorithme principal
    a, b, c : entier
    lire a, b
    somme(a, b)            <- On appelle la fonction sans utiliser sa valeur.
    a <- somme(a, b)
    écrire somme(a, 3)
    écrire somme(a, a)
    écrire somme(a, c)     <- Ici c n'a pas encore reçu de valeur.
    c <- somme(a, b)
    écrire somme(a, c)
    écrire somme(x, y)     <- Ici les valeurs x et y n'existent pas dans l'alogrithme.
    écrire somme(a, b, c)  <- La fonction somme a trois arguments, mais lors de la déclaration elle n'a que deux arguments.
    écrire somme(a, a + b)
    a <- a + somme(a, b)
    b <- somme(a, somme(a, b))
fin
algorithme somme(x, y : entier) : entier
    z : entier
    z <- +y
    retourner z
fin

```

Algorithme corrigé.

```
algorithme principal
    a, b, c : entier
    lire a, b
    a ← somme(a, b)
    écrire somme(a, 3)
    écrire somme(a, a)
    c ← somme(a, b)
    écrire somme(a, c)
    écrire somme(a, a + b)
    a ← a + somme(a, b)
    b ← somme(a, somme(a, b))
fin
algorithme somme(x, y : entier) : entier
    z : entier
    z <- +y
    retourner z
fin

```

| Étape | Instruction exécutée      | a   | b   | c   | Sortie (écran)    |
| ----- | ------------------------- | --- | --- | --- | ----------------- |
| 0     | Après lire a, b           | 5   | 10  | ?   | —                 |
| 1     | a ← somme(a, b)           | 15  | 10  | ?   | —                 |
| 2     | écrire somme(a, 3)        | 15  | 10  | ?   | 18                |
| 3     | écrire somme(a, a)        | 15  | 10  | ?   | 18 ; 30           |
| 4     | c ← somme(a, b)           | 15  | 10  | 25  | 18 ; 30           |
| 5     | écrire somme(a, c)        | 15  | 10  | 25  | 18 ; 30 ; 40      |
| 6     | écrire somme(a, a + b)    | 15  | 10  | 25  | 18 ; 30 ; 40 ; 40 |
| 7     | a ← a + somme(a, b)       | 40  | 10  | 25  | 18 ; 30 ; 40 ; 40 |
| 8     | b ← somme(a, somme(a, b)) | 40  | 90  | 25  | 18 ; 30 ; 40 ; 40 |

### Exercice 2

Tracer le déroulement de l’algorithme principal ci-dessous en prenant 1 et 4 comme
valeurs de départ.

```
algorithme principal
    a, b : entiers
    lire a, b
    a <- calculs(a, 2*b)
    b <- calculs(b, a)
    écrire a
fin


algorithme calculs(a, b : entier)  entier
    c : entier
    c <- a+b
    a <- fonction(c)
    retourner a
fin

algorithme fonction(x : entier)  entier
    y : entier
    si x > 10 alors
        y <- x MOD 10
    sinon
        y <- 2*x
    fin si
    retourner x + y
fin
```

| Étape | Instruction          | a   | b   | Valeur affichée |
| ----- | -------------------- | --- | --- | --------------- |
| 0     | Valeurs initiales    | 1   | 4   | —               |
| 1     | a ← calculs(a, 2\*b) | 27  | 4   | —               |
| 2     | b ← calculs(b, a)    | 27  | 32  | —               |
| 3     | écrire a             | 27  | 32  | **27**          |

### Exercice 3

Voici encore une variante de l’algorithme pour le calcul du maximum de 3 nombres, qui fait appel à l’algorithme maximum (qui calcule lui le maximum de 2 nombres).

Cet algorithme n’utilise cependant que 2 variables. Vérifiez la validité de l’algorithme, et corrigez-le si nécessaire.

Algorithme correcte.

```
algorithme maximum3nombres
    a, b : entier
    lire a, b
    a <- maximum(a, b)
    lire b
    a <- maximum(a, b)
    écrire "Le maximum des 3 nombres vaut", a
fin

```

L'algorithme est correct.

Une variable supplémentaire c serait possible, mais pas utile.

L'algorithme est correct ET plus efficace que la version avec 3 variables !

Algorithme avec 3 variables.

```
algorithme maximum3nombres
a, b, c : entier
    lire a
    lire b
    lire c

    a ← maximum(a, b)
    a ← maximum(a, c)

    écrire "Le maximum des 3 nombres vaut ", a
fin

```

### Exercice 4

XXXX En cours de correction XXXX

Tracer l'algorithme maximum3nombres avec 2 valeurs les valeurs avec les valeurs a = 2 b=5.

| Étape | Instruction                | a   | b   | Sortie              |
| ----- | -------------------------- | --- | --- | ------------------- |
| 0     | lire a, b                  | 2   | 5   |                     |
| 1     | a ← maximum(2, 5) = 5      | 5   | 5   |                     |
| 2     | lire b (3ᵉ valeur lue = 7) | 5   | 7   |                     |
| 3     | a ← maximum(5, 7) = 7      | 7   | 7   |                     |
| 4     | écrire                     | 7   | 7   | "Le maximum vaut 7" |

Tracer l'algorithme maximum3nombres avec 3 valeurs les valeurs avec les valeurs a = 2 b=5 et c=8.

| Étape | Instruction                           | a   | b   | c   | Sortie                |
| ----- | ------------------------------------- | --- | --- | --- | --------------------- |
| 0     | lire a                                | 2   | —   | —   |                       |
| 1     | lire b                                | 2   | 5   | —   |                       |
| 2     | lire c                                | 2   | 5   | 8   |                       |
| 3     | a ← maximum(a, b) = maximum(2, 5) = 5 | 5   | 5   | 8   |                       |
| 4     | a ← maximum(a, c) = maximum(5, 8) = 8 | 8   | 5   | 8   |                       |
| 5     | écrire "Le maximum vaut ", a          | 8   | 5   | 8   | Le maximum vaut **8** |

XXXX En cours de correction XXXX

### Exercice 5

Ecrire un algorithme qui retourne la valeur absolue d’un nombre réel reçu en paramètre.

```
algorithme calcul_valeur_absolue(param:réel) ->  réel
    r: réel
    r <- valeur_absolue(param)
    retourner r
fin

algorithme valeur_absolue(param: réel) -> réél
    y : réel
    si param < 0 alors
        y <- -param
    sinon
        y <- param
    fin si
    retourner y
fin

```

### Exercice 6

Ecrire un algorithme qui retourne le maximum de 4 nombres entrés en paramètres. Cet algorithme fera appel de façon imaginative au module qui calcule le maximum de 2 nombres.

```
algorithme maximum4nombres (a: réel, b: réel, c: réel, d: réel ) -> réel
    maxi : réel
    maxi <- calcul_maximum(a, b)
    maxi <- calcul_maximum(maxi, c)
    maxi <- calcul_maximum(maxi, d)
    retourne maxi
fin

algorithme  calcul_maximum(param_1 :réel, param_2 :réel) -> réel
    resultat :réel
    si param_1 > param_2 alors
        resultat <- param_1
    sinon
        resultat <- param_2

    retourner resultat

```

### Exercice 7

Ecrire un algorithme qui vérifie si une date est valide ou non. Pour ce faire, suivre
les étapes suivantes :

écrire un algorithme qui vérifie si une année est bissextile : cet algorithme recevra une année en paramètre et retournera un booléen indiquant si l’année est bissextile ou non

écrire un algorithme qui reçoit un mois et une année en paramètre, et retourne le nombre de jours qu’il y a dans ce mois (cet algorithme fera appel au précédent pour traiter le cas particulier du mois de février)

écrire un algorithme qui reçoit deux entiers en paramètre (x et max), et vérifie si x est compris dans l’intervalle [1, max]

enfin, écrire l’algorithme principal qui reçoit une date en paramètre sous la forme de 3 entiers J, M, A et retourne un booléen indiquant si la date est valide ou non. Il faut vérifier pour cela que le mois M est compris entre 1 et 12, et que le jour J est compris entre 1 et le nombre de jours de ce mois.

Réflexion : que proposeriez-vous comme contrainte sur l’année ?

L'année est natrelle.

```

algorithme annee_bissextile(annee : naturel) -> booléen
    // Une année est bissextile si :
    // - divisible par 4 et pas par 100
    //   OU
    // - divisible par 400

    si (annee MOD 400 = 0) alors
        retourner vrai
    sinon si (annee MOD 100 = 0) alors
        retourner faux
    sinon si (annee MOD 4 = 0) alors
        retourner vrai
    sinon
        retourner faux
    fin si
fin
algorithme nombre_jours(mois : naturel, annee : naturel) -> naturel
    jours : naturel

    // Mois à 31 jours
    si mois = 1 OU mois = 3 OU mois = 5 OU mois = 7 OU mois = 8 OU mois = 10 OU mois = 12 alors
        jours <- 31

    // Mois à 30 jours
    sinon si mois = 4 OU mois = 6 OU mois = 9 OU mois = 11 alors
        jours <- 30

    // Février
    sinon si mois = 2 alors
        si annee_bissextile(annee) = vrai alors
            jours <- 29
        sinon
            jours <- 28
        fin si

    // (Optionnel) Mois invalide : on pourrait mettre jours <- 0
    sinon
        jours <- 0
    fin si

    retourner jours
fin


algorithme dans_intervalle(x : entier, max : entier) -> booléen
    si x >= 1 ET x <= max alors
        retourner vrai
    sinon
        retourner faux
    fin si
fin


algorithme date_valide(J : entier, M : entier, A : naturel) -> booléen
    nb_jours : entier

    // Vérifier que le mois est entre 1 et 12
    si dans_intervalle(M, 12) = faux alors
        retourner faux
    fin si

    // Récupérer le nombre de jours de ce mois
    nb_jours <- nombre_jours(M, A)

    // Si nb_jours = 0, le mois était invalide (cas de sécurité)
    si nb_jours = 0 alors
        retourner faux
    fin si

    // Vérifier que le jour est compris entre 1 et nb_jours
    si dans_intervalle(J, nb_jours) = vrai alors
        retourner vrai
    sinon
        retourner faux
    fin si
fin

```

## Chapitre 5

Jusqu'ici, les algorithmes ont manipulé uniquement des variables simples, comme les entiers, les réels, les booléens ou les chaînes, qui ne peuvent contenir qu’une seule valeur à la fois. Pourtant, de nombreuses données réelles sont composées de plusieurs éléments : une date comporte un jour, un mois et une année ; un moment de la journée se décrit par une heure, une minute et une seconde ; une adresse en Belgique regroupe une rue, un numéro, un code postal, une ville et éventuellement un pays. Pour pouvoir manipuler ce type de données complexes de manière cohérente, on introduit les variables structurées, qui permettent de rassembler plusieurs informations dans une seule structure.

Pour utiliser une variable structurée, il faut d’abord définir son type, en listant ses différents champs ainsi que leur type respectif. Par exemple, un type date regroupera un jour, un mois et une année ; un type moment contiendra une heure, une minute et une seconde ; un type adresse regroupera une rue, un numéro de maison, un code postal, une ville et un pays. Une fois ces types définis, ils peuvent être utilisés comme n’importe quel type simple dans les déclarations de variables.

Un champ d’une structure peut lui-même être une structure, ce qui permet de modéliser des données encore plus complexes. On peut ainsi définir un type carteIdentité contenant un nom, un prénom, une date de naissance (de type date), une adresse de domicile (de type adresse) et un numéro de registre national.

La déclaration d’une variable structurée se fait exactement comme celle d’une variable simple, en indiquant son nom suivi du type structuré utilisé. Par la suite, pour accéder ou modifier un champ particulier d’une variable structurée, on emploie la notation pointée, par exemple : dateAnniversaire.jour ← 5, adresseEcole.rue ← "Rue Royale" ou retourner maCarte.domicile.codePostal. Selon le contexte, il est également possible de manipuler l’ensemble de la structure, par exemple en affectant une date à une autre ou en retournant directement une structure complète.

Cette capacité à retourner ou transférer en une seule opération un ensemble de valeurs regroupées dans une structure offre une grande souplesse : elle permet de transmettre des données complexes à un algorithme ou d’en recevoir en retour, tout en gardant un code clair et organisé.

## Exercice 1

Les exercices utilisent les types structurés moment et date définis dans ce chapitre. A partir de maintenant, nous privilégions l’utilisation des paramètres et des valeurs de retour aux lectures et écritures, sauf si ces dernières sont explicitement demandées.

Ecrire un algorithme qui reçoit un moment en paramètre et retourne ce moment
augmenté d’une seconde.
Exemples :
• si le moment reçu est 13h 21’ 23’’, le retour sera 13h 21’ 24’’
• si le moment reçu est 15h 17’ 59’’, le retour sera 15h 18’ 00’’

```
algorithme ajouter_une_seconde(moment : Moment) → Moment

   resultat : Moment

   // Copier le moment reçu
   resultat.h ← moment.h
   resultat.m ← moment.m
   resultat.s ← moment.s + 1

   // Gestion du dépassement des secondes
   si resultat.s = 60 alors
       resultat.s ← 0
       resultat.m ← resultat.m + 1
   fin si

   // Gestion du dépassement des minutes
   si resultat.m = 60 alors
       resultat.m ← 0
       resultat.h ← resultat.h + 1
   fin si

   // Gestion du dépassement des heures
   si resultat.h = 24 alors
       resultat.h ← 0
   fin si

   retourner resultat
fin


```

### Exercice 2

Ecrire un algorithme qui compare 2 dates reçues en paramètres. L’algorithme
retournera un entier valant :

• –1 si la première date est antérieure à la 2ème

• 1 si la première date est postérieure à la 2ème

• 0 si les 2 dates sont identiques

```

type Date = structure
    jour : entier
    mois : entier
    annee : entier
fin structure

algorithme date_comparaison(date_1 : Date, date_2 : Date) → entier

    // Comparaison des années
    si date_1.annee < date_2.annee alors
        retourner -1
    sinon si date_1.annee > date_2.annee alors
        retourner 1
    fin si

    // À ce stade, les années sont égales
    si date_1.mois < date_2.mois alors
        retourner -1
    sinon si date_1.mois > date_2.mois alors
        retourner 1
    fin si

    // À ce stade, les mois sont aussi égaux
    si date_1.jour < date_2.jour alors
        retourner -1
    sinon si date_1.jour > date_2.jour alors
        retourner 1
    fin si

    // À ce stade, tout est égal
    retourner 0

fin






    retourner résultat


```
