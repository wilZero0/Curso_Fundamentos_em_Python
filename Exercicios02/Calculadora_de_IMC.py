# calcular o IMC
peso=float(input('Digite seu peso em Kg: '))
altura=float(input('Digite sua altura: '))
imc=peso/ (altura**2)
if (imc<18):
    print('Esta a baixo do peso')
elif(imc>18.5 and imc == 24.9):
    print('Voce está no peso ideal')
elif(imc>=25):
    print('Sobrepeso')
else:
    print('Obesidade')