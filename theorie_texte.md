🧭 Chapitre 1 – Introduction à la sécurité

⚙️ Introduction

Depuis la Seconde Guerre mondiale, la nécessité de protéger les systèmes informatiques s’est imposée.
Les menaces se sont multipliées, et chaque type de menace demande une protection adaptée.

💡 Problème :
Une sécurité forte est souvent contraignante et lourde à mettre en œuvre.

🧩 Solution :
Il faut analyser les risques :

Identifier chaque menace

Évaluer sa probabilité

Adapter la stratégie de sécurité en conséquence

👉 Ne pas “tuer les moustiques avec une bombe nucléaire” — autrement dit, il faut un niveau de sécurité proportionné au risque.

⚠️ Types de risques étudiés dans le cours

Le cours se concentre sur cinq grandes familles de risques :

🔐 Accès non autorisé : accéder à une ressource ou un service restreint

🕵️ Usurpation d’identité : se faire passer pour quelqu’un d’autre

🧾 Accès à des données confidentielles : lire des données sensibles sans autorisation

✏️ Falsification : modifier des informations de manière frauduleuse

🧠 Contrefaçon / Forgerie : créer de fausses données ou fausses signatures

Pour chaque risque, plusieurs types d’attaques existent et plusieurs contre-mesures sont possibles.

🎣 Exemple concret : le phishing

Principe :
L’attaquant exploite la confiance de la victime pour lui soutirer des informations sensibles (mots de passe, numéros de carte, etc.).

Étapes typiques :

Identification de la cible

Préparation de l’appât (email, lien, page web…)

Envoi du message/piège

Récupération des informations

Défenses :
Sensibiliser les utilisateurs ne suffit pas toujours.
Des outils techniques sont nécessaires :

Anti-phishing

Anti-malware

Authentification multifacteur (MFA, voir chapitre 4)

Filtrage des mails inconnus

🧮 Contraintes et calculs

“When in doubt, use brute force.”

Beaucoup de systèmes de sécurité reposent sur des problèmes mathématiques difficiles à résoudre sans les clés appropriées.

Exemples de problèmes complexes :

Factorisation de grands nombres

Inversion de fonctions complexes

Optimisation combinatoire ou stochastique

Ces contraintes rendent les attaques incomputables ou trop longues, garantissant ainsi la robustesse des systèmes.
(Les détails mathématiques sont laissés de côté dans ce cours.)

🎯 Objectifs fondamentaux de la sécurité

Le chapitre présente les six objectifs principaux de la sécurité informatique, souvent regroupés dans la triade CIA + AAA :

🕒 Availability (Disponibilité) : s’assurer que le système est fonctionnel et accessible

👤 Authentication (Authentification) : identifier correctement “qui est qui”

🧾 Authorisation (Autorisation) : déterminer “qui peut faire quoi”

🧍‍♂️ Accountability (Traçabilité) : savoir “qui a fait quoi”

🧩 Integrity (Intégrité) : détecter toute modification non autorisée des données

🔒 Confidentiality (Confidentialité) : empêcher la divulgation d’informations sensibles

💡 Remarque :
Les trois premiers — Authentication, Authorisation, Accountability — forment le modèle AAA.

⚖️ Principes de base de la sécurité

Quelques principes fondamentaux guident la mise en place d’un système sécurisé :

Principe du moindre privilège : un utilisateur ne doit avoir accès qu’à ce dont il a besoin.

Principe de défense en profondeur : multiplier les couches de sécurité.

Principe de transparence : la sécurité ne doit pas dépendre du secret de la méthode.

Principe de simplicité : plus un système est complexe, plus il est vulnérable.

Principe de séparation des responsabilités : aucune personne ne doit contrôler tout le système.

(Ces principes sont développés plus en détail dans la suite du cours.)
