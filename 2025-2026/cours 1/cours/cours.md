
# Python

Copyright Orange - tous droits réservés
---

# Commentaires

Introduits par `#`

```python
# ceci est le premier commentaire
spam = 1    # et ceci est le deuxième
            # ... et encore un !
            
string = "# Ceci n'est pas un commentaire."
```

---

# Définition de noms

```python
width = 20
width += 10
print(width)
# 30

height = 5 * 9

a, b = 0, 1
```

---

# Chaines de caractères

Utilise `'` ou `"`

```python
'spam eggs'
"spam eggs"

"doesn't"
'"Yes," he said.'
```

`\` pour échappement

```python
'doesn\'t'
"\"Yes,\" he said."
'"Isn\'t," she said.'
```

---

# Chaines de caractères

`\` pour continuer une ligne

```python
hello = "This is a rather long string containing\n\
several lines of text just as you would do in C.\n\
    Note that whitespace at the beginning of the line is\
 significant."
```

`"""` sur plusieurs lignes

```python
print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```

---

# Chaines de caractères
Utilisation de l'interpréteur interactif

```python
>>> a = "C'est \"OK\""
```

Évaluation

```python
>>> a
'C\'est "OK"'
```

Affichage

```python
>>> print(a)
C'est "OK"
```

---

# Chaines de caractères

Mode par défaut :

```python
>>> word = 'a\nb'
>>> print(word)
a
b
```

Mode brut (raw) :

```python
>>> word = r'a\nb'
>>> print(word)
a\nb
```

---

# Chaines de caractères

Concaténation par `+`, duplication par `*`

```python
>>> word = 'Help' + 'A'
>>> word
'HelpA'
>>> '<' + word * 5 + '>'
'<HelpAHelpAHelpAHelpAHelpA>'
```

---

# Chaines de caractères

**Accès à un caractère par index**

```
 +---+---+---+---+---+
 | s | a | l | u | t |
 +---+---+---+---+---+
   0   1   2   3   4
  -5  -4  -3  -2  -1
```

```python
>>> word = 'salut'
>>> word[4]
't'
>>> word[-2]
'u'
>>> word[10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

---

# Chaines de caractères

**Tranches (slices)**

```
 +---+---+---+---+---+
 | s | a | l | u | t |
 +---+---+---+---+---+
   0   1   2   3   4
  -5  -4  -3  -2  -1
```

Le premier indice est **compris**, le deuxième est **non compris**

```python
>>> word[0:2]
'sa'
>>> word[2:4]
'lu'
```

---

# Chaines de caractères

**Tranches (slices) - autre explication**

En écrivant les indices avant les cases, cela permet de calculer plus facilement les slices.

```
 +---+---+---+---+---+
 | s | a | l | u | t |
 +---+---+---+---+---+
 0   1   2   3   4   5
-5  -4  -3  -2  -1
```

```python
>>> word[0:2]
'sa'
>>> word[2:4]
'lu'
```

---

# Chaines de caractères

**Tranches (slices) - cas particuliers**

```
+---+---+---+---+---+       +---+---+---+---+---+
| s | a | l | u | t |       | s | a | l | u | t |
+---+---+---+---+---+       +---+---+---+---+---+
  0   1   2   3   4         0   1   2   3   4   5
 -5  -4  -3  -2  -1        -5  -4  -3  -2  -1
```

```python
>>> word[-3:]
'lut'
>>> word[3:]
'ut'

>>> word[3:100] # pas d'exception
'ut'
```

---

# Chaines de caractères

Test d'appartenance

```python
>>> s = 'abcde'
>>> 'a' in s
True
>>> 'bcd' in s
True
>>> 'b' not in s
False
>>> 'x' in s
False
```

---

# Chaines de caractères

Les chaines sont immuables

```python
>>> word = 'HelpA'
>>> word[1] = 'a'
TypeError: 'str' object does not support item assignment
```

Mais les variables peuvent être réaffectées

```python
>>> word = 'HelpA'
>>> word = 'new String'
>>> word
new String
>>> word = 42
>>> word
42
```

---

# Chaines de caractères

Longueur d'une chaine

```python
>>> word = 'intergouvernementalisations'
>>> len(word)
27
```

Chaine vide

```python
>>> empty = ''
>>> len(empty)
0
```

---

# Listes

```python
>>> a = ['spam', 'eggs', 100, 1234]
>>> a
['spam', 'eggs', 100, 1234]
```

Accès par index ou par tranche

```python
>>> a[0]
'spam'
>>> a[3]
1234
>>> a[-2]
100
>>> a[1:-1]
['eggs', 100]
```

---

# Listes

Les listes sont mutables

```python
>>> a
['spam', 'eggs', 100, 1234]
>>> a[2] += 23
>>> a
['spam', 'eggs', 123, 1234]
```

---

# Listes

Concaténation par `+`, duplication par `*`

```python
>>> a = ['spam', 'eggs', 100, 1234]
>>> 3 * a[:3] + ['Boo!']
['spam', 'eggs', 100, 'spam', 'eggs', 100, 'spam', 'eggs', 100, 'Boo!']
```

---

# Listes

Affectation et clonage

```python
>>> a = [0, 1]
>>> b = a       
>>> b[0] = 9    
>>> a  
```
```python
[9, 1]  # toute modification sur b modifie aussi a
>>> c = a.copy()    # clonage : création d'un objet différent de a
>>> c = deepcopy(a) # en cas de liste de liste
>>> c[0] = 10
>>> a
[9, 1]
```
<!-- .element: class="fragment" -->

---

# Listes

Longueur d'une liste par `len`

```python
>>> a = ['a', 'b', 'c', 'd']
>>> len(a)
4
```
---
# Conversion de types

`str(x)` : convertit x en chaîne de caractères  
`int(x)` : convertit x en entier (si possible)  
etc...  

```python
str(25) # '25'
str([1, 2, 3]) # '[1, 2, 3]'
int("23") # 23
int("12A") # ValueError: invalid literal for int() with base 10: '12A'
list("abc") # ['a', 'b', 'c']
list(2) # TypeError: 'int' object is not iterable
```

---

# Listes

Découper une chaine de caractères en éléments d'une liste : méthode `split()`

```python
>>> s = "La cigale et la fourmi"
>>> s.split()
['La', 'cigale', 'et', 'la', 'fourmi']
>>> s = "et un ! et deux ! et trois zéro !"
>>> s.split('!')
['et un ', ' et deux ', ' et trois zéro ', '']
```

Transformer une liste de chaines en une seule chaine : méthode `join` appliquée au _séparateur_

```python
>>> a = ["O rage", "ô désespoir", "ô vieillesse ennemie"]
>>> ' ! '.join(a)
'O rage ! ô désespoir ! ô vieillesse ennemie'
```

---

# Listes

Une liste peut contenir d'autres listes

```python
>>> b = [2, 3]
>>> a = [1, b, 4]  # len(a) == ?
```

<!-- .element: class="fragment" -->
```python
>>> len(a)
3
>>> a[1] # b
[2, 3]
>>> a[1][0] # b[0]
2
```
<!-- .element: class="fragment" -->
---

# Listes

Ajout d'un élément à la fin d'une liste par `append`

```python
>>> t = [2, 3]
>>> t.append('xtra')
>>> t
[2, 3, 'xtra']
```

Insertion d'un élément à une position donnée par `insert`

```python
>>> t.insert(1, 'new')
>>> t
[2, 'new', 3, 'xtra']
>>>
```

---

# Tuples

Comme une liste, mais immuable

```python
>>> t = (1, 2, 'a')
>>> t[1]
2
>>> t[2] = 'b'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

---

# Tuples

C'est la virgule qui crée un tuple, pas la parenthèse

```python
>>> t = 1, 2
>>> t
(1, 2)
```

---

# Tuples

Tuple avec un seul élément

```python
>>> x = (1) # eh non !
>>> x
1
>>> x = 1,
>>> x
(1,)
```

Tuple vide

```python
>>> t = ()
>>> t
()
```

---

Kahoot

---

# Blocs de code

Puissances de 3:

```python
a = 3
while a < 100:
    print(a)
    a *= 3
print('fini')
```

```
3
9
27
81
fini
```

---

# Indentation

Un bloc commence après une ligne qui se termine par `:`

Toutes les lignes du même bloc doivent avoir la même indentation

```python
if condition:
    x += 1
   print('condition vraie')  # Indentation incorrecte, code invalide !
```

---

# Indentation

Imbrication des blocs

```python
while seconds < delay:

    if seconds < 60:
        print("Less than a minute")
    else:
        print("Remaining minutes: ", seconds % 60)

    wait_a_bit()

print("Timed out!")
```

À noter :

- Nouveau bloc => niveau d'indentation supplémentaire
- Les lignes vides ne changent pas le sens du code

---

# Conditions : `if, elif, else`

```python
x = int(input("Please enter an integer: ")) 

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```

À noter :

- pas de "switch / case"
- `match` en Python 3.10+

---

# Conditions

Booléens : `True` et `False`

Test d'égalité : `==`, d'inégalité `!=`

```python
>>> 1 == 0
False
>>> 1 != 0
True
```

Négation : `not`

```python
>>> not 1 == 0
True
```

---

# Conditions

Test sur les types intégrés : `False` pour un nombre égal à 0, une chaine vide, une liste vide, `None`.

```python
servers = []
if not servers: # plus pythonique que "if servers == []:"
    print("Aucun serveur")
```

Opérateur ternaire

```python
x = a[0] if a else None
```

---

# Conditions

Test d'identité : `is`

```python
>>> a = [1, 2]
>>> b = a.copy()
>>> a == b # tous les éléments de chaque liste sont-ils égaux ?
True
>>> a is b # est-ce le même objet ?
False
```

Principalement utilisé pour comparer une variable avec `None`

```python
if a is None:
    ...
```

---

# Boucle `for`

Un des outils les plus puissants de Python

```python
animals = ['chat', 'chien', 'oiseau']
for animal in animals:
    print(animal, len(animal))
```

```
chat 4
chien 5
oiseau 6
```

L'itération par `for ... in` permet de manipuler des *valeurs* plutôt que des *index*.

---

# Boucle `for`

Itération sur une chaine de caractères:

```python
for car in 'abcdef':
    print(car)
```

```
a
b
c
d
e
f
```

---

# La fonction `range`

```python
for i in range(5):
    print(i)
```

```
0
1
2
3
4
```

syntaxe : `range(start, stop, step)` ou `range(start, stop)` ou `range(stop)`


---


# 3 façons d'itérer sur une liste

Itérer sur les valeurs (si je n'ai pas besoin de l'index)
```python
animals = ['chat', 'chien', 'oiseau']
for animal in animals:
    print(animal)
```
Itérer sur les index (si j'ai besoin de l'index)
```python
animals = ['chat', 'chien', 'oiseau']
for index in range(len(animals)):
    print(index, animals[index])
```

Itérer sur les 2 : (cf slide plus loin)
```python
animals = ['chat', 'chien', 'oiseau']
for index, animal in enumerate(animals):
    print(index, animal)
```
---

Exercices 1 à 8  
Et 12 et 13 en bonus pour les plus rapides

---

# List comprehensions

Création par _list comprehensions_

```python
print([x for x in range(5)])
# [0, 1, 2, 3, 4]
print([x * 2 for x in range(5)])
# [0, 2, 4, 6, 8]
print([x * 2 for x in range(5) if x != 3])
# [0, 2, 4, 8]
```
Eviter les list comprehensions imbriquées ou trop compliquées. 

---

# Itérations

Pour affecter plusieurs variables à la fois

```python
a, b, c = x
```

itère sur x et affecte les valeurs

```python
title, first_name, name = "Mme Ada Lovelace".split()
print(first_name) # Ada

a, b, c = range(3)
print(c) # 2
```

Il faut le même nombre de valeurs des deux côtés !

---
# Itérations

`zip` pour itérer sur plusieurs séquences à la fois

```python
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for question, answer in zip(questions, answers):
    print('What is your ' + question + '?  It is ' + answer)
```

``` text
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

---

# Itérations

`enumerate` pour itérer sur le tuple (rang, valeur)

```python
cities = ['bordeaux', 'rennes']
for index, city in enumerate(cities):
    print(index, city)
```

``` text
0 bordeaux
1 rennes
```



---

# `continue`

```python
vowels = 'aeiouy'
consonants = ''
for character in 'une souris verte':
    if character in vowels or character == ' ':
        continue
    consonants += character
```

`consonants == 'nsrsvrt'`
---

# `break`

```python
while True:
    number = int(input('Entrer un nombre de 0 à 5: '))
    if 0 <= number <= 5:
        break
```


---

# Fonctions

```python
def three_powers(n: int):
    """Print powers of 3 until n."""
    a = 3
    while a < n:
        print(a, end=' ')
        a *= 3
    print()

three_powers(10_000)
# 3 9 27 81 243 729 2187 6561
```

---

# Fonctions

Par défaut, une fonction renvoie `None`

```python
print(three_powers(0))  # Affiche None
```

---

# Fonctions

`return` pour définir une ou plusieurs valeur(s) de retour

```python
def three_powers2(n: int) -> list[int]:
    """Return power of 3 sequence until n."""
    result = []
    a = 3
    while a < n:
        result.append(a)
        a *= 3
    return result

p10000 = three_powers2(10_000)
print(p10000)
# [3, 9, 27, 81, 243, 729, 2187, 6561]
```

---

# Fonctions - typage statique

```python
def extract_word(sentence: str, i: int) -> str:
    """Extract i-th word from sentence, starting at 0"""
    return sentence.split()[i]
```
Le typage statique est optionnel, mais il est utile :
- documentation
- détection de bugs par l'IDE ou un outil d'analyse de code (*mypy*)
---

# Fonctions

Définition de paramètres par défaut

```python
def add(x: int, y: int = 4) -> int:
    return x + y

print(add(2))      # 6
print(add(2, 3))   # 5
```


---

# Fonctions

Le paramètre par défaut est calculé _une fois pour toutes_ au moment de la définition de la fonction

```python
def add_to_list(number: int, numbers: list[int]=[]) -> list[int]:
   numbers.append(number)
   return numbers

print(add_to_list(1)) # [1]
print(add_to_list(2)) # [1, 2]
```
Par précaution, ne pas utiliser d'objet mutable ([], {}, ...) comme valeur par défaut d'une fonction 

---

# Fonctions

```python
def substract(x: int, y: int) -> int:
    return x - y
```

On peut appeler une fonction avec des _arguments positionnels_:

```python
print(substract(1, 2)) # -1
```

ou des _mots-clés_:

```python
print(substract(y=6, x=2) # -4
```

---

# Fonctions

On ne peut pas donner deux fois le même argument:

```python
def substract(x: int, y: int) -> int:
    return x - y

print(substract(3, x=8))
# TypeError: substract() got multiple values for argument 'x'
```

---

# Fonctions

Une fonction peut accepter un nombre variable d'arguments positionnels ou mots-clés ; ils sont gérés par des paramètres spécifiques.

```python
>>> def f(*args):
...    print(args) # tuple
...
>>> f(1, 2, 'a')
(1, 2, 'a')
```

```python
>>> def f(*args, **kwargs):
...    print(args) # tuple
...    print(kwargs) # dictionnaire
...
>>> f(1, 2, u=0, v='a')
(1, 2)
{'u':0, 'v':'a'}
```



---

# Fonctions

Appel de fonction par "déballage de tuple" _(tuple unpacking)_

```python
>>> def f(x, y):
...     return x + y
...
>>> t = (3, 5)
>>> f(*t) # comme f(3, 5)
8
```

ou par "déballage de dictionnaire" _(dict unpacking)_

```python
>>> d = {'x':3,'y':5}
>>> f(**d) # comme f(x=3, y=5)
8
```



---

TODO: reste du document à adapter pour le cours de BSI

---

# Ensembles (set)

Comme une liste, mais sans duplication ni ordre

```python
>>> fruits = {'pomme', 'orange', 'pomme', 'poire', 'orange', 'banane'}
>>> fruits     # les doublons sont éliminés
{'banane', 'poire', 'pomme', 'orange'}
>>> 'orange' in fruits
True
>>> 'abricot' in fruits
False
```

Limitation sur les types de données qu'on peut mettre dans un set : nombres, chaines, mais pas listes ou autres sets.

---

# Ensembles (set)


Création par _set comprehensions_

```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```

---

# Ensemble

```python
>>> fruits.add('abricot')
>>> fruits
{'banane', 'poire', 'abricot', 'pomme', 'orange'}
```

Passage par un ensemble pour supprimer les doublons d'une liste

```python
>>> fruits = ['banane', 'banane', 'poire']
>>> fruits = list(set(fruits))
>>> fruits
['banane', 'poire']
```

Intersection ou union d'ensembles ... voir la doc.

---

# Dictionnaires

Associe une clé (immuable : chaine, entier, tuple...) à une valeur

```python
>>> tel = {'jack': 4098, 'sape': 4139} # création
>>> tel['guido'] = 4127                # ajoute un nouvel élément
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']                        # accès par clé
4098
>>> tel['jack'] = 4099                 # changement de valeur
>>> tel.pop('sape')                    # suppression
4139
>>> del tel['sape']                    # suppression aussi
>>> tel['irv'] = 4127                  # même valeur pour plusieurs clés
>>> tel
{'jack': 4099, 'guido': 4127, 'irv': 4127}
>>> 'guido' in tel                     # test d'appartenance (clé)
True
>>> 'jack' not in tel
False
```

---

# Dictionnaires

```python
>>> tel['jenny']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'jenny'
>>> tel.get('guido')
4127
>>> tel.get('jenny')       # renvoie None
>>> tel.get('jenny', 4000) # valeur par défaut
4000
```

---

# Dictionnaires

`tel.keys()` renvoie un itérable sur la liste des clés

Même chose pour `tel.values()` (valeurs) et `tel.items()` (tuples clé, valeur)

```python
>>> for name, number in tel.items():
...     print(name, "'s number is", number)
...
jack 's number is 4099
guido 's number is 4127
irv 's number is 4127
```

---

# Dictionnaires

Itérer sur un dictionnaire c'est itérer sur ses clés

```python
>>> for key in tel:
...     print(key)
...
jack
guido
irv
```

contrairement aux listes qui itèrent sur les valeurs

```python
>>> for value in [1, 'a']:
...     print(value)
...
1
'a'
```

---

# Dictionnaires

Construction par `dict`

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

ou par _dict comprehensions_

```python
>>> {x: x ** 2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

---

# Dictionnaires

Depuis Python 3.6, les dictionnaires sont ordonnés


---

# Scripts

Enregistrement du programme dans un fichier _script.py_

```python
for i in range(5):
    print(i)
```

Dans l'invite de commandes, aller dans le répertoire de _script.py_ et exécuter

```console
C:\test python>python script.py
0
1
2
3
4
```

---

# Modules

Sauvegarde dans un fichier three.py

```python
"""Provide some power of 3 functions."""

def three_powers(n):
    """Print powers of 3 until n."""
    a = 3
    while a < n:
        print(a, end=' ')
        a *= 3
    print()

def three_powers2(n):
    """Return power of 3 sequence until n."""
    result = []
    a = 3
    while a < n:
        result.append(a)
        a *= 3
    return result
```

---

# Modules

`import` pour importer un module

```python
>>> import three
>>> three.three_powers(1000)
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> three.three_powers2(100)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> three.__name__
'three'
```

---

# Modules

`from X import n1, n2...` pour importer des noms d'un module

```python
>>> from three import three_powers, three_powers2
>>> three_powers(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

`from X import *` pour importer tous les noms du module _(attention aux conflits de noms !)_

```python
>>> from three import *
>>> three_powers2(100)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

alias : `from X import un_nom_de_fonction_tres_long as f`

---

# Modules

Recherche d'un module par son nom :

- dans la librairie standard
- puis dans le répertoire courant
- puis dans `Lib/site-packages` (modules tiers)

Arborescence de fichiers :

```
+ mes_scripts
    test.py
    mon_module.py
```

dans test.py :

```python
import os            # bibliothèque standard
import mon_module    # répertoire courant
```

---

# Packages

Pour structurer des librairies qui contiennent plusieurs modules

Organisation en répertoires qui contiennent un fichier *__init__.py*

```
+ sound
    __init__.py
    + formats
        __init__.py
        wavread.py
        ...
    + effects
        __init__.py
        echo.py
```

```python
import sound
import sound.formats
from sound.formats import wavread
```

---

# La fonction `dir()`

pour inspecter les noms définis par un module

```python
>>> import three, sys
>>> dir(three)
['__name__', 'three_powers', 'three_powers2']
```

Sans arguments : liste les noms définis dans le module courant

```python
>>> a = [1, 2, 3, 4, 5]
>>> import three
>>> three_powers = three.three_powers
>>> dir()
['__builtins__', '__doc__', '__file__',
 '__name__', 'a', 'three', 'three_powers']
```

---

# La fonction `help()`

Affiche les noms définis avec l'aide (les _doctrings_)

```python
>>> import three
>>> help(three)
Help on module three:

NAME
    three - Provide some power of 3 functions.

FUNCTIONS
    three_powers(n)
        Print powers of 3 until n.

    three_powers2(n)
        Return power of 3 sequence until n.

FILE
    /Path/to/imported/file/three.py
```

---

# Formatage de chaînes

2 techniques principales :

- les "f-strings" : à utiliser pour python >= 3.6
- la méthode str.format() : à utiliser pour les versions python < 3.6, et à connaître pour relire du code existant.

---

# Formatage de chaînes : les f-strings

Permet de mettre en forme une chaine de caractères selon certains paramètres.

Les séquences *{_expression_}* sont remplacées par la valeur de l'expression, avec éventuellement des instructions pour la mise en forme.

A privilégier pour les version de Python >= 3.6+ :

```python
>>> name = 'world'
>>> f'Hello {name}'
'Hello world'
>>> f'Hello {name.upper()}'
'Hello WORLD'
>>> f'The value of PI is approximately {math.pi:.3f}.'
'The value of PI is approximately 3.142.'
```

---

# Formatage de chaînes : la méthode format()

```python
>>> fighters = 'knights'
>>> motto = 'Ni'
>>> print('We are the {} who say "{}!"'.format(fighters, motto))
We are the knights who say "Ni!"
```

Les séquences `{}` sont remplacées par les arguments de `format`.

---

# Formatage de chaînes : la méthode format()

On peut spécifier le nombre de décimales à utiliser

```python
>>> import math
>>> print('The value of PI is approximately {0:.3f}.'.format(math.pi))
The value of PI is approximately 3.142
```

et le nombre minimal de caractères

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print('{0:10} ==> {1:10d}'.format(name, phone))
...
Jack       ==>       4098
Dcab       ==>       7678
Sjoerd     ==>       4127
```

---

# Formatage de chaînes : la méthode format()

On peut spécifier le rang de l'argument à insérer

```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

On peut spécifier des mots-clés

```python
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

---

# Formatage de chaînes : ancien (ne pas utiliser)

```python
>>> 'Hello %s' % name
Hello world

>>> duration = 5
>>> unit = 'minutes'
>>> 'Attendez %d %s' % (duration, unit)
```

---

# Fichiers

`open(_filename, mode, encoding_)`

Le *mode* peut être

- 'r' : lecture seule (valeur par défaut)
- 'a' : écriture en fin de fichier
- 'w' : effacement si le fichier existe déjà, puis écriture

Ajouter 'b' pour indiquer qu'on veut ouvrir les fichiers en mode binaire ('rb', 'wb'...)

---

# Fichiers

`open(_filename, mode, encoding_)`

*encoding* spécifie l'encodage d'un fichier texte (la table de conversion entre un caractère et un ou plusieurs octets) :

- 'utf-8' : convertit le caractère __é__ en deux octets : __c3 a9__
- 'latin-1' : convertit __é__ en un octet : __e9__
- 'ascii' : ne sait pas convertir les caractères accentués

_Il faut spécifier l'encodage systématiquement_ : les valeurs par défaut varient selon les OS, les versions, etc.

*encoding* doit être passé comme argument mot-clé :

```python
opened_file = open("fichier.txt", "r", encoding="utf-8")
```

---

# Fichiers

Lecture d'un fichier texte ligne par ligne :

```python
>>> with open('/tmp/workfile', 'r', encoding="utf-8") as opened_file:
...     for line in opened_file:
...         print(line[:3])
```

Utilisation du mot-clé `with` ("context manager") : s'occupe de la fermeture du fichier.

---

# Fichiers

Autres fonctions pour la lecture (moins utilisées):

- `file.read(_nb_)` pour lire au plus _nb_ caractères. Renvoie la chaine vide `''` en fin de fichier
- `file.read()` pour lire tout le fichier
- `file.readline()`: lit une ligne ; se termine par `\n`, ou `''` en fin de fichier
- `file.readlines()` lit toutes les lignes et les met dans une liste

---

# Fichiers

`file.write(_data_)` pour écrire la chaine _data_ dans le fichier

```python
>>> file.write('This is a test\n')
```

Pour écrire autre chose qu'une chaine, il faut d'abord convertir en chaine par `str()`

```python
>>> file.write(42)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: expected a character buffer object
>>> file.write(str(42))
```

---

# Sérialisation : le module `json`

Sérialisation : transformation d'un objet en chaine de caractère : pour stockage, envoi sur le réseau (API web...).

Le format JSON définit un mode de sérialialisation, limité aux types simples : nombres, chaines de caractères, listes, dictionnaires dont les clés sont des chaines de caractères.

```python
import json

json.dumps(obj)     # sérialise l'objet

obj = json.loads(s) # récupère l'objet sérialisé
```

---

# Erreurs et exceptions

Python distingue :

- les erreurs : détectées dans la phase d'analyse du programme
  - erreurs de syntaxe
  - erreur d'indentation
- les exceptions : surviennent pendant l'exécution d'un programme

---

# Erreurs

`SyntaxError`

```python
>>> while True print 'Hello world'
  File "<stdin>", line 1, in ?
    while True print 'Hello world'
                   ^
SyntaxError: invalid syntax
```

`IndentationError`

```python
>>> for i in range(5):
... print i
  File "<stdin>", line 2
    print i
        ^
IndentationError: expected an indented block
```

---

# Exceptions

Exemples :

```python
>>> 10 * (1 / 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ZeroDivisionError: integer division or modulo by zero

>>> 4 + spam * 3
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
NameError: name 'spam' is not defined

>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: cannot concatenate 'str' and 'int' objects
```

---

# Exceptions

`try ... except` pour gérer des exceptions

```python
while True:
     try:
         x = int(input("Veuillez entrer un nombre: "))
         break
     except ValueError:
         print("Ce n'est pas un nombre valide. Veuillez recommencer")

print(f"Vous avez saisi le nombre {x}")
```

Si une instruction du bloc `try` déclenche une exception, on arrête l'exécution du bloc

Si l'exception est du type spécifié dans `except` on exécute le bloc de cet `except`

---

# Exceptions

Variantes de `except` :

```python
try:
    ...
except IOError:
    ...
except (TypeError, ValueError): # plusieurs types d'exceptions
    ...
except:        # toutes les exceptions non encore gérées
    ...
```

---

# Exceptions

`as` pour récupérer l'objet exception

```python
>>> x = [6]
... try:
...     x[2]
... except IndexError as exc:
...    print(f'erreur index : {exc}')
...
erreur index: list index out of range
```

L'objet `exc` est une _instance_ de la _classe_ `IndexError`

---

# Exceptions

`raise` pour déclencher des exceptions

```python
>>> def square_root(x):
...     if x < 0:
...         raise ValueError('nombre négatif')
...
>>> square_root(-6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in square_root
ValueError: nombre négatif
>>>
```

---

# Exceptions

Sans argument : re-déclenche la dernière exception gérée

```python
>>> valeur = -1
>>> try:
...     square_root(valeur)
... except ValueError:
...     print('erreur pour la valeur', valeur)
...     raise
...
erreur pour la valeur -1
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 3, in square_root
ValueError: nombre négatif
```

---

# Exceptions

`finally` pour exécuter un code qu'il y ait eu exception ou pas

Si une exception n'a pas été gérée, elle est déclenchée après `finally`

```python
>>> x = [5]
>>> try:
...     print(x[2])
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list index out of range
```

---

# Exceptions

```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division par zero!")
...     else:
...         print(f"le resultat est {result}")
...     finally:
...         print("fin de fonction")
...
>>> divide(2, 1)
le resultat est 2
fin de fonction

>>> divide(2, 0)
division par zero!
fin de fonction
```

---

# Exceptions

Mot-clé `assert`

```python
>>> def age(birth_year, year):
...     assert birth_year <= year, "pas né !"
...     return year - birth_year
...
>>> age(1974, 2015)
41
>>> age(1974, 1960)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in age
AssertionError: pas né !
>>>
```

Attention, les asserts sont ignorés en _mode optimisé_

---

# Espaces de noms

Permet de définir et d'utiliser le même nom dans des contextes différents

```python
>>> a = 1
>>> def f():
...    a = 3
...    print(a)
...
>>> f()
3
>>> a
1
```

---

# Espaces de noms

`global` pour forcer l'utilisation d'une variable globale

```python
>>> a = 1
>>> def f():
...    global a
...    a = 3
...    print(a)
...
>>> f()
3
>>> a
3
```

---

# Espaces de noms

```python
x = 0

def f(x):
    import Z

import X

from Y import A

for i in range(5):
    j = 2 * i
```

définit les noms `x, f, X, A, i, j` dans l'espace de noms global ; `x, Z` dans l'espace de noms de `f` (aucun rapport entre les deux `x`)

NB : le nom `Y` n'est __pas__ dans l'espace de noms

---

# Espaces de noms

A l'exécution, quand l'interpréteur rencontre un nom, il cherche dans l'espace de nom le plus proche, puis "remonte" jusqu'au niveau module puis aux noms intégrés de Python

```python
a = 6
def f():
    b = 8
    def g(n):
        print(n)
        print(b)
        print(a)
    g(8)
```

Dans l'exécution de g :

- pas de nom `print` dans les espaces locaux ni globaux, mais `print` est une fonction intégrée de Python
- le nom `n` est dans l'espace de noms de g
- pas de nom `b` dans l'espace de noms de g, on remonte jusqu'à l'espace de noms de f
- pas de nom `a` dans l'espace de noms de g ni de f, on remonte jusqu'à l'espace de noms global

---

# Espaces de noms

Un nom défini ("bound") dans un bloc est local à ce bloc.

```python
>>> a = 0
>>> def f():
...   print(a)
...   a = 1
...
>>> f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
UnboundLocalError: local variable 'a' referenced before assignment
>>>
```

---

# Classes

Définis par le mot clé `class`

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

Le nom `ClassName` est ajouté dans l'espace de noms où la classe est définie.

Une classe possède son propre espace de noms.

---

# Classes

```python
>>> class MyClass:
...    i = 12345
...
>>> print(MyClass.i)
```

Les noms définis dans `MyClass` (_attributs_) sont accessibles depuis l'espace de noms "supérieur" par des _noms qualifiés_ (forme `klass.X`)

On peut modifier dynamiquement les attributs de la classe

```python
>>> MyClass.i = 23456
```

et ajouter des attributs de classe "à la volée" :

```python
>>> MyClass.j = 8
>>> MyClass.j
8
```

---

# Classes

Pour créer des instances d'une classe, on l'utilise comme une fonction :

```python
>>> class MyClass:
...    i = 12345
...
>>> x = MyClass()
```

L'instance possède les mêmes attributs que la classe

```python
>>> x.i
12345
```

On peut ajouter des attributs d'instance "à la volée" :

```python
>>> x.name = "homer"
>>> x.name
'homer'
```

---

# Classes

Les _fonctions_ définies dans la classe deviennent les _méthodes_ des instances de cette classe

Par convention, on les écrit avec l'instance comme premier argument, appelé `self`

```python
>>> class MyClass:
...
...     def f(self):
...         print('hello')
...
...     def greet(self, name):
...         print('hello, ', name)
...
>>> x = MyClass()
>>> x.f()
hello
>>> x.greet('world')
hello, world
```

`x.greet('world')` est équivalent à  `MyClass.greet(x,'world')`

---

# Classes

Pour initialiser une instance avec des attributs spécifiques : fonction spéciale `__init__()`

```python
>>> class MyClass:
...     def __init__(self):
...         self.data = []
...
>>> x = MyClass()
>>> x.data
[]
```

---

# Classes

Bien distinguer attributs de classe (partagés entre toutes les instances)

```python
>>> class A:
...     data = []
...
>>> a = A()
>>> a.data.append(1)
>>> b = A()
>>> b.data
[1]
```

et attributs propres à chaque instance

```python
>>> class B:
...     def __init__(self):
...         self.data = []
>>> a = B()
>>> a.data.append(1)
>>> b = B()
>>> b.data
[]
```

---

# Classes

On peut passer des arguments à la fonction `__init__`

```python
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

---

# Classes

Les méthodes peuvent appeler d'autres méthodes

```python
class Bag:

    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

---

# Héritage

```python
class DerivedClass(BaseClass):
    <statement-1>
    .
    .
    .
    <statement-N>
```

`DerivedClass` _hérite_, ou est _dérivée_, ou est une _sous-classe_ de `BaseClass`

---

# Héritage

```python
>>> class A:
...     x = 0
...
>>> class B(A):
...     y = 1
...
>>> obj = B()
>>> obj.y
1
>>> obj.x
0
```

La recherche (_résolution_) d'attribut est exécutée dans la classe B, puis dans la classe A dont B hérite

---

# Héritage

Une sous-classe peut réécrire (_surcharger_) les fonctions de la classe dont elle hérite

```python
class A:
    x = 0
    def show(self):
        print('je suis A')

class B(A):
    def show(self):
        print('je suis B')
```

---

# Héritage

On peut utiliser les fonctions de A dans les fonctions de B

```python
class A:
    def __init__(self, x):
        self.x = x ** 2

class B(A):
    def __init__(self, x, y):
        A.__init__(self, x)
        self.y = y
```

---

# Héritage

Exemple : les modules peuvent définir des _classes_ d'exception spécifiques, dérivées de la classe `Exception`

```python
>>> class MyError(Exception):
...     def __init__(self, value):
...         self.value = value
...
>>> try:
...     raise MyError(4)
... except MyError as e:
...     print('My exception occurred, value:', e.value)
...
My exception occurred, value: 4
```

`MyError(4)` crée une _instance_ de la classe `MyError` en passant l'argument `4`

La méthode `__init__(self, value)` initialise l'instance avec l'argument _value_

---

# Héritage

Héritage multiple

```python
class Derived(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

Construit pour la classe `Derived` un _ordre de résolution de méthodes_ (MRO) pour la résolution d'attributs ; exception en cas d'impossibilité.

---

# Héritage

Ordre de résolution quand 2 classes parentes définissent le même attribut

```python
>>> class A:
...     info = "classe A"
...
>>> class B:
...     info = "classe B"
...
>>> class C(A, B):
...     pass
...
>>> C().info
'classe A'
>>> class D(B, A):
...     pass
...
>>> D().info
'classe B'
```

---

# Héritage

`issubclass(_A, B_)` teste si la classe _A_ hérite de la classe _B_

`isinstance(_obj, A_)` teste si l'objet _obj_ est une instance de _A_ ou d'une classe qui hérite de _A_

Variante :  `isinstance(_obj, [A, B]_)`

```python
def carre(x):
    if not isinstance(x, [int, float]):
        raise ValueError("l'argument n'est pas un nombre")
    return x * x
```

---

# Méthodes spéciales

`__str__(self)` pour définir le résultat de `print(objet)`

```python
class A:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return '{} {}'.format(self.prenom, self.nom)

x = A('Einstein', 'Albert')
print(x)
```

---

# Méthodes spéciales

`__getitem__(self, pos)` pour définir l'accès par index

```python
>>> class A:
...     def __init__(self):
...         self.data = 'la cigale et la fourmi'
...     def __getitem__(self, i):
...         return self.data[i]
...
>>> x = A()
>>> x[3]
c
```

---

# Méthodes spéciales

`__mul__(self, other)` pour définir la multiplication d'une instance par _other_

```python
>>> class Vecteur:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
...     def __mul__(self, vec):
...         return self.x * vec.x + self.y * vec.y
...
>>> Vecteur(2,3) * Vecteur(-1,2)
4
```

de même : `__add__, __sub__, __div__, __pow__ ...`

`__eq__` pour tester l'égalité, `__ne__` pour inégalité

`__le__` pour <=  
`__gt__` pour > etc.

---

# Itérateurs

Utilisés très fréquemment en Python

```python
for element in [1, 2, 3]:
    ...

for element in (1, 2, 3):
    ...

for key in {'one':1, 'two':2}:
    ...

for char in "123":
    ...

for line in open("myfile.txt"):
    ...
```

---

# Itérateurs

Pour pouvoir itérer sur une instance d'une classe, la classe doit définir une fonction `__iter__`, qui renvoie un objet qui possède une méthode `__next__`

`__next__` déclenche `StopIteration` quand l'itération est finie.

```python
class Reverse:
    """Iterateur pour parcourir une séquence à l'envers."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]
