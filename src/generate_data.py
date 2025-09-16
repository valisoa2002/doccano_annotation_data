import json
import random

# Listes d'exemples
produits = ["ordinateur portable", "smartphone", "sac à dos", "montre connectée", "canapé", "table", "chaussures", "casque audio"]
caracteristiques = ["avec beaucoup de RAM", "avec un bon appareil photo", "léger et résistant", "avec GPS intégré", "confortable", "design moderne", "en cuir", "batterie longue durée"]
usages = ["pour le travail", "pour la randonnée", "pour le sport", "pour le salon", "pour la maison", "pour les voyages", "pour les étudiants"]
demande_types = ["Je veux", "Je cherche", "Je souhaite acheter", "Je voudrais", "Je désire"]

# Nombre de phrases à générer
nb_phrases = 5000

dataset = []

for _ in range(nb_phrases):
    produit = random.choice(produits)
    caracteristique = random.choice(caracteristiques)
    usage = random.choice(usages)
    demande = random.choice(demande_types)
    
    # Construire la phrase
    text = f"{demande} un {produit} {caracteristique} {usage}"
    
    # Définir les labels pour Doccano (sequence labeling)
    start_produit = text.find(produit)
    end_produit = start_produit + len(produit)
    
    start_carac = text.find(caracteristique)
    end_carac = start_carac + len(caracteristique)
    
    start_usage = text.find(usage)
    end_usage = start_usage + len(usage)
    
    labels = [
        [start_produit, end_produit, "PRODUIT"],
        [start_carac, end_carac, "CARACTERISTIQUE"],
        [start_usage, end_usage, "USAGE"]
    ]
    
    dataset.append({"text": text, "labels": labels})

# Sauvegarder au format JSONL
with open("dataset_doccano.jsonl", "w", encoding="utf-8") as f:
    for entry in dataset:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

print(f"{nb_phrases} phrases générées et sauvegardées dans dataset_doccano.jsonl")
