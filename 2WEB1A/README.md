### HTML

| Balise HTML           | Rôle / Explication                                     |
| --------------------- | ------------------------------------------------------ |
| `<html>`              | Contient tout le document HTML.                        |
| `<head>`              | Contient les informations de configuration de la page. |
| `<body>`              | Contient le contenu visible de la page web.            |
| `<title>`             | Définit le titre affiché dans l’onglet du navigateur.  |
| `<link>`              | Permet de relier des fichiers externes (CSS).          |
| `<script>`            | Sert à ajouter du JavaScript.                          |
| `<h1>`                | Titre principal de la page.                            |
| `<h2>` jusqu’à `<h6>` | Titres de différents niveaux.                          |
| `<p>`                 | Définit un paragraphe.                                 |
| `<ul>`                | Liste à puces (liste non ordonnée).                    |
| `<ol>`                | Liste numérotée (liste ordonnée).                      |
| `<li>`                | Élément d’une liste.                                   |
| `<a>`                 | Crée un lien hypertexte.                               |
| `<img>`               | Affiche une image.                                     |
| `<header>`            | Représente l’en-tête de la page.                       |
| `<nav>`               | Contient le menu de navigation.                        |
| `<main>`              | Contient le contenu principal.                         |
| `<aside>`             | Contient un contenu secondaire.                        |
| `<footer>`            | Représente le bas de page.                             |
| `<dl>`                | Liste descriptive.                                     |
| `<dt>`                | Élément à décrire dans une liste descriptive.          |
| `<dd>`                | Description de l’élément.                              |
| `<abbr>`              | Définit une abréviation ou un sigle.                   |

---

| Balise HTML | Explication                                                                                               |
| ----------- | --------------------------------------------------------------------------------------------------------- |
| `<span>`    | Balise en ligne utilisée pour modifier ou cibler une petite partie de texte sans créer de nouvelle ligne. |
| `<div>`     | Balise de bloc utilisée pour regrouper des éléments HTML et organiser la page.                            |

---

<b>Exemple: dl, dt, dd:</b>

```
<dl>
  <dt>HTML</dt>
  <dd>Langage utilisé pour structurer une page web.</dd>

  <dt>CSS</dt>
  <dd>Langage utilisé pour la mise en forme.</dd>
</dl>

```

---

Une entité HTML est un code utilisé pour afficher des caractères réservés (ex : <, >), invisibles ou non présents

sur le clavier. Il commence par & et finit par ;. Les plus utiles à connaitre sont :

| Entité HTML | Caractère affiché | Rôle / Utilisation                                                                 |
| ----------- | ----------------- | ---------------------------------------------------------------------------------- |
| `&lt;`      | `<`               | Affiche le symbole inférieur `<` sans qu’il soit interprété comme une balise HTML. |
| `&gt;`      | `>`               | Affiche le symbole supérieur `>`.                                                  |
| `&amp;`     | `&`               | Affiche le symbole esperluette `&`.                                                |
| `&quot;`    | `"`               | Affiche des guillemets doubles.                                                    |
| `&nbsp;`    | espace insécable  | Ajoute un espace qui ne sera pas coupé lors du retour à la ligne.                  |

---

<b>Les formulaires:</b>

| Balise       | Rôle                                |
| ------------ | ----------------------------------- |
| `<form>`     | Conteneur principal du formulaire   |
| `<input>`    | Champ de saisie polyvalent          |
| `<textarea>` | Zone de texte multiligne            |
| `<button>`   | Bouton cliquable                    |
| `<select>`   | Liste déroulante                    |
| `<option>`   | Élément d’une liste déroulante      |
| `<optgroup>` | Groupe d’options dans un `<select>` |
| `<label>`    | Étiquette associée à un champ       |
| `<fieldset>` | Groupe logique de champs            |
| `<legend>`   | Titre d’un `<fieldset>`             |
| `<datalist>` | Liste de suggestions pour un input  |
| `<output>`   | Affichage d’un résultat calculé     |
| `<meter>`    | Jauge de valeur dans une plage      |
| `<progress>` | Barre de progression                |

---

<b>Types principaux de <input> en HTML5:</b>

| Type             | Utilisation         |
| ---------------- | ------------------- |
| `text`           | Texte simple        |
| `password`       | Mot de passe        |
| `email`          | Adresse email       |
| `number`         | Nombre              |
| `tel`            | Téléphone           |
| `url`            | Adresse web         |
| `search`         | Recherche           |
| `date`           | Date                |
| `time`           | Heure               |
| `datetime-local` | Date + heure        |
| `month`          | Mois                |
| `week`           | Semaine             |
| `color`          | Choix d’une couleur |
| `range`          | Curseur             |
| `checkbox`       | Case à cocher       |
| `radio`          | Bouton radio        |
| `file`           | Envoi de fichier    |
| `hidden`         | Champ caché         |
| `submit`         | Envoi du formulaire |
| `reset`          | Réinitialisation    |
| `button`         | Bouton simple       |
| `image`          | Bouton image        |

---

<b>Attributs fréquents des formulaires:</b>

| Attribut       | Rôle                            |
| -------------- | ------------------------------- |
| `id`           | Identifiant unique              |
| `name`         | Nom du champ                    |
| `value`        | Valeur du champ                 |
| `type`         | Type d’input                    |
| `placeholder`  | Texte indicatif                 |
| `required`     | Champ obligatoire               |
| `readonly`     | Lecture seule                   |
| `disabled`     | Désactivé                       |
| `checked`      | Coché par défaut                |
| `selected`     | Option sélectionnée             |
| `multiple`     | Plusieurs valeurs possibles     |
| `min`          | Valeur minimale                 |
| `max`          | Valeur maximale                 |
| `step`         | Pas numérique                   |
| `maxlength`    | Taille maximale                 |
| `pattern`      | Expression régulière            |
| `autocomplete` | Auto-complétion                 |
| `action`       | URL d’envoi du formulaire       |
| `method`       | Méthode HTTP (`GET`/`POST`)     |
| `for`          | Associe un `<label>` à un champ |

