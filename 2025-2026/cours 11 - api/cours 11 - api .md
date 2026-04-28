Cours 11 - utilisation d'API en Python
======================================

Une API est une interface entre 2 programmes. La plupart d'entre elles utilisent le protocole HTTP, et 
transmettent des données en json.

## Exercice 1 - récupération des coordonnées GPS d'une ville

- On veut écrire une fonction qui reçoit le nom d'une ville en paramètre, et qui renvoie les coordonnées GPS de
cette ville, en faisant appel à une API offerte par openstreetmap.
- installer la librairie `requests` (pip install requests). Puis `import requests`
- créer un dictionnaire `headers` avec un seul élement dont la clé est "User-Agent" et la valeur "python-weather-example"
- créer une chaine `url = "https://nominatim.openstreetmap.org/search?q=Rennes&format=json&limit=1"`
  (pour l'instant on ne demande que les coordonnées de Rennes, on généralisera tout à l'heure)
``` python
response = requests.get(url, headers=headers)
print(f"""{response.status_code=}
{response.text=}""")
```
- essayer de mettre un user agent égal à "", puis de remplacer `search` dans l'url par `aaa`, que constatez-vous ?
  (chercher des explications sur les principaux codes de retour HTTP)
- response.text est du texte (sous un format qu'on appelle json => explications orales à donner en cours). 
Transformez-le en utilisant la fonction json.loads. Quel est le type de l'objet Python qu'on obtient ?
  (vous pouvez l'afficher avec pprint)
- simplification du code :
  - utiliser l'URL `url = "https://nominatim.openstreetmap.org"` et créer un dictionnaire `params` 
  avec clé=q => valeur=nom de la ville, clé=format => valeur="json", clé=limit, valeur=1
  Et ajoutez params=params à l'appel de requests.get
- adaptez le dictionnaire pour utiliser le nom de la ville passée en paramètre, et essayer votre fonction avec 
différents noms de villes.


## Exercice 2 - récupération des prévisions météo d'une ville

- écrire une fonction qui prend en paramètre la latitude, la longitude, et la date (format YYYY-MM-DD)
et qui renvoie la température maximale, la température minimale, et la pluie prévue
- pour celà on utilisera l'API à l'URL : "https://api.open-meteo.com/v1/forecast", avec les paramètres
"latitude" : la latitude de la ville, "longitude" : la longitude de la ville, "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum"
"start_date" : la date souhaitée, "end_date" : la même date souhaitée
- dans votre fonction principale, appeler successivement la fonction qui récupère les coordonnées, puis la fonction qui 
récupère la météo avec ces coordonnées
- bonus : aller voir la doc de l'api, et voir comment vous pouvez modifier les paramètres

## Exercice 3 - récupérer des idées d'activité

- écrire une fonction qui renvoie une liste de titres d'activités possibles pour vous occuper ce week-end
- url : "https://bored-api.appbrewery.com/filter", paramètres : `"type": "recreational"`
- Attention : l'API vous renvoie de nombreuses informations, mais on veut renvoyer juste la liste des descriptions de l'activité
  (donc une liste de chaînes de caractères)

## Exercice 4 - de l'IA !

- aller sur https://v2.auth.mistral.ai/login, créer un compte (ou se connecter avec votre compte google)
- S'il vous le demande, mettez un nom d'équipe  /"expérimenter gratuitement" / accepter les conditions / S'abonner 
/ vérifier le téléphone
- Menu "Clés API" / "créer une nouvelle clé" / copier la clé sur votre PC
- L'API Mistral est un peu plus compliquée que ce que nous avons utilisé jusqu'à maintenant. Il faut utiliser
uen requête POST et non plus GET.
- Tout d'abord préparez un dictionnaire :
```python
headers = {"Authorization": f"Bearer {api_key}", 
            "Content-Type": "application/json"}

```
- Puis le payload de la requête :
```python
    payload = {
        "model": "mistral-small-latest",
        "messages": [{"role": "user", "content": question}],
    }
```
où `question` est une chaine de caractères correspondant à la question que vous 
voulez poser à Mistral.
- Transformez ce dictionnaire payload en une chaîne de caractères au format json,
en utilisant json.dumps.
- puis utilisez :
```python
    requests.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers=headers, data=json_payload, timeout=30 )
```

- Enchaînez les différentes API :
  - Demandez les coordonnées de la ville, la météo, la liste des activités, mettez 
  tout ça dans une question que vous envoyez à Mistral pour lui demander de 
  vous conseiller la meilleure activité possible en fonction du temps qu'il fait.

## Bonus :
Essayez d'autres enchainements d'API, d'autres questions vers Mistral ...
