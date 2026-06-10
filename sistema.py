from rotas import Rota
from veiculo import Veiculo
from motorista import Motorista
from cartao import CartaoTransporte
from tarifa import CalculadorTarifa, TarifaNormal
from typing import List, Optional
from datetime import datetime

class SistemaTransporte:
    def __init__(self):
        self.rotas: List[Rota] = []
        self.veiculos: List[Veiculo] = []
        self.motoristas: List[Motorista] = []
        self.cartoes: List[CartaoTransporte] = []
        self.calculador_tarifa: CalculadorTarifa = TarifaNormal()
    
    def definir_politica_tarifaria(self, calculador: CalculadorTarifa):
        # OCP - Permite trocar a política tarifária facilmente
        self.calculador_tarifa = calculador
        print(f"✓ Política tarifária alterada para: {calculador.__class__.__name__}")
    
    def realizar_viagem(self, cartao: CartaoTransporte, transporte: Transporte, 
                       metodo_pagamento: MetodoPagamento, horario: datetime = None):
        # DIP - Usa injeção de dependência para método de pagamento
        if horario is None:
            horario = datetime.now()
        
        valor = self.calculador_tarifa.calcular(transporte, horario)
        
        print(f"\n--- Viagem em {transporte.get_tipo()} ---")
        print(f"Tarifa calculada: R$ {valor:.2f}")
        print(f"Método: {metodo_pagamento.get_nome()}")
        
        if metodo_pagamento.processar_pagamento(valor, cartao):
            print(f"✓ Pagamento aprovado! Saldo restante: R$ {cartao.saldo:.2f}")
            return True
        else:
            print(f"✗ Pagamento recusado! Saldo insuficiente: R$ {cartao.saldo:.2f}")
            return False
    
    def adicionar_rota(self, rota: Rota):
        self.rotas.append(rota)
        print(f"✓ Rota adicionada: {rota}")
    
    def adicionar_veiculo(self, veiculo: Veiculo):
        self.veiculos.append(veiculo)
        veiculo.transporte.adicionar_veiculo(veiculo)
        print(f"✓ Veículo adicionado: {veiculo}")
    
    def adicionar_motorista(self, motorista: Motorista):
        self.motoristas.append(motorista)
        print(f"✓ {motorista}")
    
    def adicionar_cartao(self, cartao: CartaoTransporte):
        self.cartoes.append(cartao)
        print(f"✓ Cartão criado: {cartao.codigo} - {cartao.titular}")