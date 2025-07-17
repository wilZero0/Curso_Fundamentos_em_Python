
# Solicita um caractere ao usuário
caractere = input("Digite um caractere: ")

# Verifica se é apenas um caractere
if len(caractere) != 1:
    print("Digite apenas um único caractere.")
else:
    if caractere.isupper():
        print("É uma letra maiúscula.")
    elif caractere.islower():
        print("É uma letra minúscula.")
    elif caractere.isalpha():
        print("É uma letra, mas não foi possível identificar o caso.")
    else:
        print("É um caractere especial.")
