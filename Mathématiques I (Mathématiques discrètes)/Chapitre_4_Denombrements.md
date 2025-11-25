# Chapitre 4 - Dénombrements

## Exercices

### Exercices 4.1

Imagine que tu dois poser les cartes l’une après l’autre :

Pour la première place : 52 choix

Pour la deuxième : tu as déjà utilisé une carte → 51 choix

Pour la troisième : 50 choix

ect ...

Dernière place : 1 choix

Tu multiplies tous les choix possibles → c’est exactement la définition de la factorielle.

Donc le nombre total de mélanges possibles est :

```
!
52×51×50×⋯×1=52!

52! ≈8.0658×1067

```

---

### Exercice 4.2

<b> Type de problème : </b>

- Combinaison sans répétition (on choisit des objets, l’ordre ne compte pas, sans doublons).

<b> Interprétation : </b>

- Tu choisis un ensemble de 6 numéros parmi 45, l’ordre n’a aucune importance.

Quelle est la situation ?

Il y a 45 numéros possibles : 1, 2, 3, …, 45

Sur ta grille, tu dois choisir 6 numéros.

On ne peut pas cocher deux fois le même numéro → pas de répétition.

L’ordre ne compte pas :

la grille 1, 2, 3, 4, 5, 6 est la même que 6, 5, 4, 3, 2, 1.

Au lotto, ce qui compte c’est l’ensemble des 6 numéros, pas dans quel ordre tu les as cochés.

Formule => C avec n=45 et k=6

La Réponse est

```
 C n=45 k=6 = (A n=45 et k=6) / 6! = (45 . 44 . 43 . 42 . 41 . 40) / (6 . 5 . 4 . 3 . 2 . 1) = 8 145 060


```

<b> Donc, il existe 8 145 060 façons différentes de remplir une grille de lotto (6 numéros parmi 45). </b>

---

### Exercice 4.3

<b> Type de problème: </b>

- Arrangement sans répétition
  (ordre important, objets tous différents, aucun doublon possible)

<b> Interprétation: </b>

- Tu dois choisir 3 chevaux parmi 20, et un cheval ne peut pas prendre deux places. L'ordre de selection des chevaux compte.

Comment compter ?

Tu choisis :

le 1ᵉ cheval : 20 possibilités

le 2ᵉ : 19 possibilités

le 3ᵉ : 18 possibilités

Donc :

```

A n=20 k=3 = 20 . 19 . 18 = 6840

```

<b> Il faut remplir 6 840 bulletins différents pour être certain de gagner le tiercé dans l’ordre.</b>

---

### Exercice 4.4

<b> Type de problème : </b>

- C’est un arrangement complet (tous les objets sont utilisés).

<b> Interprétations : </b>

Chaque personne reçoit exactement 1 chapeau - Aucun chapeau n’est donné deux fois → pas de répétition.

L’ordre compte parce que -> donner le chapeau A à Paul et B à Marie est différent de A à Marie et B à Paul.

Pour distribuer :

le 1ᵉ chapeau : 5 choix

le 2ᵉ : 4 choix

le 3ᵉ : 3 choix

le 4ᵉ : 2 choix

le 5ᵉ : 1 choix

Donc :

```
5! = 5 . 4 . 3 . 2 . 1 = 120

```

<b> Il existe 120 façons de distribuer 5 chapeaux différents à 5 personnes. </b>

---

### Exercice 4.5

<b> Type de problème : </b>

- Donc une arête est un choix de 2 sommets parmi 15,

  sans répétition,

  l’ordre n’a aucune importance.

<b> Interprétations : </b>

- Un graphe d’ordre 15 possède 15 sommets. On cherche le nombre maximal d’arêtes possible, donc le graphe est complet.

  Dans ce genre de graphe, chaque sommet est connecté à tous les autres.

  Donc, une arête correspond à un couple de sommets distincts, mais dans n’importe quel ordre (car ce n’est pas orienté).

  Ici, la manière dont on relie les sommets (ordres) n'est pas ordonnée, ainsi nous pouvons commencer par le sommet(ordre) de notre choix.

Nous avons une Combinaison sans répétition où n= 15 et k=2

<b> Un graphe d’ordre 15 peut contenir au maximum 105 arêtes. </b>

