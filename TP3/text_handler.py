import re
import nltk
from nltk.corpus import stopwords
from typing import List, Dict

# Télécharger les stopwords de NLTK
nltk.download("stopwords")
STOPWORDS = set(stopwords.words("english"))

class TextHandler:
    @staticmethod
    def tokenize(text: str) -> List[str]:
        """
        Tokenise un texte en supprimant les stopwords et en ne gardant que les mots alphabétiques.
        """
        return [word for word in re.findall(r'\b\w+(?:-\w+)*\b', text.lower()) if word.isalpha() and word not in STOPWORDS]

    @staticmethod
    def expand_tokens(tokens: List[str], synonyms_dict: Dict[str, List[str]]) -> List[str]:
        """
        Étend les tokens avec des synonymes fournis dans un dictionnaire.
        """
        expanded_tokens = set(tokens)
        for token in tokens:
            if token in synonyms_dict:
                expanded_tokens.update(synonyms_dict[token])
        return list(expanded_tokens)
