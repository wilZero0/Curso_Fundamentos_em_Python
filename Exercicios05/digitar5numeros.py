
# Cria um conjunto vazio
numeros = set()

# Solicita 5 números ao usuário
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.add(num)

# Exibe os números sem repetições
print(f"\nNúmeros digitados (sem repetições): {numeros}")

# Exibe quantos valores únicos foram inseridos
print(f"Quantidade de valores únicos: {len(numeros)}")
