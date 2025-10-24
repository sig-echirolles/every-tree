import pandas as pd

# Lire le fichier CSV
presets_csv = pd.read_csv("presets.csv", sep=";")

# Initialiser la structure YAML
yaml_content = {
    "name": "Every Tree Echirolles",
    "presets": {},
    "fields": {
        "access_i": {"label": "Accès", "labels": ["Public", "Privé", "Permissif"]},
        "health_i": {"label": "État phyto", "labels": ["Bon", "Moyen", "Mauvais"]},
        "age_i": {"label": "Âge", "labels": ["Jeune", "Semi-mature", "Mature"]},
        "species_i": {"label": "Espèce", "labels": []},
    },
    "modes": {"tree": {"name": "Arbre", "primary": {"tooltip": "Arbre"}}},
}

# Remplir les noms des presets
for _, row in presets_csv.iterrows():
    yaml_content["presets"][f"{row['id']}"] = {"name": row["name"]}

# Remplir les labels des espèces
species_labels = presets_csv["species"].tolist()
yaml_content["fields"]["species_i"]["labels"] = species_labels

# Écrire le résultat dans un fichier YAML
with open("../langs/fr.yaml", "w") as file:
    file.write("---\n")
    file.write(f'name: "{yaml_content["name"]}"\n')
    for preset_id, preset in yaml_content["presets"].items():
        file.write(f'presets.{preset_id}.name: "{preset["name"]}"\n')
    for field_id, field in yaml_content["fields"].items():
        file.write(f'fields.{field_id}.label: "{field["label"]}"\n')
        file.write(f"fields.{field_id}.labels:\n")
        for label in field["labels"]:
            file.write(f'  - "{label}"\n')
    file.write(f'modes.tree.name: "{yaml_content["modes"]["tree"]["name"]}"\n')
    file.write(
        f'modes.tree.primary.tooltip: "{yaml_content["modes"]["tree"]["primary"]["tooltip"]}"\n'
    )

print("Le fichier YAML a été généré avec succès.")
