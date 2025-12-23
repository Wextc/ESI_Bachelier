# Chapitre 1

## Représentation des nombres

### 1.1 Calcul dans une base quelconque

<b>Calcul dans une base quelconque</b>

Un calcul dans une base quelconque consiste à représenter et manipuler des nombres dans un système de numération dont la base

n’est pas forcément 10 (le système décimal habituel). La base, notée B, indique le nombre de symboles différents utilisés

pour écrire les nombres et la valeur par laquelle chaque position est pondérée.

Dans une base B, les chiffres possibles vont de 0 à B−1. La valeur d’un chiffre dépend donc à la fois de sa valeur propre et

de sa position dans le nombre. Chaque position correspond à une puissance de la base.

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/chapitre_1_form_general.png)
![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/chapitre_1_exemple.png)

<b> Remarque </b>

l’écriture d’un nombre peut être ambiguë si la base n’est pas précisée. En effet, une même suite de chiffres peut représenter

des valeurs très différentes selon le système de numération utilisé.

Prenons l’exemple de l’écriture 101. Si on la lit en base 10 (système décimal), elle représente simplement le nombre cent un.

En revanche, si on interprète cette même écriture en base 6, sa valeur change : le chiffre 1 de gauche correspond à

6², le 0 à 6¹ et le 1 de droite 6⁰. On obtient alors 1×62+0×6+1=36+1=37. Enfin, en base 2 (binaire), l’écriture 101

correspond à 1×22+0×2+1=4+1=5.

Ainsi, sans indication de la base, il est impossible de connaître la valeur exacte du nombre. Pour lever toute ambiguïté, on précise généralement la base en l’indiquant en indice. On écrit par exemple

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/Ch_1_10.png)

pour le décimal,

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/Ch_1_06.png)

pour la base 6 ou

​![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/Ch_1_02.png)

pour le binaire. Cette notation permet de savoir immédiatement dans quel système de numération le nombre est exprimé et

d’éviter toute confusion.

### 1.2 Bases classiques en informatique

<b> Calcul binaire :</b>

Le calcul binaire est un mode de calcul fondé sur le système de numération en base 2. Dans ce système, seuls deux chiffres

sont utilisés : 0 et 1. Toutes les opérations numériques, comme l’addition, la soustraction ou la multiplication, reposent

sur des combinaisons de ces deux valeurs. Le calcul binaire est au cœur du fonctionnement des ordinateurs, car les circuits

électroniques peuvent facilement représenter deux états distincts, par exemple allumé ou éteint.

<b>Base 2 : </b>

La base 2, <b> aussi appelée système binaire </b>, est un système de numération dans lequel les nombres sont écrits en

utilisant uniquement deux chiffres : 0 et 1. La base 2 indique que chaque position dans un nombre représente une puissance de

2.

Dans ce système, la valeur d’un chiffre dépend de sa position : en partant de la droite, les positions correspondent à 2⁰,

2¹, 2², 2³, et ainsi de suite. Un chiffre égal à 1 signifie que la puissance de 2 correspondante est prise en compte, tandis

qu’un chiffre égal à 0 signifie qu’elle ne l’est pas.

La base 2 est fondamentale en informatique, car elle correspond directement au fonctionnement des composants électroniques,

qui peuvent représenter deux états distincts, comme ouvert ou fermé, vrai ou faux.

<b> Nombre binaire: </b>

Un nombre binaire est un nombre écrit dans ce système en base 2. Il est constitué uniquement de chiffres binaires, appelés

bits, qui sont 0 et 1. Comme dans le système décimal, la valeur d’un chiffre dépend de sa position dans le nombre : chaque

position correspond à une puissance de 2. Ainsi, un nombre binaire représente une quantité en combinant des puissances de 2

pondérées par des 0 ou des 1.

<b> Octet :</b>

Un octet est un regroupement de huit chiffres binaires, c’est-à-dire de huit bits. Il constitue une unité fondamentale de

l’informatique, notamment pour représenter des données comme des caractères, des nombres ou des instructions. Un octet peut

représenter 256 valeurs différentes, ce qui permet par exemple de coder une lettre, un symbole ou une petite valeur numérique.

