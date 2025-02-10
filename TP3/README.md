# Projet de Recherche de Produits

## Description
Ce projet implémente un moteur de recherche de produits basé sur le modèle BM25. Il permet d'analyser et d'indexer un ensemble de données produit, d'effectuer des recherches avancées en utilisant le traitement du langage naturel et de classer les résultats en fonction de leur pertinence.

## Structure du Projet

Le projet est organisé en plusieurs fichiers pour séparer les différentes fonctionnalités :

- `data_manager.py` : Gère le chargement des index et du catalogue de produits.
- `text_processor.py` : Assure le traitement du texte (tokenisation, suppression des stopwords, expansion avec synonymes).
- `document_filter.py` : Filtre les documents en fonction des termes de la requête.
- `bm25_ranker.py` : Implémente l'algorithme BM25 pour classer les documents pertinents.
- `save_results.py` : Sauvegarde les résultats de recherche en fichiers JSON dans un dossier dédié.
- `main.py` : Script principal qui orchestre le traitement des requêtes et l'affichage des résultats.

## Installation

1. **Cloner le dépôt**
   ```sh
   git clone https://github.com/ayoub0258/TP-Indexation-Web.git
   cd TP3

2. **Installer les dépendances**
   ```sh
   pip install -r requirements.txt  
   ```

3. **Télécharger les ressources NLTK (si nécessaire)**
   ```sh
   import nltk
   nltk.download("stopwords")
   ```

## Configuration
Avant d'exécuter le projet, assurez-vous que les fichiers de données sont placés dans le dossier `data/`. Voici la liste des fichiers requis :

- `data/brand_index.json` : Index des marques des produits.
- `data/description_index.json` : Index des descriptions des produits.
- `data/domain_index.json` : Index des domaines des produits.
- `data/origin_index.json` : Index des origines des produits.
- `data/origin_synonyms.json` : Dictionnaire des synonymes des origines.
- `data/reviews_index.json` : Index des avis des utilisateurs sur les produits.
- `data/title_index.json` : Index des titres des produits.
- `data/products.jsonl` : Liste des produits avec leurs métadonnées.

## Exemple de Requêtes
Voici quelques exemples de requêtes pouvant être utilisées avec ce moteur de recherche :

- **"Red Shoes"** 
- **"Coffee Mug"** 
- **"Bluetooth Speaker"** 
- **"Box of Chocolate Candy"**
- **"Classic Sneakers"** 
- **"Kids' Sneakers"** 
- **"Shoes for Men"** 
- **"Running Shoes"**
- **"Running Shoes for Men"** 
- **"Women's Sandals"** 
- **"Energy Potion"** 
- **"Red Energy Potion"**
- **"Hiking Boots"** 
- **"Boots for Outdoor"** 

## Utilisation

Exécuter le script principal pour effectuer les recherches :

   ```sh
   python main.py
   ```
Les résultats seront affichés dans la console et sauvegardés dans le dossier `results/`.