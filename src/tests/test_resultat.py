import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mon_module.models.resultat import ResultatEpargne

def test_resultat_affichage():
    r = ResultatEpargne("LEP", 500, 10000, True)
    assert r.nom_produit == "LEP"
    assert r.objectif_atteint is True
