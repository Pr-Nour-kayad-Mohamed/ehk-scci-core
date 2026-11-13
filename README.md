# EHK–SCCI Core
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24184737.svg)](https://doi.org/10.5281/zenodo.24184737)
Noyau logiciel de recherche pour le calcul géométrique sur graphes,
le diagnostic discriminant et les politiques de supervision.

Auteur : NOUR KAYAD Mohamed 
Affiliation :Ministere de l'Éducation Nationale et de la Formation Professionnelle (MENFOP),république de djibouti  MENFOP — Djibouti  
Version initiale : 0.1.0

## Statut du projet

EHK–SCCI Core est un prototype de recherche en développement.

Les tests unitaires et l’intégration continue vérifient les comportements
couverts par la suite de tests. Ils ne constituent pas une certification
de sûreté, une validation industrielle ou une démonstration de performance
sur un système physique réel.

Le dépôt ne doit pas être utilisé seul comme mécanisme de protection
d’un équipement critique.

## Modules actuellement présents

| Module | Emplacement | Périmètre |
|---|---|---|
| W1 | `src/ehk_scci/curvature/w1_core.py` | Calculs de transport Wasserstein-1 et cas de référence sur graphes |
| Discriminant | `src/ehk_scci/spectral/discriminant_core.py` | Calcul et vérification des fonctions discriminantes implémentées |
| Politique | `src/ehk_scci/safety/policy_core.py` | Règles de décision et politiques de supervision implémentées |

Les définitions exactes, hypothèses et conventions doivent être consultées
dans le code et les tests associés.

## Organisation du dépôt

```text
ehk-scci-core/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── ehk_scci/
│       ├── curvature/
│       │   └── w1_core.py
│       ├── safety/
│       │   └── policy_core.py
│       └── spectral/
│           └── discriminant_core.py
├── tests/
│   ├── test_discriminant_core.py
│   ├── test_policy_core.py
│   └── test_w1_core.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## Prérequis

Le projet déclare Python 3.10 ou supérieur dans `pyproject.toml`.

La configuration CI actuelle utilise Python 3.11 sous Ubuntu.
Les versions minimales des dépendances sont déclarées dans
`pyproject.toml`.

L’exécution locale rapportée sous Termux constitue un résultat distinct
de l’exécution CI sous Ubuntu. Elle ne démontre pas une compatibilité
universelle avec toutes les versions de Python ou architectures.

## Installation

Depuis la racine du dépôt :

```bash
python -m pip install -e ".[test]"
```

Cette commande installe le paquet en mode éditable et les dépendances
de test.

L’installation de certaines dépendances peut nécessiter une procédure
spécifique selon la plateforme, notamment sous Android/Termux.

## Exécuter les tests

Après installation du paquet :

```bash
python -m pytest -v
```

Pour reproduire la commande utilisée dans l’environnement Termux
déjà configuré :

```bash
PYTHONPATH=src python -m pytest -v --disable-warnings
```

### Résultat initial rapporté

La suite initiale comprend 49 tests :

- 17 tests du module discriminant ;
- 18 tests du module de politique ;
- 14 tests du module W1.

Une exécution locale sous Termux a donné :

```text
49 passed in 0.73s
```

Cette durée correspond à une exécution particulière.
Elle n’est ni un benchmark matériel standardisé ni une garantie
de temps d’exécution.

## Couverture de code

Exécuter les tests avec mesure de couverture :

```bash
python -m pytest \
  --cov=ehk_scci \
  --cov-report=term-missing \
  --cov-report=xml:coverage.xml \
  --cov-report=html:coverage_html \
  --cov-fail-under=70
```

Les sorties sont :

- résumé de couverture dans le terminal ;
- rapport XML : `coverage.xml` ;
- rapport HTML : `coverage_html/index.html`.

Le seuil actuellement configuré est de 70 %.

La couverture mesure les portions de code exécutées par les tests.
Elle ne prouve ni la correction de toutes les entrées possibles,
ni la validité scientifique du cadre, ni la sûreté du système supervisé.

## Intégration continue

Le workflow `.github/workflows/ci.yml` se déclenche :

- lors d’un push sur `main` ;
- lors d’une pull request ciblant `main` ;
- lors d’un lancement manuel depuis GitHub Actions.

Il réalise :

1. l’installation de Python et des dépendances ;
2. l’exécution des tests avec couverture ;
3. la génération des rapports HTML et XML ;
4. le contrôle du seuil minimal de couverture ;
5. l’archivage des rapports et du résultat JUnit.

Les artefacts sont configurés pour être conservés pendant 14 jours,
dans les limites des paramètres du dépôt.

La première exécution CI associée au commit `4cbe1d0`
a été rapportée comme réussie.

### Fonctions non encore activées dans ce workflow

- Validation des schémas JSON.
- Publication du rapport sur GitHub Pages.
- Benchmarks cyberphysiques complets.
- Publication automatisée des données.

La génération du rapport HTML ne signifie pas qu’il est déjà publié
comme site GitHub Pages.

## Données et reproductibilité

Les données volumineuses ne sont pas destinées à être stockées dans
l’historique Git de ce dépôt.

L’architecture prévue distingue :

- le code et les tests ;
- les protocoles de benchmark ;
- les jeux de données et leurs métadonnées.

Les futures publications de résultats devront préciser :

- le commit du code ;
- la version du protocole ;
- la configuration et les graines aléatoires ;
- la provenance et la version des données ;
- les empreintes SHA-256 des artefacts concernés ;
- les conditions matérielles et logicielles d’exécution.

Une empreinte SHA-256 permet de vérifier l’intégrité d’un fichier
par comparaison avec une référence de confiance.
Elle ne valide pas son contenu scientifique.

## Limites et précautions

- Les tests ne couvrent que les cas explicitement vérifiés.
- La stabilité d’une représentation interne ne garantit pas
  la sûreté d’un procédé physique.
- Un score géométrique ne remplace pas l’authentification,
  le chiffrement ou le contrôle d’accès.
- Une politique de supervision doit être évaluée avec le contrôleur,
  les capteurs, les actionneurs et les contraintes du procédé.
- Aucune conformité NIST, certification de sûreté ou validation
  industrielle n’est revendiquée par cette version.

## Feuille de route

- Documenter les interfaces et conventions mathématiques.
- Ajouter des tests de cas limites et d’erreurs.
- Définir et valider les schémas JSON.
- Configurer les benchmarks reproductibles.
- Mesurer les performances sur plusieurs environnements.
- Préparer une release logicielle archivée sur Zenodo.

## Citation et archivage

**Archivage Zenodo de la version 0.1.0 :**  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24184737.svg)](https://doi.org/10.5281/zenodo.24184737)

**Protocole méthodologique associé :**

- [Articulation formelle : du noyau de transport optimal W1 à l’invariant d’entonnoir J(v)](https://doi.org/10.5281/zenodo.24141069)
- [EHK–SCCI : cadre variationnel et géométrique pour la régulation des représentations latentes, la détection d’anomalies et l’abstention contrôlée](https://doi.org/10.5281/zenodo.23968613)
- [EHK-SCCI / — Termux ARM64 corrigée v2 — 4x SHA-256 OK](https://doi.org/10.5281/zenodo.24047126)

## Référence de provenance des données

Le protocole d’intégration avec le jeu de données Elliptic fait référence à une ressource cataloguée dans le NLM Dataset Catalog :

- [NLM Dataset Catalog — recherche 0003380829](https://datasetcatalog.nlm.nih.gov/dataset?q=0003380829)

Ce référencement indique une source documentaire ou de provenance. Il ne constitue pas une validation scientifique du logiciel EHK-SCCI Core, du protocole de benchmarking ou des résultats obtenus.

## Fichier de citation

Un fichier `CITATION.cff` précise les informations de citation.



## Licence

EHK–SCCI Core est distribué sous la licence Apache-2.0.
Voir le fichier [LICENSE](LICENSE) pour le texte intégral.

Copyright 2026 NOUR KAYAD Mohamed.
