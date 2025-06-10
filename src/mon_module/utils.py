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
