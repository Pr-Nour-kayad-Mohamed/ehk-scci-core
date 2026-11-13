EHK-SCCI Core

DOI : https://doi.org/10.5281/zenodo.24184737

Noyau logiciel de recherche pour le calcul geometrique sur graphes, le diagnostic discriminant et les politiques de supervision.

Auteur : NOUR KAYAD Mohamed
Affiliation : Ministere de l'Education nationale et de la Formation professionnelle (MENFOP), Republique de Djibouti
Version initiale : 0.1.0
Licence : Apache-2.0

STATUT DU PROJET

EHK-SCCI Core est un prototype de recherche en developpement.

Les tests unitaires et l'integration continue verifient les comportements couverts par la suite de tests. Ils ne constituent pas une certification de surete, une validation industrielle ou une demonstration de performance sur un systeme physique reel.

Le depot ne doit pas etre utilise seul comme mecanisme de protection d'un equipement critique.

MODULES

W1
Emplacement : src/ehk_scci/curvature/w1_core.py
Perimetre : calculs de transport Wasserstein-1 et cas de reference sur graphes.

Discriminant
Emplacement : src/ehk_scci/spectral/discriminant_core.py
Perimetre : calcul et verification des fonctions discriminantes implementees.

Politique
Emplacement : src/ehk_scci/safety/policy_core.py
Perimetre : regles de decision et politiques de supervision implementees.

Les definitions exactes, les hypotheses et les conventions doivent etre consultees dans le code et les tests associes.

ORGANISATION DU DEPOT

ehk-scci-core/
  .github/
    workflows/
      ci.yml
  src/
    ehk_scci/
      curvature/
        w1_core.py
      safety/
        policy_core.py
      spectral/
        discriminant_core.py
  tests/
    test_discriminant_core.py
    test_policy_core.py
    test_w1_core.py
  .gitignore
  pyproject.toml
  README.md

PREREQUIS

Le projet requiert Python 3.10 ou superieur, comme declare dans pyproject.toml.

La configuration d'integration continue utilise Python 3.11 sous Ubuntu. Les versions minimales des dependances sont declarees dans pyproject.toml.

L'execution locale rapportee sous Android/Termux constitue un resultat distinct de l'execution CI sous Ubuntu. Elle ne demontre pas une compatibilite universelle avec toutes les versions de Python ou toutes les architectures.

INSTALLATION

Depuis la racine du depot :

python -m pip install -e ".[test]"

Cette commande installe le paquet en mode edit
