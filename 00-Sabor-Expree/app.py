from Modelos.restaurante import Restaurante

Restaurante_praca = Restaurante('Praça', 'Gourmet')
Restaurante_pizza = Restaurante('Pizza', 'Fast Food')

Restaurante_praca.adicionar_avaliacao('kaio', 7)
Restaurante_praca.alterar_status()
Restaurante_praca.adicionar_avaliacao('Laio', 9)
Restaurante_praca.adicionar_avaliacao('Paio', 6)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()