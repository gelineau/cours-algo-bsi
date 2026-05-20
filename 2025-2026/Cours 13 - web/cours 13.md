# Cours 13 - Introduction à Flask

Règles du jeu :
- Bien suivre les étapes dans l'ordre et lire les instructions attentivement.
- Contrairement à ce qu'on fait d'habitude, certaines étapes sont marquées "**IA**". Vous pourrez utiliser une IA 
(exemple Claude) pour vous aider à les faire. Par contre vous devrez prendre le temps de comprendre ce qu'il vous propose. 
- Pour les autres étapes, vous faites le travail vous-même, sans IA (sinon vous n'apprendrez rien !).

## 1. Installation d'un premier serveur Flask

### 1.1. Copier le répertoire fourni
Commencez par copier le répertoire **"fourni avant le cours"** dans votre espace de travail. Ce répertoire contient 
tous les fichiers nécessaires pour démarrer.

### 1.2. Installer Flask
```bash
pip install flask 
```
(de préférence dans un environnement virtuel)

### 1.3. Lancer l'application
Exécutez le fichier `controller.py` :

Vous devriez voir un message comme :
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### 1.4. Ouvrir votre navigateur
Ouvrez votre navigateur web et accédez à l'adresse suivante :

```
http://localhost:5000
```

Vous devriez voir une page HTML simple s'afficher !

N.B. :
- Flask s'exécute en **mode debug**, ce qui signifie que toute modification que vous faites au code sera automatiquement rechargée - il suffit de rafraîchir la page du navigateur.
- Pour arrêter le serveur, appuyez sur **Ctrl+C** dans le terminal.

## 2. Étape 2 : deuxième page et CSS

### 2.1. Modifier la page d'index

Modifiez le template `templates/index.html` pour ajouter un peu de texte à la page d'accueil.

### 2.2. Ajouter une nouvelle page `/hello`

Ajoutez une nouvelle page accessible à l'adresse `/hello` :

- créez une nouvelle controller function dans `controller.py`
- créez un nouveau template `templates/hello.html`.

### 2.3. Ajouter un lien depuis la page d'accueil

Ajoutez dans la page d'accueil un hyperlien permettant d'aller vers la page `/hello`.

### 2.4. Ajouter un fichier CSS statique

Ajoutez un répertoire `static` contenant un fichier `style.css` avec le contenu suivant :

```css
body {
	background-color: #f0f0f0;
}
```

### 2.5. Référencer le fichier CSS dans `hello.html`

Référencez ce fichier CSS dans le template `hello.html`. Pour cela, ajoutez la ligne suivante dans la section `<head>` de votre template :

```html
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
```

## 3. Étape 3 : rendre la page plus jolie

### 3.1. Ajouter une image (**IA**)

- Ajoutez une image dans le dossier `static`.
- Affichez-la sur la page hello (`templates/hello.html`).

### 3.2. Embellir le CSS (**IA**)

- Demandez à une IA de proposer un `style.css` plus joli.
- Intégrez sa proposition, puis adaptez-la si besoin.

## 4. Étape 4 : tenir compte des paramètres d'URL

### 4.1. Créer un contrôleur qui reçoit un âge

Dans cette étape, vous allez créer une nouvelle `controller function` qui reçoit un âge dans l'URL.

#### Comment déclarer la fonction

- Dans `controller.py`, ajoutez une route avec un paramètre d'URL.

```python
@app.route('/greet/<int:age>', methods=['GET'])
def greet_controller(age: int) -> str:
	...
```

- Si `age` est plus petit que 18, la fonction doit renvoyer `render_template('child.html')`.
- Sinon, elle doit renvoyer `render_template('adult.html')`.


#### Tester dans le navigateur

Testez les deux cas dans votre navigateur :

- par exemple avec `http://localhost:5000/greet/12`
- puis avec `http://localhost:5000/greet/18`

Vous devez vérifier que la bonne page s'affiche dans chaque cas.

### 4.2. Afficher l'âge dans le template

Pour l'instant, la page s'affiche correctement mais elle ne montre pas l'âge reçu. Vous allez passer la valeur de `age` au template.

#### Modifier le controller

Dans `render_template`, passez `age` en argument nommé :

```python
render_template('child.html', age=age)
# ou
render_template('adult.html', age=age)
```

#### Modifier les templates

Dans `child.html` et `adult.html`, affichez l'âge avec Jinja2 :

```html
<p>Vous avez {{ age }} ans.</p>
```

#### Tester dans le navigateur

Rechargez `http://localhost:5000/greet/12` et `http://localhost:5000/greet/18` : l'âge doit maintenant apparaître sur la page.

---

## 5. Étape 5 : modèle et formulaire de saisie

### 5.1. Créer un modèle et afficher une liste d'utilisateurs

#### Créer `model.py`

Créez un fichier `model.py` à la racine du projet. Ce fichier contiendra les données de l'application.

- Déclarez une variable globale `users` qui contient une liste de 3 noms d'utilisateurs (des strings).
- Ajoutez une fonction `get_users()` qui retourne cette liste.


#### Créer le controller et le template

Dans `controller.py`, importez `model` en haut du fichier, puis créez une nouvelle controller function pour la route `/users` :

- Elle appelle `model.get_users()` pour récupérer la liste.
- Elle passe cette liste au template avec `render_template('users.html', users=users)`.

Dans `templates/users.html`, affichez les utilisateurs dans un tableau HTML avec une boucle Jinja2 :

```html
<table>
{% for user in users %}
<tr><td>{{ user }}</td></tr>
{% endfor %}
</table>
```

Testez en ouvrant `http://localhost:5000/users`.

### 5.2. Amélioration de la présentation (**IA**)

Vous pouvez rendre le tableau plus joli, en ajoutant un header, des bordures ... En 
modifiant le CSS et/ou le template.

### 5.3. Créer un formulaire de saisie

#### La page `user_form` 

Créez une controller function `/user_form` dans `controller.py` qui affiche un 
template `user_form.html`.
```
<form action="{{ url_for('create_user_controller') }}" method="POST">
    <input type="text" name="username">
    <button type="submit">Valider</button>
</form>
```

#### La route `create_user`

Créez une route `/create_user` qui accepte uniquement la méthode `POST`.

Pour récupérer la valeur saisie dans le formulaire, utilisez :

```python
from flask import request
username = request.form['username']
```

Pour l'instant, affichez simplement le nom de l'utilisateur dans un template `create_user.html`.

Testez en allant sur `http://localhost:5000/user_form`, en saisissant un nom et en validant.

---

### 5.4. Ajouter l'utilisateur dans le modèle

#### Modifier `model.py`

Ajoutez une fonction `create_user(username: str)` qui ajoute le nom dans la liste `users` :

#### Modifier le controller

Dans `create_user_controller`, appelez `model.create_user(username)` avant de rendre le template.

Le template `create_user.html` doit afficher un message de confirmation pour dire que l'utilisateur
a été créé.
Et proposer un lien vers la page `/users`.

Testez les deux étapes : ajoutez un utilisateur via le formulaire, puis vérifiez qu'il apparaît dans `/users`.

### 5.5. Amélioration de la présentation (**IA**)

Vous pouvez rendre les différentes pages plus jolies. En 
modifiant le CSS et/ou le template.


## 6. Étape 6 : ajouter des champs aux utilisateurs

### 6.1. Ajouter `email` et `password` aux utilisateurs

Dans cette étape, un utilisateur n'est plus une simple string. C'est maintenant une liste de 3 valeurs :
username, email, password

#### Modifier `model.py`

- `users` doit devenir une liste de listes.
- Exemple :

```python
users = [
    ['bob', 'bob.doe@orange.fr', 'my_password'],
    ['alice', 'alice.smith@gmail.com', 'azerty123!'],
    ['charlie', 'charlie.dupont@yahoo.fr', 'pass-word_42'],
]
```

- `get_users()` continue de renvoyer `users`.
- `create_user` doit maintenant recevoir 3 paramètres : username, email, password

#### Modifier `user_form.html`

Ajoutez 3 champs de saisie :

```html
<input type="text" name="username">
<input type="text" name="email">
<input type="text" name="password">
```

#### Modifier `controller.py`

Dans `create_user_controller`, récupérez les 3 champs du formulaire :

```python
username = request.form['username']
email = request.form['email']
password = request.form['password']
```


#### Modifier `users.html`

Le tableau doit afficher 3 colonnes :
- `Username`
- `Email`
- `Password`

Et dans la boucle `{% for ...}`, affichez les 3 valeurs de chaque utilisateur.

#### Testez : 
ajoutez un utilisateur via `/user_form`, puis vérifiez son apparition dans `/users`.

### 6.2. (IA) Cacher les caractères du mot de passe

Demandez à une IA comment déclarer le champ mot de passe pour masquer les caractères saisis.

### 6.3. (IA) Valider email et password en JavaScript

- Créez `static/user.js`.
- Référencez ce fichier dans `user_form.html` avec une balise `<script>`.
- Demandez à une IA du JavaScript qui :
  - affiche un message d'erreur si l'email n'est pas valide,
  - bloque l'envoi du formulaire tant que l'email n'est pas valide,
  - affiche un message d'erreur si le mot de passe ne respecte pas des contraintes,
  - bloque aussi l'envoi tant que les contraintes mot de passe ne sont pas respectées.


Testez dans le navigateur :
- un email invalide (doit bloquer),
- un mot de passe trop faible (doit bloquer),
- puis un formulaire valide (doit envoyer).

## 7. Étape 7 : Utiliser une base de données SQLite

Dans cette étape, on garde les mêmes pages (`/users`, `/user_form`, `/create_user`) mais on remplace 
la liste Python dans model.py par une base de données SQLite.

### 7.1. (IA) Créer un modèle SQLite

Demandez à une IA de modifier `model.py` avec :
- une connexion SQLite (`sqlite3`),
- du code d'initialisation **directement au niveau du module **, à la place de la déclaration de users
(quand on importe `model`, la table se crée automatiquement),
- modifier la fonction `get_users()` pour qu'elle lise les utilisateurs dans la base de données,
- modifier la fonction `create_user(username, email, password)` pour qu'elle insère un utilisateur
dans la base de données.

Gardez les mêmes signatures de fonctions qu'à l'étape 6, afin de ne pas avoir besoin de modifier le
controller.

### 7.2. Tester dans le navigateur

- Ouvrez `/users` (les utilisateurs doivent s'afficher),
- ajoutez un utilisateur via `/user_form`,
- revenez sur `/users` pour vérifier qu'il est bien enregistré.

Relancez le serveur Flask : l'utilisateur ajouté doit rester présent (contrairement à la liste en mémoire).

### 7.3. (IA) Injection SQL
Si l'IA a bien travaillé, elle a utilisé des requêtes paramétrées pour éviter les injections SQL. 
Demandez-lui plus d'explications sur ce sujet, et demandez-lui de modifier les requêtes pour
ne pas utiliser de requête paramétrée. Vous pourrez alors faire une injection SQL dans le formulaire d'ajout d'utilisateur.


## 8. Étape 8 : Authentification

Dans cette étape, on ajoute un système de login simple avec des cookies pour protéger certaines pages.

### 8.1. (IA) Ajouter une fonction de vérification d'identifiants

Ajoutez à `model.py` une fonction `check_user_credentials(username, password)` qui :
- cherche l'utilisateur via son `username` en base,
- compare le `password` saisi avec celui en base,
- retourne `True` si match, `False` sinon.

Pour simplifier, les mots de passe ne seront **pas chiffrés** 
pour cette étape.

### 8.2. (IA) Créer une page de login avec formulaire

- Créez une route `GET /login` qui affiche `login.html`,
- le formulaire POST envoie vers `/do_login` avec `username` et `password`.

### 8.3. (IA) Traiter le login et créer un cookie

Créez une route `POST /do_login` dans `controller.py` qui :
- récupère `username` et `password` du formulaire,
- appelle `model.check_user_credentials()`,
- **si OK** : 
  - crée un cookie `username` avec la valeur,
  - affiche une page de succès,
- **sinon** : affiche une page d'erreur.

Pour créer un cookie en Flask : utilisez `make_response()` et `set_cookie()`.

### 8.4. (IA) Protéger les routes avec un décorateur

Demandez à une IA comment créer un décorateur `@require_login` qui :
- vérifie la présence du cookie `username`,
- redirige vers `GET /login` si absent,
- laisse passer la requête sinon.

Appliquez ce décorateur sur les pages liées aux utilisateurs :
- `/users`
- `/user_form`
- `/create_user`

### 8.5. Tester dans le navigateur

- Essayez d'accéder à `/users` → vous êtes redirigé vers `/login`,
- essayez aussi `/user_form` sans login → redirection vers `/login`,
- allez à `/login`, entrez `bob` / `my_password` → login réussi,
- retournez à `/users` et `/user_form` → maintenant accessibles.

## 9. Étape 9 : soyez imaginatifs !

Chiffrer les mots de passe, ajouter une page de logout, ajouter des rôles d'utilisateur, 
améliorer le design, ajouter des fonctionnalités ... à vous de jouer ! 
Demander de l'aide à une IA pour vous guider dans vos idées d'amélioration.

