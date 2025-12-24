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

```
cat < file

```

Elle va afficher le contenu de file.

```
cat > file

```

Cette commande va permettre de saisir des données via le terminal et l'enregistrer dans le fichier.
