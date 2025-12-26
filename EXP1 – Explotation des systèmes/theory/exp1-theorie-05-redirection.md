## EXP1A-T – Chapitre 5 : Redirections et tuyaux

### 5.1 – Entrée-sorties standards et redirection

Comment comprendre ceci ?

```
$ ls
test

$ ls > out
$ ls
out test

$ cat out
out
test



```

Ls va simplement afficher le contenu du repertoire courant. Ici il y a un seul élément test.

Ls va envoyer le résultat vers la sortie standard du terminal.

´´´
$ ls
test

```

Le symbole  > signifie redirection.

Via ce symbole le système redirigge la sortie standard de la commande ls vers un fichier nommé out. Cela implique que le

contenu du répertoire ne soit plus afficher à l'écran mais est écrit dans le ficher créé appelé out.



´´´
$ ls > out
$ ls

```

Si on refait ls sur le répertoire courant on peut observer le fichier out.

´´´
$ ls
test
out test

```
Grâce à la commande cat on peut afficher le contenu du ficher out. On voit qu'il contient ce que la commande ls aurait

afficher s'il n'y avait pas eut de redirection. Le fichier out est listé, ici car le fichier out est créé avant que la

commande ls ne soit lancée.


´´´
$ cat out
out
test

```

**Entrées et sorties standard**

l’entrée standard (stdin) : le clavier par défaut

la sortie standard (stdout) : l’écran par défaut

la sortie d’erreur standard (stderr) : l’écran par défaut également

Dans les système UNIX les processus ne manipulent directement le clavier et l'écran.

Ils utilisent 3 cannaux de communication définis par défaut. Ce sont les entrées et sorties standards, qui sont identifiées

par des numéros.

**Numérotation des entrées/sorties**

