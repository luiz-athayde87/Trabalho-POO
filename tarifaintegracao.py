from calculadora import CalculadorTarifa
from transporte import Transporte
from datetime import datetime

class TarifaIntegracao(CalculadorTarifa):
    def __init__(self, integracoes: int = 1):
        self.integracoes = integracoes
    
    def calcular(self, transporte: Transporte, horario: datetime = None) -> float:
        tarifa_base = transporte.get_tarifa_base()
        desconto = 0.3 * self.integracoes  
        return max(tarifa_base - desconto, 1.0)