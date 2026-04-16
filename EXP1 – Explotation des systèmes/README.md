# Bash – Modifier le système de fichiers

### 1 - Créer un répertoire:

Créer un répertoire my-dir sur le bureau:

```
mkdir ~/Bureau/my-dir

```

"~/Bureau" correspond au dossier Bureau (Desktop) en français (sur certains systèmes ce sera ~/Desktop).

---

Essayer de recréer my-dir.

```
mkdir ~/Bureau/my-dir

```

Résultat :

Bash affiche une erreur du type :

```
mkdir: cannot create directory ‘my-dir’: File exists

```

Explication :

Le dossier existe déjà, donc mkdir refuse de le recréer.

---

Créer la hiérarchie avec -p

Structure demandée :

```
my-documents
└── photos
    └── personal

```

Commande :

```
mkdir -p my-documents/photos/personal

```

-p permet :

- de créer tous les dossiers en une fois

- d’éviter les erreurs si certains existent déjà

---

Créer toute la hiérarchie en une seule commande avec expansion d’accolades

Structure demandée :

```
my-documents
├── photos
│   ├── personal
│   └── work
└── videos
    ├── personal
    └── work
```

Commande :

```
mkdir -p my-documents/{photos,videos}/{personal,work}

```

Explication rapide de l’expansion

```
{photos,videos}

```

devient :

photos videos

```
{personal,work}

```

devient :

personal work

Donc Bash génère automatiquement :

```
my-documents/photos/personal

my-documents/photos/work

my-documents/videos/personal

my-documents/videos/work

```

<b>Remarque:</b>

Avec la commande tree (le plus clair)

```
tree my-documents

```

Cela donne:

```
my-documents
├── photos
│   ├── personal
│   └── work
└── videos
    ├── personal
    └── work

```

C’est la meilleure commande pour visualiser une arborescence.

### 2 - Éditeur de texte:

<b>Création de fichier avec nano:</b>

```
cd ~/Bureau/my-dir

```

Ecrit nano:

```
nano

```

Écris quelques lignes, puis :

```
Ctrl + S → sauvegarder
tape : my-file.txt
Entrée
Ctrl + X → quitter

```

---

<b>Modifier un fichier existant: </b>

```
nano my-file.txt

```

Modifie le texte.

Tu verras "Modified" en haut si tu changes quelque chose

Ensuite :

```
Ctrl + S pour sauvegarder
Ctrl + X pour quitter
❓ 5. Aide de nano

```

---

<b>Utiliser des options de nano:</b>

Afficher les numéros de ligne:

```
nano -l my-file.txt

```

Affiche les numéros de ligne à gauche du texte.

Utile pour :

- se repérer dans un fichier

- coder ou corriger des erreurs

Activer la souris:

```
nano -m my-file.txt

```

Tu peux utiliser la souris pour:

- placer le curseur

- sélectionner du texte

- faire défiler

Utile si tu n’aimes pas tout faire au clavier.

Mode lecture seule (view):

```
nano -v my-file.txt

```

Effet :

ouvre le fichier sans possibilité de modifier

Tu peux :

- lire le fichier

- naviguer

Tu ne peux pas :

- modifier

- sauvegarder

---

<b>Vérifier les dates avec stat:</b>

Commande :

```
stat my-file.txt

```

Tu verras plusieurs dates :

- Access (accès)

- Modify (modification du contenu)

- Change (changement des métadonnées)

Après modification avec nano :

- seule la date Modify change

- les autres restent généralement identiques

### 3 - Créer un fichier vide:

<b> Création d'un fichier vide :</b>

```
touch fichier-vide.txt

```

- La commande "touch" crée le fichier s’il n’existe pas.

- Si le fichier existe déjà, touch met à jour sa date de modification.

---

<b> Vérifier avec ls que le fichier existe et qu’il est vide:</b>

```
ls -l fichier-vide.txt

```

- "ls" liste les fichiers.

- "-l" affiche les détails.

- Si le fichier est vide, sa taille affichée sera 0.

Exemple de résultat :

```
-rw-r--r-- 1 user user 0 avril 16 10:20 fichier-vide.txt

```

