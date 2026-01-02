# Synthèse qui reprend toutes les commandes

## TD02 – Bash – Parcourir le système de fichiers

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

## TD03 – Bash – Modifier le système de fichiers

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

## TD04 – Bash – Manipuler des fichiers textes

Bash – Manipuler des fichiers textes (commandes + options)

Objectif : analyser / filtrer / transformer du texte dans le terminal.

La plupart de ces commandes n’écrasent pas le fichier source : elles affichent un résultat (qu’on pourra ensuite rediriger plus tard).

### 1. wc — Statistiques (lignes, mots, octets)

Rôle : compter lignes / mots / octets.

Syntaxe

```
wc fichier.txt

```

| Option | Longue              | Effet                                           |
| ------ | ------------------- | ----------------------------------------------- |
| `-l`   | `--lines`           | nombre de lignes uniquement                     |
| `-L`   | `--max-line-length` | longueur (en octets) de la ligne la plus longue |

Exemples

```
wc dudh.txt
wc -l apache.log
wc -L apache.log

```

### 2) uniq — Éliminer les doublons consécutifs

Rôle : supprime uniquement les lignes identiques consécutives (souvent après un sort).

Syntaxe

```
uniq fichier.txt

```

Options utiles

| Option | Longue    | Effet                                            |
| ------ | --------- | ------------------------------------------------ |
| `-c`   | `--count` | préfixe chaque ligne par le nombre d’occurrences |

Exemple

```
uniq -c apache.log

```

⚠️ Important : si les doublons ne sont pas côte à côte, uniq ne les verra pas.
Souvent on fait :

```
sort fichier.txt | uniq -c

```

### 3) nl — Numéroter les lignes non vides

Rôle : afficher un fichier en numérotant les lignes non vides.

Syntaxe

```
nl fichier.txt

```

Exemple

```
nl apache.log

```

### 4) head — Afficher le début d’un fichier

Rôle : affiche les 10 premières lignes par défaut.

Syntaxe

```
head fichier.txt

```

Options

| Option  | Longue      | Effet                                              |
| ------- | ----------- | -------------------------------------------------- |
| `-n K`  | `--lines K` | affiche les K premières lignes                     |
| `-n -K` | —           | affiche toutes les lignes **sauf** les K dernières |

Exemples

```
head -n 5 elevation-extremes.csv
head -n -1 elevation-extremes.csv

```

### 5) tail — Afficher la fin d’un fichier

Rôle : affiche les 10 dernières lignes par défaut.

Syntaxe

```
tail fichier.txt

```

Options

| Option  | Longue      | Effet                          |
| ------- | ----------- | ------------------------------ |
| `-n K`  | `--lines K` | affiche les K dernières lignes |
| `-n +K` | —           | affiche à partir de la ligne K |

Exemples

```
tail -n 5 elevation-extremes.csv
tail -n +2 elevation-extremes.csv

```

### 6) cat — Concaténer / afficher des fichiers

Rôle : afficher plusieurs fichiers à la suite.

Syntaxe

```
cat f1 f2 f3

```

Exemples

```
cat cities/eu.be.tsv cities/eu.nl.tsv
cat cities/eu.*.tsv

```

### 7) sort — Trier des lignes

Rôle : tri alphabétique ligne par ligne.

Syntaxe

```
sort fichier.txt

```

Options importantes

| Option | Longue                   | Effet                                     |
| ------ | ------------------------ | ----------------------------------------- |
| `-r`   | `--reverse`              | ordre inverse                             |
| `-u`   | `--unique`               | supprime doublons (après tri)             |
| `-n`   | `--numeric-sort`         | tri numérique                             |
| `-g`   | `--general-numeric-sort` | tri numérique “scientifique” (ex: `6e10`) |
| `-t X` | `--field-separator X`    | séparateur de colonnes (CSV/TSV)          |
| `-k N` | `--key N`                | numéro de colonne (clé de tri)            |
| `-o f` | `--output f`             | écrit le résultat dans un fichier         |

Exemples simples

```
sort unordered.txt
sort -r unordered.txt
sort -u unordered.txt

```

Trier un CSV par colonne (ex: 3e colonne)

```
sort data.csv -t ',' -k 3

```

Trier un TSV (tabulation) : séparateur tab

Méthode ANSI-C quoting :

```
sort cities/eu.be.tsv -t $'\t' -k 2

```

Tri numérique (important pour planètes/séismes) :

```
sort planets.csv -t ',' -k 4 -n
sort planets.csv -t ',' -k 2 -g
sort earthquakes.dsv -t ',' -k 5 -n


```

Sauvegarder :

sort unordered.txt -o unordered-sorted.txt

### 8) cut — Extraire des caractères ou des colonnes

