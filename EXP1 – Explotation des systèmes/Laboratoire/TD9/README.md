Vidéo d'introduction :

git : FR:

https://www.youtube.com/watch?v=gGKZLfPYORs

https://www.youtube.com/watch?v=hwP7WQkmECE

git lab: ENG:

https://www.youtube.com/watch?v=qKxytMuUiJA&list=PLZMWkkQEwOPmGolqJPsAm_4fcBDDc2to_

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

### Attention :

Lors de l'examen. Ilfaut se connecter sur le serveur linux1 pour pouvoir utiliser gtilab. Il faudra pouvoir

trouver des dossiers sur le linux puis les envoyer sur le gitlab.

Il faut faire les configurations avant d'aller en examen.

Pour se connecter sur gitlab la seule connection possible sera la la connection via le NOM D UTILISATEUR et le

PASSWD.

### Voici une liste des commandes :

<b> Commandes de configuration</b>

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

<b> Comparaison des versions => git diff </b>

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

<b> Aide et documentation => git --help </b>

Affiche la liste des commandes Git.

```
git --help

git <commande> --help

```

Affiche l’aide détaillée d’une commande.

git log --help

➜ Très utile quand tu ne te rappelles plus des options.
