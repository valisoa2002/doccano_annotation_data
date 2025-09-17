import json
import random
from sklearn.model_selection import train_test_split

# ----------------------
# 1️⃣ Catégories générales + food
all_categories = [
    "PPN", "Animal", "Appareillage", "Art de la table", "Article de bébé", 
    "Auto-moto", "Bagage", "Beauté", "Bijou", "Bricolage", "Bureau", "Cadeau",
    "Cosmétique", "Déco", "Electronique", "Enfant", "Hygiène", "Industries",
    "Informatique", "Jeu", "Live shopping", "Livre", "Lunettes", "Matelas",
    "Mode", "Papeterie", "Produit local", "Quincaillerie", "Sport",


    "Viennoiserie", "Plat", "Hot Drinks", "Pâte", "Pâtisserie", "Vegan", 
    "Végétarien", "Local", "Fast-food", "Entrée", "Friandise", "Alcool", 
    "Sans Porc", "Dessert", "Grillade", "Cuisine", "Boisson"
]

# ----------------------
# 2️⃣ Produits représentatifs
category_products = {
    # --- Pour les produits consommables ---
    "PPN": ["farine", "sucre", "riz", "pâtes", "huile", "café", "riz"],
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
    "Sport": ["ballon de football", "raquette", "vélo", "tapis de yoga", "gants de boxe"],

    # --- Pour les catégories alimentaires ---
    "Viennoiserie": ["croissant", "pain au chocolat", "brioche", "chausson aux pommes"],
    "Plat": ["riz cantonais", "poulet rôti", "pâtes bolognaises", "curry de légumes"],
    "Hot Drinks": ["café", "thé", "chocolat chaud", "cappuccino"],
    "Pâte": ["spaghetti", "penne", "raviolis", "tagliatelles"],
    "Pâtisserie": ["éclair", "tarte aux fruits", "millefeuille", "macaron"],
    "Vegan": ["salade de quinoa", "tofu grillé", "wrap vegan", "légumes sautés"],
    "Végétarien": ["pizza végétarienne", "omelette aux légumes", "ratatouille"],
    "Local": ["romazava", "ravitoto", "mokary", "koba"],
    "Fast-food": ["burger", "pizza", "sandwich", "tacos"],
    "Entrée": ["soupe", "salade", "bruschetta", "charcuterie"],
    "Friandise": ["bonbon", "caramel", "nougat", "réglisse"],
    "Alcool": ["vin rouge", "bière", "rhum", "whisky"],
    "Sans Porc": ["poulet rôti", "poisson grillé", "tajine végétarien"],
    "Dessert": ["glace", "mousse au chocolat", "tiramisu", "crème brûlée"],
    "Grillade": ["brochette de bœuf", "côtelette d’agneau", "poisson grillé"],
    "Cuisine": ["épices", "sauce soja", "huile d’olive", "curry"],
    "Boisson": ["jus d’orange", "eau minérale", "soda", "cocktail"]
}

# ----------------------
# 3️⃣ Variations pour les phrases
demande_types = ["Je veux", "Je cherche", "Je souhaite acheter", "Je voudrais", "Je désire", "J'ai besoin de", "Je souhaite trouver"]
usages = ["pour la maison", "pour le travail", "pour le sport", "pour les enfants", "pour les voyages", "pour la cuisine", "pour les loisirs", "pour le bureau"]
caracteristiques = ["léger", "résistant", "élégant", "grand", "portable", "durable", "coloré", "compact"]
usages = ["pour la maison", "pour le travail", "pour le sport", "pour les enfants", "pour les voyages", "pour la cuisine"]
marques = ["Samsung", "Apple", "Nike", "Adidas", "Sony", "LG", "Dell", "Nespresso", "Nestlé"]
vendeurs = ["Shoprite", "Score", "Leader Price", "Amazon", "Jumia", "Carrefour"]
couleurs = ["rouge", "bleu", "noir", "blanc", "vert"]
tailles = ["S", "M", "L", "XL", "XXL"]
etats = ["neuf", "occasion"]
budgets = ["5.000Ar", "10.000Ar", "20.000Ar", "50.000Ar", "100.000Ar"]

la
# 4️⃣ Templates
templates = [
    "{demande} un {produit} {carac} {usage}",
    "Je voudrais un {produit} de la marque {marque}",
    "Je cherche un {produit} disponible chez {vendeur}",
    "J’ai un budget de {budget} pour un {produit}",
    "Est-ce que vous avez un {produit} {couleur} en taille {taille} ?",
    "Je veux un {produit} en état {etat}",
]

# ----------------------
# 5️⃣ Génération
phrases_per_category = 350  # ~ 30k phrases

all_data = []

for cat in all_categories:
    products = category_products.get(cat, ["produit générique"])
    for _ in range(phrases_per_category):
        produit = random.choice(products)
        carac = random.choice(caracteristiques)
        usage = random.choice(usages)
        marque = random.choice(marques)
        vendeur = random.choice(vendeurs)
        budget = random.choice(budgets)
        couleur = random.choice(couleurs)
        taille = random.choice(tailles)
        etat = random.choice(etats)

        template = random.choice(templates)
        text = template.format(
            demande=random.choice(demande_types),
            produit=produit,
            carac=carac,
            usage=usage,
            marque=marque,
            vendeur=vendeur,
            budget=budget,
            couleur=couleur,
            taille=taille,
            etat=etat
        )

        # labels NER
        labels = []
        for ent, tag in [
            (produit, "PRODUIT"), (carac, "CARACTERISTIQUE"), (usage, "USAGE"),
            (marque, "MARQUE"), (vendeur, "VENDEUR"), (budget, "BUDGET"),
            (couleur, "COULEUR"), (taille, "TAILLE"), (etat, "ETAT")
        ]:
            start = text.find(ent)
            if start != -1:
                end = start + len(ent)
                labels.append([start, end, tag])

        all_data.append({"text": text, "labels": labels, "category": cat})

# ----------------------
# 7️⃣ Shuffle + split
random.shuffle(all_data)
train, temp = train_test_split(all_data, test_size=0.3, random_state=42)
val, test = train_test_split(temp, test_size=0.5, random_state=42)

# ----------------------
# 8️⃣ Sauvegarde JSONL
def save_jsonl(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for entry in data:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

save_jsonl(train, "../data/train_data.jsonl")
save_jsonl(val, "../data/validation_data.jsonl")
save_jsonl(test, "../data/test_data.jsonl")

print(f"✅ Dataset généré avec {len(all_data)} phrases")
print(f"Train: {len(train)}, Validation: {len(val)}, Test: {len(test)}")
