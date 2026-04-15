import random
from abc import ABC, abstractmethod
from classes.Stock import Risk, Stock

from GeneCollections import ST_LS_N_GENES, ST_LS_P_GENES, RISK_GENES, TYPE_GENES, SCHEDULE_GENES

RISE = [-1,1]

class InvestStrategy():
    def __init__(self, chosen_stock = TYPE_GENES[0], schedule = 0): #all parameters are genes
        self.chosen_stock : Stock = chosen_stock #Stock(performance = 0, sector_risk = 0)
        self.extra_risk : Risk = Risk(0)
        self.schedule : int = schedule
        self.net_worth : float = 1000
        self.rise : int = 0 # decides if the stock will rise or not. 0 = drop 1 = rise
        self.total_risk = self.chosen_stock.get_risk() + self.extra_risk.get_added_risk()
        

    def rise_calculation(self) -> None:
        random_num = random.randint(0,100) #different everytime
        risk_calc : float = (random_num + self.total_risk) / 100
        rise_trenchmark : float = 0.5
        print(risk_calc)
        if risk_calc > rise_trenchmark: #when risk calculation is over trenchmark, rise gets set to 0
            self.rise = 0
        else:
            self.rise = 1
        return

    # @abstractmethod
    #def invest(self, baseStrength : int) -> int:
        
    
    def growth(self) -> None:
        self.rise_calculation()
        print(RISE[self.rise])
        total_yield = (self.chosen_stock.get_performance() + self.extra_risk.get_bonus_performance()) / 100
        self.net_worth *= (1 + (total_yield * RISE[self.rise]))
        self.check_net_worth()
        return
    
    def check_net_worth(self) -> None:
        if self.net_worth <= 0:
            self.net_worth = 0
        return

    def simulate_month(self) -> None:
        for i in range(self.schedule):
            #add invest function
            self.growth()
        self.print_net_worth()        
        return

    def print_gene_catalogue(self) -> None:
        gene_catalogue = [ST_LS_P_GENES, ST_LS_N_GENES, RISK_GENES, TYPE_GENES, SCHEDULE_GENES]
        for gc in gene_catalogue:
            for g in gc:
                print(g)

    def print_net_worth(self) -> None:
        print(self.net_worth)

