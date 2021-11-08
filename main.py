# Jeu de Carte
import random

# Param Global
paq_carte = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nb_essai = 2000
nb_individus = 4
somme_final = 36
produit_final = 360

## List Fonctions

def declare_individu_binaire():
    indiv = [0,0,0,0,0,0,0,0,0,0]
    for i in range(9):
        indiv[i] = random.randint(0,1)

    #print("Individu déclarer :", indiv)
    return indiv

def verifier_solution(indiv):

    if indiv == None:
        return None, None
    else:
        somme = 0
        prod = 1
        index = 0

        for i in indiv:
            if i == 1:
                somme += paq_carte[index]
            else:
                prod *= paq_carte[index]
            index += 1

        #print("Paquet 1 Somme : ", somme)
        #print("Paquet 2 Produit : ", prod)
        return somme, prod

def croisement(ind1, ind2):
    index_croisement = random.randint(0,9)
    switch = 0
    proba = random.random()
    #print("Probabilité :", proba)
    if proba <= 0.8 :
        #print("CROISEMENT")
        #print("Debut de croisement : ", index_croisement)
        while index_croisement < 10:
            switch = ind1[index_croisement]
            ind1[index_croisement] = ind2[index_croisement]
            ind2[index_croisement] = switch
            index_croisement += 1

    return ind1, ind2

def mutation(ind1):
    index_mutation = random.randint(0,9)
    proba = random.random()
    #print("Probabilité :", proba)
    if proba <= 0.01 :
        #print("MUTATION")
        #print("Index de mutation : ", index_mutation)
        if ind1[index_mutation] == 1:
            ind1[index_mutation] = 0
        else:
            ind1[index_mutation] = 1
    return ind1

def generation_next_population(population):

    nb_individus = len(population) + 1
    counter = 1

    # Initialisation de la nouvelle population.
    new_population = []

    # Génération de la nouvelle population.
    while counter < nb_individus:

        if nb_individus - counter != 1:

            # Selection
            index_indiv1 = random.randint(0, len(population)-1)
            index_indiv2 = random.randint(0, len(population)-1)

            # On evite qu'on drop les même index
            while index_indiv1 == index_indiv2:
                index_indiv2 = random.randint(0, len(population) - 1)

            indiv1 = population[index_indiv1]
            indiv2 = population[index_indiv2]

            # Retirer de la liste
            population.pop(population.index(indiv1))
            population.pop(population.index(indiv2))

            # Croisemnt
            indiv1, indiv2 = croisement(indiv1, indiv2)

            # Mutation
            indiv1 = mutation(indiv1)
            indiv2 = mutation(indiv2)


            # Maj nouvelle population
            new_population.append(indiv1)
            new_population.append(indiv2)

            counter += 2
        else:
            #On fait que la mutation sur le dernier individu dans le cas ou la population est impairS
            indiv3 = mutation(population[0])
            new_population.append(indiv3)
            counter +=1

    print(new_population)
    return new_population

def get_meilleur_soluce(best_indiv, population):

    best_sum, best_prod = verifier_solution(best_indiv)

    soluce_total_finale = produit_final + somme_final

    for indiv in population:
        somme, prod = verifier_solution(indiv)

        # Verification Somme
        if best_sum == None and best_prod == None:
            best_indiv = indiv
            best_sum, best_prod = verifier_solution(best_indiv)

        else:
            if(abs(soluce_total_finale - (best_sum + best_prod)) > abs(soluce_total_finale - (somme + prod))):
                best_indiv = indiv.copy()
    return best_indiv

## Main Test


print("Jeu de carte")

# Intialisation du jeu
population = []

for i in range(nb_individus):
    population.append(declare_individu_binaire())

best_indiv =  get_meilleur_soluce(None, population)

#Debut des Essai

counter = 1
while counter <= nb_essai:
    print("GENERATION ", counter)
    population = generation_next_population(population)
    best_indiv =  get_meilleur_soluce(best_indiv, population)
    counter += 1


print("+++ RESULTAT ++++")
print("Meilleur Individu", best_indiv)
best_sum, best_prod = verifier_solution(best_indiv)
print("Meilleur Somme ", best_sum)
print("Meilleur Produit", best_prod)
print("Meilleur Ecart", abs(best_sum + best_prod - 396))

## Afichage des différents paquet du meilleur individu.
paquet1 = []
paquet2 = []
index = 0
for i in best_indiv:
    if i == 1:
        paquet1.append(paq_carte[index])
    else:
        paquet2.append(paq_carte[index])

    index += 1


print("Paquet 1 : ", paquet1)
print("Paquet 2 : ", paquet2)

#Réponse du jeu
# Paquet 1  : 2 + 10 + 9 + 8 + 7  = 36
# Paquet 2 : 6 * 5 * 4 * 3 * 1 = 360