A) Extraire des caractères (positions)

Rôle : extraire une tranche de caractères sur chaque ligne.

```
cut -c 5-20 document.txt

```

5-20 : du 5e au 20e caractère

-20 : du début au 20e

5- : du 5e jusqu’à la fin

plusieurs intervalles : -c 1-4,10-12

Exemples (génériques) :

```
cut -c 1-10 apache.log
cut -c 6- apache.log

```

B) Extraire des colonnes (DSV : CSV/TSV/…)

Rôle : extraire des champs délimités.

Options utiles

| Option     | Longue           | Effet               |
| ---------- | ---------------- | ------------------- |
| `-d X`     | `--delimiter X`  | séparateur          |
| `-f LISTE` | `--fields LISTE` | colonnes à extraire |

Exemple CSV :

```
cut planets.csv -d ',' -f 1,3,5
cut data.csv -d ',' -f 2-4,7

```

### 9) paste — “Inverse” de cut (coller des colonnes)

Rôle : fusionner les lignes correspondantes de plusieurs fichiers (en colonnes).

Syntaxe

```
paste f1 f2

```

Exemple

```
paste col1.txt col2.txt

```

### 10) grep — Extraire des lignes qui matchent

Rôle : filtrer des lignes contenant un motif/texte.

Syntaxe

```
grep -e 'motif' fichier.txt

```

Options essentielles

| Option | Longue            | Effet                                 |
| ------ | ----------------- | ------------------------------------- |
| `-e X` | —                 | expression (peut être répétée)        |
| `-F`   | `--fixed-strings` | recherche “texte brut” (pas regex)    |
| `-n`   | `--line-number`   | affiche les numéros de ligne          |
| `-v`   | `--invert-match`  | lignes qui NE matchent PAS            |
| `-r`   | `--recursive`     | cherche dans un dossier récursivement |

Exemples

```
grep -e 'jk' apache.log
grep -e 'it' quote*.txt
grep -e 'jk' -e 'in' apache.log

```

Chercher le symbole $ (éviter regex → -F) :

```
grep -F -e '$' iso-4217.csv

```

Avec numéros de ligne :

```
grep -n -e 'jk' apache.log

```

Inverser (ne contient pas) :

```
grep -n -v -e 'jk' apache.log

```

Récursif sur un dossier + plusieurs mots :

```
grep -r -e 'are' -e 'but' exercises/

```

### 11) sed — Remplacer du texte (substitution)

Rôle : transformer du texte avec une règle, sans éditer le fichier source.

Remplacer la 1re occurrence par ligne

```
sed 's/term/replacement/' document.txt

```

Remplacer toutes les occurrences (global)

```
sed 's/term/replacement/g' document.txt

```

Exemples (génériques)

```
sed 's/de l.homme/humains/g' dudh.txt
sed 's/\./!/g' quote\*.txt
sed 's/,/\&/g' quote5.txt

```

⚠️ Rappels d’échappement :

Dans le term (regex) : échapper . \* \ [ ] ^ $

Dans le replacement : échapper & et \

📊 DSV (CSV/TSV) — Les commandes les plus utiles

Trier par colonne (sort)

CSV (virgule) :

```
sort elevation-extremes.csv -t ',' -k 2

```

TSV (tab) :

```
sort cities/eu.be.tsv -t $'\t' -k 2

```

Numérique :

```
sort planets.csv -t ',' -k 4 -n
sort planets.csv -t ',' -k 2 -g

```

Extraire des colonnes (cut)

```
cut planets.csv -d ',' -f 1,6,7

```

✅ Mémo ultra-rapide

| Besoin                         | Commande        |
| ------------------------------ | --------------- |
| compter                        | `wc`            |
| retirer doublons consécutifs   | `uniq`          |
| numéroter lignes               | `nl`            |
| début / fin                    | `head` / `tail` |
| concaténer                     | `cat`           |
| trier                          | `sort`          |
| extraire caractères / colonnes | `cut`           |
| coller des colonnes            | `paste`         |
| filtrer des lignes             | `grep`          |
| remplacer                      | `sed`           |

---

## TD05 – Bash – Redirection

Redirections, flux standard et pipes

### 1) Flux standard (standard streams)

Chaque programme lancé a 3 flux (avec un numéro appelé file descriptor) :

| Flux            | Nom      | Numéro | Par défaut |
| --------------- | -------- | -----: | ---------- |
| Entrée standard | `stdin`  |    `0` | clavier    |
| Sortie standard | `stdout` |    `1` | terminal   |
| Sortie d’erreur | `stderr` |    `2` | terminal   |

### 2) Lire depuis le clavier (stdin) + terminer avec Ctrl+D

Beaucoup de commandes lisent :