---

### Exercice 4.6

<b> Type de problème </b>

Dans les cas nous avons une combinaison sans répétition et l'ordre ne compte.

<b> Interprétations : </b>

1. Former une équipe de 10 personnes parmi 20

Il y a :

12 garçons

8 filles

total = 20 personnes

Une équipe de 10 personnes est un ensemble :

l’ordre ne compte pas (une équipe n’a pas d’ordre)

pas de répétition (une personne ne peut pas être choisie deux fois)

2. Former une équipe de 10 personnes avec 5 garçons et 5 filles

Ici, on impose :

choisir 5 garçons parmi 12

choisir 5 filles parmi 8

Les deux choix sont indépendants, donc on multiplie.

Les deux sont des combinaisons sans répétition, car :

on choisit un ensemble

l’ordre ne compte pas

pas de répétition

Réponse :

```
# Pour le cas 1:

C où n=20 et k=10


# Pour le cas 2:

(C où n=12 et k=5)* (C où n=8 et k=5)


```

<b>Dans le premier cas nous pouvons créer 184 756 équipes de 10 personnes possible. Dans le second cas, nous avons 44 352 équipes possibles constituées de 5 garçons et de 5 filles.</b>

Remarque ici nous multiplions nous voulons des équipes constituer de 5 garçon ET 5 filles. Si nous voulions des équipes constituer de garçon OU de filles il aurait fallut additions.

```
Example:

(C où n=12 et k=5) + (C où n=8 et k=5)

```

---

### Exercice 4.7

<b> Type de problème </b>

C’est un cas de produit avec répétitions possibles.

<b> Interprétations : </b>

On veut compter toutes les possibilités, donc :

l’ordre compte (changer l’ordre donne une plaque différente)

répétition autorisée (ex : 442 peut exister)

indépendance entre cases

- C’est un cas de produit avec répétitions possibles.
- On utilise le principe fondamental du dénombrement.

<b> Nombre de possibilités pour chaque position</b>

1 chiffre – 3 lettres – 3 chiffres

C−LLL−CCC

- 1er caractère : un chiffre

  10 possibilités (0–9)

- 2e, 3e, 4e caractères : des lettres

  26 possibilités chacune (A–Z)

- 5e, 6e, 7e caractères : des chiffres

  10 possibilités chacune (0–9)

Calcul total:

```
10×26×26×26×10×10×10 = 17576×10000 = 175760000

```

<b>Il existe 175 760 000 plaques d’immatriculation possibles.</b>

---

### Exercice 4.8

<b>Combien y en a-t-il de différents ?</b>

<b> Type de problèmes : </b>

Arrangement avec répétition (ordre important, répétitions autorisées)

<b>Interprétation : </b>

Pour chaque position nous avons 10 possibilités. Les chiffres vont de 0 à 9.

. . . . . => Pour chaque point, il y a 10 possibilités.

<b>Réponse : </b>

Donc, le résultat est

```
10 . 10 . 10 . 10 = 10⁴

```

<b>Combien se terminent par 3 ?</b>

<b> Type de problèmes : </b>

Arrangement avec répétition (ordre important, répétitions autorisées)

<b>Interprétation : </b>

. . . 3 => Pour chaque point, il y a 10 possibilités mais la dernière position est occupé par le 3 (chiffre donné).

<b>Réponse : </b>

Donc le résultat est

```
10 . 10 . 10  = 10³

```

<b>Combien commencent par 12 ?</b>

<b> Type de problèmes : </b>

Arrangement avec répétition (ordre important, répétitions autorisées)

<b>Interprétation : </b>

1 2 . . => La 1ère et la 2ème positions sont exclues donc il reste car occupées respectivement par 1 et 2.

<b>Réponse : </b>

```
10 . 10 = 10²

```

<b>Combien se terminent par 3 ou par 6?</b>

<b> Type de problèmes : </b>

Arrangement avec répétition (ordre important, répétitions autorisées)

<b>Interprétation : </b>

. . . 3 ou . . . 6 => Il faut calculer toutes les possibilités pour les codes qui se terminent par 3 et il faut faut la même opération pour les codes qui se terminent par 6.

<b>Réponse : </b>

Pour les codes qui se terminent par 3, obtenons :

