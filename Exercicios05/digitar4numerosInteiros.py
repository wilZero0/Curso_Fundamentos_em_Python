
# Solicita 4 números ao usuário e armazena em uma tupla
numeros = (
    int(input("Digite o 1º número: ")),
    int(input("Digite o 2º número: ")),
    int(input("Digite o 3º número: ")),
    int(input("Digite o 4º número: "))
)

# Conta quantos números são pares
quantidade_pares = sum(1 for n in numeros if n % 2 == 0)

# Verifica se o número 10 está na tupla
tem_dez = 10 in numeros

# Exibe os resultados
print(f"\nNúmeros digitados: {numeros}")
print(f"Quantidade de números pares: {quantidade_pares}")
print("O número 10 está na tupla?" , "Sim" if tem_dez else "Não")
