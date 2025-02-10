import json
import os
from datetime import datetime

def export_results_to_json(results: dict, query: str):
    """
    Sauvegarde les résultats de recherche dans un dossier 'results'.
    """
    # Création du dossier 'results' s'il n'existe pas
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)

    # Création du nom du fichier avec la requête et l'horodatage
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{results_dir}/search_results_{query.replace(' ', '_')}_{timestamp}.json"

    # Sauvegarde des résultats au format JSON
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    
    print(f"Résultats sauvegardés dans {filename}")