Ici, le 0 signifie que le fichier est vide.

Tu peux aussi vérifier le contenu :

```
cat fichier-vide.txt

```

Comme le fichier est vide, rien ne s’affiche.

---

<b>Créer toute la hiérarchie demandée avec un minimum de commandes:</b>

Structure voulue :

```
my-documents
|-- exercises
| |-- part1.md
| |-- part2.md
| |-- part3.md
| `-- part4.md
`-- solutions
|-- part1.md
|-- part2.md
|-- part3.md
`-- part4.md

```

Commande en une seule ligne

```
mkdir -p my-documents/{exercises,solutions} && touch my-documents/{exercises,solutions}/part{1..4}.md

```

Explication de la commande:

Partie 1 : créer les dossiers.

```
mkdir -p my-documents/{exercises,solutions}

```

mkdir crée des répertoires.

-p crée aussi les parents si nécessaire, sans erreur s’ils existent déjà.

{exercises,solutions} est une expansion d’accolades.

Bash développe cela en :

```
my-documents/exercises

my-documents/solutions

```

Partie 2 : créer les fichiers:

```
touch my-documents/{exercises,solutions}/part{1..4}.md

```

touch crée des fichiers vides.

{exercises,solutions} donne les deux dossiers.

{1..4} donne 1 2 3 4.

Bash développe donc en :

```
touch my-documents/exercises/part1.md
touch my-documents/exercises/part2.md
touch my-documents/exercises/part3.md
touch my-documents/exercises/part4.md
touch my-documents/solutions/part1.md
touch my-documents/solutions/part2.md
touch my-documents/solutions/part3.md
touch my-documents/solutions/part4.md

```

---

<b> Vérifier la structure créée: </b>

Avec tree :

```
tree my-documents

```

Ou sans tree :

```
ls -R my-documents

```

Résumé des commandes:

```
touch fichier-vide.txt
ls -l fichier-vide.txt
mkdir -p my-documents/{exercises,solutions} && touch my-documents/{exercises,solutions}/part{1..4}.md
ls -R my-documents

```

### 4 - Télécharger un fichier:

<b>Télécharger le fichier texte:</b>

```
curl https://www.rfc-editor.org/rfc/rfc791.txt --output downloaded-file.txt

```

Explication:

```
curl → télécharge depuis Internet

```

--output → nom du fichier local

Télécharger une image:

```
curl https://curl.se/logo/curl-logo.svg --output downloaded-image.svg

```

### 5 - Supprimer un fichier:

Supprimer downloaded-file.txt:

```
rm downloaded-file.txt

```

Explication:

```
rm → supprime définitivement (pas de corbeile)

```

---

<b>Supprimer tous les .tmp:</b>

```
rm *.tmp

```

Explication:

- → tous les fichiers

- .tmp → tous les fichiers finissant par .tmp

Mode sécurisé:

```
rm -i fichier.txt

```

demande confirmation avant suppression

Danger de cette commande

```
rm -ri ~/ pictures/ blurry.jpg

```

---

<b>Supprime :</b>

- tout le dossier ~ (home !)

- le dossier pictures/

- le fichier blurry.jpg

/!\ tu peux supprimer énormément de données sans le vouloir.

### 6 - Supprimer un répertoire:

<b> Créer puis supprimer:

```
mkdir test-dir
rmdir test-dir

```

"rmdir" fonctionne seulement si le dossier est vide

---

<b>Supprimer un dossier avec contenu:</b>

```
mkdir -p new-dir/dir1/dir2
rm -r new-dir

```

Explication:

- "-r" → suppression récursive (tout le contenu)

---

<b>Supprimer my-dir avec fichier:</b>

```
rm -r my-dir

```

### 7 - Créer un raccourci (lien):

Créer le dossier et fichiers:

```
mkdir books
nano books/my-life.txt
nano books/tales.txt

```

Créer un lien (hard link):

```
ln books/my-life.txt books/favorite

```

Ouvrir avec less:

```
less books/favorite

```

Créer avec extension:

```
ln books/my-life.txt books/favorite.txt

```

---

<b>Observer les liens:</b>

```
ls -l books