<b> Pourquoi utiliser le système binaire? </b>

Par souci de simplicité.

Il est en effet simple de distinguer deux valeurs de tension sur un fil.

Si l’on avait souhaité reproduire directement le calcul décimal, dix valeurs différentes de la tension auraienté été

nécessaires, ce qui aurait rendu les circuits beaucoup plus complexes.

<b> Quelle technique à-t-on trouvé pour rendre l'écriture binaire le plus compacte possible?</b>

Le calcul binaire, fondé sur la base 2 et utilisant uniquement les chiffres 0 et 1, est essentiel en informatique car il

correspond au fonctionnement des circuits électroniques. Un nombre binaire est donc une suite de bits, et huit bits forment

un octet, unité fondamentale pour représenter les données.

Cependant, l’écriture binaire présente un inconvénient majeur : elle est peu compacte. Pour un même nombre, la représentation

binaire nécessite environ trois fois plus de symboles que la représentation décimale. Cette différence s’explique par le fait

que le nombre de chiffres nécessaires dépend du logarithme du nombre dans la base choisie.

Pour pallier ce problème de longueur, d’autres bases ont été utilisées en informatique, notamment la base 8 (octale) et la

base 16 (hexadécimale). Ces systèmes offrent une écriture plus courte et plus lisible que le binaire, tout en restant

étroitement liés à celui-ci. Ils constituent ainsi un compromis pratique entre la simplicité du binaire pour les machines et

la lisibilité pour les humains.

<b> Atttention : </b>

La base 8 n'est plus utilisée contrairement à la base 16. La base 16 est adaptée en informatique car on a besoin que de 2

symbolse pour représenter des octets, alors que pour la base 8 il en faut 3.

<b>Qu'est ce qui détermine le poids des bits? </b>

​![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/Ch_1_10_poids.png)

Dans un nombre binaire ou dans une donnée composée de plusieurs octets, l’octet de poids fort est celui qui se situe le plus

à gauche. C’est lui qui représente la valeur la plus élevée, car il est associé aux puissances de 2 les plus grandes. À

l’inverse, l’octet de poids faible se trouve le plus à droite et correspond aux plus petites puissances de 2.

De manière générale, le poids d’un bit ou d’un octet dépend de sa position dans l’écriture du nombre. Lorsqu’on se déplace

vers la gauche, le poids augmente : chaque déplacement vers la gauche multiplie la valeur par 2. À l’inverse, lorsqu’on se

déplace vers la droite, le poids diminue : chaque déplacement divise la valeur par 2.

Il est souvent utile de pouvoir désigner la partie la plus ou la moins importante d’un nombre, c’est-à-dire celle qui pèse le

plus ou le moins dans le calcul de sa valeur. Cela correspond aux symboles placés le plus à gauche ou le plus à droite dans

l’écriture du nombre, quelle que soit la base utilisée. On parle ainsi du bit de poids fort et du bit de poids faible pour un

nombre binaire, du chiffre de poids fort ou de poids faible pour un nombre décimal, ou encore du symbole hexadécimal de poids

fort ou faible.

Par extension, lorsqu’un nombre binaire est écrit sur plusieurs octets, on appelle octet de poids fort l’ensemble des huit

bits situés le plus à gauche dans l’écriture binaire de ce nombre, et octet de poids faible l’ensemble des huit bits situés

le plus à droite. Ainsi, la position détermine directement l’importance d’un bit ou d’un octet dans la valeur totale du

nombre, ce qui justifie les notions de poids fort et de poids faible.

### 1.3 Changement de base

<b> Pourquoi faut-il faire des conversions de base? </b>

Il faut faire des conversions entre les base 10 et les base 2. La base 10 est compréhensible par les être humains mais ne peut être traitée par les ordinateurs. Les ordinateurs ne peuvent calculer qu'en base 2.

<b> Comment convertir un nombre binaire en base 8 (octale) ou en base 16 (hexadécimale)? </b>

Pour passer de la base 2 à la base 8, on regroupe les bits par paquets de 3, en partant toujours des bits de poids faible,

c’est-à-dire depuis la droite. Chaque groupe de 3 bits correspond directement à un chiffre octal. Par exemple, pour le nombre

