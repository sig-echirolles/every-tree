import pandas as pd
import yaml # pip install PyYAML

# Lire le fichier CSV
presets_csv = pd.read_csv("presets.csv", sep=";")

# Construire la structure principale du plugin
plugin_yaml = {
    "id": "echirolles-tree",
    "name": "Échirolles Tree",
    "version": "0.2",
    "description": "A customised plugin for Every Door to contribute trees in OpenStreetMap, coming from Every tree plugin by @Binnette",
    "author": "SIG Échirolles (eric.vinouze@echirolles.fr), Binnette (binnette@gmail.com)",
    "icon": "echirolles-tree-logo.svg",
    "homepage": "https://github.com/sig-echirolles/every-tree",
    "source": "https://raw.githubusercontent.com/sig-echirolles/every-tree/refs/heads/main/echirolles-tree.edp",
    "experimental": True,
    "presets": {},
    "kinds": {
        "tree": {
            "matcher": {
                "natural": {
                    "only": ["tree"]
                }
            }
        }
    },
    "fields": {
        "access_i": {
            "type": "combo",
            "key": "access",
            "label": "Access",
            "options": ["yes", "private", "permissive"],
            "labels": ["Public", "Private", "Permissive"]
        },
        "health_phyto_i": {
            "type": "combo",
            "key": "health:phyto_status",
            "label": "Phyto status",
            "options": ["good", "average", "bad"],
            "labels": ["Good", "Average", "Bad"],
        },
        "health_physio_i": {
            "type": "combo",
            "key": "health:physio_status",
            "label": "Physio status",
            "options": ["good", "average", "bad"],
            "labels": ["Good", "Average", "Bad"],
        },
        "species_i": {
            "type": "combo",
            "customValues": True,
            "key": "species",
            "label": "Species",
            "options": presets_csv["species"].dropna().tolist(),
            "labels": presets_csv["name"].dropna().tolist()
        }
    },
    "modes": {
        "tree": {
            "type": "entrances",
            "icon": "tree.svg",
            "name": "Tree",
            "kinds": ["tree"],
            "markers": {
                "tree": {
                    "requiredKeys": ["species"],
                    "icon": "tree-ok.svg",
                    "iconPartial": "tree-ko.svg"
                }
            },
            "primary": {
                "onMainKey": False,
                "preset": "natural/tree",
                "icon": "tree.svg",
                "tooltip": "Tree",
                "adjustZoom": 0.7,
                "kind": "tree",
                "fields": [
                    "health_phyto_i",
                    "health_physio_i",
        }
    }
}

# Fonction pour transformer une ligne CSV en entrée YAML
def transform_row(row):
    terms_list = [term.strip() for term in row["terms"].split(",")]
    return {
        "name": row["name"],
        "terms": terms_list,
        "area": False,
        "tags": {"natural": "tree", "species": row["species"]},
        "addTags": {
            "natural": "tree",
            "genus": row["genus"],
            "species": row["species"]
        },
        "fields": [
            "health_phyto_i",
            "health_physio_i",
    }

# Remplir les presets
for _, row in presets_csv.iterrows():
    plugin_yaml["presets"][row["id"]] = transform_row(row)

# Écrire le fichier YAML
path = "../plugin.yaml"
with open(path, "w", encoding="utf-8") as file:
    file.write("---\n")  # Délimiteur YAML
    yaml.dump(plugin_yaml, file, allow_unicode=True, sort_keys=False)

print(f"✅ Le fichier '{path}' a été généré avec succès.")