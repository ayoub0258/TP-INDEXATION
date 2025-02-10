import json
import re

def read_jsonl(file_path):
    """
    Loads data from a JSONL file.

    Args:
        file_path (str): The file path.

    Returns:
        list: A list of dictionaries.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return [json.loads(line.strip()) for line in file]

def parse_product_url(url):
    """
    Parses the product ID and variant from a URL.

    Args:
        url (str): The product URL.

    Returns:
        tuple: (product_id, variant) or (None, None) if not found.
    """
    pattern = r'/product/(\d+)(?:\?variant=(.*))?'
    match = re.search(pattern, url)
    return (match.group(1), match.group(2)) if match else (None, None)