soit depuis un fichier (si tu donnes un fichier en argument),

soit depuis stdin (si aucun fichier n’est donné).

Exemple avec sort :

```
sort
travaille
tartine
tram
^D

```

➡️ Ctrl + D (après retour à la ligne) envoie un “EOF” (fin de fichier) → la commande termine.

Exemples demandés

Tri inverse à partir du clavier :

```
sort -r
mot1
mot2
mot3
^D

```

Compter mots/caractères d’un texte tapé au clavier :

```
wc
un petit texte
sur deux lignes
^D

```

### 3) tr — Remplacer des caractères (lit uniquement stdin)

Rôle : traduit / remplace des caractères.

Syntaxe

```
tr 'source' 'cible'

```

Exemples

Remplacer . par , et , par espace (selon ton exemple) :

```
tr '.,' ', '

```

Remplacer les virgules par des retours à la ligne :

```
tr ',' '\n'

```

⚠️ tr lit uniquement depuis stdin → très utile avec redirections et pipes.

⬅️➡️ Redirections

### 4) Redirection de l’entrée standard : < (stdin)

Rôle : lire depuis un fichier au lieu du clavier.

```
Syntaxe
commande < fichier
commande 0< fichier

```

Exemple (avec tr)

Mettre une énumération (virgules) en lignes :

```
tr ',' '\n' < enum.txt

```

Note : pour certaines commandes, c’est équivalent à passer le fichier en argument (ex: sort < file ≈ sort file), mais c’est indispensable pour les pipes.

### 5) Redirection de la sortie standard : > et >> (stdout)

```
> écrase / crée
commande > fichier
commande 1> fichier

```

Exemple :

```
sort unordered.txt > ordered.txt

```

Créer quotes-all.txt avec tous les quote\* :

```
cat quote* > quotes-all.txt

```

Créer un fichier avec echo :

```
echo "hello, world" > greetings.txt

>> ajoute à la fin (append)
commande >> fichier
commande 1>> fichier

```

Exemple :

```
echo "how are you doing ?" >> greetings.txt

```

### 6) tail -f — Suivre un fichier en direct

Rôle : affiche la fin puis continue d’afficher les nouvelles lignes ajoutées.

```
tail -f greetings.txt

```

Dans un autre terminal :

```
echo "nouvelle ligne" >> greetings.txt

```

### 7) ⚠️ Piège important : redirection faite AVANT l’exécution

Donc ceci vide le fichier :

```
sort unordered.txt > unordered.txt

```

✅ Solution typique : utiliser un fichier temporaire puis renommer :

```
sort unordered.txt > unordered.tmp
mv unordered.tmp unordered.txt

```

(Plus tard, tee peut aussi aider pour des cas proches.)

### 8) Redirection de stderr : 2> et 2>>

Écraser / créer

```
commande 2> errors.txt

```

Ajouter

```
commande 2>> errors.txt


```

Exemple :

ls fichier-qui-nexiste-pas 2> errors.txt

🧩 Composition sans pipes (avec fichiers intermédiaires)

Exemple (comme dans le cours) :

```
sort -n values.seq > sorted-values.seq
head -n 3 sorted-values.seq

```

🧵 Pipes (tubes) : |

### 9) Principe

Rôle : connecter stdout de la commande A vers stdin de la commande B.

Exemple

```
sort -n values.seq | head -n 3

```

Pipeline

Une pipeline = une ou plusieurs commandes reliées par |.

⚠️ À droite d’un pipe, il faut idéalement une commande qui lit stdin.
Exemple inutile :

```
sort values.seq | echo "ok"

```

(echo n’utilise pas stdin → le résultat de sort est “perdu”.)

🧪 Exemples de pipelines typiques (copiables)

A) 3 plus grands nombres (si values.seq = nombres)

⚠️ “plus grands” = fin → donc tail après tri :

```
sort -n values.seq | tail -n 3

```

B) Compter les lignes d’erreur dans un log Apache (exemple générique)

Si les lignes d’erreur contiennent le mot error :

```
grep -i -e "error" apache.log | wc -l

```

C) Top 3 lignes les plus fréquentes (en ignorant la date)

Méthode générique (suppose date au début, on enlève les N premiers caractères) :

```
cut -c 21- apache.log | sort | uniq -c | sort -nr | head -n 3

```

cut -c 21- : enlève les 20 premiers caractères (à adapter selon ton format)

uniq -c : compte occurrences consécutives (après tri)

sort -nr : tri numérique décroissant

🪜 Résultat intermédiaire : tee

#### 10) tee — “dupliquer” le flux (écran + fichier)

Rôle : écrit ce qu’il reçoit sur stdout et le copie dans un fichier.

Syntaxe