```

colonne 2 = nombre de liens

Supprimer un lien:

```
rm books/favorite

```

Le nombre de liens diminue.

Afficher les identifiants (inode):

```
ls -i books

```

- mêmes numéros = même fichier (hard link)

Supprimer fichier original:

```
rm books/my-life.txt

```

- favorite.txt fonctionne encore (car les données existent toujours via le lien)

Vérifier avec stat:

```
stat books/favorite.txt

```

- seule la date Change est modifiée, car les métadonnées (liens) changent

### 8 - Copier avec cp:

<b>Copier un fichier:</b>

```
cp readme.txt texts/general-readme.txt

```

- Cas d’erreurs.

```
cp long-text.txt long-text.txt

```

- erreur (même fichier)

```
cp long-text.txt dossier-inexistant/

```

- erreur (dossier absent)

---

<b>Copier avec nouveau nom:</b>

```
cp long-text.txt long-text-copy.txt

```

---

<b>Empêcher écrasement:</b>

```
cp -n fichier.txt dossier/

```

Cas de cp license folder

- si folder est un fichier → écrasé

- si folder est un dossier → copie dedans

- si n’existe pas → créé comme fichier

---

<b>Copier un dossier:</b>

```
cp -r originals originals-save
```

Cas cp -r photos backup:

- backup fichier → erreur

- backup dossier → copie dedans

- inexistant → créé comme copie

### Renommer:

Renommer avec mv:

```
mv ancien.txt nouveau.txt

```

Explication:

- mv = move (déplacer)

Mais si tu restes dans le même dossier → ça devient un renommage.

Exemple :

```
mv fichier.txt notes.txt

```

Le fichier change juste de nom.

Renommer plusieurs fichiers avec rename.

Contrairement à mv, rename peut modifier plusieurs fichiers en une fois.

Exemple simple:

```
rename 's/.txt/.md/' _.txt

```

Explication:

```
_.txt → tous les fichiers .txt

```

- 's/.txt/.md/' → remplace .txt par .md

Résultat :

```
file1.txt → file1.md
file2.txt → file2.md
```

Attention importante:

```

rename

```

- n’est pas toujours installé

- peut avoir plusieurs versions différentes

  Exemple :

- sur certains systèmes → syntaxe avec 's/.../.../' (Perl)

- sur d’autres → syntaxe différente

## Bash – Manipuler des fichiers textes:

### 1 Obtenir quelques statistiques:

Compter lignes, mots et octets avec wc.

<b>Voir lignes + mots + octets:</b>

```
wc dudh.txt

```

Explication:

- wc = word count.

Affiche :

- nombre de lignes

- nombre de mots

- nombre d’octets

Exemple de sortie :

```
120 450 3000 dudh.txt

```

120 lignes, 450 mots, 3000 octets

---

<b>Afficher uniquement le nombre de lignes:</b>

```
wc -l apache.log

```

Explication:

- "-l" → affiche seulement les lignes

Exemple :

```
250 apache.log

```

---

<b>Vérifier avec un éditeur:</b>

```
nano apache.log

```

En bas de nano → numéro de ligne total visible.

---

<b>Longueur de la plus longue ligne:</b>

```
wc -L apache.log

```

Explication:

-L → longueur (en caractères) de la ligne la plus longue

---

### 2 Supprimer les doublons avec "uniq":

Afficher sans doublons + nombre d’occurrences

```
uniq -c apache.log

```

Explication:

- uniq → supprime les doublons consécutifs

- "-c" → affiche combien de fois chaque ligne apparaît

Exemple :

```
3 GET /index.html
1 POST /login

```

Important:

- "uniq" fonctionne seulement si

- les lignes identiques sont à la suite

Donc souvent on fait :

```
sort apache.log | uniq -c

```

---

<b> Vérifier que le fichier n’est pas modifié:</b>

```
cat apache.log

```

Le contenu original est inchangé.

Explication :

- "uniq" affiche le résultat

- mais ne modifie pas le fichier

---

### 3 Numéroter des lignes:

<b>Numéroter les lignes avec nl:</b>

```
nl apache.log
```

Explication:

- nl = number lines

- affiche le fichier avec numéros de ligne

- ne numérote que les lignes non vides

Exemple :

```
1  GET /index.html
2  POST /login

