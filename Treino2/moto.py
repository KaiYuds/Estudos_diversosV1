from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, estilo):
        super().__init__(marca, modelo)
        self.estilo = estilo

    def __str__(self):
        return f'{super().__str__()} - Estilo: {self.estilo}'