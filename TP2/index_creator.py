import string
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOPWORDS = set(stopwords.words("english"))

def process_text(text):
    """
    Tokenizes and cleans text by removing punctuation and stopwords.

    Args:
        text (str): Input text.

    Returns:
        list: A list of cleaned tokens.
    """
    translator = str.maketrans("", "", string.punctuation)
    tokens = word_tokenize(text.lower().translate(translator))
    return [token for token in tokens if token not in STOPWORDS]

def build_inverted_index(records, key):
    """
    Creates an inverted index for a specified field.

    Args:
        records (list): List of product dictionaries.
        key (str): The field to index.

    Returns:
        dict: Inverted index.
    """
    index = defaultdict(set)
    for record in records:
        tokens = process_text(record.get(key, ""))
        for token in tokens:
            index[token].add(record["url"])
    return {token: list(urls) for token, urls in index.items()}

def build_positional_index(records, key):
    """
    Creates a positional index for a specified field.

    Args:
        records (list): List of product dictionaries.
        key (str): The field to index.

    Returns:
        dict: Positional index.
    """
    index = defaultdict(lambda: defaultdict(list))
    for record in records:
        tokens = process_text(record.get(key, ""))
        for position, token in enumerate(tokens):
            index[token][record["url"]].append(position)
    return index

def build_reviews_index(records):
    """
    Computes review statistics for each product.

    Args:
        records (list): List of product dictionaries.

    Returns:
        dict: Review statistics indexed by URL.
    """
    index = {}
    for record in records:
        reviews = record.get("product_reviews", [])
        ratings = [review.get("rating") for review in reviews if "rating" in review]
        index[record["url"]] = {
            "total_reviews": len(ratings),
            "average_score": round(sum(ratings) / len(ratings), 2) if ratings else None,
            "last_score": ratings[-1] if ratings else None,
        }
    return index

def build_feature_index(records):
    """
    Builds an inverted index for product features.

    Args:
        records (list): List of product dictionaries.

    Returns:
        dict: Feature index.
    """
    index = defaultdict(lambda: defaultdict(set))
    for record in records:
        for feature, value in record.get("product_features", {}).items():
            index[feature][value.lower()].add(record["url"])
    return {feature: {val: list(urls) for val, urls in feature_dict.items()} for feature, feature_dict in index.items()}
