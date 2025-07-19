
def eh_palindromo(palavra):
    invertida = palavra[::-1]
    return palavra == invertida
texto = input("Digite uma palavra: ")
if eh_palindromo(texto):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
