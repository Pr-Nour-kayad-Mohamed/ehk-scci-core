# EHK–SCCI Core

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24184737.svg)](https://doi.org/10.5281/zenodo.24184737)

Noyau logiciel de recherche pour le calcul géométrique sur graphes, le diagnostic discriminant et les politiques de supervision.

**Auteur :** NOUR KAYAD Mohamed  
**Affiliation :** Ministère de l’Éducation nationale et de la Formation professionnelle (MENFOP), République de Djibouti  
**Version :** 0.1.0  
**Licence :** Apache-2.0

## Statut

Prototype de recherche en développement. Les tests et l’intégration continue vérifient les comportements couverts par la suite de tests ; ils ne constituent ni une certification de sûreté, ni une validation industrielle, ni une démonstration de performance sur un système physique réel.

## Modules

| Module | Emplacement | Périmètre |
|---|---|---|
| W1 | `src/ehk_scci/curvature/w1_core.py` | Transport Wasserstein-1 sur graphes |
| Discriminant | `src/ehk_scci/spectral/discriminant_core.py` | Fonctions discriminantes |
| Politique | `src/ehk_scci/safety/policy_core.py` | Règles de décision et supervision |

## Tests

```bash
python -m pip install -e ".[test]"
python -m pytest -v
