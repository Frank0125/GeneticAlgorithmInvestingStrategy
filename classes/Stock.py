from abc import ABC, abstractmethod

class Stock(ABC):
    def __init__(self, performance : int, sector_risk : int):
        self.performance = performance
        self.sector_risk = sector_risk

    def get_performance(self) -> int:
        return self.performance

    def get_risk(self) -> int:
        return self.sector_risk


class Risk(ABC):
    def __init__(self, added_risk_and_bonus_performance : int):
        self.added_risk = added_risk_and_bonus_performance
        self.bonus_performance = added_risk_and_bonus_performance
    
    def get_added_risk(self) -> int:
        return self.added_risk

    def get_bonus_performance(self) -> int:
        return self.bonus_performance

