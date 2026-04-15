from typing import Dict, List

from classes.Stock import Risk, SimpleStock, Stock

#*Stop Loss
# porcentage over the total invested to limit and sell
# st_ls_p: stop-loss positive genes and _n is for negative
st_gene_size : int = 10
ST_LS_P_GENES : List[int] = [10,15,20,25,30,35,40,45,50,100]

ST_LS_N_GENES : List[int]= [15,20,25,35,45,55,65,75,85,100]

#* Declaring Type of Stock
TechStock : Stock = SimpleStock(8, 8)
HealthStock : Stock = SimpleStock(3, 2)
ServicesStock : Stock = SimpleStock(5, 4)
FinanceStock : Stock = SimpleStock(6, 6)

TYPE_GENES : List[Stock] = [TechStock, HealthStock, ServicesStock, FinanceStock]

#*Risk
NoRisk : Risk = Risk(0)
LowRisk : Risk = Risk(5)
MediumRisk : Risk = Risk(10)
HighRisk : Risk = Risk(20)
RISK_GENES : List[Risk]= [NoRisk, LowRisk, MediumRisk, HighRisk]


#*
SCHEDULE_GENES : List[int] = [1, 2, 3, 4]