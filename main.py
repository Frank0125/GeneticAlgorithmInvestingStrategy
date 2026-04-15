import lib #setting seed first
from classes.InvestStrategy import InvestStrategy

InvestStrategy1 = InvestStrategy(schedule=1)

def main():
    # InvestStrategy1.print_gene_catalogue()
    InvestStrategy1.simulate_month()


main()