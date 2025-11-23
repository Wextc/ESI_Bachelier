### 1 Permissions et groupes

Linux est un système multi-utilisateur : plusieurs personnes (ou processus) peuvent utiliser le même système en même temps.

Pour garantir la sécurité, Linux met en place un mécanisme strict de contrôle d’accès basé sur :

Le propriétaire du fichier/dossier

Le groupe associé

Les permissions accordées aux trois catégories d’utilisateurs :

le propriétaire,

le groupe,

les autres (tout le monde).

#### 1.1 Propriétaire d’un fichier/dossier

Chaque fichier ou dossier appartient à un utilisateur du système.

Ce propriétaire est souvent l’utilisateur qui crée le fichier.

Le propriétaire dispose généralement du contrôle principal sur les permissions du fichier.

Pour afficher le propriétaire d’un fichier :

´´´

ls -l monfichier

´´´

Exemple de sortie :

´´´

-rw-r--r-- 1 alice etudiants 1200 Jan 20 10:00 rapport.txt

```

→ Le propriétaire ici est alice.

#### 1.2 Les groupes d’utilisateurs

#### 1.3 Groupe d’un fichier

#### 1.4 Catégories de personnes

#### 1.5 Les permissions sur un fichier

#### 1.6 Modifier les permissions

#### 1.7 Modifier le groupe

#### 1.8 Récapitulons

#### 1.9 Permissions sur les dossiers
```
