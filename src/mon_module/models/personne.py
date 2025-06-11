class Personne:
    def __init__(self, nom: str, age: int, revenu_annuel: float, loyer: float, depenses_mensuelles: float, objectif: float, duree_epargne: int, versement_mensuel_utilisateur: float = None):
        # Initialisation des attributs de la personne
        self.nom = nom
        self.age = age
        self.revenu_annuel = revenu_annuel
        self.loyer = loyer
        self.depenses_mensuelles = depenses_mensuelles
        self.objectif = objectif
        self.duree_epargne = duree_epargne
        self.versement_mensuel_utilisateur = versement_mensuel_utilisateur
        self.capacite_epargne = self._calcul_capacite_epargne()

    def _calcul_capacite_epargne(self) -> float:
        # Calcule la capacité d’épargne mensuelle en soustrayant le loyer et les dépenses du revenu mensuel
        revenu_mensuel = self.revenu_annuel / 12
        return max(revenu_mensuel - self.loyer - self.depenses_mensuelles, 0)

    def __str__(self):
        # Représentation lisible de l'objet Personne
        return f"Personne: {self.nom}, Âge: {self.age}, Capacité d'épargne: {self.capacite_epargne:.2f}€/mois"
