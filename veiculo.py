from typing import List, Optional
from transporte import Transporte
from motorista import Motorista
from rota import Rota

class Veiculo:
    def __init__(self, placa: str, transporte: Transporte, capacidade: int):
        self.placa = placa
        self.transporte = transporte
        self.capacidade = capacidade
        self.motorista: Optional[Motorista] = None
        self.rota_atual: Optional['Rota'] = None
    
    def definir_rota(self, rota: 'Rota'):
        self.rota_atual = rota
    
    def __str__(self):
        return f"Veículo {self.placa} - {self.transporte}"