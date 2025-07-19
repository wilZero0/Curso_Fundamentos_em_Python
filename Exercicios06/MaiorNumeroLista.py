
def encontrar_maior(lista):
    maior = lista[0]  # Assume que o primeiro é o maior, inicialmente
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior
numeros = [10, 25, 3, 42, 18]
maior_valor = encontrar_maior(numeros)
print(f"O maior número da lista é {maior_valor}.")

