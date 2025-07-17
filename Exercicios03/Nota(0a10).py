
# Solicita a nota do aluno
nota = float(input("Digite a nota do aluno (0 a 10): "))

# Verifica e mostra o resultado
if nota < 0 or nota > 10:
    print("Nota inválida. Digite um valor entre 0 e 10.")
elif nota < 5:
    print("Reprovado")
elif 5 <= nota <= 6.9:
    print("Recuperação")
else:
    print("Aprovado")
