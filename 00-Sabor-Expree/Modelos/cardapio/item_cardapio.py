from abc import ABC

class ItemCardapio(ABC):
    def __init__(self, nome: str, preco: float):
        self._nome = nome
        self._preco = preco

    def __str__(self):
        return f"{self._nome} - R${self._preco:.2f}"
    
    def aplicar_desconto(self):
        pass