# 1 Permissions et groupes

Linux est un système multi-utilisateur : plusieurs personnes (ou processus) peuvent utiliser le même système en même temps.

Pour garantir la sécurité, Linux met en place un mécanisme strict de contrôle d’accès basé sur :

Le propriétaire du fichier/dossier

Le groupe associé

Les permissions accordées aux trois catégories d’utilisateurs :

le propriétaire,

le groupe,

les autres (tout le monde).

## 1.1 Propriétaire d’un fichier/dossier

Chaque fichier ou dossier appartient à un utilisateur du système.

Ce propriétaire est souvent l’utilisateur qui crée le fichier.

Le propriétaire dispose généralement du contrôle principal sur les permissions du fichier.

Pour afficher le propriétaire d’un fichier :

```

ls -l monfichier

```

Exemple de sortie :

```
-rw-r--r-- 1 alice etudiants 1200 Jan 20 10:00 rapport.txt

```

→ Le propriétaire ici est alice.

Le propriétaire d’un fichier a-t-il forcément tous les droits sur ce fichier ?

Non, pas nécessairement.

Même si un utilisateur est propriétaire d’un fichier, il peut choisir de limiter ses propres droits.

Par exemple, il peut mettre un fichier en lecture seule pour éviter de le modifier accidentellement.

Ainsi, être propriétaire ne garantit pas automatiquement tous les droits :

ce sont les permissions définies sur le fichier qui déterminent ce qu’il peut faire.

## 1.2 Les groupes d’utilisateurs

Linux est un système multi-utilisateur. Pour gérer efficacement les permissions, il utilise un mécanisme appelé groupes.

Un groupe est simplement un ensemble d’utilisateurs à qui l’on peut attribuer des droits communs.

<b>Pourquoi utiliser des groupes ?</b>

Les groupes permettent de :

- Donner des permissions à plusieurs utilisateurs en même temps

- Organiser les utilisateurs selon leurs rôles (ex. : etudiants, profs, admin)

- Contrôler l’accès à certains fichiers ou dossiers de manière simple et centralisée

Exemple :

Si un dossier appartient au groupe projetA, tous les utilisateurs membres de ce groupe peuvent y accéder selon les permissions du groupe.

<b> À quels groupes appartient un utilisateur ? </b>

Sous Linux, un utilisateur :

Possède un groupe principal (souvent le même nom que l’utilisateur)

Peut appartenir à plusieurs groupes secondaires

Tu peux voir les groupes d’un utilisateur avec :

```

groups nom_utilisateur


```

#### 1.3 Groupe d’un fichier

#### 1.4 Catégories de personnes

#### 1.5 Les permissions sur un fichier

#### 1.6 Modifier les permissions

#### 1.7 Modifier le groupe

#### 1.8 Récapitulons

#### 1.9 Permissions sur les dossiers