binaire 101101000110₂, on le découpe de droite à gauche en groupes de trois bits : 110, 000, 101 et 101. Chaque groupe est

ensuite remplacé par sa valeur en base 8 : 110 vaut 6, 000 vaut 0, et 101 vaut 5. On obtient ainsi le nombre 5506₈.

Le même principe s’applique pour passer de la base 2 à la base 16, mais cette fois en regroupant les bits par groupes de 4,

car 16 = 2⁴.Le nombre 101101000110₂ devient alors (1011 0100 0110)₂, ce qui correspond en hexadécimal à b46₁₆.

Voici deux exemples détaillés, l’un pour la base 8 (octale) et l’autre pour la base 16 (hexadécimale), à partir d’un nombre binaire.

Exemple de conversion en base 8 (octale):

Prenons le nombre binaire :

```
1101011(base2)

```

On regroupe les bits par 3, en partant de la droite (bits de poids faible) :

Attention => (1101011)² le 2 veut dire en Base 2 et pas exposant.

```
(1101011)² ​→ 1 101 011

```

On complète avec des zéros à gauche si nécessaire :

```
001 101 011

```

On convertit chaque groupe de 3 bits en octal :

```
001 = 1

101 = 5

011=3

```

On obtient le nombre en base 8 :

```

153(base8)

```

Exemple de conversion en base 16 (hexadécimale):

```
(101111010)² → 1 0111 1010

```

On complète avec des zéros à gauche si nécessaire :

```
0001 0111 1010

```

On convertit chaque groupe de 3 bits en octal :

```
0001 = 1

0111= 7

1010 = a (10 en décimal) (8+0+2+0=10)

```

On obtient le nombre en base 8 :

```
17a (base16)

```

<b> Comment convertir un nombre binaire en base 8 (octale) ou en base 16 (hexadécimale)? </b>

le passage entre la base 2 (binaire) et la base 10 (décimale) est plus complexe que le passage vers les bases 8 ou 16. En

effet, il n’existe pas de correspondance directe entre les bits et les chiffres décimaux, ce qui oblige à effectuer des

calculs intermédiaires.

Pour convertir un nombre binaire en décimal, on utilise le principe des puissances de 2. Chaque bit à 1 dans l’écriture

binaire représente une puissance de 2 qu’il faut additionner. Par exemple, pour le nombre 101101000110₂, on repère les

des bits égaux à 1 et on additionne les puissances de 2 correspondantes :

2¹¹ + 2⁹ + 2⁸ + 2⁶ + 2² + 2¹.

La somme de ces valeurs donne 2886 en base 10. Les bits à 0, quant à eux, ne contribuent pas à la valeur du nombre.

Dans le sens inverse, pour passer du décimal au binaire, on procède par divisions successives par 2. À chaque division, le

reste (0 ou 1) indique le bit de poids faible du nombre. On recommence ensuite la division avec le quotient obtenu, et ce

jusqu’à ce que le quotient soit égal à 1. Les restes sont alors lus de bas en haut pour former l’écriture binaire du nombre.

Cette méthode garantit une conversion correcte entre le système décimal et le système binaire, même si elle est plus longue

que les conversions impliquant les bases 8 ou 16.

Exemple 1 : passage du binaire au décimal

Prenons le nombre binaire :

```
101101 (base 2)

```

On repère les positions des bits à 1 et on additionne les puissances de 2 correspondantes.

```
101101₂ = 1 × 2⁵ + 0 × 2⁴ + 1 × 2³ + 1 × 2² + 0 × 2¹ + 1 ×2⁰

```

Ce qui donne :

```
= 32 + 8 + 4 + 1 = 45

```

Donc :

```
101101 (base 2) = 45 (base 10)

```

<b> Comment convertir un nombre décimal en code (système) binaire? </b>

​![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/Ch_1_conversion2a10.png)

<b> Exemple détaillé </b>

Convertissons 117 en base 10 en binaire.

```
117 ÷ 2 = 58  reste 1

58  ÷ 2 = 29  reste 0

29  ÷ 2 = 14  reste 1

14  ÷ 2 = 7   reste 0

7   ÷ 2 = 3   reste 1

3   ÷ 2 = 1   reste 1

1   ÷ 2 = 0   reste 1

```

