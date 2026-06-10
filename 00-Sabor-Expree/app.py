from Modelos.restaurante import Restaurante
from Modelos.cardapio.bebida import Bebida
from Modelos.cardapio.prato import Prato


Restaurante_praca = Restaurante('Praça', 'Gourmet')
Restaurante_pizza = Restaurante('Pizza', 'Fast Food')
bebida1 = Bebida('Suco de Laranja', 5.0, '500ml')
bebida1.aplicar_desconto()
Prato1 = Prato('Cachorro quente', 15, '1kg')
Prato1.aplicar_desconto()

Restaurante_praca.adicionar_item_cardapio(bebida1)
Restaurante_praca.adicionar_item_cardapio(Prato1)


def main():
    #Restaurante.listar_restaurantes()
    Restaurante_praca.exibir_itens_cardapio()


if __name__ == "__main__":
    main()