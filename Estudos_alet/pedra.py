import random

def jogar_pedra_papel_tesoura():
    JOGO = ["pedra", "papel", "tesoura"]
    escolha_jogador = input("Escolha pedra, papel ou tesoura: ").lower()
    escolha_computador = random.choice(JOGO)

    if escolha_jogador not in JOGO:
        print("Opção inválida. Por favor, escolha pedra, papel ou tesoura.")
        return


    print(f"Você escolheu: {escolha_jogador}")
    print(f"O computador escolheu: {escolha_computador}")

    if escolha_jogador == escolha_computador:
        print("Empate!")
    elif ((escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
        (escolha_jogador == "papel" and escolha_computador == "pedra") or \
        (escolha_jogador == "tesoura" and escolha_computador == "papel")):
        print("Parabéns! Você venceu!")

    else:
        print("O computador venceu!")
    
def main():
    jogar_pedra_papel_tesoura()

if __name__ == "__main__":
    main()