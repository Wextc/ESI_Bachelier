Chapitre 0 – Introduction

1. 🎓 Présentation du cours

Le cours fait partie du module INT1 et dure 2 heures par semaine.

La présence est “optionnelle”, mais la réussite dépend de l’assiduité et de la participation.

Objectif global
Fournir une introduction à la sécurité informatique, en expliquant les concepts, terminologies et outils de base, sans exiger de mise en pratique complexe.
Le cours s’appuie sur des démonstrations et des exemples concrets, mais les étudiants ne doivent pas les reproduire eux-mêmes.

2. 👩‍🏫 Les enseignants

R. Absil (ABS)

J. Dossogne (JDS)

Deux enseignants accessibles et disponibles : « Si vous avez une question, demandez. Nous ne mordons pas… trop souvent ! »

3. 💡 Pourquoi un cours de sécurité ?

La sécurité informatique est partout :

Comptes bancaires, jeux en ligne, réseaux sociaux.

Systèmes administratifs : vote électronique, fiscalité, santé, etc.

➡️ Ces applications manipulent des données sensibles : authentification, contrôle d’accès, stockage ou transmission sécurisée.
➡️ Il est donc essentiel de comprendre les concepts fondamentaux liés à ces processus.

Citation clé
“Dire que vous ne vous souciez pas de la vie privée parce que vous n’avez rien à cacher, c’est comme dire que vous ne vous souciez pas de la liberté d’expression parce que vous n’avez rien à dire.”
(Rappel : la vie privée = un droit fondamental, pas un luxe.)

4. 🎯 Objectifs pédagogiques

À la fin du cours, l’étudiant doit :

Comprendre les caractéristiques désirées de la sécurité : confidentialité, intégrité, authentification, etc.

Connaître les outils cryptographiques de base :

Fonctions de hachage

Algorithmes de chiffrement

Signatures et certificats numériques

Savoir ce qu’est l’authentification et pourquoi elle est cruciale.
➡️ Les notions avancées seront approfondies plus tard (en 3ᵉ année ou au master).

5. 📚 Références recommandées

W. Du, Computer and Internet Security: A Hands-On Approach, 2ᵉ éd., 2019

J. Pelzl & C. Paar, Understanding Cryptography, Springer, 2010

B. Schneier, Secrets and Lies: Digital Security in a Networked World, Wiley, 2015

OWASP — https://owasp.org

NIST — https://www.nist.gov

6. 🧾 Modalités d’évaluation

Première session :

Pas d’évaluation intermédiaire

Examen en janvier : 100 % de la note

Seconde session :

Examen en août : 100 % de la note

Format :

QCM (Questions à choix multiples)

Peu de points négatifs

Format choisi pour des raisons de logistique (nombre élevé d’étudiants)

🧩 En résumé
Aspect Description
Nature du cours Introduction théorique et conceptuelle à la sécurité informatique
Objectif Comprendre les bases, les enjeux et les outils cryptographiques
Évaluation 100 % examen QCM
Enseignants R. Absil & J. Dossogne
Mot-clé du cours Responsabilité individuelle face à la sécurité et à la vie privée
🧭 Chapitre 1 – Introduction à la sécurité

1. ⚙️ Introduction

Depuis la Seconde Guerre mondiale, la nécessité de protéger les systèmes informatiques s’est imposée. Les menaces se sont multipliées, et chaque type de menace demande une protection adaptée.

Problème : une sécurité forte est souvent contraignante et lourde à mettre en œuvre.
Solution : analyser les risques :

Identifier chaque menace

Évaluer sa probabilité

Adapter la stratégie de sécurité en conséquence

👉 Ne pas “tuer les moustiques avec une bombe nucléaire” — viser un niveau de sécurité proportionné au risque.

2. ⚠️ Types de risques étudiés dans le cours

Le cours se concentre sur cinq grandes familles de risques :

