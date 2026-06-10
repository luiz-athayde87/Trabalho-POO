from typing import List, Optional
from veiculo import Veiculo
from rota import Rota

class Motorista:
    def __init__(self, nome: str, cnh: str):
        self.nome = nome
        self.cnh = cnh
        self.veiculo_atual: Optional['Veiculo'] = None
    
    def atribuir_veiculo(self, veiculo: 'Veiculo'):
        self.veiculo_atual = veiculo
        veiculo.motorista = self
    
    def __str__(self):
        return f"Motorista: {self.nome} (CNH: {self.cnh})"