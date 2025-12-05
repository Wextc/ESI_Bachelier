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

<b>Traçage d’algorithme</b>

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

---

- Cas 2 : x1 = 4, x2 = 1

| Étape | Instruction    | x1  | x2  | ok   | Action exécutée                                         |
| ----- | -------------- | --- | --- | ---- | ------------------------------------------------------- |
| 1     | lire x1, x2    | 4   | 1   | -    | -                                                       |
| 2     | ok ← x1 > x2   | 4   | 1   | vrai | 4 > 1 → vrai                                            |
| 3     | si ok alors …  | 4   | 1   | vrai | Bloc si exécuté : ok ← ok ET x1=4 → vrai ET vrai = vrai |
| 4     | si ok alors …  | 4   | 1   | vrai | Bloc exécuté : x1 ← x1 \* 100 → x1 = 400                |
| 5     | écrire x1 + x2 | 400 | 1   | vrai | Affiche 400 + 1 = 401                                   |

Résultat affiché : 401
