from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from enum import Enum
from transporte import Transporte
from metro import Metro
from trem import Trem
from onibus import Onibus
from vlt import VLT
from calculadora import CalculadorTarifa
from tarifanormal import TarifaNormal
from tarifahorapico import TarifaHorarioPico
from tarifafimdesemana import TarifaFimDeSemana
from tarifaintegracao import TarifaIntegracao
from pagamentos import MetodoPagamento, PagamentoSaldo, PagamentoCredito, CartaoTransporte
from motorista import Motorista
from veiculo import Veiculo
from rota import Rota
from sistema import SistemaTransporte

def demonstrar_sistema():
    print("=" * 60)
    print("SISTEMA DE TRANSPORTE URBANO - SOLID")
    print("=" * 60)
 
    sistema = SistemaTransporte()

    onibus = Onibus("BUS-01", 50)
    metro = Metro("MET-01", 300)
    trem = Trem("TRE-01", 200)
    vlt = VLT("VLT-01", 80)
 
    rota1 = Rota("R01", "Centro", "Zona Sul", 12.5)
    rota2 = Rota("R02", "Centro", "Zona Norte", 15.0)
    rota3 = Rota("R03", "Estação Central", "Aeroporto", 25.0)
    
    sistema.adicionar_rota(rota1)
    sistema.adicionar_rota(rota2)
    sistema.adicionar_rota(rota3)
    
    veiculo1 = Veiculo("Maricá-Rio", onibus, 50)
    veiculo2 = Veiculo("Metrô Rio", metro, 300)
    veiculo3 = Veiculo("Trem Central", trem, 200)
    
    sistema.adicionar_veiculo(veiculo1)
    sistema.adicionar_veiculo(veiculo2)
    sistema.adicionar_veiculo(veiculo3)
    
    motorista1 = Motorista("João Silva", "5641564")
    motorista2 = Motorista("Maria Santos", "231546572")
    
    sistema.adicionar_motorista(motorista1)
    sistema.adicionar_motorista(motorista2)
    
    motorista1.atribuir_veiculo(veiculo1)
    motorista2.atribuir_veiculo(veiculo2)
    
    cartao1 = CartaoTransporte("CARD01", "João Silva")
    cartao2 = CartaoTransporte("CARD02", "Maria Santos")
    
    sistema.adicionar_cartao(cartao1)
    sistema.adicionar_cartao(cartao2)
    
    cartao1.carregar_saldo(50.0)
    cartao2.carregar_saldo(30.0)
    
    print("\n" + "=" * 60)
    print("DEMONSTRAÇÃO DE VIAGENS")
    print("=" * 60)
    
    sistema.realizar_viagem(cartao1, onibus, PagamentoSaldo())
    
    print("\n--- Alterando política tarifária para Horário de Pico ---")
    sistema.definir_politica_tarifaria(TarifaHorarioPico())
    horario_pico = datetime.now().replace(hour=8, minute=30)
    sistema.realizar_viagem(cartao2, metro, PagamentoSaldo(), horario_pico)
    
    print("\n--- Alterando política tarifária para Fim de Semana ---")
    sistema.definir_politica_tarifaria(TarifaFimDeSemana())
    fim_semana = datetime.now().replace(day=datetime.now().day + (5 - datetime.now().weekday()))
    sistema.realizar_viagem(cartao1, trem, PagamentoSaldo(), fim_semana)
    
    print("\n--- Usando pagamento por CRÉDITO ---")
    sistema.definir_politica_tarifaria(TarifaNormal())
    sistema.realizar_viagem(cartao2, vlt, PagamentoCredito())
    
    print("\n--- Tentativa com saldo insuficiente ---")
    cartao2.saldo = 1.0
    sistema.realizar_viagem(cartao2, onibus, PagamentoSaldo())
    
    cartao1.ver_historico()
    cartao2.ver_historico()
    
    print("\n" + "=" * 40)
    print("RESUMO DOS PRINCÍPIOS SOLID APLICADOS:")
    print("=" * 40)
    print("✓ LSP - Classes Onibus, Metro, Trem, VLT substituem Transporte")
    print("✓ OCP - Políticas tarifárias extensíveis (Normal, HorárioPico, etc.)")
    print("✓ DIP - Métodos de pagamento injetados (Saldo, Crédito, Débito)")
    print("=" * 40)

if __name__ == "__main__":
    demonstrar_sistema()