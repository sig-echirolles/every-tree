# 🌳 Échirolles Tree 🌲

A plugin for [`Every Door`](https://every-door.app/) to contribute 🌳 **trees** from the city of [Échirolles](https://en.wikipedia.org/wiki/%C3%89chirolles) to OpenStreetMap.

![Échirolles Tree Logo](assets/echirolles-tree-logo.png)

## ⭐ Features

### 👀 Quick survey of tree species

- Trees with known species are **green 🟩**
- Others are in **brown 🟫**

![Main](assets/echirolles-tree-main.png)

### 🌿 Tree species presets adapted for Échirolles

The plugin includes a set of identified species and species that are planned to be planted, making it easier to tag trees species in Échirolles and nearby.

![Presets](assets/echirolles-tree-species.png)

### 🩺 New `health:phyto_status` `health:physio_status` tags proposal

These proposed tags aim to collect field data to alert tree owners about potential health issues of their trees. More details are available on the [dedicated wiki page](https://wiki.openstreetmap.org/wiki/Echirolles/Suivi_arbres) (in French) of our tree referential.

![Form](assets/echirolles-tree-form.png)

## 🛠️ How to create the plugin file

### Using bash

```bash
# Remove old plugin file
rm -f echirolles-tree.edp
# Create the plugin archive
zip -r echirolles-tree.edp icons/ langs/ LICENSE plugin.yaml
```

### Using PowerShell

```powershell
Remove-Item .\echirolles-tree.edp
Compress-Archive -Path icons, langs, LICENSE, plugin.yaml, README.md -DestinationPath echirolles-tree.edp
```

## 📥 Installation

📲 Scan this QR code with `Every Door` version **6 or later**:

![QR Code](assets/qr-code.png)

Or [⬇️ download the plugin here](https://raw.githubusercontent.com/sig-echirolles/every-tree/refs/heads/main/echirolles-tree.edp).

[🔍 More information on installation](https://every-door.app/plugins/install/).

## 🌱 About

- `echirolles-tree` is a fork of the [every-tree](https://github.com/Binnette/every-tree) plugin, originally created by [Binnette](https://github.com/Binnette/). Huge thanks to him!
- This plugin was developed to meet the needs of the city of [Échirolles](https://www.echirolles.fr/).
