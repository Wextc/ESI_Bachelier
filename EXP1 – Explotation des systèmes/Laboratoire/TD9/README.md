Vidéo d'introduction :

git : FR:

https://www.youtube.com/watch?v=gGKZLfPYORs

https://www.youtube.com/watch?v=hwP7WQkmECE

git lab: ENG:

https://www.youtube.com/watch?v=qKxytMuUiJA&list=PLZMWkkQEwOPmGolqJPsAm_4fcBDDc2to_

### Pré-requis :

Pour pouvoir travailler avec gitlab, il faut installer git (un programme qui vous permet d'envoyer les

instructions sur les serveur de gitlab).

### Attention :

Lors de l'examen. Ilfaut se connecter sur le serveur linux1 pour pouvoir utiliser gtilab. Il faudra pouvoir

trouver des dossiers sur le linux puis les envoyer sur le gitlab.

Il faut faire les configurations avant d'aller en examen.

Pour se connecter sur gitlab la seule connection possible sera la la connection via le NOM D UTILISATEUR et le

PASSWD.

### 1.1 Concepts

Git est un logiciel de gestion de versions qui repose sur une organisation précise des données d’un projet

L’élément central est le dépôt (repository) : il contient l’ensemble de l’historique du projet, c’est-à-dire

toutes les versions successives des fichiers et les informations associées.

L’historique est constitué de commits.

Un commit représente l’état complet du projet à un instant donné. Il inclut :

le contenu des fichiers,

des métadonnées (auteur, date),

un message descriptif,

un identifiant unique.

Les commits sont organisés dans des branches.

Une branche permet de développer ou modifier le projet de manière indépendante. La branche principale s’appelle

généralement main (anciennement master). Une fois le travail terminé sur une branche secondaire, les

changements peuvent être fusionnés (merge) dans la branche principale.

Chaque commit référence son commit parent, ce qui forme un historique en chaîne. Lors d’une fusion, un commit

peut avoir plusieurs parents. Le tout premier commit est appelé commit racine.

### 1.2 Avant de commencer

Avant toute utilisation de Git sur une machine, il est indispensable de configurer l’identité de l’utilisateur

à l’aide de la commande git config.

Cela consiste à définir :

un nom (user.name)

une adresse e-mail (user.email)

Ces informations apparaissent dans l’historique des commits et sont visibles par toute personne ayant accès au

dépôt, notamment s’il est public. Il est donc important de les définir correctement dès le départ.

La configuration peut être :

globale (valable pour tous les dépôts),

ou locale (spécifique à un dépôt).

Les exercices du TD peuvent être réalisés sous Linux ou via Git Bash sous Windows.

### 1.3 Dépôt d’exercice

Pour faciliter le travail collaboratif et l’hébergement des projets Git, des plateformes comme GitHub, GitLab

ou Bitbucket sont utilisées.

À l’HE2B-ESI, une instance GitLab interne est mise à disposition des étudiants.

Le dépôt servant aux exercices du TD est accessible en lecture seule.

Pour pouvoir travailler dessus, chaque étudiant doit créer un fork, c’est-à-dire une copie personnelle du dépôt

original. Ce fork permet de disposer de son propre dépôt avec des droits d’écriture, tout en conservant un lien

avec le projet de départ.

Une fois le fork créé, son URL sera utilisée pour la suite du TD, notamment pour cloner le dépôt en local.

### Voici une liste des commandes :

<b> Commandes de configuration => git config :</b>

git config

Configure le comportement de Git.

Configurer son identité (obligatoire avant de commencer)

```
git config --global user.name "Votre Nom"

git config --global user.email "email@exemple.com"

```

➜ Définit le nom et l’email qui apparaîtront dans chaque commit.

--global : configuration valable pour tous les dépôts

--local : configuration valable uniquement pour le dépôt courant

<b> Dépôts et récupération du projet => git clone : </b>

Copie un dépôt distant sur ta machine.

```

git clone <url-du-depot> [nom-dossier]

```

➜ Crée un dossier contenant :

les fichiers du projet

le dossier caché .git (historique, branches, commits…)

Exemple :

```
git clone https://git.esi-bru.be/exp1/git-discover mon-projet

```

<b> Historique et exploration => git log : </b>

Affiche l’historique des commits.

git log

Chaque commit affiche :

son identifiant (hash)

l’auteur

la date

le message

```
git log --oneline

```

Version compacte de l’historique.

```
git log --oneline

```

➜ Un commit par ligne, avec :

identifiant court

message

Très pratique pour naviguer rapidement.

```
git log --name-status

```

Montre les fichiers modifiés dans chaque commit.

```
git log --name-status

```

Statuts possibles :

A : fichier ajouté (Added)

