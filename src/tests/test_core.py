import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mon_module.utils import calcul_interets_composes
from mon_module.core import import_personnes, nettoyer_dataframe
import pandas as pd


def test_interets_composes():
    assert round(calcul_interets_composes(1000, 0.03, 5), 2) == 5468.41

def test_nettoyage_dataframe():
    df = pd.DataFrame({
        "taux_interet": ["0.03", "None", "0.05"],
        "duree_min": ["3", "4", "5"]
    })
    df_clean = nettoyer_dataframe(df)
    assert df_clean["taux_interet"].iloc[0] == 0.03
    assert pd.isna(df_clean["taux_interet"].iloc[1])
