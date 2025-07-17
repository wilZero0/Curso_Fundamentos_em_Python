
# Solicita a temperatura em graus Celsius
temperatura = float(input("Digite a temperatura em graus Celsius: "))

# Verifica e mostra a mensagem correspondente
if temperatura < 0:
    print("Está congelando!")
elif 0 <= temperatura <= 25:
    print("Temperatura amena.")
else:
    print("Está quente!")
