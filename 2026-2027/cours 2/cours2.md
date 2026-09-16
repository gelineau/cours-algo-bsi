# Exercices String - 1
## 1
Une fonction qui prend en paramètres une chaîne et un nombre n, et qui renvoie les n premiers caractères de la chaîne.
Exemple : "bonjour", 2 => "bo"
Tester avec n plus grand que la taille de la chaîne.

## 2  
Renvoyer le nombre de “a” dans le deuxième mot de la chaîne reçue
Exemple : ("chien canard chat") => 2

## 3 
Prendre l’avant-dernier mot de la chaîne reçue, et retourner ce mot après avoir enlevé les deux premiers et les deux derniers caractères
Exemple : ("chien cheval canard chat") => "na"

## 4
Renvoyer le dernier mot de la chaîne, transformé en int. Si le dernier mot n’est pas un nombre, la fonction doit planter.
Exemple : ("chien cheval canard 42") => 42

## 5 
Renvoyer les n derniers caractères de la chaîne transformée en majuscules. Si la chaîne est moins grande que n, 
compléter avec des espaces.
Exemple : ("chien", 7) => "  CHIEN"

## 6
Renvoyer une nouvelle chaîne contenant uniquement des “*”, de la même taille que la chaîne reçue
Exemple : ("chien") => "*****"

## 7
Renvoyer les n premiers caractères d’une chaîne, mais si n est plus grand que la taille de la chaîne, répéter la chaîne 
plusieurs fois pour atteindre n caractères.
Exemple : ("chien", 12) => "chienchiench"

# Manipulation de listes et de chaînes
## 1
Construire une nouvelle liste constituée du double de chaque élément de la liste de départ.
Avec une boucle, puis (bonus) avec une list comprehension
Exemple : [1, 2, 3] => [2, 4, 6]

## 2
2.1. Rechercher si une valeur est présente dans une liste d’entiers.
Exemple : (3, [1, 2, 3, 4]) => True
2.2. Faire aussi une version avec une boucle sans utiliser les fonctions de recherche.

## 3
3.1. Rechercher à quelle position cette valeur est présente.
Exemple : (3, [1, 2, 3, 4]) => 2
3.2. Faire aussi une version avec une boucle sans utiliser les fonctions de recherche.
3.3. Utiliser enumerate pour faire cette itération.

## 4
Calculer la moyenne d’une liste d’entiers (en utilisant sum et sans l’utiliser).
Exemple : [1, 2, 3, 4] => 2.5

## 5
Recevoir une phrase : Afficher chaque mot sur une ligne, avec son rang et sa taille.
Exemple : ("chien cheval canard") affiche :
1 : chien (5)
2 : cheval (6)
3 : canard (6)  

## 6
Insérer un élément au milieu d’une liste d’entiers (à une position donnée) (en utilisant insert et sans l’utiliser).
Exemple : (élément 99, position 2, [1, 2, 3, 4]) => [1, 2, 99, 3, 4]

## 7
Dans une liste d’entiers, remplacer chaque zéro par la somme de tous les entiers qui se trouvent avant lui.
Exemple : ([1, 2, 0, 3, 0, 4]) => [1, 2, 3, 3, 9, 4]

## 8
Générer la liste ['ad', 'ae', 'bd', 'be', 'cd', 'ce'] à partir des chaînes "abc" et "de" 
(avec 2 boucles ou avec une list comprehension).

# Exercices String - 2
## 1
Écrivez une fonction qui compte le nombre de voyelles d’une chaîne de caractères.
Exemple : "bonjour" => 3

## 2
Écrivez une fonction qui réécrit une adresse email du format prenom.nom@domaine.pays au format 
nom.prenom@domaine-pro.pays

Exemple : "jean.dupont@intradef.fr" => "dupont.jean@intradef-pro.fr"

## 3
Écrivez une fonction qui vérifie si une chaîne donnée est un palindrome 
(se lit de la même façon de gauche à droite et de droite à gauche)

Exemple : "kayak" => True, "bonjour" => False

## 4
Écrivez une fonction qui prend une chaîne en entrée et retourne cette chaîne inversée.

Exemple : "bonjour" => "ruojnob"

# Continue / break

## 9
Demander des mots à l’utilisateur, pour chaque mot afficher sa taille. S’interrompre quand il saisit “fin” en 
utilisant l’instruction break.

## 10
Utilisez l’instruction continue pour afficher tous les mots d’une phrase, sauf le 5ième, le 10ième, etc.

# zip / enumerate

## 11
Le classement FIFA par pays (au 9/2/2017) est fourni sous forme de deux tableaux :

```python
teams = ['Brésil', 'Argentine', 'Allemagne', 'Chili', 'Belgique']
scores = [1635, 1529, 1433, 1386, 1371]
```

Écrire une fonction qui imprime le classement sous la forme :
```
1 Brésil : 1635 points
2 Argentine : 1529 points
etc.
```

# Listes imbriquées

## 12
On vous donne deux listes de listes d'entiers, par exemple :

```python
a = [[1, 4, 9], [2, 6], [11]]
b = [[3, 5], [7, 8, 10]]
```

Écrire une fonction qui :
- Fusionne les deux listes en une seule liste plate (c'est-à-dire sans sous-listes).
- Trie la liste obtenue.
- Retourne la liste finale sous forme de tuples de deux éléments consécutifs, le dernier tuple pouvant contenir un seul élément 
  si la liste a un nombre impair d'éléments.

Résultat attendu pour l'exemple ci-dessus :
[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11,)]

## 13 - Bonus
Même question si les listes de départ peuvent avoir une profondeur quelconque, par exemple :

```python
[[1, [2, [3, 5, [8]]]], [10, 11]]
```

# Bonus pour les plus avancés : advent of code 2024

https://adventofcode.com/2024

Se connecter (n'hésitez pas à créer un compte github si vous n'en avez pas encore)
Rejoindre le leaderboard 462223-220291ae
Sauvez le père Noël !

jours 1 et 2 : OK. 
jour 3 : conseil : se renseigner sur les regex en Python. 
jour4 : OK. 
jour 5 et 6 : première étoile faisable, deuxième étoile pour les meilleurs 
jour 7 : faisable  
...