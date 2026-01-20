https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-indicateurs-de-resultat-des-lycees-gt_v2/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B

1-
Sauvegarder le fichier csv
Lire les n premières lignes du fichier (sauf la première), et sauvegarder ces différentes lignes dans une liste. Afficher la liste

2- si n est None, afficher toutes les lignes

3- après avoir lu les n lignes, appeler une fonction qui découpe chaque ligne en fonction du séparateur (,) et ne garde dans la liste que les lignes pour 2024 et la Bretagne
(l'année et la région seront passées en paramètres)

4- ajoute une fonction qui sauvegarde les données filtrées dans un nouveau fichier. Pour cela, penser à sauvegarder le header initital dans
une variable à part, pour pouvoir le réécrire en début du nouveau fichier

5- utilise csv.reader et csv.writer pour faire la lecture et l'écriture

6- ajoute une fonction qui relit le fichier filtré, et qui compte le nombre de lycées par ville
Utiliser un dictionnaire. (bonus : simplifier le code en utilisant un defaultdict ou un Counter)

7- affiche les lycées par ordre décroissant de réussite au bac

8- représenter sur un graphique l'évolution du taux de réussite pour le lycée 0350795Z au cours des années

9- quels autres graphiques intéressants pouvez-vous afficher ?