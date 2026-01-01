# Synthèse qui reprend toutes les commandes

## TD01 \_ Bash – Parcourir le système de fichiers

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

cd texts ls

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

## TD02 \_ Modifier le système de fichiers

### 1) mkdir — Créer des répertoires

Rôle : créer un ou plusieurs répertoires.

Syntaxe

mkdir dir

mkdir dir1 dir2 dir3

Options importantes

| Option | Longue      | Effet                                                                          |
| ------ | ----------- | ------------------------------------------------------------------------------ |
| `-p`   | `--parents` | crée aussi les parents (hiérarchie) et ne plante pas si un dossier existe déjà |

Exemples

Créer un dossier sur le bureau (Git Bash : ~/Desktop) :

```
cd ~/Desktop
mkdir my-dir

```

Créer une hiérarchie en une commande :

```
mkdir -p my-documents/photos/personal/

```

Créer plusieurs dossiers d’un coup (brace expansion) :

```
mkdir -p my-documents/{photos,videos}/{personal,work}

```

### 2) Expansion d’accolades {} (brace expansion)

Rôle : générer des chaînes sans dépendre des fichiers existants (contrairement à \* et ?).

Forme “liste”

```
echo a{x,y,z}b

```

axb ayb azb

Forme “intervalle”

```
echo file{1..5}.txt
#Tu obtiens :> file1.txt file2.txt file3.txt file4.txt file5.txt

```

Avec pas (incrément) :

```
echo file{1..9..2}.txt
#Tu obtiens :> file1.txt file3.txt file5.txt file7.txt file9.txt

```

Avec zéros (largeur fixe) :

```
echo part{01..04}.md
part01.md part02.md part03.md part04.md

```

### 3. nano — Éditer/créer un fichier texte (éditeur en terminal)

Rôle : créer ou modifier un fichier.

Ouvrir nano

```
nano

```

Créer / éditer un fichier directement

```
nano my-file.txt

```

| Option | Longue          | Effet                                         |
| ------ | --------------- | --------------------------------------------- |
| `-l`   | `--linenumbers` | affiche les numéros de ligne                  |
| `-m`   | `--mouse`       | active la souris (curseur, sélection, scroll) |
| `-v`   | `--view`        | lecture seule                                 |

```
nano -l my-file.txt
nano -v my-file.txt

```

Raccourcis essentiels dans nano

Ctrl + S : sauvegarder (Save)

Ctrl + X : quitter (Exit)

### 4) touch — Créer un fichier vide / mettre à jour les dates

Rôle :

si le fichier n’existe pas → le crée vide

sinon → met à jour les timestamps (accès/modification)

Syntaxe

```
touch fichier
touch f1 f2 f3

```

Exemples

```
touch empty.txt
ls -l empty.txt

```

Créer plusieurs fichiers avec brace expansion :

```
touch my-documents/exercises/part{1..4}.md
touch my-documents/solutions/part{1..4}.md

```

Créer dossiers + fichiers (minimum de commandes) :

```
mkdir -p my-documents/{exercises,solutions}
touch my-documents/{exercises,solutions}/part{1..4}.md

```

### 5) curl — Télécharger un fichier depuis le Web

Rôle : télécharger une ressource URL.

Syntaxe

```
curl URL --output fichier

```

Exemples

```
curl https://www.rfc-editor.org/rfc/rfc791.txt --output downloaded-file.txt
curl https://curl.se/logo/curl-logo.svg --output downloaded-image.svg

```

### 6) rm — Supprimer un fichier (⚠️ définitif)

Rôle : supprimer un fichier (pas de corbeille).

Syntaxe

```
rm fichier

```

Options importantes

| Option | Longue          | Effet                                    |
| ------ | --------------- | ---------------------------------------- |
| `-i`   | `--interactive` | demande confirmation                     |
| `-r`   | `--recursive`   | supprime un dossier + contenu (récursif) |

Exemples

Supprimer un fichier :

```
rm downloaded-file.txt

```

Supprimer tous les .tmp du dossier courant :

```
rm *.tmp

```

Supprimer en demandant confirmation (attention : peut être pénible si beaucoup de fichiers) :

```
rm -i fichier.txt

```

