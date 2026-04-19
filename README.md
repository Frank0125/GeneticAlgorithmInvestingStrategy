# Homegrown Genetic Algorithm: Investment Strategy
-by Francisco Rochín Gómez - A01252974

#### A custom Python GA built to evolve investment strategies by balancing high returns against risk levels.

$~$

🧬 What’s inside?

    The Brain: A reproduction/crossover/mutation engine that optimizes the best Investing Strategy from a declared Gene Collection.

    Strategy Logic: Uses the Decorator Design Pattern to swap between different risk-profile behaviors dynamically.

    The Gene Array: A modular collection of risk and performance traits stored in int arrays.

$~$

## Gene Array Arrangement and Tags:
### Indexes:
```sh
0. -> Stop Loss Gene -- tag -> --sl
1. -> Take Profit Gene -- tag -> --tk
2. -> Stock Gene -- tag ->  --s
3. -> Risk Gene -- tag ->  --r
4. -> Schedule Gene -- tag -> --sc
```

$~$

🛠 Installation

Grab the code and set up your local environment:

## Clone the repo: 
#### Bash
```sh
    git clone https://github.com/Frank0125/GeneticAlgorithmInvestingStrategy.git
    cd GeneticAlgorithmInvestingStrategy
```

## Setup Virtual Environment:
#### Bash
```sh
    python -m venv .venv
    # Activate on Windows:
    .venv\Scripts\activate
    # Activate on Mac/Linux:
    source .venv/bin/activate
```

$~$

🚀 Running it
-- 
To ensure all internal dependencies and classes (like Stock and InvestStrategy) load correctly, run the project with the following in mind:

> [!NOTE]
> This program uses script params to alternative between testing a singular gene array or executing generations of the Genetic Algorithm

### To test a singular gene array (debuging):
Enable **debuging** by including ***--debug*** tag and include all corresponding tags to each gene following gene arrangement declared above. Example:

#### Bash
```sh
    python main.py --debug 1 --sl 1 --tk 2 --s 0 --r 3 --sc 1
```

### To run generations of Genetic Algorithm:
Include **mutation rate** with the tag ***--mr*** and the **number of generations** with the tag ***--gens***, the arg handler will display in the console the choices available of each if an invalid option is introduced to the tag.

#### Bash
```sh
    python main.py --mr 5 --gens 100
```