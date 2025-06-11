import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mon_module.models.personne import Personne

def test_initialisation_personne():
    p = Personne("Alice", 30, 30000, 800, 500, 20000, 5, 200)
    assert p.nom == "Alice"
    assert p.age == 30

def test_capacite_epargne():
    p = Personne("Bob", 40, 36000, 1000, 500, 100000, 10, 400)
    assert p._calcul_capacite_epargne() == 36000 / 12 - 1000 - 500