```
10 . 10 . 10 = 10³

```

Pour les codes qui se terminent par 6, obtenons :

```
10 . 10 . 10 = 10³

```

Le résultat finale est égale à la somme des possibilités calculées ci-dessus.

```
10³ + 10³ = 2000

```

<b>Combien ne se terminent ni par 3, ni par 6?</b>

<b> Type de problèmes : </b>

Arrangement avec répétition (ordre important, répétitions autorisées)

<b>Interprétation : </b>

. . . X -> 3 et . . . X -> 6 => On calcule toutes les possibilités pour la 1ère, 2ème et 3ème positions qui sont égales à 10, mais pour la 4ème position on retire des possibilités les chifres 3 et 6.

<b>Réponse : </b>

```
10 . 10 . 8 = 8 . 10²

```

<b>Combien commencent par 3 et finissent par 6?</b>

<b> Type de problèmes : </b>

Arrangement avec répétition (ordre important, répétitions autorisées)

<b>Interprétation : </b>

3 . . 6 => La 1ère et la 4ème sont bloquées respectivement par 3 et 6. Mais les possiblités sont pour la 2ème place et la 3ème place sont toutes les deux 10.

<b>Réponse : </b>

```
10 . 10 = 20

```

<b>Combien commencent par 3 ou finissent par 6?</b>

<b> Type de problèmes : </b>

Arrangement avec répétition (ordre important, répétitions autorisées)

<b>Interprétation : </b>

<b>Réponse : </b>

```
10 . 10 . 8 = 8 . 10²

```

<b>Combien commencent par 3 et finissent par 6?</b>

<b> Type de problèmes : </b>

Arrangement avec répétition (ordre important, répétitions autorisées)

<b>Interprétation : </b>

3 . . . Si on considère l'enssemble A constitué par les codes qui commencent par 3 seulement.

A noter que cette ensemble comprend les codes qui se terminent par 6.

A = 10³

. . . 6 Si on considère l'enssemble B constitué par les codes qui finissent par 6 seulement.

A noter que cette ensemble comprend les codes qui se comment par 3.

B = 10³

Dans le chapitre consacré aux ensembles, nous avons vu que pour obtenir le OU exclusif, il faut soustraire de la somme des deux ensembles l’ensemble correspondant à leur intersection.

Ici l'intersection correspond aux code qui commencent par 3 et se terminent par 6, calculé plus haut et qui vaut 10².

<b>Réponse : </b>

```
|A| + |B| - |A ∩ B|

10³ + 10³ - 10² = 1000 + 1000 - 100 = 2900

```

<b>Combien contiennent la séquence « 42 »?</b>

<b> Type de problèmes : </b>

Arrangement avec répétition (ordre important, répétitions autorisées)

<b>Interprétation : </b>

<b>Comptage des codes contenant la séquence "42"</b>

Pour qu’un code PIN de 4 chiffres contienne la séquence `42`, celle-ci peut apparaître dans trois positions :

- **Positions 1–2** : `42xy`
- **Positions 2–3** : `x42y`
- **Positions 3–4** : `xy42`

On applique alors le principe d’inclusion–exclusion.

#### Cas individuels

- **A :** séquence `42` en positions 1–2 → `42xy`  
  Nombre de codes : `10 × 10 = 100`

- **B :** séquence `42` en positions 2–3 → `x42y`  
  Nombre de codes : `10 × 10 = 100`

- **C :** séquence `42` en positions 3–4 → `xy42`  
  Nombre de codes : `10 × 10 = 100`

#### Intersections

- **A ∩ B :** impossible  
  (Le chiffre en position 2 devrait être à la fois `2` et `4`) → `0`

- **B ∩ C :** impossible  
  (Le chiffre en position 3 devrait être à la fois `2` et `4`) → `0`

- **A ∩ C :** possible seulement pour un code  
  `4242` → `1`

<b>Réponse : </b>

```
|A| + |B| - |A ∩ B|

100 + 100 + 100 − 0 − 0 − 1 = 299

```

---

<b>Combien de codes différents ?</b>

<b> Type de problèmes : </b>

Les choix se font sans répétition.

<b>Interprétation : </b>

