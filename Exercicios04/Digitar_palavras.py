
# Lista para armazenar as palavras digitadas
palavras = []

print("Digite palavras (digite 'fim' para encerrar):")

# Loop infinito até que o usuário digite "fim"
while True:
    palavra = input("Palavra: ")
    if palavra.lower() == "fim":
        break
    palavras.append(palavra)

# Exibe todas as palavras digitadas
print("\nPalavras digitadas:")
for p in palavras:
    print(p)