```

---

<b>Afficher les premières lignes avec head:</b>

Afficher les 5 premières lignes.

```
head -n 5 elevation-extremes.csv

```

Explication:

- "head" → affiche le début du fichier

- "-n" 5 → limite à 5 lignes

---

<b>Afficher toutes sauf la dernière:</b>

```
head -n -1 elevation-extremes.csv

```

Explication:

- "-n -1" → enlève la dernière ligne

- donc affiche tout sauf la dernière

---

<b>Afficher les dernières lignes avec tail:</b>

Afficher les 5 dernières lignes.

```
tail -n 5 elevation-extremes.csv

```

Explication:

- "tail" → affiche la fin du fichier

- "-n 5" → 5 dernières lignes

---

<b>Afficher toutes sauf la première</b>

```
tail -n +2 elevation-extremes.csv

```

Explication:

- "+2" → commence à la ligne 2

- donc ignore la première ligne

---

<b>Afficher les dernières lignes avec tail:</b>

Afficher les 5 dernières lignes

```
tail -n 5 elevation-extremes.csv

```

Explication:

- tail → affiche la fin du fichier

- "-n 5" → 5 dernières lignes

<b>Afficher toutes sauf la première:</b>

```
tail -n +2 elevation-extremes.csv

```

Explication:

- "+2" → commence à la ligne 2

- donc ignore la première ligne

### 4 Afficher les 5 premières lignes:

```
head -n 5 elevation-extremes.csv

```

Explication:

- head → affiche le début du fichier

- "-n 5" → limite à 5 lignes

---

<b>Afficher toutes les lignes sauf la dernière:</b>

```
head -n -1 elevation-extremes.csv

```

Explication:

- "-n -1" → enlève 1 ligne à la fin

- donc affiche tout sauf la dernière

<b>Afficher les 5 dernières lignes:</b>

```
tail -n 5 elevation-extremes.csv

```

Explication:

- "tail" → affiche la fin du fichier

- "-n 5" → les 5 dernières lignes

<b>Afficher toutes les lignes sauf la première:</b>

```
tail -n +2 elevation-extremes.csv

```

Explication:

- "+2 "→ commence à la ligne 2

- donc ignore la première ligne

### 5 Concaténer des fichiers avec cat

Afficher 2 fichiers.

```
cat cities/eu.be.tsv cities/eu.nl.tsv

```

Explication:

- cat = concaténer

- affiche les fichiers l’un à la suite de l’autre

---

<b>Afficher tous les fichiers des villes d’Europe</b>

```
cat cities/eu.\*.tsv

```

Explication:

- = tous les fichiers correspondants

- eu.\*.tsv → tous les fichiers Europe

---

<b>Trier des lignes avec sort:</b>

Trier un fichier

```
sort unordered.txt

```

Explication:

- trie les lignes par ordre alphabétique

- Trier en ordre inverse

```
sort -r unordered.txt

```

Explication:

- "-r" → inverse l’ordre (Z → A)

<b>Trier sans doublons:</b>

```
sort -u unordered.txt

```

Explication:

- "-u" → supprime les doublons après tri

<b>Extraire des caractères avec cut:</b>

Extraire uniquement les dates (exemple).

```
cut -c 1-10 apache.log

```

Explication:

- "-c "→ sélection des caractères

- "1-10" → du caractère 1 à 10 (souvent les dates sont au début des logs)

---

<b>Extraire les messages sans les dates:</b>

```
cut -c 12- apache.log

```

Explication:

- "12-" → du caractère 12 jusqu’à la fin

- donc on enlève la date au début

Exemple général:

```
cut -c 5-20 fichier.txt

```

extrait les caractères 5 à 20

---

<b>Concaténer ligne par ligne avec paste:</b>

Exemple:

paste file1.txt file2.txt

Explication:

- combine les lignes en parallèle

Exemple :

```
file1: A file2: 1
file1: B file2: 2

```

Résultat :

```
A 1
B 2
```
