import pandas as pd
import numpy as np

def calcul_interets_composes(versement_annuel: float, taux_annuel: float, duree_annees: int) -> float:
    """
    Calcule le capital final avec intérêts composés.
    
    :param versement_annuel: Montant versé chaque année
    :param taux_annuel: Taux d'intérêt (ex: 0.03 pour 3%)
    :param duree_annees: Durée en années
    :return: Montant total accumulé
    """
    montant = 0.0
    for _ in range(duree_annees):
        montant = (montant + versement_annuel) * (1 + taux_annuel)
    return round(montant, 2)

def nettoyer_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    # Remplace les chaînes "None", "none", "NaN" et les np.nan par None (valeur manquante standard Python)
    df = df.replace(["None", "none", "NaN", np.nan], None)

    colonnes_float = ['taux_interet', 'fiscalite', 'versement_max']
    colonnes_int = ['duree_min', 'age']

    # Pour chaque colonne devant être en float
    for col in colonnes_float:
        if col in df.columns: # Vérifie si la colonne existe dans le DataFrame
            try:
                # Convertit la colonne en float
                df[col] = df[col].astype(float)
            except Exception as e:
                raise ValueError(f"Erreur de conversion float pour la colonne '{col}': {e}")
    # Pour chaque colonne devant être en int
    for col in colonnes_int:
        if col in df.columns:
            try:
            # Convertit la colonne en float, arrondit, puis en int
                df[col] = df[col].astype(float).round().astype(int)  # sécurité
            except Exception as e:
                raise ValueError(f"Erreur de conversion int pour la colonne '{col}': {e}")

    return df