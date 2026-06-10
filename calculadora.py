from abc import ABC, abstractmethod
from datetime import datetime
from transporte import Transporte

class CalculadorTarifa(ABC):
    """Classe base para cálculo de tarifas (OCP)"""
    
    @abstractmethod
    def calcular(self, transporte: Transporte, horario: datetime = None) -> float:
        pass