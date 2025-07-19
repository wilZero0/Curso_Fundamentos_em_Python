
def multiplicar(a, b):
    return a * b

# Parte fora da função: coleta dos números e exibição do resultado
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = multiplicar(num1, num2)
print(f"O produto entre {num1} e {num2} é {resultado}.")