---

| Attribut HTML | Explication                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------- |
| `id`          | Identifiant unique d’un élément HTML. Permet de le cibler avec CSS ou JavaScript.                       |
| `href`        | Définit l’adresse d’un lien ou d’une ressource (utilisé avec `<a>` ou `<link>`).                        |
| `rel`         | Indique la relation entre le document actuel et la ressource liée.                                      |
| `src`         | Spécifie la source d’un fichier externe (image, script, vidéo, etc.).                                   |
| `defer`       | Retarde l’exécution d’un script JavaScript jusqu’au chargement complet du HTML.                         |
| `type`        | Définit le type d’un élément, souvent pour `<input>` (`text`, `email`, `password`, etc.) ou `<button>`. |
| `value`       | Définit la valeur initiale d’un champ ou d’un bouton.                                                   |

---

| Attribut | Valeur         | Explication                                                        |
| -------- | -------------- | ------------------------------------------------------------------ |
| `type`   | `"number"`     | Crée un champ permettant de saisir uniquement des nombres.         |
| `type`   | `"button"`     | Définit un bouton cliquable sans action automatique de formulaire. |
| `rel`    | `"stylesheet"` | Indique que le fichier lié est une feuille de style CSS.           |

### CSS

| Propriété CSS      | Explication                                                                 |
| ------------------ | --------------------------------------------------------------------------- |
| `color`            | Définit la couleur du texte.                                                |
| `border`           | Définit la bordure d’un élément.                                            |
| `background-color` | Définit la couleur d’arrière-plan.                                          |
| `text-align`       | Positionne le texte horizontalement (`left`, `right`, `center`, `justify`). |
| `text-decoration`  | Ajoute une décoration au texte (souligné, barré, etc.).                     |
| `text-indent`      | Indente la première ligne d’un paragraphe.                                  |
| `letter-spacing`   | Modifie l’espace entre les caractères.                                      |
| `font-size`        | Définit la taille du texte.                                                 |
| `font-style`       | Met le texte en italique ou oblique.                                        |
| `font-weight`      | Définit l’épaisseur du texte (gras, normal…).                               |
| `font-variant`     | Permet par exemple d’utiliser des petites majuscules.                       |
| `font-family`      | Définit la police de caractères.                                            |

border-radius:
box-shadow:

---

| Sélecteur CSS | Explication                           |
| ------------- | ------------------------------------- |
| `h1`          | Sélectionne tous les titres `<h1>`.   |
| `h2`          | Sélectionne tous les titres `<h2>`.   |
| `ul`          | Sélectionne toutes les listes `<ul>`. |

### JS

| Fonction JavaScript         | Explication                                       |
| --------------------------- | ------------------------------------------------- |
| `console.log()`             | Affiche un message dans la console du navigateur. |
| `Number()`                  | Convertit une valeur en nombre.                   |
| `document.getElementById()` | Récupère un élément HTML grâce à son `id`.        |
| `addEventListener()`        | Ajoute un écouteur d’événement à un élément.      |

---

| Événement  | Explication                                               |
| ---------- | --------------------------------------------------------- |
| `"click"`  | Déclenché lorsqu’un utilisateur clique sur un élément.    |
| `"keyup"`  | Déclenché lorsqu’une touche du clavier est relâchée.      |
| `"input"`  | Déclenché lorsqu’un champ de formulaire est modifié.      |
| `"change"` | Déclenché lorsqu’un champ est modifié puis perd le focus. |

---

| Méthode / Propriété           | Explication                                                      |
| ----------------------------- | ---------------------------------------------------------------- |
| `document.getElementById()`   | Récupère un élément HTML grâce à son attribut `id`.              |
| `document.querySelector()`    | Sélectionne le premier élément correspondant à un sélecteur CSS. |
| `document.querySelectorAll()` | Sélectionne tous les éléments correspondant à un sélecteur CSS.  |
| `document.createElement()`    | Crée un nouvel élément HTML en JavaScript.                       |
| `appendChild()`               | Ajoute un élément HTML à l’intérieur d’un autre élément.         |
| `removeChild()`               | Supprime un élément enfant d’un élément parent.                  |
| `addEventListener()`          | Associe un événement à un élément HTML.                          |
| `setAttribute()`              | Ajoute ou modifie un attribut HTML.                              |
| `getAttribute()`              | Récupère la valeur d’un attribut HTML.                           |
| `classList.add()`             | Ajoute une classe CSS à un élément.                              |
| `classList.remove()`          | Supprime une classe CSS d’un élément.                            |
| `classList.contains()`        | Vérifie si une classe CSS est présente sur un élément.           |
| `classList.toggle()`          | Ajoute ou retire une classe CSS selon son état actuel.           |
| `innerHTML`                   | Lit ou modifie le contenu HTML d’un élément.                     |
| `textContent`                 | Lit ou modifie le texte contenu dans un élément.                 |
| `.value`                      | Lit ou modifie la valeur d’un champ de formulaire.               |

| Méthode                             | Explication                                            |
| ----------------------------------- | ------------------------------------------------------ |
| `document.createElement("tagName")` | Crée un nouvel élément HTML non encore attaché au DOM. |
| `elem.prepend(node)`                | Ajoute le nœud comme premier enfant de l’élément.      |
| `elem.append(node)`                 | Ajoute le nœud comme dernier enfant de l’élément.      |
| `elem.before(node)`                 | Insère le nœud juste avant l’élément.                  |
| `elem.after(node)`                  | Insère le nœud juste après l’élément.                  |
| `elem.replaceWith(node)`            | Remplace l’élément par un autre nœud.                  |
| `elem.remove()`                     | Supprime l’élément de la page HTML.                    |

<b>Gestion des classes CSS</b>

