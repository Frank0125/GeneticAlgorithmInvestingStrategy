from typing import Dict, List

from classes.Stock import Risk, SimpleStock, Stock

#*Stop Loss
# porcentage over the total invested to limit and sell
# st_ls_p: stop-loss positive genes and _n is for negative
st_gene_size : int = 10
STOP_LOSS_GENES : List[int] = [10,30,50,100] #!1

TAKE_PROFIT_GENES : List[int]= [15,30, 45,100] #!2

#* Declaring Type of Stock
TechStock : Stock = SimpleStock(8, 8)
HealthStock : Stock = SimpleStock(3, 2)
ServicesStock : Stock = SimpleStock(5, 4)
FinanceStock : Stock = SimpleStock(6, 6)

TYPE_GENES : List[Stock] = [TechStock, HealthStock, ServicesStock, FinanceStock] #!3

#*Risk
NoRisk : Risk = Risk(0)
LowRisk : Risk = Risk(5)
MediumRisk : Risk = Risk(10)
HighRisk : Risk = Risk(20)

RISK_GENES : List[Risk]= [NoRisk, LowRisk, MediumRisk, HighRisk] #!4


#*
SCHEDULE_GENES : List[int] = [1, 2, 3, 4] #!5