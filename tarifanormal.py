from calculadora import CalculadorTarifa
from transporte import Transporte
from datetime import datetime

class TarifaNormal(CalculadorTarifa):
    def calcular(self, transporte: Transporte, horario: datetime = None) -> float:
        return transporte.get_tarifa_base()