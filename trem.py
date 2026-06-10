from transporte import Transporte

class Trem(Transporte):
    def get_tipo(self) -> str:
        return "Trem"
    
    def get_tarifa_base(self) -> float:
        return 4.00