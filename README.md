# Homegrown Genetic Algorithm: Investment Strategy

A custom Python GA built to evolve investment strategies by balancing high returns against risk levels.
🧬 What’s inside?

    The Brain: A selection/crossover/mutation engine that optimizes "investor DNA."

    Strategy Logic: Uses the Strategy Pattern to swap between different risk-profile behaviors dynamically.

    The Gene Pool: A modular collection of risk and performance traits stored in flexible dictionaries.

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

🚀 Running it
-- 
To ensure all internal dependencies and classes (like Stock and InvestStrategy) load correctly, run the project as a module from the root directory:
#### Bash
```sh
python -m main
```