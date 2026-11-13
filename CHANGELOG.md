# Changelog

Ce fichier décrit les principales évolutions d’EHK–SCCI Core.

## [Unreleased]

### Prévu

- Validation des schémas JSON.
- Documentation des interfaces et conventions mathématiques.
- Tests supplémentaires des cas limites et des erreurs.
- Benchmarks reproductibles et mesures sur plusieurs environnements.
- Publication du rapport de couverture sur GitHub Pages.

## [0.1.0]

Version initiale du prototype de recherche, préparée pour une
première release GitHub et un archivage Zenodo.

### Ajouté

- Module de calcul Wasserstein-1 :
  `src/ehk_scci/curvature/w1_core.py`.
- Module discriminant :
  `src/ehk_scci/spectral/discriminant_core.py`.
- Module de politique de supervision :
  `src/ehk_scci/safety/policy_core.py`.
- Suite initiale de 49 tests unitaires :
  - 17 tests du module discriminant ;
  - 18 tests du module de politique ;
  - 14 tests du module W1.
- Configuration du paquet et de ses dépendances dans `pyproject.toml`.
- Workflow GitHub Actions pour les tests et la couverture.
- Génération des rapports de couverture HTML et XML.
- Génération d’un rapport de tests JUnit.
- Seuil minimal de couverture configuré à 70 %.
- Archivage des rapports comme artefacts CI avec une rétention
  configurée à 14 jours.
- README décrivant l’installation, les tests, le périmètre
  et les limites du prototype.

### Vérifications rapportées

- Exécution locale sous Android/Termux :
  `49 passed in 0.73s`.
- Première exécution GitHub Actions réussie sur le commit `4cbe1d0`,
  avec Python 3.11 sous Ubuntu.

La durée locale correspond à une exécution particulière et ne constitue
pas un benchmark matériel standardisé.

### Traçabilité initiale

- `83b67a9` : introduction du code et des 49 tests unitaires.
- `4cbe1d0` : ajout du workflow de tests, de couverture
  et de génération des rapports.

### Limites

- Prototype de recherche en développement.
- Aucune certification de sûreté ou conformité NIST revendiquée.
- Aucune validation industrielle ou clinique établie par cette version.
- La réussite des tests et le respect du seuil de couverture
  ne constituent pas une validation scientifique du cadre.
- La validation des schémas JSON, les benchmarks cyberphysiques
  complets et la publication GitHub Pages ne sont pas encore activés.
- Le DOI logiciel sera indiqué après confirmation de l’archivage Zenodo.
