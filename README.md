# Woodle
Outil pour transformer un fichier de notes Moodle (xlsx) en fichier SNW (csv)

# Installation

## Pré-requis

* Python >=3.5
* pip
* Git

## Installation avec pip

    pip install git+https://github.com/Epithumia/Woodle.git

# Utilisation

Cet utilitaire permet de passer les notes de Moodle à SNW

Utilisation seule :

```
woodle <fichier moodle> <fichier snw> <colonne>

Options:
  -b BAREME   Barême.
  -h, --help  Affiche ce message d'aide et termine.
```

**Attention : le fichier SNW doit exister et avoir le bon entête (le télécharger depuis SNW avant).**

Exemple :

    woodle "Bilan S4 Notes.xlsx" "Extract_SN_Web.csv" "Admi/Sys/Res CC (Brut)"

# Versions

* 0.1 Version initiale
