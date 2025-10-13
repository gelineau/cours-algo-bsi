# Exercices Python


## Chaines de caractères

Etant donné une chaine __s__, afficher une chaine faite des deux premiers et des deux derniers caractères.

```python
s = 'exercice'
print(s[:2] + s[-2:])
```
<!-- .element: class="fragment" -->

---

## Chaines de caractères

Afficher les textes suivants à l’aide d’une seule instruction print :

```
un peu
beaucoup
passionnément

"je t'aime" dit-elle

le fichier à importer est Z:\nouveau\fichier.txt
```

```python
print("""un peu
beaucoup
passionnément""")
print('"je t\'aime" dit-elle')
print('le fichier à importer est Z:\\nouveau\\fichier.txt')
print(r'le fichier à importer est Z:\nouveau\fichier.txt')
```
<!-- .element: class="fragment" -->

---

## Listes

Créer une variable liste égale à [1, 2, 7, 3, 'a']

Remplacer le troisième élément (7) par 8 et afficher la liste

Ajouter l’élément 'toto' à la fin de la liste, et l’afficher

```python
t = [1, 2, 7, 3, 'a']
t[2] = 8
print(t)
t.append('toto')
print(t)
```
<!-- .element: class="fragment" -->

---

## Listes

Écrire un programme qui demande trois nombres à l’utilisateur, puis les affiche dans l’ordre croissant :

```python
numbers = []
numbers.append(int(input('Entrez un nombre: ')))
numbers.append(int(input('Entrez un nombre: ')))
numbers.append(int(input('Entrez un nombre: ')))
numbers.sort()
print(numbers)
```
<!-- .element: class="fragment" -->

---

## Boucles `for`

On considère la liste

```python
t = [1, 2, 4, 8, 16]
```

1. Affichez chaque élément de la liste en utilisant une boucle `for`.

```python
for num in t:
    print(num)
```
<!-- .element: class="fragment" -->

2. Construire une nouvelle liste __t1__ constituée du double de chaque élément de __t__

```python
t1 = []
for num in t:
    t1.append(2 * num)
print(t1)
```
<!-- .element: class="fragment" -->

Ou par _list comprehension_ :

```python
t1 = [2 * num for num in t]
```
<!-- .element: class="fragment" -->

---

## Boucles `for`

Affichez chaque caractère d’une chaîne en utilisant une boucle `for`.

```python
s = 'abcde'
for car in s:
    print(car)
```
<!-- .element: class="fragment" -->

Affichez les entiers de 0 compris à 15 non compris, de trois en trois, en utilisant une boucle `for` et l'instruction `range()`

```python
for i in range(0, 15, 3):
    print(i)
```
<!-- .element: class="fragment" -->

---

## Listes

Générer la liste :

```python
['ad', 'ae', 'bd', 'be','cd', 'ce']
```
à partir des chaînes `"abc"` et `"de"`.

Indication : utilisez deux boucles for imbriquées.

```python
t = []
for car1 in "abc":
    for car2 in "de":
        t.append(car1 + car2)
```
<!-- .element: class="fragment" -->

---

## Boucles `for`

Utilisez l’instruction `break` pour interrompre une boucle `for` d’affichage des entiers de 1 à 10 compris, lorsque la variable de boucle vaut 5.

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```
<!-- .element: class="fragment" -->

Utilisez l’instruction `continue` pour modifier une boucle `for` d’affichage de tous entiers de 1 à 10 compris, sauf lorsque la variable de boucle vaut 5.

```python
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
```
<!-- .element: class="fragment" -->

---

## Fonctions

Définir une fonction `max_of_2()` qui prend deux nombres comme arguments et retourne le plus grand des deux.

Définir une fonction `max_of_3()` qui prend trois nombres comme arguments et retourne le plus grand des trois.

```python
def max_of_2(x, y):
    if x > y:
        return x
    return y
```
<!-- .element: class="fragment" -->

Ou en plus concis :

```python
def max_of_2(x, y):
    return x if x > y else y
