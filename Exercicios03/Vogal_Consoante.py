
# Solicita uma letra ao usuário
letra = input("Digite uma letra: ").lower()

# Verifica se é uma letra do alfabeto
if len(letra) == 1 and letra.isalpha():
    if letra in 'aeiou':
        print("É uma vogal.")
    else:
        print("É uma consoante.")
else:
    print("Entrada inválida. Digite apenas uma letra.")
