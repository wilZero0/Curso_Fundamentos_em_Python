
# Inicializa contador
quantidade = 0

# Laço for para percorrer de 0 a 20
for i in range(0, 21):
    if i % 2 == 0:
        print(i)
        quantidade += 1

# Exibe a quantidade de números pares
print(f"\nTotal de números pares exibidos: {quantidade}")
