# Chapitre 0 – Introduction

## 1. 🎓 Présentation du cours

Le cours fait partie du module INT1 et dure 2 heures par semaine.

La présence est “optionnelle”, mais la réussite dépend de l’assiduité et de la participation.

Objectif global :

Fournir une introduction à la sécurité informatique, en expliquant les concepts, terminologies et outils de base, sans exiger de mise en pratique complexe.

Le cours s’appuie sur des démonstrations et des exemples concrets, mais les étudiants ne doivent pas les reproduire eux-mêmes.

## 2. 👩‍🏫 Les enseignants

    • R. Absil (ABS)

    • J. Dossogne (JDS)

Deux enseignants accessibles et disponibles : « Si vous avez une question, demandez. Nous ne mordons pas… trop souvent ! »

## 3. 💡 Pourquoi un cours de sécurité ?

La sécurité informatique est partout :

    • Comptes bancaires, jeux en ligne, réseaux sociaux.

    • Systèmes administratifs : vote électronique, fiscalité, santé, etc.

➡️ Ces applications manipulent des données sensibles : authentification, contrôle d’accès, stockage ou transmission sécurisée.

➡️ Il est donc essentiel de comprendre les concepts fondamentaux liés à ces processus.
Citation clé :

“Dire que vous ne vous souciez pas de la vie privée parce que vous n’avez rien à cacher, c’est comme dire que vous ne vous souciez pas de la liberté d’expression parce que vous n’avez rien à dire.”

(Rappel : la vie privée = un droit fondamental, pas un luxe.)

## 4. 🎯 Objectifs pédagogiques

À la fin du cours, l’étudiant doit :

    • Comprendre les caractéristiques désirées de la sécurité : confidentialité, intégrité, authentification, etc.

    • Connaître les outils cryptographiques de base :

        ◦ Fonctions de hachage

        ◦ Algorithmes de chiffrement

        ◦ Signatures et certificats numériques

    • Savoir ce qu’est l’authentification et pourquoi elle est cruciale.

➡️ Les notions avancées seront approfondies plus tard (en 3ᵉ année ou au master).

## 5. 📚 Références recommandées

Quelques ouvrages et ressources de référence :

    • W. Du, Computer and Internet Security: A Hands-On Approach, 2ᵉ éd., 2019

    • J. Pelzl & C. Paar, Understanding Cryptography, Springer, 2010

    • B. Schneier, Secrets and Lies: Digital Security in a Networked World, Wiley, 2015

    • OWASP — https://owasp.org

    • NIST — https://www.nist.gov

## 6. 🧾 Modalités d’évaluation

Première session :

    • Pas d’évaluation intermédiaire

    • Examen en janvier : 100 % de la note

Seconde session :

    • Examen en août : 100 % de la note

Format :

    • QCM (Questions à choix multiples)

        ◦ Peu de points négatifs

        ◦ Format choisi pour des raisons de logistique (nombre élevé d’étudiants)

# 🧭 Chapitre 1 – Introduction à la sécurité

## 1. ⚙️ Introduction

Depuis la Seconde Guerre mondiale, la nécessité de protéger les systèmes informatiques s’est imposée.

Les menaces se sont multipliées, et chaque type de menace demande une protection adaptée.

💡 Problème :

Une sécurité forte est souvent contraignante et lourde à mettre en œuvre.

🧩 Solution :

Il faut analyser les risques :

    • Identifier chaque menace

    • Évaluer sa probabilité

    • Adapter la stratégie de sécurité en conséquence

👉 Ne pas “tuer les moustiques avec une bombe nucléaire” — autrement dit, il faut un niveau de sécurité proportionné au risque.

## 2. ⚠️ Types de risques étudiés dans le cours

Le cours se concentre sur cinq grandes familles de risques :

Type de risque

Description

🔐 Accès non autorisé

Accéder à une ressource ou un service restreint

🕵️ Usurpation d’identité

