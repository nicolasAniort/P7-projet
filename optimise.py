import csv
import time

start = time.time()

def ponderation(actions, max_budget):
    moy_benef = (sum((action['Profit'] * action['Cost']) for action in actions))/len(actions)
    sorted_actions = sorted(actions, key=lambda x: x['Cost'] * x['Profit'], reverse=True)
    result = []
    sum_cost2 = 0
    sum_cost1 = 0
    sum_cost0 = 0

    
    for a in sorted_actions:  # Modification : Utilisation de "a" au lieu de "action"
        benef = a['Profit'] * a['Cost']  # Modification : Utilisation de "a" au lieu de "action"
        if benef > moy_benef and ((sum_cost2 + a['Cost']) <= max_budget):
            a['Ponderation'] = 2
            result.append(a)
            sum_cost2 += a['Cost']
        elif benef > (moy_benef * 0.25) and ((sum_cost2 + sum_cost1+ a['Cost']) <= max_budget):
            a['Ponderation'] = 1
            result.append(a)
            sum_cost1 += a['Cost']
        elif benef > (moy_benef * 0.1) and ((sum_cost2 + sum_cost1 + sum_cost0 + a['Cost']) <= max_budget):
            a['Ponderation'] = 0
            result.append(a)
            sum_cost0 += a['Cost']

    return result  # Modification : Retourne la liste d'actions modifiée

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
best_combination = ponderation(actions, max_budget)

# Affichage des résultats
print("Meilleure combinaison d'actions :")
for action in best_combination:
    print(action['Action'], '- Coût:', action['Cost'], '€ - Bénéfice:', action['Profit'], '€ - ponderation:', action['Ponderation'])

end = time.time()
print("Profit total :", sum((action['Profit'] * action['Cost']) for action in best_combination))
print("Dépense :", sum(action['Cost'] for action in best_combination))
print(f"Temps d'exécution : {end - start} secondes")
