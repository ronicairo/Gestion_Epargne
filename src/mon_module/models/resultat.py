class ResultatEpargne:
    def __init__(self, nom_produit: str, effort_mensuel: float, montant_net_final: float, objectif_atteint: bool):
        self.nom_produit = nom_produit
        self.effort_mensuel = effort_mensuel
        self.montant_net_final = montant_net_final
        self.objectif_atteint = objectif_atteint

    def afficher(self):
        statut = "✅ Objectif atteint" if self.objectif_atteint else "❌ Objectif non atteint"
        print(f"{self.nom_produit:<25} | Effort : {self.effort_mensuel:.2f} €/mois | "
              f"Montant net final : {self.montant_net_final:.2f} € | {statut}")

    def to_dict(self):
        return {
            "nom_produit": self.nom_produit,
            "effort_mensuel": self.effort_mensuel,
            "montant_net_final": self.montant_net_final,
            "objectif_atteint": self.objectif_atteint
        }

    def to_dataframe(self):
        import pandas as pd
        return pd.DataFrame([self.to_dict()])
