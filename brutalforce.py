import csv
import time

start= time.time()

def maximize_profit(actions, max_budget):
    best_profit = 0
    best_combination = []

    for i in range(1, 2**len(actions)):
        combination = []
        total_cost = 0
        total_profit = 0

        for j in range(len(actions)):
            if (i >> j) & 1:
                combination.append(actions[j])
                total_cost += actions[j]['Cost']
                total_profit += actions[j]['Profit']

        if total_cost <= max_budget and total_profit > best_profit:
            best_profit = total_profit
            best_combination = combination  
    return best_combination


# Lecture des données à partir du fichier CSV
actions = []

with open('data_test.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        actions.append({
            'Action': row['name'],
            'Cost': int(row['price']),
            'Profit': float(row['benefit'].replace(',', '.'))
        })

# Paramètres pour l'algorithme
max_budget = 500

# Appel de la fonction pour maximiser le profit
best_combination = maximize_profit(actions, max_budget)

# Affichage des résultats
print("Meilleure combinaison d'actions :")
for action in best_combination:
    print(action['Action'], '- Coût:', action['Cost'], '€ - Bénéfice:', action['Profit'])

end = time.time()
print("Profit total :", sum((action['Profit'] * action['Cost']) for action in best_combination))
print("depense:", sum(action['Cost'] for action in best_combination))
print(f"Temps d'execution : {end - start} secondes")