from transporte import Transporte

class Metro(Transporte):
    def get_tipo(self) -> str:
        return "Metrô"
    
    def get_tarifa_base(self) -> float:
        return 5.00