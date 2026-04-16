# Bash – Modifier le système de fichiers

### 1 - Créer un répertoire

1.1 Créer un répertoire my-dir sur le bureau

```
mkdir ~/Bureau/my-dir

```

"~/Bureau" correspond au dossier Bureau (Desktop) en français (sur certains systèmes ce sera ~/Desktop).

1.2 Essayer de recréer my-dir

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

1.3 Créer la hiérarchie avec -p

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

de créer tous les dossiers en une fois
d’éviter les erreurs si certains existent déjà

1.4 Créer toute la hiérarchie en une seule commande avec expansion d’accolades

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

🔎 Explication rapide de l’expansion

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

### 2 - Éditeur de texte

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

#### 3 -

#### 4 -

#### 5 -

#### 6 -

#### 7 -

#### 8 -

#### 9 -

```

```
