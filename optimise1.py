import csv
import time
import os, psutil

start = time.time()

# Mesurer l'utilisation des ressources avant l'exécution de l'algorithme bruteforce
cpu_before = psutil.cpu_percent(interval=1, percpu=True)
memory_before = psutil.virtual_memory().used


def ponderation(actions, max_budget):
    moy_profit = (sum((action['Profit']) for action in actions))/len(actions)
    moy_cost = (sum((action['Cost']) for action in actions))/len(actions)
    
    sorted_actions = sorted(actions, key=lambda x: x['Profit'], reverse=True)
    
    result = []
    sum_cost = 0
  
    for a in sorted_actions:         
        profit = a['Profit']
        cost = a['Cost']
        #
        if profit <= moy_profit and cost <= moy_cost and ((sum_cost + a['Cost']) < (max_budget)):
                a['Ponderation'] = 2
                result.append(a)
                sum_cost += a['Cost']
                
        elif profit >= (moy_profit) and cost <= moy_cost and((sum_cost + a['Cost']) < max_budget):
                a['Ponderation'] = 1
                result.append(a)
                sum_cost += a['Cost']
                
        elif profit >= (moy_profit) and cost >= moy_cost and((sum_cost + a['Cost']) < max_budget):
                a['Ponderation'] = 0
                result.append(a)
                sum_cost += a['Cost']
                
    
    return result  #  Retourne la liste d'actions modifiée

# Lecture des données à partir du fichier CSV
actions = []

with open('dataset1_Python+P7.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        if float(row['price']) > 0 and float(row['profit']) > 0:
            actions.append({
                'Action': row['name'],
                'Cost': round(float(row['price']), 2),
                'Profit': round(float(row['profit'].replace(',', '.')), 2)
            })

# Paramètres pour l'algorithme
max_budget = 500

# Appel de la fonction pour maximiser le profit
best_combination = ponderation(actions, max_budget)

# Mesurer l'utilisation des ressources après l'exécution de l'algorithme bruteforce
cpu_after = psutil.cpu_percent(interval=1, percpu=True)
memory_after = psutil.virtual_memory().used

# Affichage des résultats
print("Meilleure combinaison d'actions :")
for action in best_combination:
    print(action['Action'], '- Coût:', action['Cost'], '€ - Bénéfice:', action['Profit'], '% - ponderation:', action['Ponderation'])

end = time.time()
total_profit = round(sum(round(float(action['Profit']) * round(float(action['Cost'])/100, 2), 2) for action in best_combination), 2)
print("Profit total :", total_profit)
total_depense = round(sum(round(float(action['Cost']), 2) for action in best_combination), 2)
print("Dépense :", total_depense)
print(f"Temps d'exécution : {end - start} secondes")

# Calculer la différence d'utilisation des ressources
cpu_diff = [after - before for before, after in zip(cpu_before, cpu_after)]
memory_diff = memory_after - memory_before

# Afficher les résultats
print("Utilisation CPU avant :", cpu_before)
print("Utilisation CPU après :", cpu_after)
print("Différence d'utilisation CPU :", cpu_diff)
print("Utilisation mémoire avant :", memory_before)
print("Utilisation mémoire après :", memory_after)
print("Différence d'utilisation mémoire :", memory_diff)