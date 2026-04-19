import random
from typing import List

from genetic_algorithm.GeneCollections import TAKE_PROFIT_GENES, STOP_LOSS_GENES, RISK_GENES, STOCK_GENES, SCHEDULE_GENES
from classes.InvestStrategy import InvestStrategy

#! Genetic algorithm to get the best arrangement of genes in an Investment Strategy to get the most amount of money in 10 years (total winnings)
class GeneticAlgorithmJohn():
    def __init__(self, popupalation_size_p : int, mutation_rate_p : int):
        self.population_size : int = popupalation_size_p
        self.mutation_rate : int = mutation_rate_p
        self.strategies : List[InvestStrategy] = [None] * self.population_size

        self.create_population()
    def create_population(self) -> None:
        self.strategies = [InvestStrategy(i%2, i%3, i%4, i%3, i%2) for i in range(self.population_size)] #cool way of doing for

        return 

    def reproduce(self):
        #!rule:
        #* Mother strat give genes 0,2,4
        #*Father gives 1,3
        return

    def run_generation(self):
        years : int = 10
        months : int = 12 * years
        [si.simulate_months(months) for si in self.strategies]
        