Se faire passer pour quelqu’un d’autre

🧾 Accès à des données confidentielles

Lire des données sensibles sans autorisation

✏️ Falsification

Modifier des informations de manière frauduleuse

🧠 Contrefaçon / Forgerie

Créer de fausses données ou fausses signatures

Pour chaque risque :

    • Plusieurs types d’attaques existent

    • Plusieurs contre-mesures sont possibles

## 3. 🎣 Exemple concret : le phishing

Principe :

L’attaquant exploite la confiance de la victime pour lui soutirer des informations sensibles (mots de passe, numéros de carte, etc.).

Étapes typiques :

    1. Identification de la cible

    2. Préparation de l’appât (email, lien, page web…)

    3. Envoi du message/piège

    4. Récupération des informations

Défenses :

    • Sensibiliser les utilisateurs ne suffit pas toujours

    • Outils techniques nécessaires :

        ◦ Anti-phishing

        ◦ Anti-malware

        ◦ Authentification multifacteur (MFA, voir Ch.4)

        ◦ Filtrage des mails inconnus

## 4. 🧮 Contraintes et calculs

“When in doubt, use brute force.”

Beaucoup de systèmes de sécurité reposent sur des problèmes mathématiques difficiles à résoudre sans les clés appropriées.

Exemples de problèmes “durs” :

    • Factorisation de grands nombres

    • Inversion de fonctions complexes

    • Optimisation combinatoire ou stochastique

Ces contraintes rendent les attaques incomputables ou trop longues, garantissant ainsi la robustesse des systèmes.
(Les détails mathématiques sont laissés de côté dans ce cours.)

## 5. 🎯 Objectifs fondamentaux de la sécurité

Le chapitre présente les six objectifs principaux de la sécurité informatique — souvent regroupés dans la triade CIA + AAA :

Objectif

Définition

🕒 Availability (Disponibilité)

S’assurer que le système est fonctionnel et accessible

👤 Authentication (Authentification)

Identifier correctement “qui est qui”

🧾 Authorisation (Autorisation)

Déterminer “qui peut faire quoi”

🧍‍♂️ Accountability (Traçabilité)

Savoir “qui a fait quoi”

🧩 Integrity (Intégrité)

Détecter toute modification non autorisée des données

🔒 Confidentiality (Confidentialité)

Empêcher la divulgation d’informations sensibles

💡 Remarque :

Les trois premiers — Authentication, Authorisation, Accountability — forment le modèle AAA.

## 6. ⚖️ Principes de base de la sécurité

Quelques principes fondamentaux guident la mise en place d’un système sécurisé :

    • Principe du moindre privilège : un utilisateur ne doit avoir accès qu’à ce dont il a besoin.

    • Principe de défense en profondeur : multiplier les couches de sécurité.

    • Principe de transparence : la sécurité ne doit pas dépendre du secret de la méthode.

    • Principe de simplicité : plus un système est complexe, plus il est vulnérable.

    • Principe de séparation des responsabilités : aucune personne ne doit contrôler tout le système.

(Ces principes sont développés plus en détail dans la suite du cours.)

# 🧭 Chapitre 2 – Cryptographic Tools

1. ⚙️ Introduction
   La cryptographie est la boîte à outils principale de la sécurité informatique.
   Elle permet d’atteindre plusieurs objectifs fondamentaux :
   Objectif
   Outil cryptographique
   🔐 Confidentialité
   Chiffrement (cipher algorithms)
   🧩 Intégrité
   Fonctions de hachage
   ✍️ Authenticité / Non-répudiation
   Signatures numériques
   Le but de ce chapitre est de comprendre les concepts et le rôle pratique de ces outils, sans les détails mathématiques.

