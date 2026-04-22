def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):   
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):    
    if num2 == 0:
        return "Erro: Divisão por zero não é permitida."
    return num1 / num2

def main():
    print("Calculadora Simples")
    try: 
        num1 = float(input("Digite o primeiro número: "))
        operação = input("Escolha a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        if operação == "+":
            print(f"Soma: {somar(num1, num2)}")
        elif operação == "-":
            print(f"Subtração: {subtrair(num1, num2)}")
        elif operação == "*":
            print(f"Multiplicação: {multiplicar(num1, num2)}")
        elif operação == "/":
            print(f"Divisão: {dividir(num1, num2)}")
        else:
            print("Erro: Operação inválida.")
            return
        
    except ValueError:
        print("Erro: Por favor, digite números válidos.")

    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")

if __name__ == "__main__":
    main()