# 🧭 Chapitre 1 – Introduction à la sécurité

## ⚙️ 1. Introduction

Q1. Pourquoi la sécurité informatique est-elle devenue essentielle depuis la Seconde Guerre mondiale ?

R : Parce que les systèmes informatiques sont devenus vitaux et exposés à de nombreuses menaces, nécessitant des protections adaptées.

---

Q2. Quel est le principal problème d’une sécurité trop forte ?

R : Elle est souvent lourde et contraignante à mettre en œuvre.

---

Q3. Quelle est la solution pour une sécurité efficace mais équilibrée ?

R : Réaliser une analyse de risques : identifier les menaces, évaluer leur probabilité, et adapter la sécurité de manière proportionnée.

---

Q4. Que signifie l’expression “Ne pas tuer les moustiques avec une bombe nucléaire” ?

R : Il faut adapter le niveau de sécurité au niveau réel du risque.

## ⚠️ 2. Types de risques étudiés

Q5. Quelles sont les cinq grandes familles de risques étudiées dans le cours ?

R :

Accès non autorisé

Usurpation d’identité

Accès à des données confidentielles

Falsification

Contrefaçon / Forgerie

---

Q6. Que signifie “accès non autorisé” ?

R : C’est lorsqu’une personne accède à une ressource ou un service restreint sans permission.

---

Q7. En quoi consiste une “usurpation d’identité” ?

R : C’est le fait de se faire passer pour quelqu’un d’autre.

---

Q8. Quelle est la différence entre falsification et contrefaçon ?

R :

Falsification : modifier une information réelle de manière frauduleuse.

Contrefaçon : créer une fausse donnée ou une fausse signature.

## 🎣 3. Exemple concret : le phishing

Q9. Quel est le principe du phishing ?

R : Tromper la victime pour obtenir ses informations sensibles (mots de passe, numéros de carte, etc.).

---

Q10. Quelles sont les étapes typiques d’une attaque de phishing ?
R :

Identification de la cible

Préparation de l’appât (email, lien, page web…)

Envoi du piège

Récupération des informations

---

Q11. Pourquoi la sensibilisation seule n’est-elle pas suffisante contre le phishing ?

R : Parce que les attaques sont souvent sophistiquées et nécessitent aussi des protections techniques.

---

Q12. Cite quelques outils de défense contre le phishing.

R : Anti-phishing, anti-malware, authentification multifacteur (MFA), filtrage des mails inconnus.

## 🧮 4. Contraintes et calculs

Q13. Que signifie la phrase “When in doubt, use brute force” ?

R : Certains systèmes reposent sur la difficulté mathématique à résoudre des problèmes sans les clés, rendant les attaques par force brute inefficaces.

---

Q14. Donne deux exemples de problèmes mathématiques “durs”.
R :

La factorisation de grands nombres

L’inversion de fonctions complexes

---

Q15. Pourquoi ces contraintes mathématiques sont-elles importantes ?
R : Elles rendent les attaques impossibles ou trop longues, garantissant la robustesse du système.

## 🎯 5. Objectifs fondamentaux de la sécurité

Q16. Quels sont les six grands objectifs de la sécurité informatique ?
R :

Availability (Disponibilité)

Authentication (Authentification)

Authorisation (Autorisation)

Accountability (Traçabilité)

Integrity (Intégrité)

Confidentiality (Confidentialité)

---

Q17. Que garantit la disponibilité ?
R : Que le système reste accessible et fonctionnel.

---

Q18. Quelle est la différence entre “Authentification” et “Autorisation” ?
R :

Authentification : identifier qui est l’utilisateur.

Autorisation : déterminer ce qu’il a le droit de faire.

---

Q19. Que signifie la “traçabilité” (Accountability) ?

R : Pouvoir savoir qui a fait quoi dans le système.

---

Q20. Quelle est la triade AAA ?

R : Authentication, Authorisation, Accountability.

## ⚖️ 6. Principes de base de la sécurité

Q21. Que signifie le principe du moindre privilège ?

R : Chaque utilisateur ne doit avoir accès qu’aux ressources nécessaires à sa fonction.

---

Q22. En quoi consiste la défense en profondeur ?

R : Utiliser plusieurs couches de sécurité successives pour renforcer la protection.

---

Q23. Pourquoi la sécurité ne doit-elle pas dépendre du secret de la méthode ?

R : Parce que la sécurité doit résider dans la solidité du système, pas dans le secret de son fonctionnement (principe de transparence).

---

Q24. Pourquoi faut-il privilégier la simplicité dans un système sécurisé ?

R : Plus un système est complexe, plus il est vulnérable aux erreurs et failles.

---

Q25. Que veut dire “séparation des responsabilités” ?

R : Aucune personne ne doit avoir le contrôle total du système, pour éviter les abus ou les erreurs critiques.

🧭 Chapitre 2 – Cryptographic Tools

## ⚙️ 1. Introduction

Q1. Quel est le rôle principal de la cryptographie en sécurité informatique ?
R : Elle est la boîte à outils qui permet d’assurer la confidentialité, l’intégrité et l’authenticité des données.

---

Q2. Quel outil cryptographique garantit la confidentialité ?

R : Le chiffrement (cipher algorithms).

---

Q3. Quel outil garantit l’intégrité des données ?

R : Les fonctions de hachage (hash functions).

---

Q4. Quel outil assure l’authenticité et la non-répudiation ?

R : Les signatures numériques.

## 🧱 2. Fonctions de hachage

Q5. Quel est l’objectif principal d’une fonction de hachage ?

R : Garantir l’intégrité d’un message, c’est-à-dire détecter toute modification.

---

Q6. Que fait une fonction de hachage ?

R : Elle transforme un message de longueur variable en un digest (empreinte) de longueur fixe.

