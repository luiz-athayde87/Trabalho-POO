from abc import ABC, abstractmethod
from typing import List, Optional
from veiculo import Veiculo

class Transporte(ABC):
    def __init__(self, codigo: str, capacidade: int):
        self.codigo = codigo
        self.capacidade = capacidade
        self.veiculos: List[Veiculo] = []
    
    @abstractmethod
    def get_tipo(self) -> str:
        pass
    
    @abstractmethod
    def get_tarifa_base(self) -> float:
        pass
    
    def adicionar_veiculo(self, veiculo: 'Veiculo'):
        self.veiculos.append(veiculo)
    
    def __str__(self):
        return f"{self.get_tipo()} - {self.codigo}"