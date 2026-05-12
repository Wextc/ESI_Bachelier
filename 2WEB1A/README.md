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

| Propriété CSS      | Explication                        |
| ------------------ | ---------------------------------- |
| `font-size`        | Définit la taille du texte.        |
| `color`            | Définit la couleur du texte.       |
| `border`           | Définit la bordure d’un élément.   |
| `background-color` | Définit la couleur d’arrière-plan. |

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

| Événement | Explication                                            |
| --------- | ------------------------------------------------------ |
| `"click"` | Déclenché lorsqu’un utilisateur clique sur un élément. |

---

| Méthode / Propriété           | Explication                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------------------- |
| `document.getElementById()`   | Permet de récupérer un élément HTML grâce à son attribut `id`.                                 |
| `document.querySelector()`    | Sélectionne le premier élément HTML correspondant à un sélecteur CSS.                          |
| `document.querySelectorAll()` | Sélectionne tous les éléments correspondant à un sélecteur CSS.                                |
| `document.createElement()`    | Crée un nouvel élément HTML en JavaScript.                                                     |
| `appendChild()`               | Ajoute un élément HTML à l’intérieur d’un autre élément.                                       |
| `removeChild()`               | Supprime un élément enfant d’un élément parent.                                                |
| `addEventListener()`          | Ajoute un événement à un élément HTML pour exécuter une fonction lorsqu’une action se produit. |
| `setAttribute()`              | Ajoute ou modifie un attribut HTML d’un élément.                                               |
| `getAttribute()`              | Récupère la valeur d’un attribut HTML.                                                         |
| `classList.add()`             | Ajoute une classe CSS à un élément HTML.                                                       |
| `classList.remove()`          | Supprime une classe CSS d’un élément HTML.                                                     |
| `innerHTML`                   | Lit ou modifie le contenu HTML à l’intérieur d’un élément.                                     |
| `textContent`                 | Lit ou modifie le texte contenu dans un élément HTML.                                          |
| `.value`                      | Lit ou modifie la valeur d’un champ de formulaire (`input`, `output`, etc.).                   |

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

Attribut (sélecteur d’attribut CSS):

Ici on parle d’un sélecteur CSS qui cible un attribut HTML.

En CSS, un style inline et un sélecteur d’attribut sont deux choses différentes, même si tous les deux utilisent des attributs HTML.

Le style inline correspond à l’attribut spécial style="" écrit directement dans une balise HTML. Par exemple :

<p style="color:red;">Bonjour</p>

Ici, le CSS est appliqué directement sur l’élément. C’est pour cela que ce type de style a une très grande priorité en CSS.
Le sélecteur d’attribut, lui, est utilisé dans un fichier CSS pour cibler des éléments selon leurs attributs HTML. Par exemple :
<input type="text">
et en CSS :
input[type="text"] { border: 1px solid blue;}
Dans ce cas, [type="text"] ne contient pas du CSS directement. Il sert seulement à sélectionner les éléments <input> qui possèdent l’attribut type="text".
Donc :

style="" applique directement du style à l’élément ;

[type="text"] sert à sélectionner des éléments dans une règle CSS.

C’est pour cela qu’ils n’ont pas la même priorité :

le style inline est très fort ;

le sélecteur d’attribut a la même priorité qu’une classe CSS.

---