M : fichier modifié (Modified)

D : fichier supprimé (Deleted)

R : fichier renommé (Renamed)

```
git log -n <nombre>

```

Limite le nombre de commits affichés.

```
git log -n 2

```

➜ Affiche uniquement les 2 derniers commits

<b> Comparaison des versions => git diff :</b>

Compare le contenu de fichiers entre deux commits.

```
git diff <id1> <id2>

```

- : lignes présentes dans le premier commit

* : lignes présentes dans le second commit

➜ Montre ce qui a changé, ligne par ligne.

```
git diff HEAD HEAD~1

```

Compare le dernier commit avec le précédent.

HEAD : dernier commit

HEAD~1 : commit précédent

HEAD~2, HEAD~3, etc. : encore plus anciens

<b> Aide et documentation => git --help :</b>

Affiche la liste des commandes Git.

```
git --help

git <commande> --help

```

Affiche l’aide détaillée d’une commande.

```
git log --help

```

➜ Très utile quand tu ne te rappelles plus des options.

### Résumé ultra-court (mémo examen):

```
git config → configurer Git

git clone → récupérer un dépôt

git log → voir l’historique

git log --oneline → historique résumé

git log --name-status → fichiers modifiés

git diff → comparer des versions

HEAD, HEAD~1 → repérer les commits
```

### Clone local 1.4 :

La commande git clone sert à créer une copie locale complète d’un dépôt Git qui existe déjà ailleurs, le plus
souvent sur un serveur distant. Concrètement, lorsqu’on exécute git clone, Git télécharge l’intégralité du
projet : tous les fichiers, mais aussi tout l’historique des versions, les branches et les métadonnées. Une
fois le clonage terminé, un nouveau dossier est créé sur la machine locale ; il contient le projet prêt à être
consulté, modifié et versionné. Le dépôt cloné est automatiquement relié à sa source d’origine, ce qui permet
ensuite de récupérer les mises à jour ou d’envoyer ses propres modifications. En résumé, git clone est la porte
d’entrée classique pour commencer à travailler sur un projet Git existant.

```
git clone <url-dépot> [<destination>
lab
```

Après avoir installer git.
Il faut oouvrir le terminal et taper, et l'url du dossier dans gitlab que l'on veut copier dans le pc.

```
git clone https://git.esi-bru.be/exp1/git-discover

```

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/TD9/img/exercice1.png)

Remarque: Il faut se situer à la racine du dossier. Sinon, l'intégralité du dossier ne sera pas copié sur votre système.

### 1.5 Historique d’événements

La commande git log permet d’afficher l’historique des commits d’un dépôt Git.

Lorsqu’on l’exécute, Git liste les différentes versions du projet, de la plus récente à la plus ancienne, en indiquant pour chaque commit des informations essentielles comme son identifiant unique, l’auteur, la date et le message qui décrit les changements effectués. Cet historique sert à comprendre comment le code
a évolué dans le temps, à identifier quand et pourquoi une modification a été faite, ou encore à retrouver l’origine d’un bug.

git log est donc un outilcentral pour analyser le passé d’un projet, suivre le travail des contributeurs et naviguer dans les différentes étapes de son développement.

git log fonctionne aussi pour les projets propriétaires, à une condition essentielle.

git log n’a aucun lien avec le caractère public ou privé d’un projet.

Cette commande fonctionne localement, sur le dépôt Git que tu as sur ta machine. Donc si tu as accès au dépôt (par exemple parce que tu l’as cloné et que tu as les droits de lecture), alors git log affichera l’historique des commits sans restriction. En revanche, si tu n’as pas le droit d’accéder au dépôt (par exemple un projet privé auquel tu n’es pas autorisé), tu ne pourras même pas le cloner, et donc tu n’auras pas accès à son historique. Dans ce cas, git log ne peut évidemment rien afficher.

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/TD9/img/exercice2.png)

### Exercice 1:

Il faut aller sur le lien : https://git.esi-bru.be/exp1/git-discover/-/forks/new

On va utiliser fork.

Git, en tant qu’outil, ne possède aucune commande appelée fork. Le fork n’est pas une fonctionnalité de Git, mais une fonctionnalité des plateformes d’hébergement comme GitLab ou GitHub.
Concrètement :
Git sait cloner, versionner, comparer et fusionner du code.
Le fork est une action effectuée sur la plateforme web : elle crée une copie complète d’un dépôt sur ton propre compte.

Quand on parle de forker un projet, cela signifie :

    créer un nouveau dépôt serveur basé sur un dépôt existant

    avec son propre propriétaire et ses propres droits

    tout en gardant un lien logique avec le dépôt original

Ensuite seulement, on utilise git clone pour récupérer ce fork en local.

