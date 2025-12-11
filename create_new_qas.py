import json

input_path = "data/qas_v2.json"
output_path = "data/qas_ds_ocr.json"

with open(input_path, "r") as f:
    data = json.load(f)

filtered = [
    obj for obj in data
    if obj["doc_name"].startswith("textbook/") or obj["doc_name"].startswith("news/")
]

with open(output_path, "w") as f:
    json.dump(filtered, f, indent=2)

print(f"Kept {len(filtered)} items out of {len(data)}")