| Syntaxe                                 | Explication                                             |
| --------------------------------------- | ------------------------------------------------------- |
| `elem.classList.add("une-classe")`      | Ajoute la classe donnée à l’élément.                    |
| `elem.classList.remove("une-classe")`   | Supprime la classe donnée de l’élément.                 |
| `elem.classList.contains("une-classe")` | Retourne `true` si la classe existe sur l’élément.      |
| `elem.classList.toggle("une-classe")`   | Ajoute la classe si elle n’existe pas, sinon la retire. |

---

<b>Array:</b>

| Syntaxe            | Explication                                                         |
| ------------------ | ------------------------------------------------------------------- |
| `arr[i]`           | Donne l’élément en position `i` dans le tableau (`i` commence à 0). |
| `arr.length`       | Donne le nombre d’éléments du tableau.                              |
| `arr.push(val)`    | Ajoute `val` à la fin du tableau.                                   |
| `arr.pop()`        | Enlève et retourne le dernier élément du tableau.                   |
| `arr.shift()`      | Enlève et retourne le premier élément du tableau.                   |
| `arr.unshift(val)` | Ajoute `val` au début du tableau.                                   |

---

<b>Les variables:</b>

| Syntaxe               | Explication                                                   |
| --------------------- | ------------------------------------------------------------- |
| `const nom = valeur;` | Déclare une constante. Sa valeur ne peut pas être réassignée. |
| `let nom = valeur;`   | Déclare une variable modifiable.                              |
| `=`                   | Opérateur d’affectation.                                      |
| `;`                   | Fin d’instruction en JavaScript.                              |

---

<b>Les Objets:</b>

| Syntaxe                         | Explication                                  |
| ------------------------------- | -------------------------------------------- |
| `objet.propriete`               | Accède à une propriété d’un objet.           |
| `objet.methode()`               | Appelle une méthode d’un objet.              |
| `document`                      | Objet représentant la page HTML.             |
| `document.getElementById("id")` | Recherche un élément HTML grâce à son `id`.  |
| `.value`                        | Contient la valeur d’un champ de formulaire. |

| Partie                   | Rôle                                                |
| ------------------------ | --------------------------------------------------- |
| `document`               | Objet représentant la page web.                     |
| `getElementById("unId")` | Méthode qui cherche un élément ayant l’id `"unId"`. |
| `.value`                 | Propriété contenant la valeur du champ trouvé.      |

---

### TD02

<b>Exercice 1 : Multiplication de deux nombres</b>

Créer une page HTML contenant :

deux champs de saisie pour entrer des nombres ;
un bouton Multiplier ;
un champ affichant le résultat.

Lorsque l’utilisateur clique sur le bouton, le programme doit :

récupérer les deux valeurs saisies ;
les convertir en nombres ;
calculer leur produit ;
afficher le résultat dans le champ prévu.

Le traitement devra être réalisé en JavaScript à l’aide d’une fonction appelée lors du clic sur le bouton.

<b>Exercice 2 : Addition et multiplication</b>

Créer une page HTML contenant :

deux champs de saisie pour entrer des nombres ;
un bouton Calculer ;
un champ pour afficher la somme ;
un champ pour afficher le produit.

Lorsque l’utilisateur clique sur le bouton, le programme doit :

récupérer les deux nombres saisis ;
calculer leur somme ;
calculer leur produit ;
afficher les deux résultats dans les champs correspondants.

Le calcul devra être effectué en JavaScript avec une fonction déclenchée par un écouteur d’événement (addEventListener).

#### HTML

<b>Addition:</b>

```
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Multiplication</title>
  <script src="mult.js" defer></script>
</head>
<body>
  <h1>Multiplication de deux nombres</h1>

  <form>
    <input id="nb1" type="number"> ×
    <input id="nb2" type="number">
    <button id="mult" type="button">=</button>
    <output id="result"></output>
  </form>
</body>
</html>

```

<b>Mulitplication: </b>

```
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Multiplication</title>
  <script src="mult.js" defer></script>
</head>
<body>
  <h1>Multiplication de deux nombres</h1>

  <form>
    <input id="nb1" type="number"> ×
    <input id="nb2" type="number">
    <button id="mult" type="button">=</button>
    <output id="result"></output>
  </form>
</body>
</html>

```

#### CSS

```
h1 {
  font-size: 4em;
  color: red;
  border: solid black;
  background-color: lightyellow;
}

h2 {
  color: darkblue;
  font-size: 2em;
  border-bottom: solid gray;
}

ul {
  color: gray;
}
```

#### JS

<b>Addition:</b>

```

"use strict";

function compute() {
  const nb1 = Number(document.getElementById("nb1").value);
  const nb2 = Number(document.getElementById("nb2").value);

  document.getElementById("result").value = nb1 * nb2;
}

document.getElementById("mult").addEventListener("click", compute);

```

---

<b>Multiplication:</b>

```
"use strict";

function compute() {
  const nb1 = Number(document.getElementById("nb1").value);
  const nb2 = Number(document.getElementById("nb2").value);

  document.getElementById("sum").value = nb1 + nb2;
  document.getElementById("product").value = nb1 * nb2;
}

document.getElementById("calc").addEventListener("click", compute);

```

Remarque:

1 => Pourquoi dire explication le type de nb1 et nb2 en type number, si dans le HTML on ne peut que récupérer ??

        Car ".value" récupère des chaines de caractères, et ceux peu importe le type de la donnée saisi.

Quelle est la différence entre ".value" "innerHTML" et "textContent"?

Les 3 servent à récupérer, ou modifier les informations dans une page HTML, mais ils ne s'utilisent pas dans les mêmes situations.

".value" :

Pour les formulaitres.

Permet d'obtenir la valeur saisie dans les champs des formulaires.

".innerHTML":

Permet de récupérer les éléments HTML et leurs balises.

".textContent":