On lit les restes du bas vers le haut :

```
1110101

```

Résultat final:

```
117 (base 10) = 1110101 (base 2)

```

### 1.4 Arithmétique binaire

<b> Addition : </b>

Règles de base de l’addition binaire

0 + 0 = 0

0 + 1 = 1

1 + 0 = 1

1 + 1 = 0 avec une retenue de 1

<b> Additionnons les deux nombres binaires suivants : </b>

```
  1011
+ 0110
------

```

<b> Calcul détaillé (de droite à gauche) </b>

Colonne la plus à droite:

```
1 + 0 = 1

```

Colonne suivante:

```
1 + 1= 2 en décimal, soit 0 en binaire avec une retenue de 1

```

Colonne suivante:

```
0+1=1 , plus la retenue  1 → 1 + 1 = 2

Résultat : 0, retenue 1

```

Colonne suivante :

```
1 + 0 = 1 plus la retenue 1, 1 → 10 en binaire

Résultat : 0, retenue 1

```

Retenue finale:

```
On écrit la retenue restante 1

```

Résultat final :

```
  1011
+ 0110
------
 10001


```

<b> Vérification :</b>

```
1011 (en base 2) = 11 (en base 10)

0110 (en base 2) = 6 (en 10)

-------------------------------
10001 (en base 2) = 17 (en base 10)

```

<b> Soustraction :</b>

Règles de base de la soustraction binaire

0 − 0 = 0

1 − 0 = 1

1 − 1 = 0

0 − 1 : impossible sans emprunt → on emprunte 1 au bit de gauche

```
  1011
- 0110
------
  0111

```

<b> Multiplication : </b>

La multiplication binaire fonctionne sur le même principe que la multiplication décimale, mais elle est beaucoup plus simple, car elle ne met en jeu que deux chiffres : 0 et 1.

Règles de base de la multiplication binaire

0 × 0 = 0

0 × 1 = 0

1 × 0 = 0

1 × 1 = 1

Autrement dit, multiplier par 0 donne toujours 0, et multiplier par 1 conserve le nombre.

Principe général

Pour multiplier deux nombres binaires, on procède de droite à gauche :

chaque bit du multiplicateur multiplie le multiplicande ;

si le bit est 0, on écrit une ligne de zéros ;

si le bit est 1, on recopie le multiplicande ;

à chaque ligne, on décale le résultat d’un rang vers la gauche ;

on additionne ensuite toutes les lignes obtenues.

Exemple détaillé

Multiplions 101₂ par 11₂.

```
    101
×    11
---------
    101   (101 × 1)
   101    (101 × 1, décalé d’un rang)
---------
  1111

```

<b> Vérification en base 10 :</b>

```
101 (en base 2) = 5 (en base 10)

11 (en base 2) = 2 (en base 10)

5 x 3  = 15

1111 (en base 2) = 15 (en base 10)

```

<b> Division : </b>

Très difficile.

### 2. NOMBRES NÉGATIFS

### 2.1 Représentation « signe et valeur absolue »

Ce texte décrit une première méthode historique pour représenter les nombres signés en binaire, appelée la représentation signe–valeur absolue. L’idée principale

consiste à utiliser le bit de poids fort, c’est-à-dire le bit le plus à gauche, pour indiquer le signe du nombre.

Dans cette représentation, sur un mot de n bits, le bit de poids fort joue le rôle de bit de signe. Selon la convention la plus courante, un bit de signe égal à

0 indique un nombre positif, tandis qu’un bit égal à 1 indique un nombre négatif. Les n− 1 bits restants servent alors à coder la valeur absolue du nombre en

binaire. Par exemple, sur 8 bits, le mot binaire 01011001 représente le nombre +89, tandis que 10110100 représente −52 : seul le bit de poids fort change pour

indiquer le signe, la partie droite donnant la valeur absolue.

Du point de vue des capacités de représentation, cette méthode ne permet pas de représenter davantage de nombres qu’une représentation non signée. Sur n bits, on

