import argparse
import lib #seed configuration first

from GeneCollections import TAKE_PROFIT_GENES, STOP_LOSS_GENES, RISK_GENES, TYPE_GENES, SCHEDULE_GENES
from classes.InvestStrategy import InvestStrategy


def argHandler():
    parser = argparse.ArgumentParser(description="A simple parameter script")
    
    # Add an optional argument with a flag
    parser.add_argument("--s", type=int, help="Schedule Gene")
    parser.add_argument("--tk", type=int, help="Take Profit Gene")
    parser.add_argument("--r", type=int, help="Risk Gene")
    parser.add_argument("--st", type=int, help="Stock Gene")
    
    args = parser.parse_args()

    return args


def main():
    gene_params = argHandler()

    InvestStrategy1 = InvestStrategy(schedule=SCHEDULE_GENES[gene_params.s], risk_gene=RISK_GENES[gene_params.r])

    # InvestStrategy1.print_gene_catalogue()
    years : int = 10
    months : int = 12 * years
    InvestStrategy1.simulate_months(months)


main()