from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, qnt_portas):
        super().__init__(marca, modelo)
        self.qnt_portas = qnt_portas

    def __str__(self):
        return f'{super().__str__()} - Portas: {self.qnt_portas}'
    
