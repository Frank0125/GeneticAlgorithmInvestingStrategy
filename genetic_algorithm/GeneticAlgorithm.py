import random
from typing import List

from genetic_algorithm.GeneCollections import TAKE_PROFIT_GENES, STOP_LOSS_GENES, RISK_GENES, STOCK_GENES, SCHEDULE_GENES
from classes.InvestStrategy import InvestStrategy
def get_crossover_genes(mother_gene_array, father_gene_array):
    offspring_gene_array = [
        mother_gene_array[0],
        father_gene_array[1],
        mother_gene_array[2],
        father_gene_array[3],
        mother_gene_array[4],
        ]
    return offspring_gene_array

#! Genetic algorithm to get the best arrangement of genes in an Investment Strategy to get the most amount of money in 10 years (total winnings)
class GeneticAlgorithmJohn():
    def __init__(self, popupalation_size_p : int, mutation_rate_p : int, ranking_p : int) -> None:
        self.population_size : int = popupalation_size_p
        self.mutation_rate : int = mutation_rate_p
        self.strategies : List[InvestStrategy] = [None] * self.population_size
        self.ranking : int = ranking_p

        self.create_first_population()
    def create_first_population(self) -> None:
        self.strategies = [InvestStrategy(gene_array=[i%2, i%3, i%4, i%3, i%2]) for i in range(self.population_size)] #cool way of doing for

        return 
    
    def kill_last_population(self) -> None:
        self.strategies : List[InvestStrategy] = [None] * self.population_size
        return

    def reproduce(self, best_strats): #! rule + crossover + mutation
        #!rule:
        #* Mother strat give genes 0,2,4
        #*Father gives 1,3
        
        self.kill_last_population()
        # self.
        
        return

    def rank_strategies(self) -> List[InvestStrategy]:
        self.strategies.sort(key=lambda x: x.total_winnings, reverse=True)
        best_strats = self.strategies[:self.ranking]
        print(self.ranking, "best total winnings: ")
        [b.print_total_winnings() for b in best_strats]
        return best_strats
    
    def run_generation(self, generations : int = 1) -> None:
        years : int = 10
        months : int = 12 * years
        [si.simulate_months(months) for si in self.strategies]
        self.rank_strategies()
        

    