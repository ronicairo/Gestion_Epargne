import pandas as pd
from typing import List
from mon_module.models.epargne import Epargne
from mon_module.models.personne import Personne
from mon_module.utils import nettoyer_dataframe

def import_personnes(fichier: str) -> List[Personne]:
    # Détermine l'extension du fichier pour choisir la méthode de lecture
    ext = fichier.split(".")[-1]
    try:
        # Lit le fichier selon son extension
        if ext == "csv":
            df = pd.read_csv(fichier)
        elif ext == "txt":
            df = pd.read_csv(fichier, sep="\t")
        elif ext == "xlsx":
            df = pd.read_excel(fichier)
        else:
            raise ValueError("Format de fichier non supporté.")
        
        df = nettoyer_dataframe(df)
        personnes = []
        # Parcourt chaque ligne du DataFrame
        for _, row in df.iterrows():
            personne = Personne(
                nom=row.get("nom"),
                age=int(row.get("age") or 0),
                revenu_annuel=float(row.get("revenu_annuel") or 0.0),
                loyer=float(row.get("loyer") or 0.0),
                depenses_mensuelles=float(row.get("depenses_mensuelles") or 0.0),
                objectif=float(row.get("objectif") or 0.0),
                duree_epargne=int(row.get("duree_epargne") or 0),
                versement_mensuel_utilisateur=float(row.get("versement_mensuel_utilisateur") or 0.0)
            )

            # Ajoute la personne à la liste
            personnes.append(personne)

        print(f"{len(personnes)} personnes importées avec succès depuis {fichier}")
        return personnes

    except Exception as e:
        print(f"Erreur d'import de personnes : {e}")
        return []

def import_epargnes(fichier: str) -> List[Epargne]:
    # Détermine l'extension du fichier pour choisir la méthode de lecture
    ext = fichier.split(".")[-1]
    try:
        if ext == "csv":
            df = pd.read_csv(fichier)
        elif ext == "txt":
            df = pd.read_csv(fichier, sep="\t")
        elif ext == "xlsx":
            df = pd.read_excel(fichier)
        else:
            raise ValueError("Format de fichier non supporté.")

        df = nettoyer_dataframe(df)

        epargnes = []
        # Parcourt chaque ligne du DataFrame
        for _, row in df.iterrows():
            epargne = Epargne(
                nom=row.get("nom"),
                taux_interet=float(row.get("taux_interet")),
                fiscalite=float(row.get("fiscalite")),
                duree_min=int(row.get("duree_min")),
                versement_max=row.get("versement_max") if pd.notna(row.get("versement_max")) else None
            )
            # Ajoute l'épargne à la liste
            epargnes.append(epargne)

        print(f"{len(epargnes)} produits d’épargne importés depuis {fichier}")
        return epargnes

    except Exception as e:
        print(f"Erreur d'import des épargnes : {e}")
        return []

def save_personnes(personnes: List[Personne], fichier: str):
    try:
        data = [vars(p) for p in personnes] # Convertit les objets Personne en dictionnaires
        df = pd.DataFrame(data) # Crée un DataFrame à partir de la liste de dictionnaires
        df.to_csv(fichier, index=False) # Enregistre le DataFrame dans un fichier CSV
        print(f"{len(personnes)} personnes enregistrées dans {fichier}")
    except Exception as e:
        print(f"Erreur export personnes : {e}")

def save_epargnes(epargnes: List[Epargne], fichier: str):
    try:
        data = [vars(e) for e in epargnes]  # Transforme chaque objet Epargne en dictionnaire
        df = pd.DataFrame(data)  # Crée un DataFrame à partir de la liste de dictionnaires
        df.to_csv(fichier, index=False)  # Enregistre le DataFrame dans un fichier CSV
        print(f"{len(epargnes)} produits épargne enregistrés dans {fichier}")
    except Exception as e:
        print(f"Erreur export épargnes : {e}")

