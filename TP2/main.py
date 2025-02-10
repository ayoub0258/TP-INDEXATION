import os
from load_data import read_jsonl, parse_product_url
from index_creator import (
    build_inverted_index,
    build_positional_index,
    build_reviews_index,
    build_feature_index,
)
from save_load import save_to_file

def main():
    """
    Main function to process and index product data.
    """
    data_file = "data/products.jsonl"
    output_dir = "indexes"
    os.makedirs(output_dir, exist_ok=True)

    # Load and preprocess data
    records = read_jsonl(data_file)
    for record in records:
        record["product_id"], record["variant"] = parse_product_url(record["url"])

    # Create indexes
    title_index = build_inverted_index(records, "title")
    description_index = build_inverted_index(records, "description")
    title_positional_index = build_positional_index(records, "title")
    description_positional_index = build_positional_index(records, "description")
    review_stats = build_reviews_index(records)
    feature_index = build_feature_index(records)

    # Save indexes
    save_to_file(title_index, os.path.join(output_dir, "title_index.json"))
    save_to_file(description_index, os.path.join(output_dir, "description_index.json"))
    save_to_file(title_positional_index, os.path.join(output_dir, "title_positional_index.json"))
    save_to_file(description_positional_index, os.path.join(output_dir, "description_positional_index.json"))
    save_to_file(review_stats, os.path.join(output_dir, "review_index.json"))
    save_to_file(feature_index, os.path.join(output_dir, "feature_index.json"))

    print("Indexing completed!")

if __name__ == "__main__":
    main()