2. 🧱 Fonctions de hachage (Hash functions)
   🎯 Objectif :
   Garantir l’intégrité des données — détecter toute modification d’un message.
   🔍 Principe :
   Une fonction de hachage prend une entrée (message) de longueur arbitraire et renvoie un digest de longueur fixe.
   C’est une fonction à sens unique : il est impossible de retrouver le message d’origine à partir du hash.
   ⚙️ Propriétés essentielles : 1. Unidirectionnalité : il n’existe pas d’inverse de la fonction. 2. Résistance à la préimage : impossible de retrouver le message à partir du hash. 3. Résistance aux collisions : impossible de trouver deux messages différents ayant le même hash. 4. Effet avalanche : une minuscule différence d’entrée produit un hash complètement différent.
   💡 Exemple :
   Un testateur confie le texte de son testament à un notaire,
   et le hash à un autre.
   ➡️ Si le testament est modifié, le hash ne correspond plus : la fraude est détectée.
   🧮 Exemples de fonctions de hachage :
   • MD5 (obsolète)
   • SHA-1 (obsolète)
   • SHA-2 / SHA-3 (actuels)

3. 🔐 Algorithmes de chiffrement (Cipher algorithms)
   🎯 Objectif :
   Assurer la confidentialité des données — empêcher les non-autorisés de lire un message.
   🔍 Principe :
   Un algorithme de chiffrement transforme un message clair (plaintext) en un message chiffré (ciphertext), à l’aide d’une clé.
   Le déchiffrement fait l’opération inverse.
   ⚙️ Deux grandes familles :
   Type
   Principe
   Exemple
   Symétrique
   Une même clé sert à chiffrer et déchiffrer
   AES, DES
   Asymétrique
   Deux clés différentes : une publique et une privée
   RSA, ECC
   ⚖️ Comparaison :
   Critère
   Symétrique
   Asymétrique
   Vitesse
   Très rapide
   Plus lent
   Distribution des clés
   Difficile
   Facile (clé publique)
   Sécurité dépend de
   Clé secrète
   Mathématiques “dures” (factorisation, etc.)
   Usage typique
   Chiffrement de données
   Authentification, échange de clés

4. 📦 Modes de fonctionnement : blocs et flux
   Les algorithmes symétriques traitent les données de deux façons :
   Mode
   Description
   Exemple
   Block cipher
   Le message est découpé en blocs de taille fixe (ex. 128 bits)
   AES, DES
   Stream cipher
   Le message est chiffré bit par bit ou octet par octet
   RC4, ChaCha20
   🔢 Padding :
   Quand le dernier bloc n’est pas complet, on le remplit (padding) pour éviter les pertes de données.
   💥 Avalanche effect :
   Une petite modification du texte clair ou de la clé doit changer complètement le résultat chiffré.
   ➡️ Garantit que le chiffrement ne laisse aucun schéma prévisible.

5. 🔁 Échange de clés (Key Exchange)
   Problème :
   Dans le chiffrement symétrique, il faut partager la clé secrète.
   Mais si la clé circule sur le réseau, elle peut être interceptée.
   ✅ Solution : Diffie–Hellman Key Exchange (DHKE)
   • Alice et Bob échangent des valeurs publiques dérivées de leurs secrets.
   • Ils calculent chacun la même clé partagée localement.
   • Un espion qui intercepte les données ne peut pas reconstruire la clé.
   💡 Ce mécanisme est la base de la confidentialité éphémère dans TLS.

6. ✍️ Signatures numériques
   🎯 Objectif :
   Garantir l’authenticité et la non-répudiation.
   🔍 Principe : 1. L’émetteur calcule le hash du message. 2. Il chiffre le hash avec sa clé privée → c’est la signature numérique. 3. Le destinataire déchiffre la signature avec la clé publique de l’émetteur. 4. Il recalcule le hash du message et compare les deux.
   → S’ils sont identiques : le message est authentique et intègre.
   🧩 Résumé du processus :
   Étape
   Action
   Outil utilisé
   1
   Hash du message
   Fonction de hachage
   2
   Chiffrement du hash
   Clé privée de l’expéditeur
   3
   Vérification
   Clé publique du destinataire
   💡 Applications :
   • Certificats électroniques (cf. Ch.3)
   • Signature de code ou de documents
   • Authentification dans les protocoles réseau

