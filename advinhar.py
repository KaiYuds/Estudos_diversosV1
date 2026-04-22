import random

def numero_aleatorio():
    return random.randint(1, 100)

def jogar_adivinhar():
    numero_secreto = numero_aleatorio()
    tentativas = 0
    acertou = False

    print("Bem-vindo ao jogo de adivinhar o número!")
    print("Tente adivinhar o número entre 1 e 100.")

    while not acertou:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                acertou = True
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def main():
    jogar_adivinhar()

if __name__ == "__main__":
    main()