Uniquement dans les éléments HTML. Il ignore les éléments HTML.

Si tu utilise .value sur autre chose que pour unne balise en dehors du formulaire, JS renvoie undefined. Pcq les seules éléments

qui ont des valeurs sont les balises des formulaires.

---

### TD03

<b>Schéma de structure — index.html :</b>

```
<!DOCTYPE html>
│
└── <html lang="fr">
    │
    ├── <head>
    │   ├── <meta charset="UTF-8">
    │   ├── <meta name="viewport">
    │   └── <title>
    │
    └── <body>
        │
        ├── <header>
        │   └── <h1>
        │
        ├── <nav>
        │   └── <ul>
        │       ├── <li>
        │       │   └── <a href="index.html">
        │       ├── <li>
        │       │   └── <a href="cv.html">
        │       └── <li>
        │           └── <a href="notes.html">
        │
        ├── <main>
        │   ├── <h2>
        │   │
        │   ├── <dl>
        │   │   ├── <dt>
        │   │   │   └── <abbr>
        │   │   ├── <dd>
        │   │   │
        │   │   ├── <dt>
        │   │   │   └── <abbr>
        │   │   ├── <dd>
        │   │   │
        │   │   ├── <dt>
        │   │   │   └── <abbr>
        │   │   └── <dd>
        │   │
        │   └── <p>
        │
        └── <footer>
            └── <p>

```

---

<b>Schéma de structure — index.html:</b>

```
<!DOCTYPE html>
│
└── <html lang="fr">
    │
    ├── <head>
    │   ├── <meta charset="UTF-8">
    │   ├── <meta name="viewport">
    │   └── <title>
    │
    └── <body>
        │
        ├── <header>
        │   └── <h1>
        │
        ├── <nav>
        │   └── <ul>
        │       ├── <li>
        │       │   └── <a href="index.html">
        │       ├── <li>
        │       │   └── <a href="cv.html">
        │       └── <li>
        │           └── <a href="notes.html">
        │
        ├── <main>
        │   ├── <p>
        │   │
        │   ├── <section>
        │   │   ├── <h2>
        │   │   └── <ul>
        │   │       ├── <li>
        │   │       │   └── <a>
        │   │       ├── <li>
        │   │       │   └── <a>
        │   │       └── <li>
        │   │           └── <a>
        │   │
        │   └── <section>
        │       ├── <h2>
        │       ├── <p>
        │       ├── <img>
        │       ├── <img>
        │       └── <img>
        │
        └── <footer>
            └── <p>

```

---

<b> Schéma de structure — cv.html: </b>

```
<!DOCTYPE html>
│
└── <html lang="fr">
    │
    ├── <head>
    │   ├── <meta charset="UTF-8">
    │   ├── <meta name="viewport">
    │   └── <title>
    │
    └── <body>
        │
        ├── <header>
        │   └── <h1>
        │
        ├── <nav>
        │   └── <ul>
        │       ├── <li>
        │       │   └── <a href="index.html">
        │       ├── <li>
        │       │   └── <a href="cv.html">
        │       └── <li>
        │           └── <a href="notes.html">
        │
        ├── <main>
        │   ├── <h2>
        │   │
        │   ├── <img>
        │   │
        │   ├── <ul>
        │   │   ├── <li>
        │   │   └── <li>
        │   │
        │   ├── <section>
        │   │   ├── <h3>
        │   │   └── <ol>
        │   │       ├── <li>
        │   │       ├── <li>
        │   │       └── <li>
        │   │
        │   └── <section>
        │       ├── <h3>
        │       └── <ul>
        │           ├── <li>
        │           ├── <li>
        │           └── <li>
        │
        └── <footer>
            └── <p>
```

### TD04

La structure d’une règle CSS. Une règle contient :

- un sélecteur → ce qu’on veut modifier ;

- des propriétés → ce qu’on change ;

- des valeurs → comment on le change.

Par exemple :

```
h2 {
color: teal;
}

```

Ici :

- h2 est le sélecteur ;

- color est la propriété ;

- teal est la valeur.

Cela signifie : “tous les titres <h2> seront affichés en bleu-vert”.

---

La notion de cascade c'est lorsque plusieurs styles peuvent s’appliquer au même élément :

les styles du navigateur, les styles CSS que tu écris, et parfois des styles ajoutés directement dans une balise.

Il existe une priorité dans l'application du style, d'où "Cascade Style Sheets".

Lors de l'application de plusieurs styles, le navigateur applique la règles la plus forte.

Voici l'ordre de la plus forte à la moins forte:

| Type                        | Exemple                 | Priorité   |
| --------------------------- | ----------------------- | ---------- |
| `!important`                | `color:red !important;` | Très forte |
| Style inline (dans le HTML) | `style="color:red"`     | 1000       |
| ID                          | `#menu`                 | 100        |
| Classe                      | `.btn`                  | 10         |
| Pseudo-classe               | `:hover`, `:focus`      | 10         |
| Attribut                    | `[type="text"]`         | 10         |
| Balise HTML                 | `div`, `p`, `h1`        | 1          |

Petit conseil moderne :

- privilégier les classes

- éviter les IDs pour le style

- éviter !important sauf exception

Remarque:

Si deux règles ont la même priorité, la dernière écrite gagne.

Il y a une différence entre attribut et style inline.

Le sélecteur d’attribut:

´´´
<input type="text">

´´´

´´´
input[type="text"] {
border: 1px solid blue;
}

´´´

Le style inline:

´´´

<p style="color:red;">Bonjour</p>

´´´
<b>In line et block :</b>

Les balises <span> et <div>. Elles servent à regrouper du contenu afin d’y appliquer un style.

- <span> est une balise “inline” : elle reste dans la ligne du texte.

- <div> est une balise “bloc” : elle prend toute la largeur disponible et passe à la ligne.

C’est une différence essentielle en HTML/CSS. Les éléments inline se placent les uns à côté des autres, alors que les éléments bloc se