7. 🧮 Problèmes mathématiques “difficiles”
   De nombreux algorithmes reposent sur des problèmes impossibles à résoudre efficacement sans clé :
   • RSA → factorisation de grands nombres
   • Diffie-Hellman → logarithme discret
   • ECC (Elliptic Curve Cryptography) → équations elliptiques complexes
   Ces problèmes assurent la robustesse des systèmes cryptographiques modernes.

8. 🧰 Synthèse : outils cryptographiques et objectifs de sécurité
   Objectif
   Outil
   Exemple
   Confidentialité
   Chiffrement (AES, RSA)
   Messages privés, stockage
   Intégrité
   Hachage (SHA-256)
   Vérification de fichiers
   Authenticité / Non-répudiation
   Signature numérique
   Documents signés
   Échange de clés
   Diffie–Hellman
   TLS, VPNs

9. ⚖️ Principes clés à retenir

   1. 🔁 Toujours combiner les outils cryptographiques pour une sécurité complète.
   2. 🚫 Ne jamais inventer son propre algorithme — utiliser les standards reconnus.
   3. ⏳ La force d’un système dépend du temps nécessaire à le casser.
   4. 🔐 Les clés sont plus importantes que les algorithmes : bien les protéger !
   5. 🧱 La cryptographie ne crée pas la confiance, elle la matérialise — la PKI (Ch.3) vient ensuite.

10. 🧩 Résumé synthétique
    Élément
    Description
    But du chapitre
    Présenter les outils cryptographiques de base et leurs usages en sécurité
    Outils étudiés
    Fonctions de hachage, chiffrements symétriques/asymétriques, signatures numériques
    Concepts clés
    Avalanche effect, block vs stream cipher, Diffie-Hellman, clé publique/privée
    Message clé
    🔐 La cryptographie est le socle de toute sécurité : elle protège les données, prouve leur intégrité et garantit l’identité de leurs auteurs.

🧭 Chapitre 3 – Certificates & Public Key Infrastructure (PKI)

1. ⚙️ Introduction
   Dans le chapitre précédent, on a vu les outils cryptographiques :
   • hachage → intégrité
   • chiffrement → confidentialité
   • signatures → non-répudiation
   Mais… un problème fondamental subsiste :
   🔍 Comment être certain que la clé publique que j’utilise appartient bien à la personne que je pense ?
   C’est ici qu’intervient la PKI (Public Key Infrastructure).

2. 🧩 Le problème d’identité
   🎯 Scénario 1 : chiffrement
   • Alice veut envoyer un message secret à Oscar.
   • Elle chiffre le message avec la clé publique d’Oscar.
   • Seul le détenteur de la clé privée correspondante (Oscar) pourra le déchiffrer.
   ❗ Mais : n’importe qui peut créer une paire de clés et prétendre être Oscar.
   ➡️ Alice ne sait pas si la clé publique est vraiment celle d’Oscar.
   🎯 Scénario 2 : signature
   • Oscar signe un message avec sa clé privée.
   • Alice vérifie la signature avec la clé publique d’Oscar.
   ❗ Même problème : si cette clé publique vient d’un imposteur, la vérification n’a aucune valeur.

3. 🕵️ Besoin d’un tiers de confiance
   “We need to link public keys to their real owners.”
   Il faut lier une clé publique à une identité de manière fiable.
   Mais sur Internet, on ne peut pas vérifier chaque utilisateur manuellement.
   Solution : créer un système de confiance décentralisé mais hiérarchisé.
   Les acteurs doivent : 1. Définir des règles communes ; 2. Identifier qui est digne de confiance ; 3. Être eux-mêmes reconnus comme fiables.
   C’est le principe fondamental de la PKI.

