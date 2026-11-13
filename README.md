Skip to content
ehk-scci-core
Repository navigation
Code
Issues
Pull requests
ehk-scci-core
/README.md
Pr-Nour-kayad-Mohamed
Pr-Nour-kayad-Mohamed
now
51 lines (39 loc) · 2.01 KB

Preview

Code

Blame
EHK–SCCI Core
DOI

Noyau logiciel de recherche pour le calcul géométrique sur graphes, le diagnostic discriminant et les politiques de supervision.

Auteur : NOUR KAYAD Mohamed
Affiliation : Ministère de l’Éducation nationale et de la Formation professionnelle (MENFOP), République de Djibouti
Version initiale : 0.1.0
Licence : Apache-2.0

Statut du projet
EHK–SCCI Core est un prototype de recherche en développement.

Les tests unitaires et l’intégration continue vérifient les comportements couverts par la suite de tests. Ils ne constituent pas une certification de sûreté, une validation industrielle ou une démonstration de performance sur un système physique réel.

Le dépôt ne doit pas être utilisé seul comme mécanisme de protection d’un équipement critique.

Modules
Module	Emplacement	Périmètre
W1	src/ehk_scci/curvature/w1_core.py	Calculs de transport Wasserstein-1 et cas de référence sur graphes
Discriminant	src/ehk_scci/spectral/discriminant_core.py	Calcul et vérification des fonctions discriminantes implémentées
Politique	src/ehk_scci/safety/policy_core.py	Règles de décision et politiques de supervision implémentées
Les définitions exactes, les hypothèses et les conventions doivent être consultées dans le code et les tests associés.

Organisation du dépôt
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
