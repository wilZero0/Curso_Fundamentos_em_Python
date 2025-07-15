print('Programando um Preço com desconto')

produto = float(input('Digite um valor: '))
desconto = produto*(10/100)
valorfinal = produto - desconto

print(f'O resultado é: {valorfinal}')