4. 🔒 Public Key Infrastructure (PKI)
   🧱 Principe général
   Une PKI (infrastructure à clés publiques) repose sur un tiers de confiance appelé Autorité de Certification (CA – Certification Authority).
   Exemple d’interaction : 1. Oscar se présente à la CA et lui fournit sa clé publique. 2. La CA vérifie son identité (selon des procédures précises). 3. La CA signe numériquement la clé publique d’Oscar :
   → cela devient un certificat. 4. Alice, en recevant ce certificat, peut :
   ◦ Vérifier qu’il n’a pas été altéré ;
   ◦ Vérifier qu’il a bien été signé par une CA reconnue.
   Ainsi, Alice peut faire confiance à la clé publique sans connaître Oscar personnellement.

5. 📜 Le certificat numérique
   Un certificat est donc un document électronique signé par une CA.
   Contient typiquement :
   • Identité du propriétaire (nom, domaine, etc.)
   • Sa clé publique
   • Nom de la CA émettrice
   • Période de validité
   • Numéro de série
   • Algorithme et signature de la CA
   Exemple : certificat X.509 (standard Internet)
   Ce format est utilisé dans la majorité des protocoles sécurisés (HTTPS, TLS, S/MIME, etc.).

6. 🪜 La chaîne de confiance (Chain of Trust)
   Principe :
   Les certificats ne sont pas isolés ; ils forment une chaîne hiérarchique : 1. Racine de confiance (Root CA)
   – Entité suprême, connue de tous (préinstallée dans les navigateurs). 2. Intermediate CA
   – Émet des certificats pour les serveurs ou sous-autorités. 3. Serveur / utilisateur final
   – Certificat signé par une CA intermédiaire.
   Vérification d’une chaîne :
   Pour faire confiance à un certificat :
   • On vérifie la signature de la CA intermédiaire.
   • Puis la signature de la CA racine.
   • Si la chaîne est ininterrompue et valide, la confiance est établie.

7. ⚔️ Man-in-the-Middle Attack (MITM)
   Situation normale :
   • Alice ↔ Oscar
   • Les messages sont chiffrés avec la clé publique d’Oscar.
   Attaque MITM :
   • Eve intercepte les communications.
   • Elle remplace la clé publique d’Oscar par la sienne.
   • Alice chiffre son message avec la clé d’Eve → Eve le déchiffre.
   • Eve le rechiffre avec la clé d’Oscar et le transfère.
   ➡️ Alice et Oscar croient communiquer ensemble,
   mais Eve lit et modifie tout ce qui transite.
   ✅ Les certificats signés par une CA empêchent ce type d’attaque :
   Alice vérifiera que la clé publique d’Oscar est bien certifiée par une autorité de confiance.

8. 🧰 Exemples d’autorités de certification (CA)
   • Let’s Encrypt → CA gratuite et automatisée.
   • DigiCert, GlobalSign, Sectigo, etc. → CA commerciales.
   • Institutions internes → certaines entreprises créent leur propre CA pour leur réseau privé.

9. 🧾 Révocation et validité des certificats
   Les certificats ne sont pas éternels :
   • Chaque certificat a une date de validité (expiration).
   • En cas de compromission, il peut être révoqué via :
   ◦ CRL (Certificate Revocation List)
   ◦ OCSP (Online Certificate Status Protocol)
   Les navigateurs vérifient régulièrement ces statuts avant d’accepter une connexion.

10. 🧩 Résumé synthétique
    Élément
    Description
    Problème
    Comment garantir qu’une clé publique appartient bien à son propriétaire ?
    Solution
    Utiliser une infrastructure de confiance (PKI) avec des certificats signés
    Acteur clé
    Certification Authority (CA)
    Outil
    Certificat numérique (ex. : X.509)
    Protection contre
    Usurpation d’identité, falsification, attaque MITM
    Principe fondamental
    La chaîne de confiance : du serveur jusqu’à la racine reconnue par tous
    Utilisations typiques
    HTTPS / TLS, VPN, signature de code, email sécurisé