placent les uns en dessous des autres.

<b>Les outils du développeur du navigateur:</b>

Ils permettent d’inspecter le HTML et le CSS d’une page, de tester rapidement des propriétés CSS, de voir quels styles sont appliqués et

d’identifier plus facilement les erreurs. C’est un outil indispensable en développement web.

---

### TD05

```
h1 {
    width: 50%;
    margin-left: auto;   // Quand un élément possède une largeur plus petite que l’espace disponible,
    margin-right: auto;  // le navigateur répartit l’espace restant entre les deux marges.
    text-align: center; //  centre le texte qui est  aligné à gauche du <h1> du rectangle
    background-color: lightgreen;
}

```

```
margin-left: auto;
margin-right: auto;

```

---

<b>Font-family:</b>
La propriété font-family sert à choisir la police d’écriture utilisée pour afficher le texte d’une page.

Par exemple :

```
font-family: Arial, Helvetica, sans-serif;

```

Ici, plusieurs polices sont écrites l’une après l’autre, séparées par des virgules.

Le navigateur va essayer de les utiliser dans l’ordre.

Il commence par chercher la police Arial sur l’ordinateur de l’utilisateur.

Si Arial existe, elle sera utilisée.

Sinon, il essaie Helvetica.

Si Helvetica n’existe pas non plus, il utilise une police générique sans-serif.

Le mot sans-serif ne désigne pas une police précise.
C’est une famille de polices.

Les polices sans serif sont des polices sans petits traits décoratifs au bout des lettres.

Exemple :

- avec empattement (serif) → Times New Roman ;

- sans empattement (sans-serif) → Arial.

Pourquoi écrire plusieurs polices ?

Parce qu’on ne sait pas quelles polices sont installées sur l’ordinateur de l’utilisateur.

Par exemple :

- Windows possède certaines polices ;

- macOS en possède d’autres ;

- Linux aussi.

Donc on écrit plusieurs possibilités pour éviter qu’un texte s’affiche mal.

Cependant, parfois on veut absolument utiliser une police précise pour avoir exactement le style désiré.

Dans ce cas, on peut demander au navigateur de télécharger cette police depuis Internet.

C’est ce que permet Google Fonts.

Le site :

- Google Fonts

- contient énormément de polices gratuites.

Quand on choisit une police, Google fournit un code comme :

```
@import url('https://fonts.googleapis.com/css2?family=Delius&display=swap');

```

Cette ligne demande au navigateur de télécharger automatiquement la police Delius.

On place cette ligne tout en haut du fichier CSS.

Ensuite, on peut utiliser la police :

```
h1 {
    font-family: "Delius", cursive;
}

```

Cela signifie :

- utiliser la police Delius ;

- si elle ne peut pas être chargée, utiliser une police de type cursive.

Le téléchargement d’une police permet d’avoir exactement le même rendu chez tous les utilisateurs, mais cela peut ralentir un peu le

chargement de la page puisque le navigateur doit récupérer la police sur Internet avant de l’afficher.

---

### TD06

<b>Fonction compter:</b>

La page offre un champ de saisie numérique. Lorsqu’on clique sur un bouton, un message apparaitavec les nombres de 1 à n (où n est le

nombre saisi). Si le nombre saisi est inférieur à 1, on affiche plutôt un message d’erreur.

```
<input id="countNumber" type="number">

<button id="countBtn">Compter</button>

<p id="countResult"></p>

```

1 - Cela active le mode strict de JavaScript.

2 - La fonction count() sera exécutée quand l’utilisateur cliquera sur un bouton.

3 - Cette partie récupère la valeur entrée dans un champ HTML ayant l’identifiant : id="countNumber". Elle est sauvé dans n.

4 - On crée une variable vide qui servira à stocker le résultat final.

5 - Si le nombre est inférieur à 1, le programme affiche "Erreur".

6 - Sinon :

7 - Sert à compter.

```
Exemple si n = 5 :

"1 "
"1 2 "
"1 2 3 "
"1 2 3 4 "
"1 2 3 4 5 "

```

8 - Cette ligne affiche le résultat dans un élément HTML ayant :

```
id="countResult"

```

- .textContent remplace le texte de cet élément.

9 - Quand l’utilisateur clique sur le bouton, exécute la fonction count().

```
"use strict";                                               // 1

function count() {                                          // 2
    const n = Number(
        document.getElementById("countNumber").value        // 3
    );

    let result = "";                                       // 4

    if (n < 1) {                                           // 5
        result = "Erreur";
    } else {                                               // 6

        for (let i = 1 ; i <= n ; i++) {                   // 7
            result += i + " ";
        }

    }

    document.getElementById("countResult").textContent =      // 8
        result;
}

document                                                       // 9
    .getElementById("countBtn")
    .addEventListener("click", count);

```

---

<b>Fonction shuffle:</b>

La page offre un champ de saisie numérique. Lorsqu’on clique sur un bouton, un code JavaScript
va :

1. Créer un tableau avec les nombres de 1 à n (où n est le nombre saisi).

2. Mélanger ce tableau.

3. Afficher à l’écran les nombres mélangés en utilisant le for-of.

1 -

```
<input id="shuffleNumber" type="number">

<button id="shuffleBtn">Mélanger</button>

<p id="shuffleResult"></p>

```

1- Cette fonction reçoit un tableau a. Son rôle est de mélanger les éléments de ce tableau.

2- Cette boucle commence à la dernière position du tableau et remonte vers le début.

3- À chaque tour, on choisit une position au hasard :

4- Math.random() donne un nombre aléatoire entre 0 et 1. On le multiplie par i + 1, puis Math.floor enlève les décimales.

5- Cette ligne échange les valeurs des positions i et j dans le tableau grâce à la décomposition de tableau (destructuring).

        Le tableau existe déjà. Cette ligne sert uniquement à échanger deux valeurs dans le tableau.

