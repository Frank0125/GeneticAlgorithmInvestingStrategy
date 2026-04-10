from abc import ABC, abstractmethod

#! Strategy Pattern Design
class Stock(ABC):
    def __init__(self, performance, risk ):
        self.performance = performance
        self.risk = risk

    def getPerformance(self):
        return self.performance

    def getRisk(self):
        return self.risk

    # @abstractmethod
    # def getPerformance(self):
    #     pass

    # def getRisk(self):
    #     pass

# class NoRiskStock(Stock):
#     # def getPerformance(self):
#     #     return self.performance

#     # def getRisk(self):
#     #     return self.risk