peut toujours coder au maximum 2 exposant n (2^n) combinaisons différentes. En revanche, l’intervalle des valeurs change : on passe de l’intervalle [0, 2^n − 1]

à un intervalle centré autour de zéro. Un inconvénient majeur apparaît alors : le zéro peut être représenté de deux façons différentes, +0 (00…0) et −0 (10…0). À

cause de cette duplication, on ne dispose en réalité que de 2^n − 1

valeurs numériques distinctes.

Sur le plan arithmétique, cette représentation présente à la fois un avantage et un inconvénient. Il est très simple de connaître le signe d’un nombre, puisqu’il

suffit de regarder le bit de poids fort, et changer le signe revient simplement à inverser ce bit. En revanche, les opérations arithmétiques comme l’addition

deviennent complexes. Les règles habituelles d’addition binaire ne s’appliquent plus directement, car additionner les bits reviendrait à additionner les valeurs

absolues sans tenir compte des signes. Il faut donc d’abord examiner les signes des deux nombres, décider s’il s’agit d’une addition ou d’une soustraction des

valeurs absolues, puis déterminer le signe du résultat. Ces manipulations compliquent et ralentissent les calculs.

En raison de ces difficultés arithmétiques et de la présence de deux zéros, cette représentation n’est aujourd’hui plus utilisée en pratique, au profit de

méthodes plus efficaces comme le complément à deux.

### 2.2 Représentation en complément à 2 :

Principe général

En complément à 2, un nombre est écrit sur un nombre fixé de bits, noté

𝑛. Avec n bits, on peut représenter exactement 2^n valeurs différentes, comprises dans l’intervalle

​![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/Ch_1_10_complement_form.png)
.

Un nombre positif est représenté de manière classique, par son écriture binaire habituelle. En revanche, un nombre négatif

est obtenu en calculant le complément à 2 de sa valeur absolue : on inverse tous les bits (complément à 1), puis on ajoute 1,

en ignorant une éventuelle retenue finale.

​![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/Ch_1_10_complement2.png)

​![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/Ch_1_10_complement2.png)

https://www.youtube.com/watch?v=26C729OYfP0

<b> Étape 1 : écrire la valeur absolue en binaire </b>

La première étape consiste à écrire la valeur absolue du nombre en binaire, sur le nombre de bits choisi. Si le nombre ne

remplit pas tous les bits, on complète à gauche avec des zéros. À ce stade, on dispose de l’écriture binaire du nombre

positif correspondant.

On commence par écrire 13 en base 10 en binaire sur 8 bits :

En base 10 :

```
5₁₀ = 101₂

```

<b> Étape 2 : Vérifier l'intervalle :</b>

Avant de calculer le complément à 2 (et donc avant même le complément à 1), il faut vérifier que le nombre à représenter

appartient bien à l’intervalle autorisé par le nombre de bits choisi.

Pour une représentation sur n bits en complément à 2, les valeurs possibles sont :

```
[ −2^(n−1) , 2^(n−1) − 1 ]

```

Ici n est le nombre de bit, ici => 3: 101₂

```
-2² < -5 < 2² - 1

 -4 < -5 < 3 > Faux

```

Comme ici -5 n'est pas compris entre -4 et 3, il faut rajouter un bit valant 0 devant 101₂.

Ici on a n = 4.

```
-2⁴ < -5 < 2⁴ - 1

 -16 < -5 < 15 > Vrai

```

On va donc reprendre ceci pour la partie suivante:

```
101₂ devient 0101₂

```

<b> Étape 3 : le calcul du complément à 1 : </b>

Ici on doit le calcul du complément à 1. Pour cela, on inverse tous les bits du nombre obtenu : chaque 0 devient 1 et chaque

1 devient 0. Cette inversion concerne l’ensemble des bits, sans exception. Le résultat représente le complément à 1 du nombre

initial.

On part du nombre binaire :

```
0101₂

```

On inverse tous les bits, sans exception :

chaque 0 devient 1

chaque 1 devient 0

```
0101

↓ ↓ ↓ ↓   Le complément à 1 de 0101₂ est 1010₂

1010

```

<b> Étape 3 : le calcul du complément à 1 : </b>

