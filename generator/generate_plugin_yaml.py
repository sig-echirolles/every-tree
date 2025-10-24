import pandas as pd

# Lire le fichier CSV
presets_csv = pd.read_csv("presets.csv", sep=";")

# Initialiser la structure YAML
presets_yaml = {"presets": {}}


# Fonction pour transformer une ligne CSV en entrée YAML
def transform_row(row):
    # Diviser les termes en une liste
    terms_list = [term.strip() for term in row["terms"].split(",")]

    entry = {
        "name": row["name"],
        "terms": terms_list,
        "area": False,
        "tags": {"natural": "tree", "species": row["species"]},
        "addTags": {
            "natural": "tree",
            "genus": row["genus"],
            "species": row["species"],
        },
        "fields": [
            "species_i",
            "genus",
            "leaf_type",
            "leaf_cycle",
            "height",
            "circumference",
            "health_i",
            # "age_i",
            # "access_i",
            # "description",
            "@natural/tree",
        ],
    }
    return entry


# Remplir la structure YAML
for _, row in presets_csv.iterrows():
    presets_yaml["presets"][row["id"]] = transform_row(row)

# Écrire le résultat dans un fichier YAML avec un format personnalisé pour 'terms' et 'fields'
with open("../plugin.yaml", "w") as file:  # Le mode 'w' écrase le fichier s'il existe
    file.write(f"---\n")
    file.write(f"id: echirolles-tree\n")
    file.write(f"name: Échirolles Tree\n")
    file.write(f"version: 0.2\n")
    file.write(
        f"description: A customised plugin for Every Door to contribute trees in OpenStreetMap, coming from Every tree plugin by @Binnette\n"
    )
    file.write(
        f"author: SIG Échirolles (eric.vinouze@echirolles.fr), Binnette (binnette@gmail.com)\n"
    )
    file.write(f"icon: echirolles-tree-logo.svg\n")
    file.write(f"homepage: https://github.com/sig-echirolles/every-tree\n")
    file.write(
        f"source: https://raw.githubusercontent.com/sig-echirolles/every-tree/refs/heads/main/echirolles-tree.edp\n"
    )
    file.write(f"experimental: true\n\n")

    file.write(f"#-----------------------------------------\n")
    file.write(f"# Début des presets\n")
    file.write(f"#-----------------------------------------\n")

    file.write("presets:\n")
    for preset_id, preset in presets_yaml["presets"].items():
        file.write(f"  {preset_id}:\n")
        file.write(f'    name: "{preset["name"]}"\n')
        file.write(f"    terms: {preset['terms']}\n")
        file.write(f"    area: {preset['area']}\n")
        file.write(f"    tags:\n")
        file.write(f"      natural: {preset['tags']['natural']}\n")
        file.write(f'      species: "{preset["tags"]["species"]}"\n')
        file.write(f"    addTags:\n")
        file.write(f"      natural: {preset['addTags']['natural']}\n")
        file.write(f'      genus: "{preset["addTags"]["genus"]}"\n')
        file.write(f'      species: "{preset["addTags"]["species"]}"\n')
        file.write(f"    fields:\n")
        for field in preset["fields"]:
            if field == "@natural/tree":
                file.write(f'      - "{field}"\n')
            else:
                file.write(f"      - {field}\n")

    file.write(f"#-----------------------------------------\n")
    file.write(f"# Fin des presets\n")
    file.write(f"#-----------------------------------------\n")

    file.write("\nkinds:\n")
    file.write("  tree:\n")
    file.write("      matcher:\n")
    file.write("        natural:\n")
    file.write("            only: [tree]\n")

    # Ajouter la section finale pour les champs et les modes
    file.write("\nfields:\n")
    file.write("  access_i:\n")
    file.write("    type: combo\n")
    file.write("    key: access\n")
    file.write("    label: Access\n")
    file.write("    options:\n")
    file.write('      - "yes"\n')
    file.write('      - "private"\n')
    file.write('      - "permissive"\n')
    file.write("    labels:\n")
    file.write('      - "Public"\n')
    file.write('      - "Private"\n')
    file.write('      - "Permissive"\n')

    file.write("  health_i:\n")
    file.write("    type: combo\n")
    file.write("    key: health:phyto_status\n")
    file.write("    label: Phyto status\n")
    file.write("    options:\n")
    file.write('      - "good"\n')
    file.write('      - "average"\n')
    file.write('      - "bad"\n')
    file.write("    labels:\n")
    file.write('      - "Good"\n')
    file.write('      - "Average"\n')
    file.write('      - "Bad"\n')

    # file.write("  age_i:\n")
    # file.write("    type: combo\n")
    # file.write("    key: age\n")
    # file.write("    label: Age\n")
    # file.write("    options:\n")
    # file.write('      - "young"\n')
    # file.write('      - "semi-mature"\n')
    # file.write('      - "mature"\n')
    # file.write("    labels:\n")
    # file.write('      - "Young"\n')
    # file.write('      - "Semi-mature"\n')
    # file.write('      - "Mature"\n')

    file.write("  species_i:\n")
    file.write("    type: combo\n")
    file.write("    customValues: true\n")
    file.write("    key: species\n")
    file.write("    label: Species\n")
    file.write("    options:\n")
    for _, row in presets_csv.iterrows():
        file.write(f'      - "{row["species"]}"\n')
    file.write("    labels:\n")
    for _, row in presets_csv.iterrows():
        file.write(f'      - "{row["name"]}"\n')

    file.write("\nmodes:\n")
    file.write("  tree:\n")
    file.write("    type: entrances\n")
    file.write("    icon: tree.svg\n")
    file.write("    name: Tree\n")
    file.write("    kinds: [fig, tree]\n")
    file.write("    markers:\n")
    file.write("      fig:\n")
    file.write("        icon: fig.svg\n")
    file.write("      tree:\n")
    file.write("        requiredKeys: [species]\n")
    file.write("        icon: tree-ok.svg\n")
    file.write("        iconPartial: tree-ko.svg\n")
    file.write("    primary:\n")
    file.write("      onMainKey: false\n")
    file.write("      preset: natural/tree\n")
    file.write("      icon: tree.svg\n")
    file.write("      tooltip: Tree\n")
    file.write("      adjustZoom: 0.7\n")
    file.write("      kind: tree\n")
    file.write("      fields:\n")
    file.write("        - species_i\n")
    file.write("        - genus\n")
    file.write("        - leaf_type\n")
    file.write("        - leaf_cycle\n")
    file.write("        - height\n")
    file.write("        - circumference\n")
    file.write("        - health_i\n")

print("Le fichier YAML a été généré avec succès.")
