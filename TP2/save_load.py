import json

def save_to_file(data, file_path):
    """
    Saves data to a JSON file.

    Args:
        data (dict): Data to save.
        file_path (str): Destination file path.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_from_file(file_path):
    """
    Loads data from a JSON file.

    Args:
        file_path (str): Source file path.

    Returns:
        dict: Loaded data.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
