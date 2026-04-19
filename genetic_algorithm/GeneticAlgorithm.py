import random
from typing import List

from genetic_algorithm.GeneCollections import TAKE_PROFIT_GENES, STOP_LOSS_GENES, RISK_GENES, STOCK_GENES, SCHEDULE_GENES
from classes.InvestStrategy import InvestStrategy

#TODO
#mutation logic
#! Genetic algorithm to get the best arrangement of genes in an Investment Strategy to get the most amount of money in 10 years (total winnings)
class GeneticAlgorithmJohn():
    def __init__(self, popupalation_size_p : int, mutation_rate_p : int, ranking_p : int) -> None:
        self.population_size : int = popupalation_size_p
        self.mutation_rate : int = mutation_rate_p
        self.strategies : List[InvestStrategy] = [None] * self.population_size
        self.ranking : int = ranking_p

        self.create_first_population()
    def create_first_population(self) -> None:
        self.strategies = [InvestStrategy(gene_array_p=[i%2, i%3, i%4, i%3, i%2]) for i in range(self.population_size)] #cool way of doing for

        return 
    
    def kill_last_population(self) -> None:
        self.strategies : List[InvestStrategy] = [None] * self.population_size
        return

    #region Crossover   
    def crossover(self, mother_gene_array : List[int], father_gene_array : List[int]) -> List[int]:
        #!rule:
            #* Mother strat give genes 0,2,4
            #*Father gives 1,3
        offspring_gene_array = [
            mother_gene_array[0],
            father_gene_array[1],
            mother_gene_array[2],
            father_gene_array[3],
            mother_gene_array[4],
            ]
        return offspring_gene_array

    def get_offspring_genes(self, best_strats_p : List[InvestStrategy]) -> List[List[int]]:
        offspring_genes: List[List[int]] = []

        for i in range(0, len(best_strats_p) - 1, 2):
            mother = best_strats_p[i]
            father = best_strats_p[i+1]
            
            child_genes = self.crossover(mother.gene_array, father.gene_array)
            offspring_genes.append(child_genes)
        
        return offspring_genes
    
    
    #region Reproduce
    def reproduce(self, offspring_genes_p : List[List[int]]) -> None: #! crossover + mutation        
        self.kill_last_population()
        self.strategies = [InvestStrategy(offspring_genes_p[i]) for i in range(self.population_size)]
        return

    def rank_strategies(self) -> List[InvestStrategy]:
        self.strategies.sort(key=lambda x: x.total_winnings, reverse=True)
        best_strats = self.strategies[:self.ranking]
        self.print_best_ranking(best_strats_p=best_strats)
        return best_strats
    
    def run_generation(self, generations : int = 1) -> None:
        years : int = 10
        months : int = 12 * years
        for g in range(1, generations + 1):
            print("Gen: ", g)        
            if (g==1):
                [si.simulate_months(months) for si in self.strategies]
                best_si = self.rank_strategies()
                gs = self.get_offspring_genes(best_strats_p=best_si)
                self.reproduce(gs)
            else:
                best_si = self.rank_strategies()
                gs = self.get_offspring_genes(best_strats_p=best_si)
                self.reproduce(gs)
        print("Gen end")        

    def print_best_ranking(self, best_strats_p : List[InvestStrategy]) -> None:
        print(self.ranking, "best total winnings: ")
        [b.print_total_winnings() for b in best_strats_p]
        return