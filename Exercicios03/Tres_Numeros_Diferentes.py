
# Solicita três números diferentes
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verifica se os números são diferentes
if num1 != num2 and num1 != num3 and num2 != num3:
    # Determina o maior número
    maior = max(num1, num2, num3)
    print(f"O maior número é {maior}.")
else:
    print("Os números devem ser diferentes.")
