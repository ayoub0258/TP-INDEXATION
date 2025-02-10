from data_manager import DataManager
from text_handler import TextHandler
from document_selector import DocumentSelector
from bm25_scorer import BM25Scorer
from save_results import export_results_to_json
from datetime import datetime

if __name__ == "__main__":
    # Initialisation des composants
    data_manager = DataManager(data_directory="./")
    text_handler = TextHandler()
    doc_selector = DocumentSelector(data_manager.data_indexes)
    ranker = BM25Scorer(data_manager.data_indexes, data_manager.product_catalog)

    # Liste des requêtes de test
    test_queries = [
        "Red Shoes",
        "Coffee Mug",
        "Bluetooth Speaker",
        "Box of Chocolate Candy",
        "Energy Potion",
        "Red Energy Potion",
        "Hiking Boots",
        "Boots for Outdoor",
        "Women's Sandals",
        "Running Shoes for Men",
        "Running Shoes",
        "Shoes for Men",
        "Kids' Sneakers",
        "Classic Sneakers"
    ]

    # Traitement des requêtes
    for query in test_queries:
        print(f"\n=== Recherche: {query} ===")
        tokens = text_handler.tokenize(query)
        expanded_tokens = text_handler.expand_tokens(tokens, data_manager.data_indexes['origin_synonyms'])

        matching_docs = doc_selector.select_with_any_token(expanded_tokens)
        ranked_docs = []
        
        for doc_url in matching_docs:
            scores = ranker.compute_final_score(doc_url, query, expanded_tokens)
            doc = data_manager.product_catalog.get(doc_url, {"title": "No Title", "description": ""})
            ranked_docs.append({
                'title': doc['title'],
                'url': doc_url,
                'description': doc['description'],
                'scores': scores,
                'score': round(scores['final_score'], 3)
            })

        ranked_docs.sort(key=lambda x: x['score'], reverse=True)

        results = {
            'metadata': {
                'query': query,
                'timestamp': datetime.now().isoformat(),
                'total_documents': len(data_manager.product_catalog),
                'filtered_documents': len(matching_docs)
            },
            'results': ranked_docs
        }

        # Affichage des trois meilleurs résultats
        for i, doc in enumerate(ranked_docs[:3], 1):
            print(f"{i}. {doc['title']} (Score: {doc['score']})")
            print(f"URL: {doc['url']}")
            print(f"Description: {doc['description'][:200]}...")
            print(f"Scores: {doc['scores']}")
            print("-" * 50)

        # Sauvegarde des résultats
        export_results_to_json(results, query)