```
commande | tee fichier | commande2

```

Exemple

```
sort -n values.seq | tee sorted-values.seq | head -n 3

```

Que fait ceci ?

```
tee f


```

Hello, world

```
^D

```

➡️ tee lit stdin (clavier), affiche Hello, world au terminal et écrit la même chose dans le fichier f. Ctrl+D termine.

✅ Mémo ultra-rapide

| Action                            | Opérateur / commande |     |
| --------------------------------- | -------------------- | --- |
| stdin depuis fichier              | `<`                  |     |
| stdout vers fichier (écrase)      | `>`                  |     |
| stdout vers fichier (ajoute)      | `>>`                 |     |
| stderr vers fichier               | `2>` / `2>>`         |     |
| connecter commandes               | `                    | `   |
| sauvegarder une étape de pipeline | `tee`                |     |
| suivi live d’un fichier           | `tail -f`            |     |
| fin de saisie clavier             | `Ctrl + D`           |     |

---

## T07 – Bash – Permissions et groupes (synthèse complète)

---

## T07 – Bash – Permissions et groupes (synthèse complète)

### 1) Propriétaire d’un fichier / dossier

Chaque fichier ou dossier appartient à un utilisateur (propriétaire).

Visualiser propriétaire, groupe et permissions

```

ls -l

```

Sortie typique :

```
-rw-r--r-- 1 alice users  1234 file.txt

```

👉 Le propriétaire n’a pas automatiquement tous les droits : il peut retirer ses propres permissions.

### 2) Groupes d’utilisateurs

Un utilisateur :

appartient à au moins un groupe

peut appartenir à plusieurs groupes

Voir ses groupes

```
groups

```

Voir les groupes d’un autre utilisateur

```
groups login

```

👉 Le premier groupe listé est le groupe principal (utilisé lors de la création de fichiers).

### 3) Groupe d’un fichier

Chaque fichier appartient à un seul groupe.

Voir le groupe d’un fichier

```
ls -l fichier

```

### 4) Catégories de personnes

Les permissions sont définies pour 3 catégories :

| Catégorie    | Lettre      |
| ------------ | ----------- |
| propriétaire | `u` (user)  |
| groupe       | `g` (group) |
| autres       | `o` (other) |

### 5) Permissions sur un fichier

Les trois permissions

| Lettre | Nom     | Effet (fichier)     |
| ------ | ------- | ------------------- |
| `r`    | read    | lire le contenu     |
| `w`    | write   | modifier le contenu |
| `x`    | execute | exécuter le fichier |

Les permissions sont toujours dans l’ordre :

rwx

Un - signifie permission absente.

Exemple

```
-rw-r--r--

```

Catégorie Droits

| Catégorie    | Droits             |
| ------------ | ------------------ |
| propriétaire | lecture + écriture |
| groupe       | lecture            |
| autres       | lecture            |

⚠️ Le premier caractère (- ou d) indique fichier ou dossier, pas une permission.

### 6) Modifier les permissions : chmod

A) Méthode numérique (octale)

Valeurs de base
| Permission | Valeur |
| ---------- | ------ |
| `r` | 4 |
| `w` | 2 |
| `x` | 1 |

Addition :

```
rw- → 6

r-x → 5

rwx → 7

```

Structure

```
chmod XYZ fichier

```

X → propriétaire

Y → groupe

Z → autres

Exemples

```
chmod 644 fichier     # rw-r--r--
chmod 750 fichier     # rwxr-x---
chmod 604 fichier     # rw----r--

```

B) Méthode symbolique (lettres)

Structure

```
chmod [u|g|o|a][+|-|=][r|w|x] fichier

```

Exemples

Ajouter écriture au groupe :

```
chmod g+w fichier

```

Supprimer tous les droits aux autres :

```
chmod o= fichier

```

Donner exécution à user et group :

```
chmod ug+x fichier

```

Modifier plusieurs catégories :

```
chmod ug+rw,o-rwx fichier

```

### 7) Modifier le groupe : chgrp

Syntaxe

```
chgrp groupe fichier

```

⚠️ Conditions :

être propriétaire du fichier

être membre du groupe cible

Exemple

```
chgrp etudiants examen

```

### 8) Cas pratique classique (TD)

Fichier lisible par :

vous

enseignants

❌ mais pas les autres étudiants

Solution

touch examen

```
chgrp etudiants examen
chmod 604 examen

```

### 9. Permissions sur les dossiers (⚠️ très important)

| Permission | Effet (dossier)                               |
| ---------- | --------------------------------------------- |
| `r`        | lister le contenu (`ls`)                      |
| `x`        | entrer / traverser (`cd`, accès aux fichiers) |
| `w`        | créer / supprimer des fichiers                |

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