---

Q7. Pourquoi dit-on qu’une fonction de hachage est “à sens unique” ?

R : Parce qu’il est impossible de retrouver le message original à partir du hash.

---

Q8. Quelles sont les propriétés essentielles d’une bonne fonction de hachage ?
R :

Unidirectionnalité

Résistance à la préimage

Résistance aux collisions

Effet avalanche

---

Q9. Donne un exemple concret illustrant l’usage d’un hash.

R : Un notaire garde le texte d’un testament, un autre le hash : si le texte change, le hash ne correspond plus → fraude détectée.

---

Q10. Cite des exemples de fonctions de hachage.

R : MD5 et SHA-1 (obsolètes), SHA-2 et SHA-3 (actuelles).

## 🔐 3. Algorithmes de chiffrement

Q11. Quel est le but du chiffrement ?

R : Protéger la confidentialité des données, empêcher les non-autorisés de lire un message.

---

Q12. Quelle est la différence entre texte clair et texte chiffré ?

R : Le texte clair (plaintext) est lisible ; le texte chiffré (ciphertext) est illisible sans la clé.

---

Q13. Quelles sont les deux grandes familles de chiffrement ?

R : Le chiffrement symétrique et le chiffrement asymétrique.

---

Q14. Quelle est la particularité du chiffrement symétrique ?

R : Une même clé sert à chiffrer et déchiffrer.

---

Q15. Donne deux exemples d’algorithmes symétriques.

R : AES et DES.

---

Q16. Quelle est la particularité du chiffrement asymétrique ?

R : Il utilise deux clés différentes : une clé publique et une clé privée.

---

Q17. Donne deux exemples d’algorithmes asymétriques.

R : RSA et ECC.

---

Q18. Quel type de chiffrement est le plus rapide ?

R : Le chiffrement symétrique.

---

Q19. Quel type de chiffrement facilite la distribution des clés ?

R : Le chiffrement asymétrique.

---

Q20. De quoi dépend la sécurité d’un chiffrement symétrique ?

R : De la confidentialité de la clé secrète.

## 📦 4. Modes de fonctionnement : blocs et flux

Q21. Quelle est la différence entre un block cipher et un stream cipher ?
R :

Block cipher : chiffre des blocs de taille fixe (ex. 128 bits)

Stream cipher : chiffre les données bit par bit ou octet par octet

---

Q22. Donne un exemple d’algorithme par blocs et un par flux.

R :

Par blocs : AES, DES

Par flux : RC4, ChaCha20

---

Q23. À quoi sert le “padding” ?

R : À compléter le dernier bloc de données pour qu’il soit de taille correcte.

---

Q24. Qu’est-ce que l’effet avalanche ?

R : Une petite modification du texte clair ou de la clé provoque un changement complet du texte chiffré.

## 🔁 5. Échange de clés

Q25. Quel problème résout l’échange de clés ?

R : Il permet de partager une clé secrète sans la transmettre directement sur le réseau.

---

Q26. Quel protocole célèbre permet cet échange sécurisé ?

R : Diffie–Hellman Key Exchange (DHKE).

---

Q27. Comment DHKE protège-t-il la clé ?

R : Alice et Bob échangent des valeurs publiques dérivées de leurs secrets, puis calculent la même clé localement — un espion ne peut pas la reconstituer.

---

Q28. Dans quels protocoles modernes DHKE est-il utilisé ?

R : TLS et VPNs.

---

## ✍️ 6. Signatures numériques

Q29. Quels sont les objectifs d’une signature numérique ?

R : Garantir l’authenticité du message et la non-répudiation.

---

Q30. Quelle est la première étape de la création d’une signature numérique ?

R : Calculer le hash du message.

---

Q31. Comment l’émetteur crée-t-il la signature ?

R : Il chiffre le hash avec sa clé privée.

---

Q32. Comment le destinataire vérifie-t-il la signature ?

R : Il déchiffre la signature avec la clé publique de l’émetteur, recalcule le hash du message et compare les deux.

---

## 🧮 7. Problèmes mathématiques “difficiles”

Q33. Sur quels types de problèmes reposent les algorithmes cryptographiques modernes ?

R : Sur des problèmes mathématiques impossibles à résoudre efficacement sans clé.

---

Q34. Cite trois exemples de ces problèmes.
R :

RSA → factorisation de grands nombres

Diffie–Hellman → logarithme discret

ECC → équations elliptiques

## 🧰 8. Synthèse : outils cryptographiques et objectifs

---

Q35. Quel outil sert à la confidentialité ?

R : Le chiffrement (AES, RSA).

---

Q36. Quel outil assure l’intégrité ?

R : Le hachage (SHA-256).

---

Q37. Quel outil prouve l’authenticité ?

R : La signature numérique.

---

Q38. Quel outil permet un échange de clés sécurisé ?

R : Diffie–Hellman.

---

## ⚖️ 9. Principes clés à retenir

Q39. Pourquoi faut-il combiner plusieurs outils cryptographiques ?

R : Parce qu’aucun outil seul ne garantit une sécurité complète.

---

Q40. Pourquoi ne faut-il jamais inventer son propre algorithme ?

R : Parce qu’il serait probablement vulnérable — seuls les standards éprouvés sont sûrs.

---

Q41. De quoi dépend réellement la force d’un système cryptographique ?

R : Du temps et des ressources nécessaires pour le casser.

---

Q42. Quelle est la ressource la plus critique à protéger ?

R : Les clés cryptographiques.

---

Q43. Que signifie “la cryptographie ne crée pas la confiance, elle la matérialise” ?

R : Elle fournit les preuves techniques de la confiance (authenticité, intégrité), mais la confiance initiale vient d’ailleurs (PKI, certificats…).
