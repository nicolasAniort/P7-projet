import csv
import time
import os, psutil

start = time.time()

# Obtenir le nombre de cœurs du processeur
num_cores = psutil.cpu_count(logical=True)
print("Nombre de cœurs du processeur :", num_cores)

# Obtenir l'utilisation de la RAM

ram_usage = psutil.virtual_memory().used
print("Utilisation de la RAM :", ram_usage, "octets")

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
        price = row['price'].replace(',', '.')
        profit = row['profit'].replace(',', '.')
        actions.append({
            'Action': row['name'],
            'Cost': int(row['price']),
            'Profit': round(float(profit), 2)
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
#print("Profit total :", sum((action['Profit'] * action['Cost']) for action in best_combination))
total_profit = round(sum(round(float(action['Profit']) * round(float(action['Cost']), 2), 2) for action in best_combination), 2)
print("Profit total :", total_profit)
print("depense:", sum(action['Cost'] for action in best_combination))
print(f"Temps d'execution : {end - start} secondes")

# Obtenez à nouveau l'utilisation de la RAM après l'exécution de votre code
ram_usage_after = psutil.virtual_memory().used
print("Utilisation de la RAM après l'exécution :", ram_usage_after, "octets")

# Calculer la différence d'utilisation de la RAM
ram_usage_diff = ram_usage_after - ram_usage
print("Différence d'utilisation de la RAM :", ram_usage_diff, "octets")

# Obtenir le nombre de cœurs utilisés par votre programme
used_cores = psutil.cpu_count(logical=True) - psutil.cpu_count(logical=False)
print("Nombre de cœurs utilisés par votre programme :", used_cores)