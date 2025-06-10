class Epargne:
    def __init__(self, nom: str, taux_interet: float, fiscalite: float, duree_min: int, versement_max: float = None):
        self.nom = nom
        self.taux_interet = taux_interet
        self.fiscalite = fiscalite
        self.duree_min = duree_min
        self.versement_max = versement_max

    def __repr__(self):
        return f"<Epargne {self.nom}>"

    def __str__(self):
        info_max = f", Plafond: {self.versement_max}€" if self.versement_max is not None else ""
        return f"{self.nom} | Taux: {self.taux_interet*100:.2f}%, Fiscalité: {self.fiscalite*100:.2f}%, Durée min: {self.duree_min} ans{info_max}"