```
<!-- .element: class="fragment" -->

---

## Fonctions

```python
def max_of_3(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    return z
```
<!-- .element: class="fragment" -->

Ou réutiliser `max_of_2()` :

```python
def max_of_3(x, y, z):
    return max_of_2(x, max_of_2(y, z))
```
<!-- .element: class="fragment" -->

---

## Fonctions

Définir une fonction `maximum` qui prend un nombre indéterminé de nombres et retourne le plus grand.

```python
def maximum(*nums):
    if not nums:
        print("Vous n'avez pas passé d'argument")
        return
    greatest = nums[0]
    for num in nums[1:]:
        if num > greatest:
            greatest = num
    return greatest
```
<!-- .element: class="fragment" -->

```python
def maximum(first_num, *other_nums):
    values = [first_num] + list(other_nums)
    values.sort()
    return values[-1]
```
<!-- .element: class="fragment" -->

---

## Fonctions

Définir une fonction `repeat` qui prend comme paramètres un caractère et un nombre `n` et affiche le caractère dupliqué n fois, ou 10 fois si le nombre n'est pas fourni.

Appeler cette fonction :
- avec un seul argument
- avec deux arguments dont le caractère en premier
- avec deux arguments dont le nombre en premier

```python
def repeat(car, n=10):
    print(car * n)

repeat('x')
repeat('y', 5)
repeat(n=8, car='r')
```
<!-- .element: class="fragment" -->

---

## Fonctions

Ecrire une fonction qui prend un caractère (une chaine de longueur 1) et retourne `True` si c'est une voyelle, `False` sinon.

```python
def is_vowel(car):
    return car in 'aeiouy'
```
<!-- .element: class="fragment" -->

Ecrire une fonction qui reconnait un palindrome (un mot qui se lit à l'endroit comme à l'envers, par exemple "laval")

```python
def is_palindrome(mot):
    for i in range(int(len(mot) / 2)):
        if mot[i] != mot[len(mot) - i - 1]:
            return False
    return True
```
<!-- .element: class="fragment" -->

```python
def is_palindrome(s):
    return s == s[::-1]
```
<!-- .element: class="fragment" -->

---

## Fonctions

Ecrire une fonction qui reconnait un pangramme (une phrase qui contient toutes les lettres de l'alphabet au moins 1 fois).

Tester avec : _"Portez ce vieux whisky au juge blond qui fume"_.

```python
def is_pangram(sentence):
    sentence = sentence.lower()
    letters = ''
    for car in sentence:
        if car == ' ':
            continue
        if not car in letters:
            letters += car
    return len(letters) == 26
```
<!-- .element: class="fragment" -->

---

## Itérations

Le classement FIFA par pays (au 9/2/2017) est fourni sous forme de deux tableaux :

- equipes = ['Brésil', 'Argentine', 'Allemagne', 'Chili', 'Belgique']
- scores = [1635, 1529, 1433, 1386, 1371]

Ecrire un programme qui imprime le classement sous la forme :

```
1 Brésil : 1635 points
2 Argentine : 1529 points
etc.
```

Correction au slide suivant
<!-- .element: class="fragment" -->

---

## Itérations (correction)

```python
teams = ['Brésil', 'Argentine', 'Allemagne', 'Chili', 'Belgique']
scores = [1635, 1529, 1433, 1386, 1371]

for i, (country, points) in enumerate(zip(teams, scores)):
    print(i + 1, country, ':', points, 'points')

for i, (country, points) in enumerate(zip(teams, scores), start=1):
    print(i, country, ':', points, 'points')

for i, country, points in zip(range(1, 6), teams, scores):
    print(i, country, ':', points, 'points')
```
<!-- .element: class="fragment" -->

---

## Scripts, modules, packages

Le module intégré `random` définit une fonction `choice(seq)` qui retourne un élément au hasard de l'itérable `seq`.

Le module intégré `string` définit une variable `ascii_lowercase`, une chaine constituée de toutes les lettres minuscules.

Utiliser ces modules pour imprimer une lettre minuscule prise au hasard.

```python
import random
from string import ascii_lowercase

print(random.choice(ascii_lowercase))
```
<!-- .element: class="fragment" -->

---

## Formatage de chaines

On dispose d'une liste d'adresses sous forme d'un dictionnaire indexé par les clés _nom, numero, nom_rue, code_postal, nom_ville_ :

Les afficher au format

```
Nom : Jean Dupont
Paris (75003)
```

```python
for adresse in adresses:
    print(f"""Nom: {adresse['nom']}
{adresse['nom_ville']} ({adresse['code_postal']})
""")
```
<!-- .element: class="fragment" -->

---

## Formatage de chaines - autre correction

```python
fmt = """Nom: {nom}
{nom_ville} ({code_postal})
"""
for adresse in adresses:
    print(fmt.format(
        nom=adresse['nom'],
        nom_ville=adresse['nom_ville'],
        code_postal=adresse['code_postal'],
    ))
```
<!-- .element: class="fragment" -->

---

## Fichiers

On dispose d'un fichier de logs.

Établir l'ensemble des chemins d'URL vers lesquelles des requêtes POST ont été émises.

On pourra utiliser un ensemble (set), à initialiser par

```python
urls = set()
```

et utiliser la méthode `startswith()` des chaines de caractères :

```python
>>> 'Opera'.startswith('Op')
True
```

Correction page suivante
<!-- .element: class="fragment" -->

---

## Fichiers - correction

```python
urls = set()
with open('logs', encoding='utf-8') as file_obj:
    for line in file_obj:
        if line.startswith('POST'):
            # Example: 'POST /sysbus/NMC:getWANStatus HTTP/1.1'
            verb, path, version = line.split()
            urls.add(path)
print(urls)
```
<!-- .element: class="fragment" -->

---

## Fichiers (suite)

Comptez le nombre de fois où chaque URL apparaît.

On pourra utiliser un dictionnaire, avec clé : url et valeur : nombre d'occurences.

```python
urls = {}

with open('logs', encoding='utf-8') as file_obj:
    for line in file_obj:
        if line.startswith('POST'):
            # Example: 'POST /sysbus/NMC:getWANStatus HTTP/1.1'
            verb, path, version = line.split()
            urls[path] = urls.get(path, 0) + 1
print(urls)
```
<!-- .element: class="fragment" -->

En utilisant une librairie (`defaultdict` ou `Counter`), on peut simplifier cette solution.

---

## Erreurs et exceptions

On rappelle le script qui calcule la valeur TTC d'un prix HT :

```python
while True:
    ht = input('Prix HT: ')
    if not ht:
        break
    print('Prix TTC', 1.2 * float(ht))
```

En exécutant ce programme, entrer une lettre au lieu d'un chiffre.

Refaire une version qui imprime un message d'erreur si on saisit autre chose qu'un nombre, et redemande une nouvelle valeur.

```python
while True:
    ht = input('Prix HT: ')
    if not ht:
        break
    try:
        print('Prix TTC', 1.2 * float(ht))
    except ValueError:
        print(ht, "n'est pas un nombre")
```
<!-- .element: class="fragment" -->

---

## Erreurs et exceptions

Compléter le programme précédent pour afficher le nombre de valeurs déjà entrées (valides ou non)

```python
nb = 0
while True:
    ht = input('Prix HT: ')
    if not ht:
        break
    try:
        print('Prix TTC', 1.2 * float(ht))
    except ValueError:
        print(ht, "n'est pas un nombre")
    finally:
        nb += 1
        print(nb, 'valeurs saisies')
```
<!-- .element: class="fragment" -->

---

## Classes

Définir une classe `Rectangle` avec :

- un constructeur donnant des valeurs (longueur et largeur) par défaut
- un attribut `nom` égal à "rectangle"
- une méthode d’affichage (`__str__`)
- une méthode `surface` renvoyant la surface d’une instance

Définir une classe `Carre` héritant de `Rectangle`, en donnant à l’attribut `nom` la valeur "carré".

Dans le programme principal, instanciez un `Rectangle` et un `Carre` et affichez-les.

---

## Classes

```python
class Rectangle:
    """Classe des rectangles."""

    nom = "rectangle"
    
    def __init__(self, longueur=30, largeur=15):
        """Initialisation avec valeurs par defaut"""
        self.lon = longueur
        self.lar = largeur

    def surface(self):
        """Retourne la surface d'un rectangle."""
        return self.lon * self.lar

    def __str__(self):
        """Affichage des caracteristiques d'un rectangle."""
        return ("Le {} de côtés {} et {} a une surface de {}".format(
            self.nom, self.lon, self.lar, self.surface()))
```
<!-- .element: class="fragment" -->

---

## Classes

```python
class Carre(Rectangle):
    """Classe des carres (herite de Rectangle)."""

    nom = "carré"
    
    def __init__(self, cote=10):
        """Constructeur avec valeur par defaut"""
        Rectangle.__init__(self, cote, cote)

print(Rectangle(12, 8))
print(Carre(8))
```
<!-- .element: class="fragment" -->

---

## Classes - Méthodes spéciales

Surcharge d'opérateurs : créer une classe Vecteur dont chaque instance a un attribut `x` et `y`.

Définir une méthode pour gérer l'addition de deux vecteurs.

Rappel : la somme du vecteur V1(x1, y1) + V2(x2, y2) est le vecteur V(x1+y1, x2+y2)

---

## Classes - Méthodes spéciales

```python
class Vecteur:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vecteur(self.x + other.x, self.y + other.y)
```
<!-- .element: class="fragment" -->

---

## Classes

Surcharge d'opérateur : créer une classe `TousEgaux` dont toutes les instances sont égales.

```python
class TousEgaux:

    def __eq__(self, other):
        return True

assert TousEgaux() == TousEgaux()
```
<!-- .element: class="fragment" -->

---

## Exceptions

Utilisez une exception pour calculer, dans une boucle évoluant de -3 à 3 compris, la valeur de sin(x)/x

```python
from math import sin
for x in range(-3, 4): # -3 -2 -1 0 1 2 3
    try:
        print("{:.3f}".format(sin(x) / x), end=" ")
    except:
        print("{:.3f}".format(float(1)), end=" ")
print()
```
<!-- .element: class="fragment" -->

---

## Appel de fonction

Écrire une autre fonction *somme* avec trois arguments, et qui renvoie leur somme.  
Dans le programme principal, définir un tuple de trois nombres, puis utilisez la syntaxe d’appel à la fonction qui décompresse le tuple.  
Affichez le résultat.

```python
def somme(a, b, c):
    return a + b + c

t = (23, 42, 13)
print(somme(*t))
```
<!-- .element: class="fragment" -->

---

## Dictionnaires

Écrire une fonction *compterMots* ayant un argument (une chaîne de caractères) qui renvoie un dictionnaire qui contient la fréquence de tous les mots de la chaîne entrée.

```python
def compterMots(texte):
    mots = texte.split() # découpage approximatif !
    freqs = {}
    for mot in mots:
        freqs[mot] = freqs.get(mot, 0) + 1
    return freqs
```
<!-- .element: class="fragment" -->

