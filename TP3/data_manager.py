import json
import os

class DataManager:
    def __init__(self, data_directory: str = "./"):
        self.data_directory = data_directory
        self.data_indexes = self._load_data_indexes()
        self.product_catalog = self._load_product_catalog()

    def _load_data_indexes(self):
        """
        Charge tous les fichiers d'index disponibles.
        """
        index_files = [
            "data/brand_index.json",
            "data/description_index.json",
            "data/domain_index.json",
            "data/origin_index.json",
            "data/origin_synonyms.json",
            "data/reviews_index.json",
            "data/title_index.json"
        ]
        return {self._extract_index_name(file): self._load_json_file(file) for file in index_files}

    def _load_json_file(self, file_path):
        """
        Charge un fichier JSON et retourne son contenu.
        """
        full_path = os.path.join(self.data_directory, file_path)
        with open(full_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _load_product_catalog(self):
        """
        Charge les produits à partir d'un fichier JSONL.
        """
        products = {}
        file_path = os.path.join(self.data_directory, "data/products.jsonl")
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                product = json.loads(line)
                products[product["url"]] = product
        return products

    @staticmethod
    def _extract_index_name(file_path):
        """
        Extrait le nom de l'index depuis le nom de fichier.
        """
        return os.path.basename(file_path).replace(".json", "")
