from calculadora import CalculadorTarifa
from transporte import Transporte
from datetime import datetime

class TarifaHorarioPico(CalculadorTarifa):
    def calcular(self, transporte: Transporte, horario: datetime = None) -> float:
        tarifa_base = transporte.get_tarifa_base()
        
        if horario and (6 <= horario.hour <= 9 or 17 <= horario.hour <= 20):
            return tarifa_base * 1.2
        
        return tarifa_base