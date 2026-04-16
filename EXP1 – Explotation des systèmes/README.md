### Bash – Modifier le système de fichiers

#### 1 - Créer un répertoire

1. Créer un répertoire my-dir sur le bureau

´´´
mkdir ~/Bureau/my-dir

´´´

"~/Bureau" correspond au dossier Bureau (Desktop) en français (sur certains systèmes ce sera ~/Desktop).

2. Essayer de recréer my-dir

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

3. Créer la hiérarchie avec -p

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

4. Créer toute la hiérarchie en une seule commande avec expansion d’accolades

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

#### 2 -

#### 3 -

#### 4 -

#### 5 -

#### 6 -

#### 7 -

#### 8 -

#### 9 -
