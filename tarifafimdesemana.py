from calculadora import CalculadorTarifa
from transporte import Transporte
from datetime import datetime

class TarifaFimDeSemana(CalculadorTarifa):
    def calcular(self, transporte: Transporte, horario: datetime = None) -> float:
        tarifa_base = transporte.get_tarifa_base()
        
        if horario and horario.weekday() >= 5:
            return tarifa_base * 0.8 
        
        return tarifa_base