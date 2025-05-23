#!/usr/bin/env python3

import csv
import time
import sys
import os


def load_actions(path, scale=100):
    """
    Load actions from a CSV file and filter out invalid entries.
    
    Parameters
    ----------
    path : str
        Path to the CSV file.
    scale : int, optional
        Scale factor to convert floats into integers for precision (default is 100).

    Returns
    -------
    list of tuples
        Valid actions as tuples: (name, cost_int, profit_int, cost_float, profit_float)
    int
        Number of actions ignored due to invalid cost
    """
    actions = []
    isolated_actions = 0
    with open(path, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        for row in reader:
            if len(row) < 3:
                continue
            name, price_s, pct_s = row[:3]
            price = float(price_s)
            pct = float(pct_s)
            if price <= 0.0:
                isolated_actions += 1
                continue
            profit_val = price * pct / 100.0
            cost_int = int(round(price * scale))
            profit_int = int(round(profit_val * scale))
            actions.append((name, cost_int, profit_int, price, profit_val))
    return actions, isolated_actions


def knapsack_dp_2d(actions, budget_float, scale=100):
    """
    Classical 2D Dynamic Programming to solve 0/1 Knapsack problem.

    Parameters
    ----------
    actions : list of tuples
        Actions with cost and profit information
    budget_float : float
        Budget in euros
    scale : int, optional
        Precision scaling factor (default is 100)

    Returns
    -------
    tuple
        (Selected actions, total cost in euros, total profit in euros)
    """
    n = len(actions)
    B = int(round(budget_float * scale))
    dp = [[0] * (B + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, c_int, p_int, _, _ = actions[i - 1]
        for w in range(B + 1):
            dp[i][w] = dp[i - 1][w]
            if c_int <= w:
                v = dp[i - 1][w - c_int] + p_int
                if v > dp[i][w]:
                    dp[i][w] = v

    w = B
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, c_int, p_int, cost_f, profit_f = actions[i - 1]
            selected.append((name, cost_f, profit_f))
            w -= c_int

    selected.reverse()
    total_profit = dp[n][B] / scale
    total_cost = sum(item[1] for item in selected)
    return selected, total_cost, total_profit


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python script.py path/to/file.csv")
        sys.exit(1)

    file_name = os.path.abspath(sys.argv[1])
    start = time.time()

    actions, isolated_actions = load_actions(file_name, scale=100)
    budget = 500.0
    selected, cost, profit = knapsack_dp_2d(actions, budget, scale=100)

    temps = time.time() - start
    print(f"Temps d'exécution         : {temps:.3f}s")
    print(f"Budget disponible         : {budget:.2f} €")
    print(f"Coût total sélectionné    : {cost:.2f} €")
    print(f"Profit total attendu      : {profit:.2f} €\n")
    print(f"Nombre d'actions traitées : {len(actions)}")
    print(f"Nombre d'actions ignorées : {isolated_actions}\n")
    print("Actions retenues :")
    for name, cost_f, profit_f in selected:
        print(f" - {name} | coût = {cost_f:.2f} € | profit = {profit_f:.2f} €")
