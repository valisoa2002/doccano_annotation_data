import json

input_file = "../data/validation_data.jsonl"
output_file = "../data/validation.jsonl"

with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
    for line in f_in:
        obj = json.loads(line)
        new_obj = {
            "text": obj["text"],
            "label": obj["labels"]  # renommer la clé
        }
        # ⚠️ on supprime "category" car Doccano ne l’attend pas pour le NER
        f_out.write(json.dumps(new_obj, ensure_ascii=False) + "\n")

print("✅ Conversion terminée :", output_file)
