
# Solicita um número ao usuário
numero = int(input("Digite um número: "))

print(f"Números entre 1 e {numero} que são divisíveis por 7:")

# Laço for para verificar os divisíveis por 7
for i in range(1, numero + 1):
    if i % 7 == 0:
        print(i)
