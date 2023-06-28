import csv
import time

start = time.time()

def ponderation(actions, max_budget):
    moy_profit = (sum((action['Profit']) for action in actions))/len(actions)
    moy_cost = (sum((action['Cost']) for action in actions))/len(actions)
    moy_benef = (sum((action['Profit'] * action['Cost']) for action in actions))/len(actions)
    
    sorted_actions = sorted(actions, key=lambda x: x['Profit'], reverse=True)
    
    result = []
    sum_cost = 0
  
    for a in sorted_actions:         
        profit = a['Profit']
        cost = a['Cost']
        
        if profit <= moy_profit and cost <= moy_cost and ((sum_cost + a['Cost']) < (max_budget)):
                a['Ponderation'] = 2
                result.append(a)
                sum_cost += a['Cost']
                #print (f"sum_cost est {sum_cost} et a['Cost'] est {a['Cost']} et max_budget est {max_budget}")
        elif profit >= (moy_profit) and cost <= moy_cost and((sum_cost + a['Cost']) < max_budget):
                a['Ponderation'] = 1
                result.append(a)
                sum_cost += a['Cost']
                #print (f"sum_cost est {sum_cost} et a['Cost'] est {a['Cost']} et max_budget est {max_budget}")
        elif profit >= (moy_profit) and cost >= moy_cost and((sum_cost + a['Cost']) < max_budget):
                a['Ponderation'] = 0
                result.append(a)
                sum_cost += a['Cost']
                #print (f"sum_cost est {sum_cost} et a['Cost'] est {a['Cost']} et max_budget est {max_budget}")
    
    return result  # Modification : Retourne la liste d'actions modifiée

# Lecture des données à partir du fichier CSV
actions = []

with open('data_test.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        if float(row['price']) > 0 and float(row['profit']) > 0:
            price = row['price'].replace(',', '.')
            profit = row['profit'].replace(',', '.')
            if float(profit) < 1 :
                profit = float(profit) * 100
            if float(price) > 0 and float(profit) > 0:
                actions.append({
                    'Action': row['name'],
                    'Cost': round(float(price), 2),
                    'Profit': round(float(profit), 2)
                })

# Paramètres pour l'algorithme
max_budget = 500

# Appel de la fonction pour maximiser le profit
best_combination = ponderation(actions, max_budget)

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

