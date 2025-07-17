
# Exercício 13: Nota do aluno

# Passo 1: Pedir a nota
nota = float(input("Digite a nota do aluno (entre 0 e 10): "))

# Passos 2 a 4: Verificar a situação do aluno
if nota >= 7:
    resultado = "Aprovado"
elif 5 <= nota < 7:
    resultado = "Em recuperação"
else:
    resultado = "Reprovado"

# Passo 5: Mostrar o resultado
print(f"O aluno está {resultado}.")
