from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from calculadora import CalculadorTarifa
from tarifanormal import TarifaNormal
from tarifahorapico import TarifaHorarioPico
from tarifafimdesemana import TarifaFimDeSemana
from tarifaintegracao import TarifaIntegracao

class MetodoPagamento(ABC):
   
    @abstractmethod
    def processar_pagamento(self, valor: float, cartao: 'CartaoTransporte') -> bool:
        pass
    
    @abstractmethod
    def get_nome(self) -> str:
        pass

class PagamentoSaldo(MetodoPagamento):
    def processar_pagamento(self, valor: float, cartao: 'CartaoTransporte') -> bool:
        if cartao.saldo >= valor:
            cartao.saldo -= valor
            cartao.adicionar_transacao(valor, "SALDO")
            return True
        return False
    
    def get_nome(self) -> str:
        return "Pagamento via Saldo"

class PagamentoCredito(MetodoPagamento):
    def processar_pagamento(self, valor: float, cartao: 'CartaoTransporte') -> bool:
        cartao.adicionar_transacao(valor, "CRÉDITO")
        return True
    
    def get_nome(self) -> str:
        return "Pagamento via Crédito"

class PagamentoDebito(MetodoPagamento):
    def processar_pagamento(self, valor: float, cartao: 'CartaoTransporte') -> bool:
        cartao.adicionar_transacao(valor, "DÉBITO")
        return True
    
    def get_nome(self) -> str:
        return "Pagamento via Débito"

class PagamentoPix(MetodoPagamento):
    def processar_pagamento(self, valor: float, cartao: 'CartaoTransporte') -> bool:
        cartao.adicionar_transacao(valor, "Pix")
        return True
    
    def get_nome(self) -> str:
        return "Pagamento via Pix"
    
class CartaoTransporte:
    def __init__(self, codigo: str, titular: str):
        self.codigo = codigo
        self.titular = titular
        self.saldo: float = 0.0
        self.historico: List[dict] = []
    
    def carregar_saldo(self, valor: float):
        self.saldo += valor
        print(f"✓ {self.titular}: Carregado R$ {valor:.2f}. Saldo atual: R$ {self.saldo:.2f}")
    
    def adicionar_transacao(self, valor: float, metodo: str):
        self.historico.append({
            'data': datetime.now(),
            'valor': valor,
            'metodo': metodo,
            'saldo_restante': self.saldo
        })
    
    def consultar_saldo(self) -> float:
        return self.saldo
    
    def ver_historico(self):
        print(f"\n--- Histórico do Cartão {self.codigo} ({self.titular}) ---")
        for transacao in self.historico[-10:]:  # Últimas 10 transações
            print(f"{transacao['data'].strftime('%d/%m %H:%M')} - "
                  f"{transacao['metodo']}: R$ {transacao['valor']:.2f} "
                  f"(Saldo: R$ {transacao['saldo_restante']:.2f})")