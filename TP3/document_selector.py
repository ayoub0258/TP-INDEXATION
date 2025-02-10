from typing import List, Set, Dict

class DocumentSelector:
    def __init__(self, data_indexes: Dict[str, dict]):
        self.data_indexes = data_indexes

    def select_with_any_token(self, tokens: List[str]) -> Set[str]:
        """
        Sélectionne les documents contenant au moins un des tokens donnés.
        """
        matched_documents = set()
        for token in tokens:
            matched_documents.update(self.data_indexes['title_index'].get(token, {}).keys())
            matched_documents.update(self.data_indexes['description_index'].get(token, {}).keys())
            matched_documents.update(self.data_indexes['brand_index'].get(token, []))
            matched_documents.update(self.data_indexes['origin_index'].get(token, []))
        return matched_documents

    def select_with_all_tokens(self, tokens: List[str]) -> Set[str]:
        """
        Sélectionne les documents contenant tous les tokens donnés.
        """
        if not tokens:
            return set()
        matched_documents = self.select_with_any_token([tokens[0]])
        for token in tokens[1:]:
            matched_documents &= self.select_with_any_token([token])
        return matched_documents