On choisit 4 chiffres tous différents. Pour la 1ère position on a 10 possibilités, puis on retire de la 2éme position on a 9 possibilités car on retire le chiffre placé en 1ère position. Pour 3ème on (10 - 2) possibilités et pour le 4ème on (10 -3) possibilités.

<b>Réponse : </b>

```
10×9×8×7=5040

```

<b>Combien se terminent par 3 ?</b>

<b> Type de problèmes : </b>

Les choix se font sans répétition.

<b>Interprétation : </b>

. . . 3

Ici une position est prise par 3. Il faut calculer les possibilités 3 autres positions.

<b>Réponse : </b>

```
9×8×7=5040

```

<b>Combien commencent par 12 ?</b>

<b> Type de problèmes : </b>

Les choix se font sans répétition.

<b>Interprétation : </b>

1 2 . .

Ici nous avons 2 positions prises par 1 et 2. Il faut calculer les possibilités 2 autres positions.

<b>Réponse : </b>

```
8×7=56

```

<b>Combien se terminent par 3 ou par 6 ?</b>

<b>Type de problème :</b>

Réunion de deux arrangements sans répétition.

<b>Interprétation :</b>

On compte les codes finissant par 3, puis ceux finissant par 6. Impossible qu’un code finisse par les deux.

<b>Réponse :</b>

```
504 + 504 = 1080

```

<b>Combien ne se terminent ni par 3 ni par 6 ?</b>

<b>Type de problème :</b>

Complément du total.

<b>Interprétation :</b>

On part du nombre total de codes, et on retire ceux qui se terminent par 3 ou par 6.

Détail du calcul :

- Total de codes (question 1) : 5 040

- Codes finissant par 3 ou 6 (question 4) : 1 008

<b>Réponse:</b>

```
5040 - 1080 = 4032

```

---

<b>Combien commencent par 3 ET finissent par 6 ?</b>

<b>Type de problème :</b>

Arrangement sans répétition avec première et dernière positions imposées.

<b>Interprétation :</b>

On fixe :

- 1ᵉ chiffre = 3

- 4ᵉ chiffre = 6

Puis on choisit 2 chiffres distincts pour les positions 2 et 3.

<b>Réponse:</b>

```
8 . 7 = 56

```

---

<b>Combien commencent par 3 OU finissent par 6?</b>

<b>Type de problème :</b>

Inclusion–exclusion sur deux ensembles :

A = “commence par 3”, B = “finit par 6”.

<b>Interprétation :</b>

On additionne :

- les codes qui commencent par 3,

- ceux qui finissent par 6.

Puis on enlève ceux qui ont été comptés deux fois (commencent par 3 et finissent par 6).

Étape 1 : Codes qui commencent par 3

1ᵉ chiffre = 3

3 autres chiffres tous différents parmi les 9 restants.

2ᵉ position : 9 possibilités

3ᵉ position : 8 possibilités

4ᵉ position : 7 possibilités

Donc :

```
9 . 8 . 7 = 504

```

Étape 2 : Codes qui finissent par 6

C’est la même logique que plus haut → 504 (comme pour 3 ou 6 fixés en 4ᵉ position).

Étape 3 : Codes qui commencent par 3 ET finissent par 6

C’est la question "Combien commencent par 3 ET finissent par 6 ?" : 56.

```

|A U B| = |A| + |B| - |A ∩ B|

504 + 504 - 56 = 952


```

<b>Combien contiennent la séquence « 42 » ?</b>

<b>Type de problème :</b>

Arrangement sans répétition + inclusion–exclusion sur les positions possibles du bloc "42".

<b>Interprétation :</b>

On veut des codes à 4 chiffres tous différents qui contiennent "42" comme bloc consécutif.

Le bloc "42" peut être placé en :

positions 1–2 → 42xy

positions 2–3 → x42y

positions 3–4 → xy42

On suppose toujours que tous les chiffres du code sont différents.

Cas A : « 42 » en positions 1–2 → 42xy

Chiffres utilisés : 4 et 2.

Il reste 8 chiffres (tout sauf 4 et 2) pour les deux dernières positions.

3ᵉ position : 8 possibilités

4ᵉ position : 7 possibilités

Donc :

```
8 . 7 = 56

```

Cas B : « 42 » en positions 2–3 → x42y

2ᵉ chiffre = 4

3ᵉ chiffre = 2

