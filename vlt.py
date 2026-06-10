from transporte import Transporte

class VLT(Transporte):
    def get_tipo(self) -> str:
        return "VLT"
    
    def get_tarifa_base(self) -> float:
        return 3.50