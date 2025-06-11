from datetime import datetime
from functools import wraps

def log_comparaison_epargne(func):
    @wraps(func)
    def wrapper(personne, epargnes, objectif, duree):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] Nous allons faire une comparaison de {len(epargnes)} placements selon la situation de {personne.nom}")
        return func(personne, epargnes, objectif, duree)
    return wrapper
