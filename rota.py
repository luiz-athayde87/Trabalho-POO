from typing import List, Optional
from veiculo import Veiculo

class Rota:
    def __init__(self, codigo: str, origem: str, destino: str, distancia_km: float):
        self.codigo = codigo
        self.origem = origem
        self.destino = destino
        self.distancia_km = distancia_km
        self.veiculos: List[Veiculo] = []
    
    def adicionar_veiculo(self, veiculo: Veiculo):
        self.veiculos.append(veiculo)
        veiculo.definir_rota(self)
    
    def __str__(self):
        return f"Rota {self.codigo}: {self.origem} → {self.destino} ({self.distancia_km}km)"