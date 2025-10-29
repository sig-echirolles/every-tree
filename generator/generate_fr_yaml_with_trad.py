import pandas as pd
import yaml # pip install PyYAML

# Lire les fichiers CSV
presets_csv = pd.read_csv("presets.csv", sep=";")
trad_csv = pd.read_csv("trad.csv", sep=";")  # contient les colonnes 'id' et 'fr'

# Créer un dictionnaire de traduction
trad_dict = dict(zip(trad_csv["id"], trad_csv["fr"]))

# Initialiser la structure YAML
yaml_content = {
    "name": "Échirolles Tree",
    "presets": {},
    "fields": {
        "access_i": {"label": "Accès", "labels": ["Public", "Privé", "Permissif"]},
        "health_phyto_i": {
            "label": "État phyto",
            "labels": ["Bon", "Moyen", "Mauvais"],
        },
        "health_physio_i": {
            "label": "État physio",
            "labels": ["Bon", "Moyen", "Mauvais"],
        },
        "age_i": {"label": "Âge", "labels": ["Jeune", "Semi-mature", "Mature"]},
        "species_i": {"label": "Espèce", "labels": []},
    },
    "modes": {"tree": {"name": "Arbre", "primary": {"tooltip": "Arbre"}}},
}

# Utiliser les noms traduits si disponibles
for _, row in presets_csv.iterrows():
    preset_id = row["id"]
    nom_fr = trad_dict.get(preset_id)
    if not nom_fr:
        print(f"⚠️ Aucun nom français trouvé pour '{preset_id}' → utilisation de row['name']")
        nom_fr = row["name"]
    yaml_content["presets"][preset_id] = {"name": nom_fr}

# Traduire les labels des espèces
translated_species_labels = []
for species_id in presets_csv["species"]:
    label_fr = trad_dict.get(species_id)
    if not label_fr:
        print(f"⚠️ Aucun nom français trouvé pour l'espèce '{species_id}' → label conservé tel quel")
        label_fr = species_id
    translated_species_labels.append(label_fr)

yaml_content["fields"]["species_i"]["labels"] = translated_species_labels

# Écrire le fichier YAML
path = "../langs/fr.yaml"
with open(path, "w", encoding="utf-8") as file:
    file.write("---\n")
    yaml.dump(yaml_content, file, allow_unicode=True, sort_keys=False)

print(f"✅ [Avec traduction] Le fichier '{path}' a été généré avec succès.")