11. ⚖️ Message clé à retenir
    🔐 La cryptographie seule ne suffit pas.
    Il faut un système de confiance pour relier les clés aux identités.
    La PKI et les certificats assurent cette confiance, permettant à la cryptographie de fonctionner à grande échelle (comme sur le web).

🧭 Chapitre 4 – Authentication

1. ⚙️ Introduction générale
   Les chapitres précédents ont présenté :
   • Les objectifs de la sécurité (disponibilité, intégrité, confidentialité, etc.)
   • Les outils cryptographiques (hachage, chiffrement, signatures)
   • Les certificats et la PKI
   🎯 Ce chapitre aborde un concept fondamental :
   Comment prouver qu’une entité est bien celle qu’elle prétend être ?
   ➡️ C’est le rôle de l’authentification.

2. 👤 Qu’est-ce que l’authentification ?
   🔍 Principe :
   L’authentification est le processus par lequel un système vérifie l’identité d’un utilisateur.
   Elle repose sur la présentation de preuves d’identité appelées “credentials”.
   ⚙️ Deux étapes : 1. Identification → “Je suis Alice.” 2. Authentification → “Voici la preuve que je suis bien Alice.”
   ⚠️ Règle importante :
   Une bonne authentification ne doit pas dépendre d’un système externe que vous ne contrôlez pas (ex. : email non sécurisé).

3. 🔑 Types de facteurs d’authentification
   Les credentials (preuves d’identité) appartiennent à trois grandes catégories :
   Type
   Description
   Exemple
   🧠 Facteur de connaissance
   Quelque chose que l’utilisateur sait
   Mot de passe, PIN
   🔐 Facteur de possession
   Quelque chose que l’utilisateur possède
   Carte, clé USB, token, smartphone
   🧬 Facteur d’inhérence
   Quelque chose que l’utilisateur est
   Empreinte digitale, reconnaissance faciale, voix

4. 🧩 Principe de base
   Lors de l’authentification :
   • L’utilisateur présente ses identifiants (identifiant + preuve)
   • Le système vérifie la validité des preuves
   • Si la vérification est réussie → accès autorisé
   Exemple simple :
   “Je connais un secret (mot de passe) que seul le vrai moi devrait connaître.”
   Mais cette méthode a une faiblesse :
   ➡️ Le secret doit être transmis au système, donc il peut être intercepté ou volé.

5. 🧮 Multi-Factor Authentication (MFA)
   🎯 Principe :
   Combiner plusieurs types de facteurs pour renforcer la sécurité.
   Type
   Description
   Exemple
   2FA (Two-Factor Authentication)
   Deux preuves d’identité
   Mot de passe + code SMS
   MFA (Multi-Factor Authentication)
   Deux ou plus
   Mot de passe + clé physique + empreinte
   💡 Objectif :
   Augmenter le niveau de confiance dans le processus d’authentification.
   ➡️ Plus un attaquant doit fournir de preuves, plus il lui est difficile d’usurper une identité.
   Exemples concrets :
   • 🏧 Distributeur bancaire : carte + code PIN
   • 🌐 Google / Steam / Facebook : mot de passe + code à usage unique (OTP)

6. 🧠 MFA vs. Social Engineering
   🎭 Social engineering :
   L’art de manipuler les gens pour qu’ils trahissent eux-mêmes la sécurité :
   • Révéler un mot de passe
   • Cliquer sur un lien
   • Accorder un accès
   C’est “l’attaque la plus humaine” — et donc la plus fréquente.
   ⚔️ Défense :
   Le MFA protège contre ces attaques :
   • Un attaquant doit tromper l’utilisateur et dérober un second facteur.
   • Une seule interaction malveillante ne suffit plus.
   👉 Le MFA est la meilleure défense contre l’erreur humaine.

