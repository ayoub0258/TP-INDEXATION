# **Web Crawler en Python**

## Installation

1. **Cloner le dépôt**
   ```sh
   git clone https://github.com/ayoub0258/TP-Indexation-Web.git
   cd TP1

2. **Installer les dépendances**
   ```sh
   pip install -r requirements.txt  
   ```

## **Description**
Ce projet est un **crawler web** simple développé en Python, qui explore les pages d'un site web en priorisant certaines pages. Il extrait les informations suivantes :
- Le titre de la page.
- Le premier paragraphe.
- Les liens internes pertinents.

Les résultats sont sauvegardés dans un fichier JSON. Le crawler est conçu pour s'arrêter après avoir visité un maximum de **50 pages**.

---

## **Fonctionnalités**
1. **Respect des règles de `robots.txt`**  
   Le crawler vérifie si l'exploration d'une page est autorisée grâce au fichier `robots.txt`.
   
2. **Extraction de contenu**  
   Pour chaque page visitée, le crawler extrait :
   - Le **titre** de la page.
   - Le **premier paragraphe**.
   - Les **liens internes** relatifs à la même base URL.

3. **Priorisation des liens**  
   Les liens contenant le mot **`product`** dans leur URL sont priorisés dans la file d'attente des URLs à visiter.

4. **Stockage des résultats**  
   Les données extraites sont enregistrées dans un fichier JSON structuré.

---
## Utilisation

Exécuter le script principal pour effectuer les recherches :

   ```sh
   python crawler.py
   ```
Les résultats seront sauvegardés dans le fichier `results.json`.