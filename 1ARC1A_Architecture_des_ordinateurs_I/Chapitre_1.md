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

​![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/Ch_1_conversion2a10.png)

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
