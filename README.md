
# 📊 Gestion de Produits d’Épargne – Tests Unitaires


## ✅ Pré-requis
Python 3.8 ou +
Pip installé
Installation de `pytest` :

```bash
pip install pytest
```

## 📁 Arborescence finale test

```
Gestion_Projet/
└── src/
    ├── mon_module/
    │   
    ├── tests/
    │   ├── test_core.py
    │   ├── test_epargne.py
    │   ├── test_personne.py
    │   └── test_resultat.py
```

Dans chaque fichier de test (ex : test_core.py, test_personne.py, etc.), il est nécessaire d’ajouter ceci en haut du fichier pour que les imports fonctionnent correctement :
```
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


## 🚀 Lancer les tests

Placez-vous dans le dossier `src/`, puis exécutez la commande suivante :

```bash
pytest tests/
```


```bash
===================== test session starts =====================
platform darwin -- Python 3.12.7, pytest-7.4.4, pluggy-1.0.0
rootdir: /Users/Roni/Downloads/DORANCO/EDWEB/PYTHON 2/Gestion_Projet/src
plugins: anyio-4.2.0
collected 6 items                                             

tests/test_core.py ..                                   [ 33%]
tests/test_epargne.py .                                 [ 50%]
tests/test_personne.py ..                               [ 83%]
tests/test_resultat.py .                                [100%]

====================== 6 passed in 1.61s ======================

