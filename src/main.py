import pandas
from mon_module.models.epargne import Epargne
from mon_module.models.personne import Personne
from mon_module.core import nettoyer_dataframe
from mon_module.utils import calcul_interets_composes
from mon_module.core import import_personnes, import_epargnes


# Exemple : 1000€ par an, 3% d'intérêt, 5 ans
capital = calcul_interets_composes(1000, 0.03, 5)
print(f"Capital accumulé : {capital}€")

df = pandas.read_csv("epargnes.csv", sep="\t") # Chargement d'un DataFrame pour démonstration
# Nettoyage du DataFrame
df_nettoye = nettoyer_dataframe(df)
print(df_nettoye.head())

if __name__ == "__main__":
    print(Epargne("Livret A", 0.003, 0.3, 1))  # Exemple de création d'une épargne
    personnes = import_personnes("personnes.csv") # Importation des personnes depuis un fichier CSV
    epargnes = import_epargnes("epargnes.csv") # Importation des épargnes depuis un fichier CSV