```

---

# Générateurs

Création automatique d'itérateurs : fonctions qui utilisent `yield` au lieu de `return`

```python
>>> def gen():
...     yield 1
...     yield 2
...
>>> it = gen()
>>> next(it)
1
>>> next(it)
2
```

Chaque appel de `next()` reprend l'exécution de la fonction à l'endroit où elle s'était arrêtée à l'itération précédente.

---

# Générateurs

Générateur infini

```python
>>> def gen():
...     i = 0
...     while True:
...         yield i
...         i += 1
...
>>> it = gen()
>>> next(it)
0
>>> next(it)
1
```

Entre deux appels de `next()` les variables locales sont conservées

---

# Générateurs

Exemple : itérateur sur tous les nombres premiers supérieurs à un seuil

```python
>>> def premiers(n):
...     while True:
...         if est_premier(n):
...             yield n
...         n += 1
...
```

---

# Générateurs

`return` dans un générateur termine l'itération

```python
>>> def enter():
...     while True:
...         t = input('? ')
...         if not t:
...             return
...         yield 'bonjour ' + t
...
>>> for item in enter():
...     print(item)
...
? essai
bonjour essai
? coucou
bonjour coucou
?
>>>
```

---

# Generator expressions

Simplifie le passage d'argument à une fonction qui attend un itérateur

```python
>>> sum(i * i for i in range(10))
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x * y for x, y in zip(xvec, yvec))
260