La dernière étape consiste à ajouter 1 au résultat précédent. Cette addition transforme le complément à 1 en complément à 2.

Si une retenue apparaît au-delà du nombre de bits choisis, elle est simplement ignorée. Le mot binaire obtenu à la fin de

cette étape est la représentation du nombre négatif en complément à 2.

```
 1010
+    1
------
  1011

```

Complément à 2 de 1010₂ = 1011₂.

<b> Pourquoi utiliser le complément à 2 (CA2)?</b>

Il permet d’éviter des circuits matériels supplémentaires, en particulier pour la soustraction.

Grâce au complément à 2 :

la soustraction est transformée en addition,

un seul circuit d’addition binaire suffit pour :

l’addition de nombres positifs,

l’addition de nombres négatifs,

la soustraction (via l’addition de l’opposé).

Ce texte explique le fonctionnement de l’arithmétique en complément à 2 et montre pourquoi cette représentation est

particulièrement efficace pour effectuer des calculs avec des nombres signés en binaire.

Le principal avantage du complément à 2 est qu’il simplifie énormément l’addition. Contrairement aux anciennes

représentations, il n’est plus nécessaire de traiter séparément le signe des nombres. Pour additionner deux entiers, qu’ils

soient positifs ou négatifs, il suffit de les écrire tous les deux en complément à 2, puis d’effectuer une addition binaire

classique bit à bit. Si une retenue dépasse le nombre de bits choisis, elle est simplement ignorée. Par exemple, pour calculer

118+(−36), on écrit 118 et −36 en complément à 2 sur le même nombre de bits, on les additionne normalement, et on obtient

directement le résultat 82. Cette propriété rend les circuits de calcul beaucoup plus simples et rapides.

Dans ce cadre, soustraire un nombre revient à additionner son opposé. Or l’opposé d’un nombre en complément à 2 est

précisément obtenu en calculant son complément à 2. Ainsi, une soustraction peut être transformée en addition, ce qui évite

d’avoir un circuit spécifique pour la soustraction.

La multiplication, en revanche, est plus complexe. La méthode la plus simple consiste à travailler sur les valeurs absolues

des deux nombres, à appliquer l’algorithme classique de multiplication binaire, puis à donner au résultat le bon signe : le

résultat est négatif si les deux nombres sont de signes opposés. Il existe toutefois des algorithmes plus avancés, comme le

recodage de Booth, qui exploitent les propriétés du binaire pour accélérer les multiplications, au prix d’une électronique

plus complexe. Pour la division, on applique également la division aux valeurs absolues, puis on ajuste le signe du quotient

(et éventuellement du reste).

Le texte rappelle aussi comment interpréter mathématiquement un nombre en complément à 2. Un mot binaire de la forme 𝑥

xn−1​…x0 est lu comme la somme des puissances de 2 associées aux bits, à l’exception du bit de poids fort, qui est soustrait

s’il vaut 1. Autrement dit, le bit de poids fort joue un rôle négatif et permet de coder les nombres inférieurs à zéro.

Plusieurs propriétés fondamentales du complément à 2 sont ensuite présentées. Sur n

n bits, un nombre et son complément à 2 vérifient la relation C2(X)=2^n−X.

Cela signifie que le complément à 2 d’un nombre peut être calculé simplement par C2(X)=2^n−X . Une autre propriété importante

est que le complément à 2 est une opération involutive : si l’on prend deux fois le complément à 2 d’un nombre, on retrouve

le nombre initial. Ainsi, pour connaître la valeur décimale d’un nombre binaire négatif, il suffit de calculer son complément

à 2 pour obtenir sa valeur absolue, puis d’ajouter le signe négatif. Par exemple, le complément à 2 de 11001100 est 00110100,

soit 52, ce qui signifie que 11001100 représente −52.

Enfin, le texte met en évidence le lien entre la lecture signée et la lecture non signée d’un même mot binaire. Un même mot

de 2^n bits peut être interprété soit comme un entier non signé (en additionnant simplement les puissances de 2), soit comme

un entier signé en complément à 2. La différence entre ces deux lectures vaut toujours 2^n.Par exemple, le mot binaire