Pourquoi forker ?

Forker permet d’avoir une copie d’un projet dont on n’est pas l’auteur sur son propre compte GitLab, tout en conservant l’historique complet des commits (c’est-à-dire toutes les modifications effectuées depuis le début du projet). Le fork permet donc de travailler et de modifier un projet sans en être le propriétaire, et sans impacter directement le dépôt original.

Comment fonctionne le fork ?

On commence par forker le projet, ce qui crée une copie sur notre compte. On peut ensuite modifier le projet librement et publier ces changements sur notre fork. Les modifications sont ensuite soumis(es) aux auteurs du projet original via une Merge Request. Ceux-ci peuvent alors accepter les modifications, ce qui les intègre à leur projet, ou les refuser.

<b> Etape 1 : </b>

Il faut aller sur l'url du projet.

```
https://git.esi-bru.be/exp1/git-discover

```

<b> Etape 2 : </b>

Appuyer sur fork.

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/TD9/img/exercice2.fork.png)

<b> Etape 3 : </b>

Dans "Project URL" il faut mettre votre "Nom d'utilidateur", qui est votre matricule sans espace ni de g.

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/TD9/img/fork2.png)

<b> Etape 4 : </b>

Il suffit de cliquer sur "fork".

<b> Etape 5 : </b>

Sur l'url https://git.esi-bru.be/6*****/git-discover.

Vous avez votre projet fork.

A partir d'ici vous pouvez créer le dossier "mon-dossier". Déplacez vous dans ce dossier via le terminal..

Puis dans ce dossier, écrivez la commande suivante:

```
git clone  https://git.esi-bru.be/6*****/git-discover

```

Vous écrivez git clone suivie de l'url complète de votre projet forké.

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/TD9/img/fork3.png)

### 1.5 Historique d’événements :

### Exercice 2:

La commande git log permet de consulter l’historique des modifications d’un projet Git. Elle affiche la liste des commits, du plus récent au plus ancien, en indiquant pour chacun des informations importantes comme l’identifiant du commit, le nom de l’auteur, la date et le message associé. Grâce à git log, on peut comprendre comment le projet a évolué au fil du temps, savoir quand une modification a été introduite et par qui, ou encore retrouver l’origine d’un changement précis. C’est donc un outil essentiel pour analyser le passé d’un dépôt et suivre le travail effectué sur le code.

```
git log

```

Il faut appuyer sur la lettre q pour quitter.

```
git log --oneline

# Donne

Latitude-5480:~/Desktop/mon-projet/git-discover$  git log --oneline
aa133d0 (HEAD -> main, origin/main, origin/HEAD) Vérifiez que l'entrée de l'utilisateur est un nombre
f0a663c Debut de l'utilisation d'un "issue tracker"
ca268bd Répétition pour l'ajout des pions
254c2dd Ajout des pions
0c30f86 Affiche le lisez-moi sur la page du dépôt
8ea2c75 Utilisation de couleurs dans le logo
025f700 Ajout du tableau


```

Cette commande affiche un historique simplifié avec :

un identifiant court

uniquement la première ligne du message de commit

on utilise l’option --oneline

### Exercice 3:

```
git log --name-status

```

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/TD9/img/exercice3.png)

### Exercice 4:

À quel moment le fichier test.py a été ajouté ?

Pour avoir la réponse, il faut faire la commande suivante.

```
git log --name-status test.py

```

La réponse est Date: Tue Jul 23 17:09:00.

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/TD9/img/exercice4_test.png)

Lors de quel commit, le fichier lisezmoi.md a été renommé readme.md ?

Pour avoir la réponse, il faut faire la commande suivante.

```
git log --name-status readme.md

```

La réponse est

```
commit 0c30f86036f0180cc0adcba459e1ef2f12ac908e

```

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/TD9/img/exercice%204_readme.png)

Durant quel commit, le fichier todo.txt a-t-il été supprimé ?

Pour avoir la réponse, il faut faire la commande suivante.

```
git log --name-status todo.txt

# Ici la commande suivante, ne marche pas car git ne reconnait pas les fichiers avec l'extension .txt. Il faut donc utiliser la commande général suivante.  Puis il suffit de chercher dans l'historique le fichier todo.txt.

git log --name-status

```

La réponse est

```
commit  f0a663cd9c95b792f6204490a46cce118c0c821c

```

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/TD9/img/exercice4_todo.png)

Quel est le seul commit où logo.png a été modifié ?

Pour avoir la réponse, il faut faire la commande suivante.

```
git log --name-status logo.png

```

La réponse est

```
commit 8ea2c7569fcf2a72e6a059922d20b51785cc0c0c


```

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/TD9/img/exercice4_todo.png)

### Exercice 5:

