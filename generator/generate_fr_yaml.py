import pandas as pd
import yaml # pip install PyYAML

# Lire le fichier CSV principal
presets_csv = pd.read_csv("presets.csv", sep=";")

# Initialiser la structure YAML
yaml_content = {
    "name": "Échirolles Tree",
    "presets": {},
    "fields": {
        "access_i": {"label": "Accès", "labels": ["Public", "Privé", "Permissif"]},
        "health_i": {"label": "État phyto", "labels": ["Bon", "Moyen", "Mauvais"]},
        "age_i": {"label": "Âge", "labels": ["Jeune", "Semi-mature", "Mature"]},
        "species_i": {"label": "Espèce", "labels": []},
    },
    "modes": {"tree": {"name": "Arbre", "primary": {"tooltip": "Arbre"}}},
}

# Utiliser les noms tels qu’ils sont dans presets.csv
for _, row in presets_csv.iterrows():
    yaml_content["presets"][row["id"]] = {"name": row["name"]}

# Utiliser les noms d’espèces tels quels
yaml_content["fields"]["species_i"]["labels"] = presets_csv["species"].tolist()

# Écrire le fichier YAML
path = "../langs/fr.yaml"
with open(path, "w", encoding="utf-8") as file:
    file.write("---\n")
    yaml.dump(yaml_content, file, allow_unicode=True, sort_keys=False)

print(f"✅ [Sans traduction] Le fichier '{path}' a été généré avec succès.")