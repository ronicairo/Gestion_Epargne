import pandas
from mon_module.models.epargne import Epargne
from mon_module.models.personne import Personne
from mon_module.core import nettoyer_dataframe
from mon_module.utils import calcul_interets_composes
from mon_module.core import import_personnes, import_epargnes
from mon_module.models.resultat import ResultatEpargne
from mon_module.core import suggestion_epargne

# Étape 2 – Test du calcul des intérêts composés
capital = calcul_interets_composes(1000, 0.03, 5)
# print(f"Capital accumulé sur 5 ans à 3% pour 1000€/an : {capital}€")

# Étape 3 – Lecture brute du fichier d’épargne
df = pandas.read_csv("epargnes.csv", sep=";")
# print(f"Données brutes chargées depuis epargnes.csv :")
# print(df.head())

# Étape 4 – Nettoyage du DataFrame
df_nettoye = nettoyer_dataframe(df)
# print(f"Données après nettoyage :")
# print(df_nettoye.head())
# print(f"Types de données :\n{df_nettoye.dtypes}")

# Étape 5 – Importation des données dans des objets Python
personnes = import_personnes("personnes.csv")
epargnes = import_epargnes("epargnes.csv")
# print(f"{len(personnes)} personnes importées")
# print(f"{len(epargnes)} produits d’épargne importés")

# Affiche un exemple
# print(f"Exemple Personne : {personnes[0]}")
# print(f"Exemple Epargne : {epargnes[0]}")
    
# Étape 6 – Simulation d’épargne
if __name__ == "__main__":
    personne = personnes[0]
    objectif = personne.objectif
    duree = personne.duree_epargne

    resultats = suggestion_epargne(personne, epargnes, objectif, duree)

    # print("Résultats de la simulation d'épargne :")
    for r in resultats:
        r.afficher()