La commande complète pour afficher les n derniers commits est :

```
git log -n <nombre>

```

Par exemple :

```
git log -n 5

```

Si tu veux un affichage plus court, tu peux combiner avec --oneline :

```
git log -n 5 --oneline

```

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/TD9/img/log_oneline.png)

### 1.6 Comparaisons de commits

La commande git diff permet de voir les différences entre deux états d’un projet. Elle sert principalement à comparer ce qui a changé dans les fichiers, ligne par ligne, avant de valider ces modifications dans l’historique.

Par défaut, git diff affiche les différences entre les fichiers modifiés dans le répertoire de travail et la dernière version enregistrée (le dernier commit). On peut ainsi vérifier précisément ce qui a été ajouté, supprimé ou modifié avant de créer un commit. C’est un outil très utile pour relire son travail et éviter d’enregistrer des erreurs.

git diff peut aussi être utilisé pour comparer d’autres éléments, comme deux commits, deux branches ou l’état préparé pour le prochain commit. Dans tous les cas, il montre les changements de manière détaillée, ce qui aide à comprendre l’évolution du code et à contrôler les modifications avant de les partager.

Les symboles moins se réfèrent toujours au premier commit et les symboles plus au second
commit de la commande. D’abord, les noms des fichiers comparés sont donnés, ici file.py.
Ensuite, est inscrit la position dans les deux fichiers du contenu affiché, sous le format
numéro de ligne,nombre de lignes. Finalement les différences de contenu sont affichées
avec les lignes spécifiques au premier commit en rouge et les lignes spécifiques au second
commit en vert.
Les lignes colorées avec des plus ou des moins correspondent aux modifications qu’il faudrait apporter au premier commit pour arriver directement au second commit.

Vous n’êtes heureusement pas obligé de copier l’entièreté de l’identifiant. Juste les quelques
premiers caractères suffisent. Le plus simple est de copier les identifiants courts donnés
par git log --oneline.

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/TD9/img/point1.5.png)

#### Exercice 6:

On a vut que git log va afficher les commit les plus récents.

On sait que, par défaut git log affiche les commits du plus récent au plus ancien.

<b> le contenu des fichiers entre le premier et le dernier commit :</b>

Ici on veut la différence entre le premier et le dernier commit. Il faut donc utliser git diff premier_commit dernier_commit.

Pour afficher le premier commit

Il faut inverser l’ordre avec reverse :

```
git rev-list --max-parents=0 main

commit  24e284aec4fb17adeea7ab290ce3b1b705d68a33
```

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/TD9/img/exercice_6_2.png)

Pour voir le dernier.

```
git rev-parse main

commit aa133d0aa3f8f744ce50567ce622b8705b580f6e

```

Pour faire la différence il faut les commandes suivantes.

```
git diff 24e284aec4fb17adeea7ab290ce3b1b705d68a33  aa133d0aa3f8f744ce50567ce622b8705b580f6e

# Ou

git diff $(git rev-list --max-parents=0 main) main

```

Remarque :

Même si tu n’as qu’une seule branche (main), tu peux quand même te retrouver avec “premier = dernier” si la commande ne te renvoie pas le vrai commit racine (ou si tu n’es pas exactement dans le dépôt que tu crois au moment où tu lances la commande).

Mais dans ton cas, comme ton git log montre clairement plusieurs commits (dont 0c30f86... en bas), le premier commit ne peut pas être aa133d0.... Donc le fait que git log --reverse -1 --format=%H te renvoie aa133d0... indique surtout que cette commande n’a pas été évaluée sur la même “référence” que celle affichée par ton log, ou qu’elle ne renvoie pas ce que tu penses.

Le moyen le plus fiable (et qui évite ce genre de surprise), c’est d’utiliser ces commandes :

```
git rev-parse main
git rev-list --max-parents=0 main

```

<b> le contenu de readme.md avant et après avoir été renommé : </b>

on peut utiliser git log pour repérer le renommage, mais git log seul ne peut pas afficher le contenu avant/après.
Il sert à trouver le bon commit, ensuite on utilise git show pour voir le contenu.

Voici la bonne façon d’utiliser git log dans ton cas.

Utiliser git log pour trouver le renommage

```
git log --follow --name-status -- readme.md

```

Ce que ça fait :

```
--follow → suit le fichier même s’il a été renommé

```

--name-status → indique le type de changement

R → renommage

Exemple de sortie :

```
commit 0c30f86036f0180cc0adcba459e1ef2f12ac908e
R100    README.txt    readme.md
```

Ici :

commit de renommage = 0c30f860...

ancien nom = README.txt

le contenu de logo.png avant et après sa modification.

#### Exercice 7

#### Exercice 8

#### Exercice 9