Type de risque Description
🔐 Accès non autorisé Accéder à une ressource ou un service restreint
🕵️ Usurpation d’identité Se faire passer pour quelqu’un d’autre
🧾 Accès à des données Lire des données sensibles sans autorisation
✏️ Falsification Modifier des informations de manière frauduleuse
🧠 Contrefaçon / Forgerie Créer de fausses données ou fausses signatures

Pour chaque risque :

Plusieurs types d’attaques existent

Plusieurs contre-mesures sont possibles

3. 🎣 Exemple concret : le phishing

Principe : exploiter la confiance de la victime pour soutirer des informations sensibles (mots de passe, numéros de carte, etc.).
Étapes typiques :

Identification de la cible → 2) Préparation de l’appât (email, lien, page web…) → 3) Envoi du message/piège → 4) Récupération des informations

Défenses :

La seule sensibilisation ne suffit pas toujours

Outils techniques nécessaires :

Anti-phishing

Anti-malware

Authentification multifacteur (MFA, voir Ch.4)

Filtrage des mails inconnus

4. 🧮 Contraintes et calculs

“When in doubt, use brute force.”

Beaucoup de systèmes reposent sur des problèmes mathématiques difficiles sans les clés appropriées (factorisation, inversion de fonctions complexes, optimisation combinatoire/stochastique).
Ces contraintes rendent les attaques incomputables ou trop longues, garantissant la robustesse des systèmes. (Les détails mathématiques sont hors-scope ici.)

5. 🎯 Objectifs fondamentaux de la sécurité (CIA + AAA)
   Objectif Définition
   🕒 Availability (Disponibilité) S’assurer que le système est fonctionnel
   👤 Authentication (Authentification) Identifier correctement “qui est qui”
   🧾 Authorisation (Autorisation) Déterminer “qui peut faire quoi”
   🧍‍♂️ Accountability (Traçabilité) Savoir “qui a fait quoi”
   🧩 Integrity (Intégrité) Détecter toute modification non autorisée
   🔒 Confidentiality (Confidentialité) Empêcher la divulgation d’infos sensibles

💡 Les trois premiers — Authentication, Authorisation, Accountability — forment le modèle AAA.

6. ⚖️ Principes de base de la sécurité

Principe du moindre privilège

Défense en profondeur (multiplier les couches)

Transparence (ne pas dépendre du secret de la méthode)

Simplicité (la complexité crée des vulnérabilités)

Séparation des responsabilités

🧩 Résumé synthétique
Élément Description
But du chapitre Présenter risques, objectifs et principes fondamentaux de la sécurité
Concepts clés Risque, menace, attaque, contre-mesure, proportionnalité
Exemple pratique Phishing
Modèles Triade CIA + AAA
Message clé La sécurité parfaite n’existe pas — viser l’équilibre risque/coût/perf.
🧭 Chapitre 2 – Cryptographic Tools

1. ⚙️ Introduction

La cryptographie est la boîte à outils principale de la sécurité informatique :

Objectif Outil cryptographique
🔐 Confidentialité Chiffrement (cipher algorithms)
🧩 Intégrité Fonctions de hachage
✍️ Authenticité/Non-rép. Signatures numériques 2. 🧱 Fonctions de hachage (Hash functions)

Objectif : garantir l’intégrité (détecter toute modification).
Principe : entrée arbitraire → digest de longueur fixe ; fonction à sens unique.

Propriétés essentielles :

Unidirectionnalité

Résistance à la préimage

Résistance aux collisions

Effet avalanche

Exemple pédagogique : texte chez un notaire, hash chez un autre → modification détectée.

Exemples : MD5 (obsolète), SHA-1 (obsolète), SHA-2 / SHA-3 (actuels).

3. 🔐 Algorithmes de chiffrement

Objectif : confidentialité.
Principe : plaintext → ciphertext via une clé ; déchiffrement inverse.

Familles :

Type Principe Exemples
Symétrique Même clé pour chiffrer/déchiffrer AES, DES
Asymétrique Deux clés : publique / privée RSA, ECC

Comparaison :