![permission_cat](https://github.com/Wextc/ESI_Bachelier/tree/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/theory/img/img_1.png)

Par convention, on attribue 3 numéros aux cannaux de communication.

l’entrée standard (stdin) : le clavier par défaut correspond descriptif numéro O

la sortie standard (stdout) : l’écran par défaut correspond descriptif numéro 1

la sortie d’erreur standard (stderr) : l’écran par défaut également correspond descriptif numéro 2

Cette numérotation rend la redirection flexible.

Pourquoi?

Lors de l'affichage des données, le programme se contente d'envoyer ces données vers la sorite standard identifiée par le

numéro 1.

Pour le programme "afficher" les données signifie simplement écrire sur 1.

Par la suite, le shell va jouer le rôle d'intermédiaire, et va décider à quoi relier le descripteur 1. S'il n'y a pas de

redirection les données sont afficher par défaut sur le terminal. S'il y a une redirection par exemple avec le symbole > le

shell le descripteur 1 au fichier où les données sont redirigées. Celles-ci ne s'affichent plus dans le terminal, mais sont

bien présentent dans le fichier.

<b> Remarque :</b>

Par défaut, tout programme a :

une entrée standard → le clavier

une sortie standard → le terminal

une sortie d’erreur → le terminal

**Redirection**

Le gestion de la redirection des entrées et des sorties par le shell fait qu'elle est transparente pour le processus qui

s'exécute.

Avant l'exécution de la commande suivante, le shell va préparer l'environnement d'exécution en créant le fichier ( ou en

écrasant s'il existe) out. Puis, il relie la sortie standard c’est-à-dire le descripteur numéro 1, à ce fichier. Une fois la

liaison effectuée le shell lance la commande ls -a brol. La commande ls affiche sur le descriptif 1, et là le shell va le

rediriger vers le fichier concerné.

**_ Syntaxe des redirections (bash)_**

```
> file
Redirige la sortie standard dans le fichier file
(le fichier est créé ou vidé)

>> file
Idem mais ajoute au fichier

< file
Redirige l’entrée standard
(les lectures se font dans le fichier et non plus au clavier)

2> file
Redirige les messages d’erreur

&> file
Redirige sortie standard et erreurs

```

La redirection < fait que l'entrée standard du programme soit le fichier à la place du clavier. Le fichier n'est pas modifié

il est uniquement lu. La sortie standard reste le terminal. Ainsi, les fichiers sont simplement affichées.

La redirection > fait que l'entrée standard du programme soit le clavier et non pas le fichier. Le fichier devient la sortie

standard. Il est modifié.

Prenons l'exemple de cat, mais la redirection fonctionne avec plein d'autre commandes.

Elle va afficher le contenu de file.

```
cat < file


```

Cette commande va permettre de saisir des données via le terminal et l'enregistrer dans le fichier.

```
cat > file

```

Avec <, les données proviennent d’un fichier. Il s’agit d’une redirection classique de l’entrée standard : le shell relie

l’entrée standard du programme à un fichier existant. Le programme lit alors ses données dans ce fichier exactement comme

s’il les recevait depuis le clavier. Il n’y a pas d’interaction particulière avec l’utilisateur pendant l’exécution : on

fournit simplement au programme une source de données externe.

Avec <<, les données ne proviennent pas d’un fichier, mais d’un texte fourni directement au shell. Le shell lit ce bloc de

texte jusqu’au mot de fin défini, le stocke temporairement dans un flux interne, puis relie l’entrée standard du programme à

ce flux. Le programme reçoit alors ces données comme s’il s’agissait d’une saisie clavier. Il ne s’agit pas de « code », mais

bien de données textuelles destinées à être lues.

Dans les deux cas, le comportement du programme est identique : il lit simplement depuis son entrée standard. Il ne sait pas

si les données viennent d’un fichier, d’un texte intégré ou du clavier. Pour lui, il n’existe qu’un flux d’entrée prêt à être

consommé, entièrement géré par le shell.

```
cat << FIN

Bonjour

Ceci est un exemple

de here-document

FIN


```

Ici, le programme s'arrète quand on atteint le mot FIN.

La redirection 2> s'intéresse à la sortie sortie d’erreur standard, qui correspond au descriptif 2. Par défaut, les

message d'erreur s'affiche à l'écran, comme la sortie standard. Cette redirection fait que le shell relie la sortie standard

d'erreur à un fichier.

```
...commande...   2> file

```

La redirection &> file permet quant à elle de rediriger à la fois la sortie standard et la sortie d’erreur vers un même

fichier.

```
...commande...   &> file

```

**_ Exemple de la commande cat _**

Lorsque la commande cat est utilisée sans argument, l’entrée standard est celle par défaut, à savoir le clavier, et la sortie

standard est celle par défaut, à savoir le terminal. Dans ce cas, cat lit ce que l’utilisateur tape au clavier et l’affiche

immédiatement à l’écran.

Lorsque la commande cat est utilisée avec un fichier en argument sans le symbole de redirection (<, >, >>, 2>, <<, etc.), ce

n’est pas le shell qui redirige l’entrée standard vers le fichier. C’est le programme cat lui-même qui ouvre le fichier, lit

son contenu et l’écrit sur la sortie standard, qui reste le terminal. C’est pour cette raison que le contenu du fichier

s’affiche à l’écran.

La combinaison Ctrl+D sert à indiquer une fin de données sur l’entrée standard lorsque celle-ci est reliée au clavier. Elle

ne quitte pas le terminal et n’arrête pas le programme de force ; elle signale simplement qu’il n’y a plus rien à lire.

Enfin, Ctrl+C ne permet pas de quitter le terminal, mais d’interrompre le programme en cours d’exécution. Le terminal reste

ouvert après l’interruption.

**_ Exemples de redirections _**

Cette commande copie lit le contenu de file1 et l'écrit dans file dans file2. Via le symbole " < " , le shell relie l’entrée

standard de cat au fichier file1, puis via le symbole " > " redirige la sortie standard vers file2. Ainsi, cat va copier le

contenue de file1 dans file 2. La commande ne sait même pas que les ficher existe elle se contente de lire sur l’entrée

standard et d’écrire sur la

sortie standard.

Ici les données dans le fichier 2 sont écrasées.

```
cat < file1 > file2

```

Ici les données dans le fichier 2 sont rajoutées sans écraser le contenu.

```
cat < file1 >> file2

```

La commande find / -name test demande à find de parcourir le système de fichiers à partir de la racine / et de chercher tous

les fichiers ou répertoires dont le nom est test.

Pendant cette recherche, find produit deux types de messages :

    des résultats normaux (les chemins des fichiers trouvés)

    des messages d’erreur (par exemple « permission refusée »)

La redirection > res indique au shell de rediriger la sortie standard de find vers le fichier res. Ce fichier contiendra donc

uniquement la liste des fichiers trouvés.

La redirection 2> err indique au shell de rediriger la sortie d’erreur standard vers le fichier err. Ce fichier contiendra

uniquement les messages d’erreur.

```
find / -name test > res 2 > err

```

Remarque :

Dans cette commande l'entrée standard des fichiers res et err n'est pas un fichier, mais l'entrée standard clavier.

Seulement, dans ce cas-ci nous n'utilisons pas le clavier comme l'entrée standard.

Pourquoi?

Car les données traitées ne sont pas en

**\* Exercices – Redirections \*\***

Que fait la commande :

```
cat >journal

```

Parmi les utilisations suivantes de cat, lesquelles n’ont qu’un seul paramètre ?

```
cat

cat f >t

cat t

cat <f >t

cat <t

```

<b> Exemples :</b>

Le symbole | joue bien un rôle proche d’une redirection, dans le sens où il modifie le trajet des données. Cependant, au lieu

de rediriger la sortie standard vers un fichier, il la redirige vers l’entrée standard d’une autre commande.

Avec une redirection classique comme >, la sortie standard d’une commande est envoyée vers un fichier. Avec un pipe |, la

sortie standard d’une commande est envoyée directement vers une autre commande, qui la reçoit comme entrée standard.

Autrement dit, | permet de chaîner des commandes entre elles. Chaque commande fait son travail, puis transmet son résultat à

la suivante, sans passer par un fichier intermédiaire. Le shell se charge de connecter ces flux entre les processus.

La commande :

```
find ~ -name test | less

```

ne lance pas la recherche dans le répertoire courant.

Le symbole ~ désigne le répertoire personnel de l’utilisateur (par exemple /home/utilisateur), et non le répertoire courant ..

Cette commande demande donc à find de chercher, à partir de ton répertoire personnel, tous les fichiers ou répertoires nommés

test. La commande find écrit les résultats sur sa sortie standard. Grâce au pipe |, cette sortie standard est transmise à

l’entrée standard de less.

```
cat test | grep mot | grep autre

```

cat test lit le contenu du fichier test (parce que test est un argument de cat) et l’écrit sur sa sortie standard. Le premier

pipe | relie alors cette sortie standard à l’entrée standard de grep mot. La commande grep mot reçoit donc le texte produit

par cat et ne garde que les lignes qui contiennent la chaîne mot, qu’elle écrit à son tour sur sa sortie standard. Le second

pipe relie ensuite cette sortie standard à l’entrée standard de grep autre. Cette dernière commande filtre encore une fois le

flux et ne conserve que les lignes (déjà sélectionnées par le premier grep) qui contiennent aussi le mot autre. Au final,

l’affichage correspond uniquement aux lignes du fichier test contenant à la fois mot et autre (dans n’importe quel ordre sur

la même ligne).

**_ Filtres et principe KISS _**

Linux suit le principe KISS (Keep It Simple, Stupid).

De nombreuses commandes sont des filtres

Elles prennent leurs données sur stdin

Elles renvoient une version modifiée sur stdout

Chaque commande fait peu, mais le fait bien

Les enchaîner permet de réaliser une tâche complexe

La commande who affiche la liste des utilisateurs actuellement connectés au système. Chaque ligne contient généralement le

nom de l’utilisateur suivi d’autres informations (terminal, date, heure, etc.). Cette liste est envoyée sur la sortie

standard.

Le premier pipe transmet cette sortie standard à la commande cut. Avec l’option -d " ", cut utilise l’espace comme séparateur

de champs, et avec -f 1, il ne conserve que le premier champ de chaque ligne, c’est-à-dire le nom de l’utilisateur. On

obtient alors une liste de noms d’utilisateurs, potentiellement avec des répétitions si un même utilisateur est connecté

plusieurs fois.

Cette liste est ensuite transmise à sort. La commande sort trie les noms par ordre alphabétique. Ce tri est nécessaire pour

que la commande suivante puisse fonctionner correctement.

Le résultat trié est envoyé à uniq. La commande uniq supprime les doublons consécutifs et ne conserve qu’une seule occurrence

de chaque nom d’utilisateur. Comme la liste a été triée juste avant, tous les doublons sont bien regroupés, ce qui permet à

uniq de fonctionner correctement.

Enfin, la sortie de uniq est transmise à wc -l. La commande wc avec l’option -l compte le nombre de lignes reçues en entrée.

Chaque ligne correspondant à un utilisateur distinct, le résultat final est le nombre d’utilisateurs différents actuellement

connectés au système.

**_Exercices – Pipes _**

Décomposons-la étape par étape :

```
ls -a | wc > res

```

La commande ls -a liste tous les fichiers et répertoires du répertoire courant, y compris les fichiers cachés. Elle écrit

cette liste sur sa sortie standard.

Le pipe | relie cette sortie standard à l’entrée standard de la commande wc. La commande wc lit donc la liste produite par ls

-a comme si elle provenait du clavier.

Sans option, wc compte le nombre de lignes, de mots et de caractères reçus en entrée, puis écrit ces résultats sur sa sortie

standard.

Enfin, la redirection > res indique au shell de rediriger la sortie standard de wc vers le fichier res. Ce fichier contiendra

donc les comptes produits par wc.