```
        [a[i], a[j]] = [a[j], a[i]];
```

        Par exemple, imaginons :

```
        a = [1, 2, 3, 4]i = 3j = 1

```

        Alors :

```
        a[i] = 4a[j] = 2

```

        La ligne devient :

```
        [a[3], a[1]] = [a[1], a[3]];
```

        JavaScript fait d’abord le tableau temporaire :

```
        [2, 4]
```

        Puis il affecte :

```
        a[3] = 2a[1] = 4
```

        Le tableau final devient :

```
        [1, 4, 3, 2]
```

        Donc :


        aucun nouvel élément n’est ajouté,

        push() n’est pas utilisé ici,

        on échange seulement deux positions déjà présentes dans le tableau.

        Sans cette syntaxe moderne, on écrirait :

```
        const temp = a[i];

        a[i] = a[j];a[j] = temp;

```

        Les deux versions font exactement la même chose.

6- Cette fonction est exécutée quand on clique sur le bouton. Elle sert à créer puis mélanger les nombres.

7- On récupère la valeur entrée dans le champ HTML ayant l’identifiant "shuffleNumber", puis on la transforme en nombre avec Number().

8- On crée un tableau vide nommé arr.

9- Cette boucle ajoute tous les nombres de 1 jusqu’à n dans le tableau.

10- push(i) ajoute le nombre i à la fin du tableau.

11- On appelle la fonction shuffle(arr) pour mélanger les éléments du tableau.

12- On crée une chaîne de caractères vide qui servira à afficher le résultat.

13- Cette boucle parcourt chaque élément du tableau mélangé.

14- Chaque nombre est ajouté dans la chaîne result avec un espace après.

15- On récupère l’élément HTML ayant l’identifiant "shuffleResult".

16- Le texte affiché dans cet élément devient le contenu de result.

17- Quand l’utilisateur clique sur le bouton "shuffleBtn", la fonction mix est exécutée.

```
"use strict";

function shuffle(a) {                              // 1

    for (let i = a.length - 1 ; i > 0 ; i--) {     // 2

        const j = Math.floor(                      // 3
            Math.random() * (i + 1)                // 4
        );

        [a[i], a[j]] = [a[j], a[i]];              // 5
    }
}

function mix() {                                 // 6

    const n = Number(
        document.getElementById("shuffleNumber").value   //7
    );

    const arr = [];                                     //8

    for (let i = 1 ; i <= n ; i++) {                    //9
        arr.push(i);                                   // 10
    }

    shuffle(arr);                                      // 11

    let result = "";                                  //12

    for (const elem of arr) {                          //13
        result += elem + " ";                          //14
    }

    document.getElementById("shuffleResult").textContent =     //15
        result;                                              //16
}

document
    .getElementById("shuffleBtn")
    .addEventListener("click", mix);                              //17

```

---

<b>On /Off:</b>

Ajoutez deux boutons à une page. Le bouton On est actif et le bouton Off ne l’est pas. Lorsqu’on clique sur le bouton actif, il devient

inactif et le bouton inactif devient actif.

<b>Réponse:</b>

1- Cette fonction est exécutée quand on clique sur le bouton “On”. Elle sert à désactiver ce bouton et activer l’autre.

2- On récupère l’élément HTML ayant l’identifiant "ex8BtnOn" et on le stocke dans la variable btnOn.

3- On récupère l’élément HTML ayant l’identifiant "ex8BtnOff" et on le stocke dans la variable btnOff.

4- btnOn.disabled = true désactive le bouton “On”. L’utilisateur ne peut plus cliquer dessus.

5- btnOff.disabled = false active le bouton “Off”. L’utilisateur peut cliquer dessus.

6- On récupère de nouveau le bouton "ex8BtnOn" dans la variable btnOn.

7- On récupère le bouton "ex8BtnOff" dans la variable btnOff.

8- btnOn.disabled = false réactive le bouton “On”.

9- btnOff.disabled = true désactive le bouton “Off”.

10- Quand l’utilisateur clique sur le bouton "ex8BtnOn", la fonction activerOff est exécutée.

11- Quand l’utilisateur clique sur le bouton "ex8BtnOff", la fonction activerOn est exécutée.

index.html

```

<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Exercice 8</title>
  <script src="code.js" defer></script>
</head>
<body>
  <h1>Exercice 8 - On/Off</h1>

  <button id="ex8BtnOn">On</button>
  <button id="ex8BtnOff" disabled>Off</button>
</body>
</html>

```

code.js

```
"use strict";

function activerOff() {                                       //1

  const btnOn = document.getElementById("ex8BtnOn");           //2

  const btnOff = document.getElementById("ex8BtnOff");        // 3

  btnOn.disabled = true;                                     //4

  btnOff.disabled = false;                                   //5
}

function activerOn() {
  const btnOn = document.getElementById("ex8BtnOn");          //6

  const btnOff = document.getElementById("ex8BtnOff");      //7


  btnOn.disabled = false;                                  //8

  btnOff.disabled = true;                                  // 9
}

document.getElementById("ex8BtnOn").addEventListener("click", activerOff); //10

document.getElementById("ex8BtnOff").addEventListener("click", activerOn); //11

```

---

### TD07

<b>Evénements:</b>

Un événement peut être une action effectuée par l’utilisateur (ex : clic sur un bouton) ou par le navigateur.

Pour associer un code à un événement survenant sur un élément :

elem.addEventListener("nomEvent", uneFonction)

Citons quelques événements courants :

. click : clic avec la souris sur un élément.

. keyUp : une touche a été enfoncée puis relâchée.

. input : un élément de formulaire a été modifié.

. change : un élément de formulaire a été modifié et a perdu le focus.

La fonction qui gère un événement reçoit toujours comme premier paramètre un objet décrivant cet évé-
nement.

Il est d’usage de l’appeler event (ou parfois simplement e).