>>> unique_words = set(word for line in page for word in line.split())
```

---

# Décorateurs

Fonction qui renvoie une autre fonction, utilisée avec `@`

```python
@controle
def f(...):
    ...
```

équivaut à

```python
def f(...):
    ...
f = controle(f)
```

---

# Décorateurs

Exemple : vérifier qu'une fonction renvoie un entier

```python
def check_int(func):
    def g(*args, **kw):
        res = func(*args, **kw)
        assert isinstance(res, int)
        return res
    return g

@check_int
def f(x):
    return x*2

f(1)
f('a')
```

---

# Quelques bonnes pratiques

Référence : [PEP 8](https://www.python.org/dev/peps/pep-0008/). Voir aussi l'outil `black`

_Le code est plus souvent lu qu'écrit_

- indentation : 4 espaces
- lignes : pas plus de 79 caractères
- docstring au début d'un module, d'une fonction, d'une classe

```python
def insort_left(a, x, lo=0, hi=None):
    """Insert item x in list a, and keep it sorted assuming a is sorted.

    If x is already in a, insert it to the left of the leftmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
```

La chaine devient l'attribut `__doc__` du module, de la fonction, de la classe.

---

# Quelques bonnes pratiques

- nom des variables : plus d'une lettre ; pas "I" ou "l" ; pas un nom intégré

```python
>>> list = ['a', 'b', 'c']
# 100 lignes plus loin...
>>> items = list(name)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
```

- nom des modules en minuscule ; nom des classes commence par une majuscule ; constantes tout en majuscules
- `variable_avec_tiret_bas` plutôt que `variableAvecDesMajuscules`
- plutôt 5 lignes lisibles qu'une ligne illisible : boucles `for` indentées plutôt que des _list comprehensions_ complexes

---

# Quelques bonnes pratiques

Des tests, des tests, des tests...

```python
from three import three_powers2

def test_powers_lower_than30():
    expected = [3, 9, 27]
    obtained = three_powers2(30)
    assert obtained == expected

def test_powers_with_0_should_return_empty_list(self):
    assert three_powers2(0) == []
```

Automatisable avec des "test runners" tels que `pytest`.

---

# Librairie standard : `os`

```python
>>> import os
>>> os.getcwd()      # renvoie le répertoire courant
'C:\\Python36'
>>> os.chdir('/server/accesslogs')   # change le répertoire courant
>>> os.mkdir('nouveau')              # crée un nouveau répertoire
>>> os.rmdir('nouveau')              # supprime un répertoire

>>> os.path.join('rep1', 'rep2', 'fichier.txt')
'rep1\\rep2\\fichier.txt'
```

---

# Librairie standard : `shutil`

Utilitaires de manipulation de fichiers et de répertoires

```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db') # recopie
>>> shutil.move('/build/executables', 'installdir') # déplacement
```

---

# Librairie standard : `sys`

Arguments passés en ligne de commande (_python demo.py one two three_)

Dans _demo.py_

```python
import sys
print(sys.argv) # liste des arguments passés après "python"
['demo.py', 'one', 'two', 'three']
```

Entrée et sortie standard : `sys.stdin, sys.stdout`

```python
sys.stdout.write('data')
```

Peut être modifié pour rediriger la sortie de `print`

```python
sys.stdout = file_obj # un objet avec une méthode write
print('data')         # équivaut à file_obj.write('data\n')
```

---

# Librairie standard : `re` (expressions régulières)

Fonctions avancées de recherche et remplacement de chaines de caractères

```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```

---

# Librairie standard : `math`

Fonctions mathématiques

```python
>>> import math
>>> math.cos(math.pi / 4.0)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```

---

# Librairie standard : `random`

Fonctions aléatoires

```python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # échantillon
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # entier dans range(6)
4
```

---

# Librairie standard : `datetime`

Heures et dates

```python
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'
```

Opérations sur les dates

```python
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```

---

# Librairie standard : compression

Modules standard `zlib, gzip, bz2, zipfile, tarfile`

```python
>>> import zlib
>>> s = 'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```

---

# Installation de packages tiers

Programme `pip` pour installer un package déposé sur le Python Package Index

```console
pip install flask
```

`pip` installe automatiquement les packages dont dépend __flask__.

Le package est ensuite disponible dans l'interpréteur :

```python
>>> from flask import Flask
```