Critère Symétrique Asymétrique
Vitesse Très rapide Plus lent
Distribution des clés Difficile Facile (clé publique)
Sécurité dépend de Clé secrète Problèmes maths “durs”
Usage typique Données Authent., échange de clés 4. 📦 Modes de fonctionnement : blocs et flux
Mode Description Exemple
Block cipher Message en blocs taille fixe (ex. 128 bits) AES, DES
Stream cipher Chiffrement bit/octet par bit/octet RC4, ChaCha20

Padding pour le dernier bloc

Avalanche effect souhaité

5. 🔁 Échange de clés (Key Exchange)

Problème : partager la clé symétrique en sécurité.
Solution : Diffie–Hellman (DHKE) → clés publiques échangées, clé partagée calculée localement. Base de la confidentialité éphémère dans TLS.

6. ✍️ Signatures numériques

Objectif : authenticité & non-répudiation.
Principe (simplifié) : hash → chiffrement du hash avec clé privée → vérification avec clé publique → comparaison des hash.

Applications : certificats (cf. Ch.3), signature de code/doc, authentification réseau.

7. 🧮 Problèmes mathématiques “difficiles”

RSA → factorisation

Diffie-Hellman → logarithme discret

ECC → problèmes sur courbes elliptiques

8. 🧰 Synthèse
   Objectif Outil Exemple
   Confidentialité Chiffrement (AES, RSA) Messages privés, stockage
   Intégrité Hachage (SHA-256) Vérification de fichiers
   Authenticité / Non-répud. Signature numérique Documents signés
   Échange de clés Diffie–Hellman TLS, VPNs
9. ⚖️ Principes clés à retenir

Combiner les outils pour une sécurité complète

Ne pas réinventer d’algorithmes — utiliser les standards

La force dépend du temps nécessaire à casser

Protéger les clés d’abord

La crypto matérialise la confiance — la PKI la relie aux identités (Ch.3)

10. 🧩 Résumé synthétique
    Élément Description
    But du chapitre Outils cryptographiques de base et leurs usages
    Outils Hachage, symétrique/asymétrique, signatures
    Concepts clés Avalanche effect, block vs stream, Diffie-Hellman, clé publique/privée
    Message clé 🔐 La cryptographie est le socle : protège, prouve l’intégrité, garantit l’identité
    🧭 Chapitre 3 – Certificates & Public Key Infrastructure (PKI)
1. ⚙️ Introduction

Hachage → intégrité ; Chiffrement → confidentialité ; Signatures → non-répudiation.
Problème : comment être sûr que la clé publique appartient à la bonne personne ?
➡️ PKI.

2. 🧩 Le problème d’identité

Scénarios chiffrement & signature : sans garantie d’identité, la clé publique peut être celle d’un imposteur → vérification invalide.

3. 🕵️ Besoin d’un tiers de confiance

Relier clés publiques ↔ identités de manière fiable, à grande échelle → règles communes, acteurs dignes de confiance → PKI.

4. 🔒 Public Key Infrastructure (PKI)

Principe : Autorité de Certification (CA) signe la clé publique → certificat.
Alice vérifie l’intégrité et la signature de la CA reconnue → confiance établie.

5. 📜 Le certificat numérique

Contient : identité du propriétaire, clé publique, CA émettrice, validité, n° de série, algo + signature.
Standard : X.509 (HTTPS, TLS, S/MIME, …).

6. 🪜 Chaîne de confiance (Chain of Trust)

Root CA (préinstallée)

Intermediate CA

Serveur / utilisateur final

Vérification : signature intermédiaire → racine → chaîne valide ⇒ confiance.

7. ⚔️ Man-in-the-Middle (MITM)

Eve remplace la clé publique → lit/modifie le trafic.
Les certificats signés par une CA empêchent l’attaque (vérification de confiance).

8. 🧰 Exemples de CA

Let’s Encrypt (gratuite, automatisée)

DigiCert, GlobalSign, Sectigo, …

CA interne (entreprises)

9. 🧾 Révocation & validité

