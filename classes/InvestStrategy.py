from abc import ABC, abstractmethod
from classes.Stock import Stock

from GeneCollections import ST_LS_N_GENES, ST_LS_P_GENES, RISK_GENES, TYPE_GENES, SCHEDULE_GENES
#!
class InvestStrategy():
    def __init__(self):
        self.stock : Stock = Stock(performance = 0, risk = 0)

    def print_gene_catalogue(self):
        gene_catalogue = [ST_LS_P_GENES, ST_LS_N_GENES, RISK_GENES, TYPE_GENES, SCHEDULE_GENES]
        for gc in gene_catalogue:
            for g in gc:
                print(g)

    # @abstractmethod
    # def invest(self, baseStrength : int) -> int:
    #     pass
    
    # def growth(self):
    #     pass