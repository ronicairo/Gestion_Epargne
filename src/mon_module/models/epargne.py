class Epargne:
    def __init__(self, nom: str, taux_interet: float, fiscalite: float, duree_min: int, versement_max: float = None):
        # Initialisation des attributs de l'épargne
        self.nom = nom
        self.taux_interet = taux_interet
        self.fiscalite = fiscalite
        self.duree_min = duree_min
        self.versement_max = versement_max

    def __repr__(self):
        # Représentation pour le débogage
        return f"<Epargne {self.nom}>"

    def __str__(self):
        # Représentation lisible de l'épargne, avec plafond affiché si défini
        info_max = f", Plafond: {self.versement_max}€" if self.versement_max is not None else ""
        return f"{self.nom} | Taux: {self.taux_interet*100:.2f}%, Fiscalité: {self.fiscalite*100:.2f}%, Durée min: {self.duree_min} ans{info_max}"
