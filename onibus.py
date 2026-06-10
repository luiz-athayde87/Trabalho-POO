from transporte import Transporte

class Onibus(Transporte):
    def get_tipo(self) -> str:
        return "Ônibus"
    
    def get_tarifa_base(self) -> float:
        return 4.50