Supprimer un dossier et tout son contenu (dangereux) :

```
rm -r my-dir
rm -ri my-dir

```

⚠️ Danger classique (espace dans un chemin) :

```
rm -ri ~/ pictures/ blurry.jpg

```

Ici rm reçoit plusieurs arguments (~/, pictures/, blurry.jpg) → risque énorme.

### 7) rmdir — Supprimer un répertoire VIDE

Rôle : supprime uniquement si le répertoire est vide.

Syntaxe

```
rmdir dossier

```

Exemple

```
mkdir temp-dir
rmdir temp-dir

```

Si le dossier contient quelque chose → erreur.

### 8) ln — Créer un lien (raccourci)

Lien matériel (hard link) — par défaut avec ln sur Windows (Git Bash)

Rôle : crée un autre nom qui pointe vers les mêmes données (même “identifiant” NTFS/FileID).

Syntaxe

```
ln target-path link-name

```

Exemple

Créer des fichiers :

```
mkdir books
nano books/my-life.txt
nano books/tales.txt

```

Créer un lien :

```
ln books/my-life.txt books/favorite
less books/favorite

```

Avec extension (pratique côté Windows Explorer) :

```
ln books/my-life.txt books/favorite.txt

```

Voir “combien de hard links” (ls -l)

```
ls -l books

```

👉 La colonne “nombre” (souvent juste après les permissions) indique le nombre de liens matériels.

Voir l’identifiant (inode/FileID) avec ls -i

```
ls -i books

```

👉 Compare my-life.txt, favorite.txt, favorite.lnk (si créé par Windows).

⚠️ Note importante : supprimer un hard link ne supprime pas les données tant qu’il en reste un autre.

### 9. cp — Copier fichiers et dossiers

Copier un fichier
cp source destination

Exemple (copie + renommage) :

```
cp readme.txt texts/general-readme.txt

```

Options utiles

| Option | Longue          | Effet                              |
| ------ | --------------- | ---------------------------------- |
| `-i`   | `--interactive` | demande avant écrasement           |
| `-n`   | `--no-clobber`  | n’écrase pas si destination existe |
| `-r`   | `--recursive`   | copie un dossier                   |

Exemples :

```
cp -i long-text.txt backup/long-text.txt
cp -n long-text.txt backup/long-text.txt
cp long-text.txt long-text-copy.txt
cp -r originals originals-save

```

Astuce anti-confusion : finir un dossier par /

```
cp image.jpg nature/birds/

```

### 10. mv — Déplacer / renommer (⚠️ écrase par défaut)

Rôle : déplacer un fichier/dossier ou renommer.

Syntaxe

```
mv source destination

```

Options utiles

| Option | Longue          | Effet                              |
| ------ | --------------- | ---------------------------------- |
| `-n`   | `--no-clobber`  | n’écrase pas si destination existe |
| `-i`   | `--interactive` | demande confirmation               |

Exemples :
Déplacer vers le parent :

```
mv fichier.txt ..

```

Renommer :

```
mv oldname.txt newname.txt

```

Déplacer dans un dossier (garde le nom) :

```
mv photo.jpg images/

```

Sans écraser :

```
mv -n dog.jpg belgium/zinneke.jpg

```

Rendre visible un fichier caché Unix (commence par .) → le renommer :

```
mv .nix-hidden.txt nix-hidden.txt

```

### 11) rename — Renommer en masse (si installé)

⚠️ Pas toujours disponible et syntaxe variable selon systèmes.

Vérifier s’il existe :

```
rename --help

```

✅ Mini mémo (ultra rapide)

---

| Action                      | Commande             |
| --------------------------- | -------------------- |
| créer dossier               | `mkdir` / `mkdir -p` |
| créer fichier vide          | `touch`              |
| éditer fichier              | `nano`               |
| télécharger                 | `curl --output`      |
| supprimer fichier           | `rm` / `rm -i`       |
| supprimer dossier vide      | `rmdir`              |
| supprimer dossier + contenu | `rm -r` / `rm -ri`   |
| créer lien                  | `ln`                 |
| copier                      | `cp` / `cp -r`       |
| déplacer / renommer         | `mv`                 |

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
