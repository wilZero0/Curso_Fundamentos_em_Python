
# Solicita um número de 1 a 12
numero = int(input("Digite um número entre 1 e 12: "))

# Lista de meses
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Verifica se o número é válido e mostra o mês
if 1 <= numero <= 12:
    print(f"O mês correspondente é {meses[numero - 1]}.")
else:
    print("Número inválido.")
