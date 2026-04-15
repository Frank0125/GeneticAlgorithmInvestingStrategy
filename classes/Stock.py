from abc import ABC, abstractmethod

class Risk(ABC):
    def __init__(self, added_risk_and_bonus_performance : int):
        self.added_risk = added_risk_and_bonus_performance
        self.bonus_performance = added_risk_and_bonus_performance
    
    def get_added_risk(self) -> int:
        return self.added_risk

    def get_bonus_performance(self) -> int:
        return self.bonus_performance

# Class Stock using Decorator

class Stock(ABC):
    @abstractmethod
    def get_performance(self) -> int:
        pass

    def get_risk(self) -> int:
        pass

class SimpleStock(Stock):
    def __init__(self, performance : int, sector_risk : int):
        self.performance = performance
        self.sector_risk = sector_risk

    def get_performance(self) -> int:
        return self.performance

    def get_risk(self) -> int:
        return self.sector_risk

class StockDecorator(Stock):
    def __init__(self, stock : Stock):
        self._decorated_stock = stock

    def get_performance(self) -> int:
        return self._decorated_stock.get_performance()

    def get_risk(self) -> int:
        return self._decorated_stock.get_risk()
    

#concrete classes / genes
class RiskDecorator(StockDecorator):
    def __init__(self, stock : Stock, extra_risk : Risk):
        super().__init__(stock)

        self.extra_risk = extra_risk

    def get_risk(self) -> int:
        return super().get_risk() + self.extra_risk.get_added_risk()
    
    def get_performance(self) -> int:
        return super().get_performance() + self.extra_risk.get_bonus_performance()