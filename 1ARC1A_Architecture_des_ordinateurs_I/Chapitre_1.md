# Chapitre 1

## Représentation des nombres

### 1. CALCUL BINAIRE ET ENTIERS POSITIFS

Calcul dans une base quelconque

Un calcul dans une base quelconque consiste à représenter et manipuler des nombres dans un système de numération dont la base n’est pas forcément 10 (le système décimal habituel). La base, notée B, indique le nombre de symboles différents utilisés pour écrire les nombres et la valeur par laquelle chaque position est pondérée.

Dans une base B, les chiffres possibles vont de 0 à B−1. La valeur d’un chiffre dépend donc à la fois de sa valeur propre et de sa position dans le nombre. Chaque position correspond à une puissance de la base.

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/chapitre_1_form_general.png)
![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/chapitre_1_exemple.png)

<b> Remarque </b>

l’écriture d’un nombre peut être ambiguë si la base n’est pas précisée. En effet, une même suite de chiffres peut représenter des valeurs très différentes selon le système de numération utilisé.

Prenons l’exemple de l’écriture 101. Si on la lit en base 10 (système décimal), elle représente simplement le nombre cent un. En revanche, si on interprète cette même écriture en base 6, sa valeur change : le chiffre 1 de gauche correspond à
6², le 0 à 6¹ et le 1 de droite 6⁰. On obtient alors 1×62+0×6+1=36+1=37. Enfin, en base 2 (binaire), l’écriture 101 correspond à 1×22+0×2+1=4+1=5.

Ainsi, sans indication de la base, il est impossible de connaître la valeur exacte du nombre. Pour lever toute ambiguïté, on précise généralement la base en l’indiquant en indice. On écrit par exemple

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/Ch_1_10.png)

pour le décimal,
![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/Ch_1_06.png)

pour la base 6 ou
​![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/Ch_1_02.png)

pour le binaire. Cette notation permet de savoir immédiatement dans quel système de numération le nombre est exprimé et d’éviter toute confusion.

#### 1.1 Calcul dans une base quelconque
