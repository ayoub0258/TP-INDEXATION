# INDEXER

## Installation

1. **Cloner le dépôt**
   ```sh
   git clone https://github.com/ayoub0258/TP-Indexation-Web.git
   cd TP2

2. **Installer les dépendances**
   ```sh
   pip install -r requirements.txt  
   ```

3. **Télécharger les ressources NLTK (si nécessaire)**
   ```sh
   import nltk
   nltk.download("stopwords")
   ```


## 📌 Description
Ce projet construit plusieurs index à partir d’un fichier JSONL contenant des informations produits pour préparer un moteur de recherche.

## 📂 Structure des index
### **1. Index inversé pour le titre et la description**
- Tokenisation simple (séparation par espace)
- Suppression des stopwords et de la ponctuation
- Associe chaque mot aux URLs des produits où il apparaît

### **2. Index inversé avec positions**
- Ajoute les positions des mots dans les titres et descriptions

### **3. Index des reviews**
- Nombre total de reviews
- Note moyenne
- Dernière note enregistrée

### **4. Index des features (marque, origine, etc.)**
- Associe chaque valeur de feature aux URLs des produits correspondants
