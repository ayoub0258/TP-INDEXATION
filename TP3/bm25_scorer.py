import math
from typing import List, Dict
from text_handler import TextHandler

class BM25Scorer:
    def __init__(self, data_indexes: Dict[str, dict], product_catalog: Dict[str, dict]):
        self.data_indexes = data_indexes
        self.product_catalog = product_catalog

    def calculate_bm25(self, doc_url: str, query_tokens: List[str], k1: float = 1.5, b: float = 0.75) -> float:
        """
        Calcule le score BM25 pour un document donné en fonction des tokens de requête.
        """
        score = 0
        doc = self.product_catalog[doc_url]
        doc_text = f"{doc.get('title', '')} {doc.get('description', '')}"
        doc_tokens = TextHandler.tokenize(doc_text)

        avg_doc_length = 300  
        doc_length = len(doc_tokens)

        for token in query_tokens:
            tf = doc_tokens.count(token)
            doc_count = len(self.data_indexes['title_index'].get(token, {})) + len(self.data_indexes['description_index'].get(token, {}))
            
            if doc_count == 0:
                continue

            idf = math.log((len(self.product_catalog) - doc_count + 0.5) / (doc_count + 0.5) + 1)
            numerator = tf * (k1 + 1)
            denominator = tf + k1 * (1 - b + b * (doc_length / avg_doc_length))
            score += idf * (numerator / denominator)

        return score

    def compute_final_score(self, doc_url: str, query: str, query_tokens: List[str]) -> Dict[str, float]:
        """
        Calcule le score final en combinant BM25, correspondance exacte, titre et avis.
        """
        doc = self.product_catalog[doc_url]
        scores = {
            'bm25_score': self.calculate_bm25(doc_url, query_tokens) * 0.4,
            'exact_match_score': 0,
            'title_match_score': 0,
            'review_score': 0,
            'final_score': 0
        }

        # Bonus pour correspondance exacte
        if query.lower().strip() == doc.get('title', '').lower().strip() or query.lower().strip() == doc.get('brand', '').lower().strip():
            scores['exact_match_score'] = 2.0

        # Bonus pour correspondance avec le titre
        title_tokens = TextHandler.tokenize(doc.get('title', ''))
        title_matches = sum(1 for token in query_tokens if token in title_tokens)
        scores['title_match_score'] = title_matches * 0.2

        # Score basé sur les avis utilisateurs
        if doc_url in self.data_indexes['reviews_index']:
            review_data = self.data_indexes['reviews_index'][doc_url]
            base_review_score = (review_data['mean_mark'] * 0.3 + min(review_data['total_reviews'], 10) * 0.1)
            scores['review_score'] = base_review_score * 0.3

        scores['final_score'] = sum(scores.values())
        return scores
