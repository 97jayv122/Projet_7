# Projet_7

# Optimisation d'investissements - Projet d'analyse combinatoire

Ce projet a pour objectif de **maximiser le profit d’un client** à partir d’un **budget de 500 €** en choisissant les **meilleures actions disponibles**.

---

## Description

Le programme lit un fichier CSV contenant les informations suivantes pour chaque action :
- **Nom de l’action**
- **Coût (en euros)**
- **Bénéfice (en % après 2 ans)**

Il utilise un **algorithme de type sac à dos (knapsack 0/1)** pour :
- Évaluer **toutes les combinaisons possibles** d’actions respectant les contraintes
- Sélectionner celles générant **le profit maximal**
- Afficher le détail des actions retenues, le coût total et le profit total

---

## Fichiers

- `optimized.py` : Script principal exécutant la stratégie d’investissement optimale


---

## Utilisation

1. Placez votre fichier CSV dans le répertoire.
2. Exécutez le script avec :

bash
`python main.py path/to/data.csv`


2.Le programme affichera :

    Le temps d’exécution

    Le budget utilisé

    Le coût total des actions sélectionnées

    Le profit attendu

    La liste des actions à acheter

