print('Programa para saber se pode tirar a CNH')
nome = input('Digite seu nome: ')
idade = int(input('Digite a idade: '))
if(idade>18):
    print(f'{nome} CNH permitido')
elif(idade==18):
    print(f'{nome} CNH permitido')
else:
    print(f'{nome} CNH não permitido')