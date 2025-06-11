import pandas as pd
from typing import List
from mon_module.models.epargne import Epargne
from mon_module.models.personne import Personne
from mon_module.utils import nettoyer_dataframe
from mon_module.utils import calcul_interets_composes
from mon_module.models.resultat import ResultatEpargne

def import_personnes(fichier: str) -> List[Personne]:
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
        personnes = []

        for _, row in df.iterrows():
            try:
                nom = row.get("nom") or "Inconnu"

                age = int(float(row.get("age") or 0))
                revenu_annuel = float(row.get("revenu_annuel") or 0.0)
                loyer = float(row.get("loyer") or 0.0)
                depenses = float(row.get("depenses_mensuelles") or 0.0)
                objectif = float(row.get("objectif") or 0.0)
                duree = int(float(row.get("duree_epargne")))
                versement = float(row.get("versement_mensuel_utilisateur") or 0.0)

                personne = Personne(
                    nom=nom,
                    age=age,
                    revenu_annuel=revenu_annuel,
                    loyer=loyer,
                    depenses_mensuelles=depenses,
                    objectif=objectif,
                    duree_epargne=duree,
                    versement_mensuel_utilisateur=versement
                )

                personnes.append(personne)

            except Exception as e:
                print(f"[ERREUR] Ligne ignorée pour {row.get('nom')}: {e}")

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

def suggestion_epargne(personne: Personne, epargnes: List[Epargne], objectif: float, duree: int) -> List[ResultatEpargne]:
    resultats = []

    efforts = []

    if personne.versement_mensuel_utilisateur:
        efforts.append(personne.versement_mensuel_utilisateur)
    
    capacite = personne._calcul_capacite_epargne()
    efforts += [capacite * p for p in [0.25, 0.5, 0.75, 1.0]]

    for produit in epargnes:
        if duree < produit.duree_min:
            continue 

        for effort_mensuel in efforts:
            versement_annuel = effort_mensuel * 12

            montant_brut = calcul_interets_composes(versement_annuel, produit.taux_interet, duree)
            montant_net = montant_brut * (1 - produit.fiscalite)
            total_verse = versement_annuel * duree

            if produit.versement_max and total_verse > produit.versement_max:
                print(f"[INFO] 💰 Plafond dépassé pour {produit.nom} → {total_verse:.2f}€ > {produit.versement_max}")
                continue 

            resultat = ResultatEpargne(
                nom_produit=produit.nom,
                effort_mensuel=round(effort_mensuel, 2),
                montant_net_final=round(montant_net, 2),
                objectif_atteint=montant_net >= objectif
            )
            resultats.append(resultat)

    return resultats