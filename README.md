# Le changement climatique en France: Analyse des tendances climatiques
Dans ce projet, nous faisons une analyse des tendances climatiques en France depuis 1996.

## Aperçu
* [Technologies](#technologies)
* [General info](#general-info)
* [Setup](#setup)

## Technologies
Dans ce projet, nous travaillons avec plusieurs technologies : 
* Visual studio Code: Editeur de code.
* Git version 2.42.0 : Il s'agit d'un système de contrôle de version distribué, conçu pour gérer rapidement et efficacement tous les projets informatique.
* Python version 3.12.0

## Information Générale
Nous travaillons avec les données qui proviennent de sources météorologiques officielles et de bases de
données gouvernementales disponible sur le site de [météo France](https://donneespubliques.meteofrance.fr/). 

## Bien démarrer le projet...
Pour démarrer le projet, il faut installer git et python sur votre machine. Pour l'installation de ces outils, je vous invite à vous référer à la documentation disponible sur internet.

Nous supposons que git et python sont installés sur notre machine.
* Etape 1: Nous créons un environnement virtuel sous python afin d'y installer tous les packages nécessaires à la réalisation de ce projet.

Pour cela nous utilisons le module [venv](https://docs.python.org/3/library/venv.html) de python pour créer notre environement virtuel nommé `name_of_env`.
```
C:\Users\nameUsers\path\to\projet\meteo> python -m venv C:\Users\nameUsers\path\to\projet\name_of_env
```
Pour activer l'environnement virtuel, il faut utiliser la commande suivante:
```
C:\Users\nameUsers\path\to\projet\meteo> C:\Users\nameUsers\path\to\projet\name_of_env\Scripts\activate.bat
```
Pour installer les packages du projet à l'aide de notre fichier requirements.txt:
```
    pip install -r requirements.txt
```

* Etape 2: Configuration de l'outil git pour gérer les différentes version de mon code.

```
$ git config --global user.name "your name"
git config --global user.email yourmail@gmail.com
```
