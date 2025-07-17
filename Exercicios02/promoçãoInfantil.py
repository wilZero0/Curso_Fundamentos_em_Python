
# Passo 1: Pedir a idade da criança
idade = int(input("Digite a idade da criança: "))

# Passo 2 e 3: Verificar se tem direito à promoção e mostrar a mensagem
if idade <= 12:
    print("Ingresso gratuito! Aproveite a promoção infantil 🎉")
else:
    print("Ingresso não gratuito. A promoção é apenas para crianças de até 12 anos.")