Chiffres interdits pour x : 4 et 2 → il reste 8 choix.

Chiffres interdits pour y : 4, 2, et x → il reste 7 choix.

Donc :

```
8 . 7 = 56

```

Cas C : « 42 » en positions 3–4 → xy42

Même logique que pour le cas A et B :

x : 8 possibilités (tous sauf 4,2)

y : 7 possibilités (tous sauf 4,2 et x)

Donc :

```
8 . 7 = 56

```

Intersections des cas

On vérifie s’il existe des codes comptés dans deux cas à la fois (pour éventuellement les soustraire).

A ∩ B :

A impose : pos1 = 4, pos2 = 2

B impose : pos2 = 4, pos3 = 2

→ pos2 devrait être à la fois 2 et 4 → impossible

➜ 0 code.

B ∩ C :

B : pos2 = 4, pos3 = 2

C : pos3 = 4, pos4 = 2

→ pos3 devrait être à la fois 2 et 4 → impossible

➜ 0 code.

A ∩ C :

A : 42xy

C : xy42

Pour avoir les deux, il faudrait 4242, mais les chiffres ne seraient plus tous différents → interdit.

➜ 0 code.

Donc les trois cas sont disjoints.

<b>Réponse : </b>

```
56 + 56 + 56 = 168

```

---

### Exercice 4.10

<b>Type de problème :</b>

- Permutation sans répétition de 5 lettres.

<b>Interprétations:</b>

On cherche tous les ordres possibles des 5 lettres distinctes.

Pour Paris:

```
5! = 5 . 4 .3 . 2 . 1 = 120

```

Pour Berne:

Ici comme nous avons 2 E, il faut retirer les répitions.

2E => 2!

<b>Réponses:</b>

```
5! / 2! = 120 / 2 = 60

```

Pour Berne:

Ici comme nous avons 2 R et 2A, il faut retirer les répitions.

2R => 2!

2A => 2!

<b>Réponses:</b>

```
5! / 2! . 2! = 120 / 2 . 2 = 30

```

Pour Berne:

Ici comme nous avons 2 R et 2A, il faut retirer les répitions.

2R => 2!

2A => 2!

<b>Réponses:</b>

```
5! / 3! = 120 / 3! = 20

```

---

### Exercice 4.11

<b>Comptons les lettres de HURLUBERLU</b>

Mot : H U R L U B E R L U

Nombre total de lettres : 10.

On compte chaque lettre :

H : 1 fois

U : 3 fois (positions 2, 5, 10)

R : 2 fois (positions 3, 8)

L : 2 fois (positions 4, 9)

B : 1 fois

E : 1 fois

Donc on a :

10 lettres au total

avec répétitions : U×3, R×2, L×2, H×1, B×1, E×1

Tous les mots possibles avec HURLUBERLU

<b>Type de problème :</b>

Permutation avec répétition.

Interprétation :

On veut tous les arrangements possibles de ces 10 lettres, en tenant compte que certaines sont identiques (les 3 U, les 2 R, les 2 L).

Formule

Nombre de permutations d’un multiensemble :

```
10! / (3! . 2! . 2!)

```

où

10! = permutations de 10 objets tous différents

on divise par 3! pour les 3 U identiques

par 2! pour les 2 R

par 2! pour les 2 L

Détail des calculs

Calcul de 10! :

```
10! = 10 . 9 . 8 . 7 . 6 . 5 . 4 . 3 . 2 . 1 = 3 628 800

```

Calcul du dénominateur :

```
3! = 3 . 2 . 1 = 6

2! = 2 => 2! . 2! : 2 . 2 = 4

```

Donc:

```
3! . 2! . 2! = 6 . 4 = 4

```

Division:

```
3 628 800 / 24

```

<b> Mots avec deux « R » consécutifs </b>

<b> Type de problème :</b>

Permutation avec répétition et bloc (on regroupe « RR »).

<b>Interprétation :</b>

On oblige les deux R à être l’un à côté de l’autre, sous la forme du bloc RR.

On traite RR comme une seule “lettre” (un bloc), puis on permute ce bloc avec les autres lettres.

Nouveau multiensemble de lettres

On remplace les deux R par un bloc X = RR.

Les lettres deviennent :

