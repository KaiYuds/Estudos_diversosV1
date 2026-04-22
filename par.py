x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

if x > 0 and y > 0:
    print("Primeiro Quadrante.")

elif x < 0 and y > 0:
    print("Segundo Quadrante.")

elif x < 0 and y < 0:
    print("Terceiro Quadrante.")

elif x > 0 and y < 0:
    print("Quarto Quadrante.")

else:
    print("Origem.")