10101010 vaut 170 en non signé, mais −86 en complément à 2, et l’on vérifie bien que

170 − ( − 86 )=256 =2⁸

En résumé, le complément à 2 offre une représentation cohérente et efficace des entiers signés, permettant de réaliser les

opérations arithmétiques de base de manière simple, rapide et fiable, ce qui explique son adoption universelle en

informatique.

### 2.3 Extension de signe

Ce texte explique le principe de l’extension d’un nombre binaire sur un plus grand nombre de bits et montre que la méthode à

utiliser dépend du type de représentation du nombre. L’objectif est toujours le même : conserver exactement la même valeur

numérique après l’extension.

Dans de nombreux cas pratiques, les systèmes informatiques doivent manipuler des données de tailles différentes. Par exemple,

pour additionner un nombre stocké sur 1 octet avec un nombre stocké sur 2 octets, il est indispensable de mettre les deux

opérandes sur la même taille, ici 16 bits. De même, lorsqu’un microprocesseur charge une valeur d’un octet depuis la mémoire

dans un registre de 32 bits, il faut étendre cette valeur sans en modifier le sens. Pour cela, on effectue ce que l’on

appelle une extension de signe.

Dans le cas des nombres non signés, la règle est très simple. Comme ces nombres ne représentent que des valeurs positives ou

nulles, il suffit d’ajouter des zéros à gauche du nombre lors de l’extension. Ces zéros n’ont aucun effet sur la valeur du

nombre. Par exemple, le nombre non signé 11010011 écrit sur 8 bits devient 0000000011010011 lorsqu’il est étendu sur 16 bits.

Lorsque l’on travaille avec des nombres signés représentés selon la convention « signe et valeur absolue », l’extension se

fait différemment. Le bit de signe doit être recopié dans le nouveau bit de poids fort, afin de conserver l’information de

signe, tandis que les autres nouveaux bits sont remplis par des zéros. Ainsi, le nombre positif 01101000 devient

0000000001101000 sur 16 bits, et le nombre négatif 11111011 devient 1000000001111011 après extension. La valeur absolue reste

inchangée et le signe est correctement conservé.

Enfin, pour la représentation en complément à 2, qui est la représentation standard des entiers signés, la règle est encore

différente mais très cohérente. Il faut recopier le bit de signe dans tous les nouveaux bits ajoutés à gauche. Si le nombre

est positif, le bit de signe vaut 0 et l’on ajoute donc des zéros en tête. Si le nombre est négatif, le bit de signe vaut 1

et l’on ajoute des uns en tête. Par exemple, 00100110 devient 0000000000100110 après extension, tandis que 10001111 devient

1111111110001111. Cette méthode garantit que la valeur du nombre, lorsqu’elle est interprétée en complément à 2, reste

exactement la même avant et après l’extension.

Ainsi, quelle que soit la représentation utilisée, l’extension d’un nombre doit respecter des règles précises pour préserver

sa valeur. En pratique, la recopie du bit de signe dans le cas du complément à 2 est essentielle, car elle assure la

cohérence des calculs et le bon fonctionnement des opérations arithmétiques dans les microprocesseurs.

### 2.4 Débordement

https://www.youtube.com/watch?v=Q7t9-Sq_4Ww

Le débordement binaire (overflow) apparaît lorsque le résultat d’une opération arithmétique ne peut pas être représenté dans

la taille de bits imposée par le système, par exemple sur 8 bits, 16 bits ou 32 bits. Comme les registres et les circuits du

processeur ont une taille fixe, tout calcul produisant une valeur en dehors de l’intervalle autorisé entraîne une perte
d’information.

Dans le cas des nombres non signés, un entier codé sur n bits peut représenter des valeurs comprises entre :

```
0 et 2^n − 1

```

Lors d’une addition, il y a débordement si la somme dépasse cette valeur maximale. En pratique, ce débordement se détecte par

la présence d’une retenue finale lors de l’addition binaire. Le processeur conserve uniquement les n bits de poids faible et

ignore la retenue, ce qui conduit à un résultat incorrect si l’on ne tient pas compte de l’overflow.

