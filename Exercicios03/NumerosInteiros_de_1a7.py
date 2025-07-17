
# Solicita um número de 1 a 7
numero = int(input("Digite um número inteiro de 1 a 7: "))

# Verifica e mostra o dia correspondente
dias_da_semana = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

if numero in dias_da_semana:
    print(f"O dia correspondente é {dias_da_semana[numero]}.")
else:
    print("Número inválido.")
