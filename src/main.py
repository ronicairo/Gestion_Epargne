from mon_module.utils import calcul_interets_composes

if __name__ == "__main__":
    # Exemple : 1000€ par an, 3% d'intérêt, 5 ans
    capital = calcul_interets_composes(1000, 0.03, 5)
    print(f"Capital accumulé : {capital}€")