Il contient notamment le propriété :

. target : l’élément qui a déclenché l’événement courant.

---

<b>Séparer les pairs et les impairs:</b>

Voici un exercice un peu plus difficile que les autres. Dans le développement, à chaque fois que votre programme retourne une mauvaise

réponse, on vous demande d’utiliser le debugger afin de comprendre et corriger le problème.

- Écrivez une fonction qui reçoit en paramètre un tableau de nombres triés et retourne un nouveau tableau avec tous les nombres pairs en

ordre décroissant suivis des nombres impairs en ordre croissant. Par exemple avec le paramètre [1, 2, 3, 4, 7, 8, 9, 10, 23, 24, 31], la

fonction retourne le tableau [24, 10, 8, 4, 2, 1, 3, 7, 9, 23, 31].

- Modifiez la fonction afin qu’elle modifie le tableau reçu en paramètre plutôt que d’en créer un autre.

<b>Réponse:</b>

1- Cette fonction reçoit un tableau de nombres et retourne un nouveau tableau avec les nombres pairs en ordre décroissant puis les nombres impairs en ordre croissant.

2- On crée un tableau vide nommé pairs qui contiendra les nombres pairs.

3- On crée un tableau vide nommé impairs qui contiendra les nombres impairs.

4- Cette boucle parcourt chaque nombre du tableau numbers.

5- Cette condition vérifie si le nombre n est pair grâce à n % 2 === 0.

6- unshift(n) ajoute le nombre au début du tableau pairs. Cela permet d’obtenir les nombres pairs en ordre décroissant.

7- push(n) ajoute le nombre à la fin du tableau impairs. Les nombres impairs restent donc en ordre croissant.

8- concat() fusionne les deux tableaux : d’abord les pairs puis les impairs.

9- console.log() affiche dans la console le résultat retourné par la fonction separate().

```
"use strict";

function separate(numbers) { //1

    const pairs = [];       //2
    const impairs = [];     //3

    for (const n of numbers) {  //4

        if (n % 2 === 0) { //5
            pairs.unshift(n); //6
        } else {
            impairs.push(n);   //7
        }
    }

    return pairs.concat(impairs);  //8
}

console.log(                                             //9
    separate([1, 2, 3, 4, 7, 8, 9, 10, 23, 24, 31])
);

```

---

<b>Une liste de tâches:</b>

Écrivez une page HTML contenant plusieurs boutons. Lorsque l’utilisateur clique sur un bouton, le texte de ce bouton doit être affiché dans

la console. Pour résoudre cet exercice, vous ne pouvez écrire qu’une seule fonction qui va gérer le clic sur n’importe quel bouton. (Vous

pouvez appeler addEventListener une fois pour chaque bouton, mais il faut utiliser la même fonction dans chacun.)

<b>Réponse:</b>

1- Cette fonction est exécutée quand on clique sur une tâche.

2- toggle("done") ajoute ou enlève la classe "done" pour barrer la tâche.

3- Cette fonction ajoute une nouvelle tâche dans la liste.

4- On crée un nouvel élément <li>.

5- On met le texte de la tâche dans le <li>.

6- On ajoute l’événement click sur la tâche.

7- On ajoute la tâche dans la liste HTML.

8- Cette fonction ajoute la tâche écrite dans le champ texte.

9- On récupère le champ de saisie.

10- On récupère le texte écrit par l’utilisateur.

11- On vérifie que le champ n’est pas vide.

12- On ajoute la nouvelle tâche.

13- On vide le champ texte après l’ajout.

14- Cette fonction supprime les tâches terminées.

15- On récupère toutes les tâches de la liste.

16- Cette boucle parcourt chaque tâche.

17- On vérifie si la tâche possède la classe "done".

18- On supprime la tâche.

19- Quand on clique sur le bouton "Ajouter", la fonction addNew est exécutée.

20- Quand on clique sur le bouton "Supprimer les tâches terminées", la fonction deleteDone est exécutée.

```
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Todo List</title>

    <link rel="stylesheet" href="todo.css">

    <script src="todo.js" defer></script>
</head>
<body>

    <h1>Mes tâches</h1>

    <ul id="todo-list">
    </ul>

    <input
        type="text"
        id="todo-input"
        placeholder="Nouvelle tâche..."
    >

    <button id="add-btn">
        Ajouter
    </button>

    <br>

    <button id="delete-btn">
        Supprimer les tâches terminées
    </button>

</body>
</html>

```

```
.done {
    text-decoration: line-through;
}

```

```
"use strict";

function toggleTodo(event) {                              //1
    event.target.classList.toggle("done");                //2
}

function add(todo) {                                      //3

    const li = document.createElement("li");              //4

    li.textContent = todo;                                //5

    li.addEventListener("click", toggleTodo);             //6

    document
        .getElementById("todo-list")
        .append(li);                                      //7
}

function addNew() {                                       //8

    const input = document.getElementById("todo-input");  //9

    const text = input.value;                             //10

    if (text !== "") {                                    //11
        add(text);                                        //12
    }

    input.value = "";                                     //13
}

function deleteDone() {                                   //14

    const todos =
        document.querySelectorAll("#todo-list li");       //15

    for (const todo of todos) {                           //16

        if (todo.classList.contains("done")) {            //17
            todo.remove();                                //18
        }
    }
}

document
    .getElementById("add-btn")
    .addEventListener("click", addNew);                   //19

document
    .getElementById("delete-btn")
    .addEventListener("click", deleteDone);               //20

```

---

<b>Afficher et cacher:</b>

Imaginons qu’on veuille ajouter une aide à notre page de liste de tâches. Cette aide doit apparaitre si on clique sur un bouton et

disparaitre si on re-clique sur ce bouton. Plutôt que de systématiquement ajouter puis supprimer l’aide, on peut demander à la montrer puis

la cacher sans la détruire.

<b>Réponse:</b>

1- Cette fonction affiche ou cache l’aide.

