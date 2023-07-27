import csv
import time
import psutil


#ligne de saisie du fichier qui est dans le meme repertoire que le script
filename = 'data_test.csv'

# Mesurer l'utilisation des ressources avant l'exécution de l'algorithme 
cpu_before = psutil.cpu_percent(interval=1, percpu=True)
memory_before = psutil.virtual_memory().used


# Obtenir l'utilisation de la RAM
ram_usage = psutil.virtual_memory().used
start = time.time()
# fonction optimisée pour trouver la meilleure combinaison d'action sur 2 ans
def optimisation(actions, max_budget):
    #calcul du profit moyen sur l'ensemble des actions
    moy_profit = (sum((action['Profit']) for action in actions))/len(actions)
    #calcul du cout moyen sur l'ensemble des actions
    moy_cost = (sum((action['Cost']) for action in actions))/len(actions)
    #tri des actions par rapport au profit en allant du plus grand au plus petit
    sorted_actions = sorted(actions, key=lambda x: x['Profit'], reverse=True)
    
    result = []
    sum_cost = 0
  
    for a in sorted_actions:         
        profit = a['Profit']
        cost = a['Cost']
        """
        si le profit est inferieur ou egal au profit moyen et que le cout est inferieur ou égal
        au cout moyen et que la somme des cout des actions selectionnées ne dépasse pas le 
        budget maximum
        
        si le profit est supérieur ou egal au profit moyen et que le cout est inferieur ou égal
        au cout moyen et que la somme des cout des actions selectionnées ne dépasse pas le 
        budget maximum
        
        si le profit est supérieur ou egal au profit moyen et que le cout est supérieur ou égal
        au cout moyen et que la somme des cout des actions selectionnées ne dépasse pas le 
        budget maximum
          
        """
        if profit <= moy_profit and cost <= moy_cost and ((sum_cost + a['Cost']) < (max_budget)):                
                result.append(a)
                sum_cost += a['Cost']
              
        elif profit >= (moy_profit) and cost <= moy_cost and((sum_cost + a['Cost']) < max_budget):
                result.append(a)
                sum_cost += a['Cost']       
        elif profit >= (moy_profit) and cost >= moy_cost and((sum_cost + a['Cost']) < max_budget):
                result.append(a)
                sum_cost += a['Cost']
    # Retourne la liste d'actions modifiée            
    return result  

# Lecture des données à partir du fichier CSV
actions = []

with open(filename, newline='', encoding='utf-8') as csvfile:
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
best_combination = optimisation(actions, max_budget)

# Mesurer l'utilisation des ressources après l'exécution de l'algorithme bruteforce
cpu_after = psutil.cpu_percent(interval=1, percpu=True)
memory_after = psutil.virtual_memory().used

# Affichage des résultats
print("Meilleure combinaison d'actions :")
for action in best_combination:
    print(action['Action'], '- Coût:', action['Cost'], '€ - Bénéfice:', action['Profit'])

end = time.time()
total_profit = round(sum(round(float(action['Profit']) * round(float(action['Cost'])/100, 2), 2) for action in best_combination), 2)
print("Profit total :", total_profit)
total_depense = round(sum(round(float(action['Cost']), 2) for action in best_combination), 2)
print("Dépense :", total_depense)
print(f"Temps d'exécution : {end - start} secondes")

# Obtenez à nouveau l'utilisation de la RAM après l'exécution de votre code
ram_usage_after = psutil.virtual_memory().used
# Calculer la différence d'utilisation de la RAM
ram_usage_diff = ram_usage_after - ram_usage
print("Utilisation de la RAM de l'algorithme:", ram_usage_diff, "octets")

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