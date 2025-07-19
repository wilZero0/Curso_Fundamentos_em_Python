
# Lista para armazenar os nomes das frutas
frutas = []

print("Digite nomes de frutas (o programa terminará quando uma tiver mais de 10 letras):")

# Laço while para continuar enquanto a condição não é satisfeita
while True:
    fruta = input("Fruta: ")
    if len(fruta) > 10:
        break
    frutas.append(fruta)

# Exibe quantas frutas foram inseridas
print(f"\nQuantidade de frutas inseridas: {len(frutas)}")
