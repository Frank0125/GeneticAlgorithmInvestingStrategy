from abc import ABC

#! NOT
class StopLoss(ABC):
    def __init__(self, performance, risk ):
        self.performance = performance
        self.risk = risk

    def getPerformance(self):
        return self.performance

    def getRisk(self):
        return self.risk


