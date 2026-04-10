from typing import Dict, List

from classes.Stock import Stock

#*Stop Loss
# porcentage over the total invested to limit and sell
# st_ls_p: stop-loss positive genes and _n is for negative
st_gene_size : int = 10
ST_LS_P_GENES : List[int] = [10,15,20,25,30,35,40,45,50,100]

ST_LS_N_GENES : List[int]= [15,20,25,35,45,55,65,75,85,100]

#* Declaring Type of Stock
TechStock : Stock = Stock(8, 8)
HealthStock : Stock = Stock(3, 2)
ServicesStock : Stock = Stock(5, 4)
FinanceStock : Stock = Stock(6, 6)

TYPE_GENES : List[Stock] = [TechStock, HealthStock, ServicesStock, FinanceStock]

#*Risk
RISK_GENES : List[Dict[str, int]]= [
    {"NO_RISK" : 0, },
    {"LOW_RISK" : 5 },
    {"MEDIUM_RISK" : 10},
    {"HIGH_RISK" : 5 }
]


#*
SCHEDULE_GENES : List[int] = [1, 2, 4]