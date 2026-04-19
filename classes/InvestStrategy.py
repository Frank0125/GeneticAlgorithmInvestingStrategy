import math
import random
from abc import ABC, abstractmethod
from classes.Stock import Risk, RiskDecorator, Stock

from GeneCollections import TAKE_PROFIT_GENES, STOP_LOSS_GENES, RISK_GENES, TYPE_GENES, SCHEDULE_GENES

RISE = [-1,1]
#TODO

#ADD year logic
#turn performance into random range-toggle
class InvestStrategy():
    def __init__(self, stock_gene = TYPE_GENES[0], risk_gene = RISK_GENES[3], schedule = SCHEDULE_GENES[0],
                 stop_loss_gene = TAKE_PROFIT_GENES[0], take_profit_gene = TAKE_PROFIT_GENES[0]): #all parameters are genes
        self.chosen_stock : Stock = RiskDecorator(stock_gene, risk_gene) #to the stock we add the values added from risk gene, now chosen_stock has total risk and performance
        self.schedule : int = schedule
        self.stop_loss : float = -(stop_loss_gene / 100) + 1
        self.take_profit : float= (take_profit_gene / 100) + 1
        
        self.positive_sells : int = 0
        self.net_worth : float = 0 #!set to 0
        self.total_winnings : float = 0
        self.rise : int = 0 # decides if the stock will rise or not. 0 = drop 1 = rise
        

    def rise_calculation(self) -> None:
        random_num = random.randint(0,100) #different everytime
        risk_calc : float = (random_num + self.chosen_stock.get_risk()) / 100
        rise_trenchmark : float = 0.5
        if risk_calc > rise_trenchmark: #when risk calculation is over trenchmark, rise gets set to 0
            self.rise = 0
        else:
            self.rise = 1
        return

    # @abstractmethod
    #def invest(self, baseStrength : int) -> int:
        
    
    def growth(self) -> None:
        self.rise_calculation()
        prev_net_worth = self.net_worth
        total_yield = (self.chosen_stock.get_performance()) / 100
        self.net_worth *= (1 + (total_yield * RISE[self.rise]))
        self.check_net_worth(prev_net_worth)
        return
    
    def add_total_winnings(self, amount : float) -> None:
        self.total_winnings += amount
        self.net_worth = 0 #reset net worth
        return
    
    def check_net_worth(self, previous_net_worth : float) -> None:  #! Selling logic
        if self.net_worth >= previous_net_worth * self.take_profit :
            self.positive_sells += 1
            self.add_total_winnings(self.net_worth)
        elif self.net_worth <= previous_net_worth * self.stop_loss :
            self.positive_sells -= 1
            self.add_total_winnings(self.net_worth)    
        elif self.net_worth <= 0: #?FUTURE: add leverage logic
            self.add_total_winnings(self.net_worth)
        return

    def simulate_months(self, months : int) -> None:
        for i in range(math.ceil(months * self.schedule)):
            
            self.growth()  #growth should be done every 2 weeks 
            #add correct invest function
            self.net_worth += (100 / self.schedule)
        self.print_total_winnings()    
        self.print_positive_sells()    
        
        return
    

    def print_gene_catalogue(self) -> None:
        gene_catalogue = [STOP_LOSS_GENES, TAKE_PROFIT_GENES, RISK_GENES, TYPE_GENES, SCHEDULE_GENES]
        for gc in gene_catalogue:
            for g in gc:
                print(g)

    def print_net_worth(self) -> None:
        print(self.net_worth)


    def print_positive_sells(self) -> None:
        print("Total positive sells: ", self.positive_sells)

    def print_total_winnings(self) -> None:
        print("Total winnings in 10 years: $", self.total_winnings)

