import csv
import time

start = time.time()

def ponderation(actions, max_budget):
    moy_profit = (sum((action['Profit']) for action in actions))/len(actions)
    moy_cost = (sum((action['Cost']) for action in actions))/len(actions)
    moy_benef = (sum((action['Profit'] * action['Cost']) for action in actions))/len(actions)
    sorted_actions = sorted(actions, key=lambda x: x['Cost'] * x['Profit'], reverse=True)
    print(sorted_actions)
    result = []
    sum_cost = 0
  
    for a in sorted_actions:  # Modification : Utilisation de "a" au lieu de "action"
        benef = a['Profit'] * a['Cost']  # Modification : Utilisation de "a" au lieu de "action"         
        profit = a['Profit']
        cost = a['Cost']
        if profit <= moy_profit and cost <= moy_cost and ((sum_cost + a['Cost']) < (max_budget)):
                a['Ponderation'] = 2
                result.append(a)
                sum_cost += a['Cost']
                print (f"sum_cost est {sum_cost} et a['Cost'] est {a['Cost']} et max_budget est {max_budget}")
        elif profit >= (moy_profit) and cost <= moy_cost and((sum_cost + a['Cost']) < max_budget):
                a['Ponderation'] = 1
                result.append(a)
                sum_cost += a['Cost']
                print (f"sum_cost est {sum_cost} et a['Cost'] est {a['Cost']} et max_budget est {max_budget}")
        elif profit >= (moy_profit) and cost >= moy_cost and((sum_cost + a['Cost']) < max_budget):
                a['Ponderation'] = 0
                result.append(a)
                sum_cost += a['Cost']
                print (f"sum_cost est {sum_cost} et a['Cost'] est {a['Cost']} et max_budget est {max_budget}")
    
    return result  # Modification : Retourne la liste d'actions modifiée

# Lecture des données à partir du fichier CSV
actions = []

with open('dataset2_Python+P7.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        if float(row['price']) > 0 and float(row['profit']) > 0:
            actions.append({
                'Action': row['name'],
                'Cost': float(row['price']),
                'Profit': float(row['profit'].replace(',', '.'))
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
print("Profit total :", sum(((action['Profit'] * action['Cost'])/100) for action in best_combination))
print("Dépense :", sum(action['Cost'] for action in best_combination))
print(f"Temps d'exécution : {end - start} secondes")

