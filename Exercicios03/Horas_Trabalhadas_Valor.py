
# Solicita as horas trabalhadas e o valor da hora
horas = float(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora: R$ "))

# Calcula o salário bruto
salario = horas * valor_hora

# Mostra o salário e sua classificação
print(f"Salário bruto: R$ {salario:.2f}")

if salario <= 1000:
    print("Salário baixo")
elif 1001 <= salario <= 3000:
    print("Salário médio")
else:
    print("Salário alto")
