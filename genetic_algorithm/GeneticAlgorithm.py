import random
from typing import List

from genetic_algorithm.GeneCollections import TAKE_PROFIT_GENES, STOP_LOSS_GENES, RISK_GENES, STOCK_GENES, SCHEDULE_GENES
from classes.InvestStrategy import InvestStrategy

#! Genetic algorithm to get the best arrangement of genes in an Investment Strategy to get the most amount of money in 10 years (total winnings)
class GeneticAlgorithmJohn():
    def __init__(self, popupalation_size_p, mutation_rate_p):
        self.population_size : int = popupalation_size_p
        self.mutation_rate : int = mutation_rate_p
        self.strategies : List[InvestStrategy] 

    def create_population(self) -> None:
        for i in self.population_size - 1:
            self.strategies[i] = InvestStrategy(i%2, i%3, i%4, i%5, i%6)
        return

    def reproduce(self):
        #!rule:
        #* Mother strat give genes 0,2,4
        #*Father gives 1,3
        return

    def run_generation(self):
        years : int = 10
        months : int = 12 * years
        for si in self.strategies:
            si.simulate_months(months)
            si.print_total_winnings()
