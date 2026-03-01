import json

INPUT_FILE = "core_set.json"
OUTPUT_FILE = "core_set_clean.json"

def remove_deck_attribute():
    # Load the JSON data
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Ensure it's a list of objects
    if not isinstance(data, list):
        raise ValueError("Expected JSON root to be a list")

    # Remove the 'deck' attribute from each item
    for item in data:
        if isinstance(item, dict):
            item.pop("deck", None)

    # Save the cleaned data
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Cleaned file saved as '{OUTPUT_FILE}'")

if __name__ == "__main__":
    remove_deck_attribute()

