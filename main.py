import lib #seed configuration first

from GeneCollections import TAKE_PROFIT_GENES, STOP_LOSS_GENES, RISK_GENES, TYPE_GENES, SCHEDULE_GENES
from classes.InvestStrategy import InvestStrategy

InvestStrategy1 = InvestStrategy(schedule=1, risk_gene=RISK_GENES[0])

def main():
    # InvestStrategy1.print_gene_catalogue()
    years : int = 10
    months : int = 12 * years
    InvestStrategy1.simulate_months(months)


main()