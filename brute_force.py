import csv
import sys
import os
import time

def read_csv(file_name):
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
        print("Une érreur est survenue :", e)

def brute_force(actions, budget):
    all_combnations = [[]]
    for act in actions:
        new_combinations = []
        for combination in all_combnations:
            new_combinations.append(combination + [act])
        all_combnations.extend(new_combinations)
    # print(len(all_combnations))
    meilleur_rendement = 0
    meilleure_combo = []
    for combination in all_combnations:
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


     
if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Usage : python script.py chemin/vers/fichier;csv")
        sys.exit(1)
    

    file_name = os.path.abspath(sys.argv[1])
    actions = read_csv(file_name)
    # print(actions)
    clean_data = []
    for item in actions:
        action, num1, num2 = item[0].replace('%', '').split(',')
        clean_data.append([action, int(num1), int(num2)])
    budget : int = 500
    start = time.time()
    combo_opt, rendement_opt = brute_force(clean_data, budget)
    
    print(f"Budget: €{budget}")
    print("Combinaison optimale :")
    print(f"Durée d'éxécution: {(time.time() - start):.2f} ")
    for nom, cout, pct in combo_opt:
        print(f" - {nom}: coût €{cout}, rendement {pct}% -> €{cout * pct / 100:.2f}")
    print(f"Rendement total maximal : €{rendement_opt:.2f}")

    