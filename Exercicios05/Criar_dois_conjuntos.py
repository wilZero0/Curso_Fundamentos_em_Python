
# Conjunto com as vogais
vogais = {'a', 'e', 'i', 'o', 'u'}

# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra: ").lower()

# Cria um conjunto com as letras da palavra
letras_palavra = set(palavra)

# Encontra as letras em comum entre os dois conjuntos
comuns = vogais & letras_palavra

# Exibe o resultado
print(f"\nLetras em comum com as vogais: {comuns}")
