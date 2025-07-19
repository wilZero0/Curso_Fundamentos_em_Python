
# Lista para armazenar os números
numeros = []

# Solicita 3 números ao usuário
for i in range(3):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Exibe a lista de números
print("\nNúmeros digitados:")
print(numeros)

# Calcula a média
media = sum(numeros) / len(numeros)

# Exibe a média
print(f"Média dos números digitados: {media:.2f}")
