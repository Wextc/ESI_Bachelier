# Synthèse qui reprend toutes les commandes

## TD01

### 1. Commande cd – Se déplacer dans les répertoires

Rôle : changer le répertoire courant (change directory).

Syntaxe

cd chemin

Exemples

cd images

cd images/thumbnails

```
cd ..
cd C:/Windows/Cursors
```

Points importants

.. : répertoire parent

Chemin relatif : dépend du répertoire courant

Chemin absolu : commence depuis la racine

Bash utilise uniquement / comme séparateur

Chaque terminal a son propre répertoire courant

### 2. Commande ls – Lister les fichiers et répertoires

Rôle : afficher le contenu d’un répertoire.

Syntaxe de base

```
ls

```

Options principales

| Option | Longue             | Effet                       |
| ------ | ------------------ | --------------------------- |
| `-l`   | —                  | affichage détaillé          |
| `-a`   | `--all`            | affiche les fichiers cachés |
| `-r`   | `--reverse`        | ordre inversé               |
| —      | `--sort=size`      | tri par taille              |
| —      | `--sort=time`      | tri par date                |
| —      | `--sort=extension` | tri par extension           |

Exemples

```
ls
ls texts
ls -l
ls -a
ls -la
ls -r
ls --sort=size
ls -l --sort=time
ls texts/quote1.txt texts/quote2.txt

```

Différence importante
ls texts
≠

cd texts
ls

👉 Le premier ne change pas le répertoire courant.

### 3. Gestion des fichiers avec espaces

Problème

ls with space.txt # ❌ faux

Solutions

```
ls 'with space.txt'
ls with\ space.txt
```

### 4. Autocomplétion (Tab ↹)

Complète automatiquement commandes et noms de fichiers

Tab une fois → complétion

Tab deux fois → liste des possibilités

### 5. Expansion de noms de fichiers (wildcards)

Rôle : sélectionner plusieurs fichiers avec des motifs.

Jokers disponibles

| Joker   | Signification                |
| ------- | ---------------------------- |
| `*`     | 0 ou plusieurs caractères    |
| `?`     | exactement 1 caractère       |
| `[abc]` | un caractère parmi a, b ou c |

Exemples

```
ls *.txt
ls quote*.txt
ls text?.txt
ls *speech*
ls *\ *

```

Fichiers cachés

```
ls *
ls .*      # inclut les fichiers cachés
```

### 6. Commande less – Lire un fichier texte

Rôle : afficher un fichier sans le modifier.

Syntaxe

less fichier.txt

Exemples

less texts/long-text.txt

Raccourcis utiles dans less

| Touche  | Action                |
| ------- | --------------------- |
| `Space` | page suivante         |
| `b`     | page précédente       |
| `/mot`  | rechercher            |
| `n`     | occurrence suivante   |
| `N`     | occurrence précédente |
| `q`     | quitter               |

Option utile

```
less -N fichier.txt
```

👉 affiche les numéros de ligne

### 7. Commande stat – Informations détaillées sur un fichier

Rôle : afficher les métadonnées d’un fichier ou répertoire.

Syntaxe

stat fichier

Exemple
stat texts/quote1.txt

Dates importantes

Access : dernier accès

Modify : modification du contenu

Change : modification des métadonnées

Birth : création

### 8. Commande find – Rechercher des fichiers

Rôle : rechercher selon nom, taille, extension, etc.

Syntaxe générale

find répertoire critères

Rechercher par nom

```
find texts -name example.txt
find texts -name '*.txt'

```

⚠️ Toujours protéger les motifs :

```
-name '*.txt'

```

Rechercher par taille

```
find texts -size 42c
find texts -size +49c -size -501c

```

Combiner critères

```
find texts -name quote2.txt -size 42c

```

Limiter la profondeur

```
find . -maxdepth 1 -size +1000c
```

### 9. Commande echo – Afficher du texte

Rôle : afficher ce qui est passé en argument (utile pour tester les motifs).

Exemples

echo Bonjour

```
echo *.txt
```

### 10. Commande exit – Quitter Bash

exit

👉 Ferme proprement la session Bash.

✅ Résumé rapide

| Commande | Utilité         |
| -------- | --------------- |
| `cd`     | se déplacer     |
| `ls`     | lister          |
| `less`   | lire un fichier |
| `stat`   | infos fichier   |
| `find`   | rechercher      |
| `echo`   | afficher        |
| `exit`   | quitter         |

---

## TD09 GIT

### Configuration Git

```
git config
git config --global user.name "Votre Nom"
git config --global user.email "email@exemple.com"
git config --local user.name "Votre Nom"
git config --local user.email "email@exemple.com"
```

### Clonage de dépôt

```
git clone <url-du-depot> [nom-dossier]
git clone https://git.esi-bru.be/exp1/git-discover mon-projet
git clone https://git.esi-bru.be/6*****/git-discover
```

### Historique des commits

```
git log
git log --oneline
git log --name-status
git log -n <nombre>
git log -n 2
git log -n 5
git log -n 5 --oneline

```

### Recherche dans l’historique par fichier

```
git log --name-status test.py
git log --name-status readme.md
git log --name-status todo.txt
git log --name-status logo.png
git log --follow --name-status -- readme.md

```

### Premier et dernier commit

```
git rev-list --max-parents=0 main
git rev-parse main
git rev-list --count main
```

### Comparaison de versions (diff)

```
git diff <id1> <id2>
git diff HEAD HEAD~1
git diff HEAD~1 HEAD
git diff HEAD HEAD~2
git diff $(git rev-list --max-parents=0 main) main
git diff 24e284aec4fb17adeea7ab290ce3b1b705d68a33 aa133d0aa3f8f744ce50567ce622b8705b580f6e
```

### Fichiers binaires (logo.png)

```
git log --oneline -- logo.png
git show MOD^:logo.png > logo_before.png
git show MOD:logo.png > logo_after.png

```

### Fichiers renommés (readme.md)

```
git show REN^:README.txt
git show REN:readme.md
```

### Aide Git

```
git --help
git <commande> --help
git log --help

```

### Références symboliques

```
HEAD
HEAD~1
HEAD~2
HEAD~3
```