7. 🧩 Challenge-Response Authentication
   Problème :
   Dans une authentification par mot de passe classique, le secret est dévoilé à chaque connexion.
   ➡️ Risque d’interception.
   Solution :
   Prouver qu’on connaît le secret sans le révéler.
   🔁 Principe : 1. Le serveur envoie un challenge (valeur aléatoire / nonce). 2. L’utilisateur signe ou chiffre ce challenge avec sa clé privée. 3. Le serveur vérifie la réponse à l’aide de la clé publique.
   ➡️ Le serveur sait que l’utilisateur détient le secret, sans jamais le voir.
   C’est une preuve à connaissance nulle (zero-knowledge proof).
   🔒 Exemple :
   Authentification par signature numérique (RSA, ECC).

8. 🔐 Token-Based Authentication
   🎯 Objectif :
   Éviter de réauthentifier l’utilisateur à chaque requête.
   🔍 Principe : 1. L’utilisateur s’authentifie une fois (mot de passe ou clé). 2. Le serveur génère un token signé ou chiffré (preuve temporaire d’identité). 3. L’utilisateur envoie ensuite ce token pour accéder aux ressources.
   ⚙️ Avantages :
   • L’utilisateur ne renvoie plus son mot de passe.
   • Les tokens peuvent expirer ou être révoqués.
   • Utilisable sur plusieurs services (SSO).
   🔐 Types de tokens :
   • JWT (JSON Web Token)
   • OAuth 2.0 tokens
   • SAML assertions

9. 🔁 Single Sign-On (SSO)
   🎯 Définition :
   Mécanisme permettant à un utilisateur de se connecter une seule fois pour accéder à plusieurs services.
   🔍 Fonctionnement : 1. L’utilisateur s’authentifie auprès d’un Identity Provider (IdP) central. 2. L’IdP délivre une assertion (preuve d’identité). 3. Les services partenaires (relying parties) font confiance à l’IdP.
   ⚠️ Inconvénient :
   • Si l’IdP est compromis, tous les services le sont → point unique de défaillance.
   ✅ Avantage :
   • Améliore l’expérience utilisateur et la gestion centralisée des accès.

10. 🏛️ Identity and Access Management (IAM)
    L’authentification n’est qu’une partie d’un écosystème plus large :
    ➡️ la gestion des identités et des accès.
    IAM englobe :
    • Création, gestion et suppression d’utilisateurs
    • Politiques d’accès
    • Authentification (vérifier qui)
    • Autorisation (décider quoi)
    • Traçabilité (journaliser qui a fait quoi)
    💡 Objectif : garantir la cohérence et la sécurité à travers toute l’organisation.

11. 🔗 Protocoles modernes d’authentification
    🌐 JSON Web Token (JWT)
    • Format standard pour transporter les informations d’identité.
    • Signé (voire chiffré) pour éviter la falsification.
    • Utilisé dans les APIs et applications web modernes.
    🔑 OAuth 2.0
    • Standard pour déléguer l’accès sans partager le mot de passe.
    • Exemple : “Se connecter avec Google / GitHub”.
    🧬 WebAuthn
    • Standard du W3C pour authentification sans mot de passe.
    • Utilise des clés asymétriques et des périphériques biométriques (ex. YubiKey, empreinte).

12. ⚖️ Résumé synthétique
    Élément
    Description
    But du chapitre
    Comprendre les mécanismes d’authentification et leurs modèles modernes
    Étapes
    Identification → Authentification → Autorisation
    Facteurs
    Connaissance, possession, inhérence
    Techniques
    Mot de passe, MFA, challenge-response, tokens, SSO
    Protocoles clés
    JWT, OAuth 2.0, WebAuthn
    Menaces principales
    Social engineering, vol d’identifiants, point de défaillance unique
    Message clé
    🔐 Une bonne authentification repose sur la combinaison de plusieurs preuves et sur la gestion centralisée des identités.
