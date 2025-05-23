#!/usr/bin/env python3

import csv
import sys
import os
import time


def read_csv(file_name):
    """
    Lit un fichier CSV et retourne une liste brute des lignes.

    Paramètre
    ---------
    file_name : str
        Chemin du fichier CSV

    Retourne
    --------
    list
        Liste des lignes extraites du fichier (sans traitement)
    """
    actions_list = []
    try:
        with open(file_name, 'r', encoding='utf-8') as fichier:
            reader = csv.reader(fichier, delimiter=";")
            next(reader)
            for ligne in reader:
                actions_list.append(ligne)
            return actions_list
    except FileNotFoundError:
        print("Fichier non trouvé :", file_name)
    except Exception as e:
        print("Une erreur est survenue :", e)


def brute_force(actions, budget):
    """
    Teste toutes les combinaisons possibles d'actions et retourne
    celle qui donne le rendement maximum sous contrainte de budget.

    Paramètres
    ----------
    actions : list
        Liste des actions au format [nom, coût, rendement]
    budget : int
        Budget maximal

    Retourne
    --------
    tuple
        (meilleure combinaison, rendement total)
    """
    all_combinations = [[]]
    for act in actions:
        new_combinations = []
        for combination in all_combinations:
            new_combinations.append(combination + [act])
        all_combinations.extend(new_combinations)

    meilleur_rendement = 0
    meilleure_combo = []
    for combination in all_combinations:
        if not combination:
            continue
        cout_total = sum(a[1] for a in combination)
        if cout_total > budget:
            continue
        rendement_total = sum(a[1] * a[2] / 100 for a in combination)
        if rendement_total > meilleur_rendement:
            meilleur_rendement = rendement_total
            meilleure_combo = combination

    return meilleure_combo, meilleur_rendement


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python script.py chemin/vers/fichier.csv")
        sys.exit(1)

    file_name = os.path.abspath(sys.argv[1])
    actions = read_csv(file_name)

    clean_data = []
    for item in actions:
        try:
            action, num1, num2 = item[0].replace('%', '').split(',')
            clean_data.append([action, int(num1), int(num2)])
        except ValueError:
            continue  # Ligne invalide ignorée

    budget = 500
    start = time.time()
    combo_opt, rendement_opt = brute_force(clean_data, budget)

    print(f"Budget : €{budget}")
    print(f"Durée d'exécution : {(time.time() - start):.2f} s")
    print("Combinaison optimale :")
    for nom, cout, pct in combo_opt:
        print(f" - {nom} : coût €{cout}, rendement {pct}% -> €{cout * pct / 100:.2f}")
    print(f"Rendement total maximal : €{rendement_opt:.2f}")
