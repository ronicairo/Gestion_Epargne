import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mon_module.models.epargne import Epargne

def test_initialisation_epargne():
    e = Epargne("Livret A", 0.02, 0.0, 0, 22950)
    assert e.nom == "Livret A"
    assert e.taux_interet == 0.02
