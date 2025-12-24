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

Ils sont les 3 cannaux de communication par défaut du système Unix / Linux. Le shell permet de rediriger ces entrées et

sorties. Dans l'expemple on a redirigé ls vers un fichier (out) à l'aide de >.

Cela veut dire que le résultat de la commande ls n'est afficher sur l'ecran, mais est enregistré dans un fichier.

**Numérotation des entrées/sorties**

Par convention, trois numéros sont attribués dès le lancement de tout processus. Le numéro 0 correspond à l’entrée standard,

généralement reliée au clavier. Le numéro 1 désigne la sortie standard, qui est reliée à l’écran et utilisée pour afficher

les résultats normaux d’un programme. Le numéro 2 correspond à la sortie d’erreur standard, elle aussi reliée à l’écran par

défaut, mais réservée aux messages d’erreur.

Lorsqu’un programme s’exécute, il n’a donc pas besoin de savoir où vont ses données. Il se contente d’indiquer qu’il veut

lire depuis l’entrée 0 ou écrire sur la sortie 1 ou 2. Par exemple, lorsqu’un programme « écrit sur 1 », cela signifie qu’il

envoie un texte vers la sortie standard. Tant que cette sortie est connectée à l’écran, le texte s’affiche dans le terminal.

Si, en revanche, la sortie standard est redirigée vers un fichier, ce même texte sera écrit dans ce fichier sans que le

programme n’ait à être modifié.

Cette numérotation rend les redirections très puissantes et flexibles. Le shell peut décider de relier ces numéros à des

fichiers, au terminal ou à d’autres programmes, tandis que le processus continue simplement à lire et écrire sur ses entrées

et sorties numérotées.

![permission_cat](https://github.com/Wextc/ESI_Bachelier/tree/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes)