X (le bloc RR) : 1 fois

U : 3 fois

L : 2 fois

H : 1 fois

B : 1 fois

E : 1 fois

Total d’objets à permuter :

```
1(X)+3(U)+2(L)+1(H)+1(B)+1(E)=9

```

Donc on permute 9 objets, avec répétitions (U×3, L×2).

Formule:

```
9! / (3! . 2!)

9!=9×8×7×6×5×4×3×2×1=362880


```

Division :

```
12362880​ / 12 = 30 240

```

<b>Réponses : </b>

30 240 mots avec les deux R consécutifs.

<b>Type de problème :</b>

On utilise le complément :

Tous les mots − ceux qui ont « RR » collés.

<b>Interprétation :</b>

On prend le nombre total de mots formés avec HURLUBERLU et on enlève ceux où les deux R sont collés.

Calcul

On a déjà :

Total des mots (question 1) : 151 200

Mots avec « RR » consécutifs (question 2) : 30 240

Donc:

```
151200 − 30240 = 120960

```

<b>Réponses:</b>

20 960 mots qui ne contiennent pas deux R consécutifs.

---

### Exercice 4.12

Type de problème

➡️ Combinaison sans répétition : on choisit des paires de personnes.

Interprétation

➡️ Chaque poignée de main correspond à un couple de personnes.
On ne distingue pas l’ordre (la poignée entre Alice et Bob = entre Bob et Alice), et on ne répète pas les paires.
Donc on doit compter combien de paires on peut former avec 50 personnes → c’est
(
50
2
)
(
2
50
​

).

Étapes de calcul

On utilise la formule :

```
50 . 49 / 2

```

On calcule le produit du numérateur :

```
50 . 49 = 2450

```

On divise par 2 :

```
22450 / 2 = 1225

```

Donc il y a 1 225 poignées de mains.

<b> 1ère réponse</b>

<b>861 poignées de mains → combien de personnes ?</b>

Ici on fait l’inverse :

on sait le nombre de paires (les poignées de main) et on cherche le nombre de personnes
n.

On sait que, pour 𝑛

```
nombre de poigneˊes= (C où n=50 et k=2) = n(n−1)​ / 2

```

On pose l'équation:

```
(C où n=50 et k=2) = 861 =  n(n−1)​ / 2

<=> n(n−1)=2×861

<=> n(n−1)=1722


```

Calcul du Delta:

```
<=> n(n−1)=1722

Delta = 1722

n = 41

```

<b>2ème réponse :</b>

S’il y a 861 poignées de main, il y avait 42 personnes à la réception.

---

### Exercice 4.14

<b>Comprendre la situation</b>

On a 20 livres distincts.

On a 3 rayons distincts (rayon 1, rayon 2, rayon 3).

Capacités :

rayon 1 : 7 places

rayon 2 : 5 places

rayon 3 : 8 places

La somme : 7 + 5 + 8 = 20 → tous les livres sont rangés.

L’ordre dans un rayon n’a pas d’importance : on ne tient pas compte de l’ordre des livres sur un même rayon.

Donc, ce qu’on doit décider, c’est :
Quels livres vont dans le rayon 1, quels dans le rayon 2, et quels dans le rayon 3.

<b>Stratégie de comptage</b>

On procède en étapes :

Choisir quels 7 livres iront sur le rayon 1.

On choisit un sous-ensemble de 7 livres parmi 20.

Nombre de choix :

```
C où n=20 et k=7
```

Il reste alors 20 − 7 = 13 livres.

On doit maintenant choisir 5 livres parmi ces 13 pour le rayon 2.

Nombre de choix :

```
C où n=13 et k=5
```

Il restera automatiquement 13 − 5 = 8 livres :
ils vont tous sur le rayon 3.

Nombre de choix :

```
C où n=8 et k=8

```

Comme ces étapes sont successives et indépendantes, on multiplie :

```
(C où n=20 et k=7) . (C où n=13 et k=5) . (C où n=8 et k=8) =  77520 . 1287 . 1 =  99 768 240
	​
```

<b> Réponses: </b>

Il y a 99 768 240 façons de répartir les 20 livres dans les 3 rayons (7, 5 et 8 places),
en ne tenant pas compte de l’ordre des livres sur chaque rayon.

---