Période de validité

Révocation : CRL / OCSP

Les navigateurs vérifient ces statuts.

10. 🧩 Résumé synthétique
    Élément Description
    Problème Lier une clé publique à son propriétaire
    Solution PKI + certificats signés
    Acteur clé Certification Authority (CA)
    Outil Certificat numérique (ex. X.509)
    Protège contre Usurpation d’identité, falsification, MITM
    Principe Chaîne de confiance jusqu’à une racine reconnue
    Usages HTTPS/TLS, VPN, signature de code, email sécurisé
11. ⚖️ Message clé

🔐 La cryptographie seule ne suffit pas.
Il faut un système de confiance pour relier les clés aux identités : PKI + certificats.

🧭 Chapitre 4 – Authentication

1. ⚙️ Introduction générale

Objectifs de sécurité, outils cryptographiques, certificats/PKI → maintenant : prouver l’identité (authentification).

2. 👤 Qu’est-ce que l’authentification ?

Processus par lequel un système vérifie l’identité via des credentials.
Étapes : Identification (“Je suis Alice”) → Authentification (“J’en apporte la preuve”).
⚠️ Éviter de dépendre d’un système externe non maîtrisé.

3. 🔑 Types de facteurs d’authentification
   Type Description Exemples
   🧠 Connaissance Quelque chose que l’utilisateur sait Mot de passe, PIN
   🔐 Possession Quelque chose qu’il possède Carte, token, smartphone
   🧬 Inhérence Quelque chose qu’il est Empreinte, visage, voix
4. 🧩 Principe de base

Soumission d’identifiants → vérification → accès.
Faiblesse du mot de passe : le secret est transmis (interception possible).

5. 🧮 Multi-Factor Authentication (MFA)
   Type Description Exemple
   2FA Deux preuves Mot de passe + code SMS
   MFA ≥ 2 preuves Mot de passe + clé physique + empreinte

Objectif : augmenter la confiance, réduire l’usurpation.
Exemples : DAB (carte + PIN), Google/Steam/Facebook (mot de passe + OTP).

6. 🧠 MFA vs. Social Engineering

Social engineering : manipulation de l’humain (révéler mot de passe, cliquer, donner accès).
Défense : MFA → l’attaquant doit contourner plusieurs facteurs.

7. 🧩 Challenge-Response Authentication

Problème : révéler le secret à chaque connexion.
Solution : prouver la connaissance sans divulguer (nonce/challenge signé).
Ex. : signatures numériques (RSA, ECC), zero-knowledge.

8. 🔐 Token-Based Authentication

Authentification initiale

Génération d’un token signé/chiffré

Accès via token (expiration/révocation possibles, SSO)

Types : JWT, OAuth 2.0 tokens, SAML assertions.

9. 🔁 Single Sign-On (SSO)

IdP central → assertions d’identité pour plusieurs services.
✅ UX & gestion centralisée ; ⚠️ point unique de défaillance.

10. 🏛️ Identity and Access Management (IAM)

Gestion des identités et des accès : cycle de vie utilisateurs, politiques, authN, authZ, traçabilité.
Objectif : cohérence et sécurité organisationnelle.

11. 🔗 Protocoles modernes

JWT : format standard, signé/chiffré, très utilisé en APIs/web.

OAuth 2.0 : délégation d’accès (login “avec Google/GitHub”).

WebAuthn : sans mot de passe, clés asymétriques + biométrie (YubiKey, empreinte).

12. ⚖️ Résumé synthétique
    Élément Description
    But Comprendre les mécanismes d’authentification et leurs modèles modernes
    Étapes Identification → Authentification → Autorisation
    Facteurs Connaissance, possession, inhérence
    Techniques Mot de passe, MFA, challenge-response, tokens, SSO
    Protocoles JWT, OAuth 2.0, WebAuthn
    Menaces Social engineering, vol d’identifiants, SPOF (IdP)
    Message clé 🔐 Combiner plusieurs preuves et gérer centralement les identités (IAM)
