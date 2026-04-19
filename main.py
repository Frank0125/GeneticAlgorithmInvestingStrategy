import argparse
from genetic_algorithm.GeneticAlgorithm import GeneticAlgorithmJohn
import lib #seed configuration first

from genetic_algorithm.GeneCollections import TAKE_PROFIT_GENES, STOP_LOSS_GENES, RISK_GENES, STOCK_GENES, SCHEDULE_GENES
from classes.InvestStrategy import InvestStrategy


def argHandler():
    parser = argparse.ArgumentParser(description="A simple parameter script")
    
    # Add an optional argument with a flag
    parser.add_argument("--sl", type=int, choices=[0,1,2,3], help="Stop Loss Gene")
    parser.add_argument("--tk", type=int,choices=[0,1,2,3], help="Take Profit Gene")
    parser.add_argument("--s", type=int, choices=[0,1,2,3], help="Stock Gene")
    parser.add_argument("--r", type=int, choices=[0,1,2,3], help="Risk Gene")
    parser.add_argument("--sc", type=int,choices=[0,1,2,3], help="Schedule Gene")
    
    
    args = parser.parse_args()

    return vars(args) if args.sc else None


def main():
    gene_params = argHandler()

    if gene_params != None:
        InvestStrategy1 = InvestStrategy(
            stop_loss_gene=gene_params.sl,
            take_profit_gene=gene_params.tk,
            stock_gene=gene_params.s,
            risk_gene=gene_params.r,
            schedule_gene=gene_params.sc, 
            )

        # InvestStrategy1.print_gene_catalogue()
        InvestStrategy1.simulate_months(120)

    genetic_algorithm = GeneticAlgorithmJohn(popupalation_size_p=100, mutation_rate_p=5)
    genetic_algorithm.run_generation()


main()