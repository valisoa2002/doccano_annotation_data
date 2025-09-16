import json
import random
from sklearn.model_selection import train_test_split

# ----------------------
# 1️⃣ Catégories
categories = [
    "PPN", "Animal", "Appareillage", "Art de la table", "Article de bébé", 
    "Auto-moto", "Bagage", "Beauté", "Bijou", "Bricolage", "Bureau", "Cadeau",
    "Cosmétique", "Déco", "Electronique", "Enfant", "Hygiène", "Industries",
    "Informatique", "Jeu", "Live shopping", "Livre", "Lunettes", "Matelas",
    "Mode", "Papeterie", "Produit local", "Quincaillerie", "Sport"
]

# ----------------------
# 2️⃣ Produits représentatifs par catégorie
category_products = {
    "PPN": ["farine", "sucre", "riz", "pâtes", "huile", "café", "thé"],
    "Animal": ["collier pour chien", "litière pour chat", "nourriture pour poisson", "jouet pour chien", "aquarium"],
    "Appareillage": ["câble HDMI", "multiprise", "adaptateur USB", "chargeur secteur", "switch réseau"],
    "Art de la table": ["assiette", "verre", "couverts", "tasse", "plat à gratin"],
    "Article de bébé": ["biberon", "couche", "gigoteuse", "chaise haute", "jouet d'éveil"],
    "Auto-moto": ["casque moto", "huile moteur", "essuie-glace", "batterie voiture", "pneu"],
    "Bagage": ["valise", "sac à dos", "trousse de toilette", "sac de voyage", "porte-documents"],
    "Beauté": ["parfum", "crème visage", "gel douche", "masque visage", "lotion"],
    "Bijou": ["bague", "collier", "bracelet", "boucles d'oreilles", "montre"],
    "Bricolage": ["marteau", "perceuse", "tournevis", "cloueuse", "scie"],
    "Bureau": ["stylo", "cahier", "agenda", "classeur", "post-it"],
    "Cadeau": ["bougie", "chocolat", "carte cadeau", "peluche", "coffret parfum"],
    "Cosmétique": ["rouge à lèvres", "fond de teint", "vernis", "mascara", "blush"],
    "Déco": ["lampe", "tapis", "cadre", "vase", "horloge murale"],
    "Electronique": ["smartphone", "ordinateur portable", "casque audio", "tablette", "enceinte Bluetooth"],
    "Enfant": ["poupée", "voiture miniature", "lego", "peluche", "jeu éducatif"],
    "Hygiène": ["savon", "dentifrice", "shampoing", "gel antibactérien", "brosse à dents"],
    "Industries": ["chaîne de montage", "machine CNC", "outil industriel", "compresseur", "convoyeur"],
    "Informatique": ["clavier", "souris", "écran", "disque dur", "routeur"],
    "Jeu": ["console", "jeu vidéo", "cartes à jouer", "plateau de jeu", "puzzle"],
    "Live shopping": ["offre flash", "pack promotionnel", "lot surprise", "vente privée", "deal du jour"],
    "Livre": ["roman", "BD", "manuel scolaire", "livre de cuisine", "guide pratique"],
    "Lunettes": ["lunettes de soleil", "lunettes correctrices", "lunettes de protection", "lunettes de sport"],
    "Matelas": ["matelas mousse", "matelas latex", "surmatelas", "coussin", "protège-matelas"],
    "Mode": ["t-shirt", "pantalon", "chaussures", "robe", "veste"],
    "Papeterie": ["carnet", "crayon", "feutres", "papier", "agenda"],
    "Produit local": ["confiture artisanale", "savon local", "huile essentielle", "artisanat", "fromage local"],
    "Quincaillerie": ["vis", "clou", "serrure", "charnière", "outil"],
    "Sport": ["ballon de football", "raquette", "vélo", "tapis de yoga", "gants de boxe"]
}

# ----------------------
# 3️⃣ Variations pour les phrases
demande_types = ["Je veux", "Je cherche", "Je souhaite acheter", "Je voudrais", "Je désire", "J'ai besoin de", "Je souhaite trouver"]
caracteristiques = ["léger", "résistant", "connecté", "élégant", "grand", "portable", "durable", "coloré", "compact", "rapide", "ergonomique"]
usages = ["pour la maison", "pour le travail", "pour le sport", "pour les enfants", "pour les voyages", "pour la cuisine", "pour les loisirs", "pour le bureau"]

# ----------------------
# 4️⃣ Paramètres
phrases_per_category = 350  # ~10 150 phrases

all_data = []

for cat in categories:
    products = category_products[cat]
    for _ in range(phrases_per_category):
        produit = random.choice(products)
        carac_count = random.randint(1, 2)  # 1 ou 2 caractéristiques
        usage_count = random.randint(1, 2)  # 1 ou 2 usages
        
        caracs = random.sample(caracteristiques, carac_count)
        usages_sel = random.sample(usages, usage_count)
        demande = random.choice(demande_types)
        
        text = f"{demande} un {produit} {' '.join(caracs)} {' '.join(usages_sel)}"
        
        # labels NER
        labels = []
        for c in [produit] + caracs + usages_sel:
            start = text.find(c)
            end = start + len(c)
            if c == produit:
                labels.append([start, end, "PRODUIT"])
            elif c in caracs:
                labels.append([start, end, "CARACTERISTIQUE"])
            else:
                labels.append([start, end, "USAGE"])
        
        all_data.append({"text": text, "labels": labels, "category": cat})

# ----------------------
# 5️⃣ Shuffle et split train/val/test
random.shuffle(all_data)
train, temp = train_test_split(all_data, test_size=0.3, random_state=42)
val, test = train_test_split(temp, test_size=0.5, random_state=42)

# ----------------------
# 6️⃣ Sauvegarde JSONL
def save_jsonl(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for entry in data:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

save_jsonl(train, "../data.dataset_train.jsonl")
save_jsonl(val, "../data/dataset_val.jsonl")
save_jsonl(test, "../data/dataset_test.jsonl")

print(f"✅ Dataset NER réaliste généré !")
print(f"Train: {len(train)}, Validation: {len(val)}, Test: {len(test)} phrases")
