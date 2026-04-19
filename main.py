import argparse
from genetic_algorithm.GeneticAlgorithm import GeneticAlgorithmJohn
import lib #seed configuration first

from genetic_algorithm.GeneCollections import TAKE_PROFIT_GENES, STOP_LOSS_GENES, RISK_GENES, STOCK_GENES, SCHEDULE_GENES
from classes.InvestStrategy import InvestStrategy


def arg_handler():
    parser = argparse.ArgumentParser(description="A simple parameter script")
    
    # Add an optional argument with a flag
    parser.add_argument("--debug", type=int, choices=[0,1], help="Debug")
    parser.add_argument("--sl", type=int, choices=[0,1,2,3], help="Stop Loss Gene")
    parser.add_argument("--tk", type=int,choices=[0,1,2,3], help="Take Profit Gene")
    parser.add_argument("--s", type=int, choices=[0,1,2,3], help="Stock Gene")
    parser.add_argument("--r", type=int, choices=[0,1,2,3], help="Risk Gene")
    parser.add_argument("--sc", type=int,choices=[0,1,2,3], help="Schedule Gene")
    #ex: --debug 1 --sl 1 --tk 2 --s 1 --r 3 --sc 1


    parser.add_argument("--ps", type=int, choices=[100], help="Population Size") #TODO
    parser.add_argument("--mr", type=int, choices=[5, 25, 50, 75], help="Mutation Rate")
    parser.add_argument("--rp", type=int,choices=[50], help="Ranking Selection") #TODO
    parser.add_argument("--gens", type=int,choices=[10, 20, 30, 50, 100], help="Generations")
    #ex: --mr 5 --gens 100

    args = parser.parse_args()
    return args if args.mr and args.gens or args.debug else None


def main():
    script_params = arg_handler()

    if script_params == None:
        print("Need mutation rate (--mr) and generations (--gens) params")

    elif script_params.debug == 1:
        InvestStrategy1 = InvestStrategy(
            gene_array_p=[script_params.sl,
            script_params.tk,
            script_params.s,
            script_params.r,
            script_params.sc, 
            ])

        # InvestStrategy1.print_gene_catalogue()
        InvestStrategy1.simulate_months(120)
        InvestStrategy1.print_total_winnings()

    else:
        #region Population size
        genetic_algorithm = GeneticAlgorithmJohn(popupalation_size_p=100, mutation_rate_p=script_params.mr, ranking_p=50)
        genetic_algorithm.run_generations(generations=script_params.gens)
    

    print("\nEND")

main()