Lors d’une soustraction non signée, le débordement apparaît lorsque le résultat devrait être négatif, ce qui est impossible à

représenter. Le calcul donne alors une valeur « repliée » modulo :

```
2^n

```

Cette valeur ne correspond pas au résultat mathématique attendu. Là encore, le résultat binaire obtenu est faux du point de

vue du calcul non signé.

Dans tous les cas, le débordement signifie que le résultat affiché ou stocké n’est pas le bon. Il est donc essentiel de le

détecter afin de corriger le calcul, d’arrêter l’exécution ou de gérer l’erreur. La gestion du débordement est un aspect

fondamental de l’arithmétique binaire et de la conception des systèmes informatiques, car elle garantit la fiabilité des

calculs effectués sur des tailles de mots fixes.

<b> Nombres non signés et débordement: </b>

Sur n bits, un entier non signé peut prendre des valeurs entre :

```
0 et 2^n − 1

```

Par exemple, sur 8 bits, l’intervalle est :

```
0 à 255

```

Exemple 1 : addition avec débordement (8 bits)

On additionne 156 et 168 sur 8 bits.

Conversion en binaire (8 bits)

156 = 10011100

168 = 10101000

Addition binaire (copiable):

```
  10011100   (156)
+ 10101000   (168)
----------
1 01000100

```

Le résultat sur 9 bits est 1 01000100

Si on ne garde que 8 bits (ce que fait un registre 8 bits), on obtient 01000100, qui vaut 68

Mais 156 + 168 = 324, et 324 ne tient pas sur 8 bits → débordement

Le 1 tout à gauche est la retenue finale : c’est elle qui signale l’overflow.

<b> Débordement en soustraction (non signé) : </b>

En non signé, une soustraction peut aussi provoquer un débordement si le résultat devrait être négatif, car les nombres non

signés ne représentent pas les valeurs < 0. Dans ce cas, la machine « replie » le résultat modulo 2^n

, ce qui donne une valeur incorrecte si on l’interprète comme un entier non signé attendu.

Exemple 2 : soustraction menant à un résultat négatif:

On calcule 27 − 100 sur 8 bits.

En décimal, le vrai résultat est : 27 − 100 = −73 (non représentable en non signé)

Sur 8 bits, la machine donnera un résultat “replié” : 183 (car 256−73=183)

Binaire (8 bits)

27 = 00011011

100 = 01100100

```
  00011011   (27)
- 01100100   (100)
----------
  10110111   (183)   <-- résultat replié sur 8 bits

```

<b> Débordément des compléments à 2 :</b>

Addition de deux nombres positifs donnant un résultat négatif → débordement

Addition de deux nombres négatifs donnant un résultat positif → débordement

Signes différents → jamais de débordement

<b> Addition de deux nombres positifs donnant un résultat négatif → débordement : </b>

Exemple : 77 + 68

Représentation binaire (8 bits):

```
77 = 01001101
68 = 01000100

```

Addition:

```
  01001101
+ 01000100
----------
  10010001


```

Interprétation:

```
10010001 (complément à 2) = -111

```

Erreur :

```
77 + 68 = 145

```

Or 145 > 127 (valeur max sur 8 bits signés)

➡️ Débordement

<b> Addition de deux nombres négatifs donnant un résultat positif → débordement : </b>

Exemple : -70 + (-80)

Représentation binaire (8 bits)

```
70  = 01000110
-70 = 10111010

80  = 01010000
-80 = 10110000

```

Addition:

```
  10111010
+ 10110000
----------
1 01101010

```

On ignore la retenue finale :

```
01101010 = 106

```

Interprétation:

```
-70 + (-80) = -150

```

Or -150 < -128 (valeur min sur 8 bits signés)

➡️ Débordement

Addition de deux nombres de signes différents → jamais de débordement

Exemple : 50 + (-30)

```
Représentation binaire (8 bits)
50  = 00110010
30  = 00011110
-30 = 11100010

Addition
  00110010
+ 11100010
----------
1 00010100

```

On ignore la retenue finale :

```
00010100 = 20

```

Vérification:

```
50 + (-30) = 20

```

👉 Résultat correct, aucun débordement

### 3. NOMBRES RÉELS