2- On récupère le texte de l’aide.

3- On récupère le bouton.

4- toggle("hidden") ajoute ou enlève la classe "hidden".

5- On vérifie si l’aide est cachée.

6- Si l’aide est cachée, le bouton affiche "Aide".

7- Sinon, le bouton affiche "Cacher".

8- Quand on clique sur le bouton, la fonction toggleHelp est exécutée.

```
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Aide</title>

    <link rel="stylesheet" href="style.css">

    <script src="script.js" defer></script>
</head>
<body>

    <button id="help-btn">
        Aide
    </button>

    <div id="help" class="hidden">
        Écrire une aide ici.
    </div>

</body>
</html>

```

```
.hidden {
    display: none;
}
```

```
"use strict";

function toggleHelp() {                                 //1

    const help = document.getElementById("help");      //2

    const btn = document.getElementById("help-btn");   //3

    help.classList.toggle("hidden");                   //4

    if (help.classList.contains("hidden")) {           //5

        btn.textContent = "Aide";                      //6

    } else {

        btn.textContent = "Cacher";                    //7
    }
}

document
    .getElementById("help-btn")
    .addEventListener("click", toggleHelp);            //8

```

---

<b>Un composant réutilisable:</b>

Il est probable qu’on rencontrera d’autres situations où il sera utile d’avoir un bouton pour afficher ou cacher du texte. Il serait

possible de copier-coller ou adapter le code écrit pour l’exercice précédent mais cette approche risque de prendre du temps et de générer

de nombreuses erreurs avant d’obtenir une copie adaptée qui fonctionne correctement.

Le but de cet exercice est d’écrire un code qui sera facilement adaptable.

Pour le code HTML, on va supposer, en toute généralité qu’un texte qui peut se cacher a la

structure suivante.

.html

```
<div class="show-hide">

<button class="show-action">Aide</button>

<button class="hide-action">Cacher</button>

<div class="show-hide-content">

```

Le contenu ici

```
</div>

</div>

```

2. Écrivez dans un fichier showHide.js une fonction qui :

(a) Cherche dans le document tous les éléments qui ont la classe show-hide.

(b) Pour chacun de ces éléments :

i. Cache les éléments de classe show-hide-content et hide-action qui s’y trouvent.

N’oubliez pas, c’est plus propre de le faire via une classe qui cache ( display: none ).

ii. Associe une fonction show(event) au clic de l’élément de classe show-action qui

s’y trouve. Cette fonction montre le contenu, cache le bouton de classe show-action et montre le bouton avec la classe hide-action.

iii. Associe une fonction hide(event) au clic de l’élément de classe hide-action qui s’y trouve. Cette fonction cache le contenu ainsi que

le bouton de classe hide-action et montre le bouton avec la classe show-action.

Testez ce que vous codez avec une page qui contient 2 éléments de classe show-hide.

<b>Réponse:</b>

1- Fonction appelée quand on clique sur le bouton pour afficher.

2- On récupère le bloc parent .show-hide.

3- On récupère le contenu à afficher.

4- On récupère le bouton "Aide".

5- On récupère le bouton "Cacher".

6- On affiche le contenu.

7- On cache le bouton "Aide".

8- On affiche le bouton "Cacher".

9- Fonction appelée quand on clique sur "Cacher".

10- On récupère le bloc parent.

11- On récupère le contenu.

12- On récupère le bouton pour afficher.

13- On récupère le bouton pour cacher.

14- On cache le contenu.

15- On cache le bouton "Cacher".

16- On réaffiche le bouton "Aide".

17- On récupère tous les blocs réutilisables.

18- On parcourt chaque bloc.

19- On récupère son contenu.

20- On récupère son bouton "Cacher".

21- On récupère son bouton d’affichage.

22- Au début, on cache le contenu.

23- Au début, on cache aussi le bouton "Cacher".

24- On associe la fonction show au bouton d’affichage.

25- On associe la fonction hide au bouton "Cacher".

```
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Show Hide</title>

    <link rel="stylesheet" href="showHide.css">
    <script src="showHide.js" defer></script>
</head>
<body>

    <div class="show-hide">
        <button class="show-action">Aide</button>
        <button class="hide-action">Cacher</button>

        <div class="show-hide-content">
            Le contenu ici
        </div>
    </div>

    <div class="show-hide">
        <button class="show-action">Infos</button>
        <button class="hide-action">Cacher</button>

        <div class="show-hide-content">
            Deuxième contenu ici
        </div>
    </div>

</body>
</html>

```

```
.hidden {
    display: none;
}

```

```
"use strict";

function show(event) {                                           //1
    const block = event.target.parentNode;                       //2

    const content = block.querySelector(".show-hide-content");   //3
    const showBtn = block.querySelector(".show-action");         //4
    const hideBtn = block.querySelector(".hide-action");         //5

    content.classList.remove("hidden");                          //6
    showBtn.classList.add("hidden");                             //7
    hideBtn.classList.remove("hidden");                          //8
}

function hide(event) {                                           //9
    const block = event.target.parentNode;                       //10

    const content = block.querySelector(".show-hide-content");   //11
    const showBtn = block.querySelector(".show-action");         //12
    const hideBtn = block.querySelector(".hide-action");         //13

    content.classList.add("hidden");                             //14
    hideBtn.classList.add("hidden");                             //15
    showBtn.classList.remove("hidden");                          //16
}

const blocks = document.querySelectorAll(".show-hide");          //17

for (const block of blocks) {                                    //18
    const content = block.querySelector(".show-hide-content");   //19
    const hideBtn = block.querySelector(".hide-action");         //20
    const showBtn = block.querySelector(".show-action");         //21

    content.classList.add("hidden");                             //22
    hideBtn.classList.add("hidden");                             //23

    showBtn.addEventListener("click", show);                     //24
    hideBtn.addEventListener("click", hide);                     //25
}

```
