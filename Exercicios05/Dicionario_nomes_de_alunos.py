
# Cria o dicionário com nomes e notas dos alunos
alunos = {
    "Ana": 8.5,
    "Bruno": 6.7,
    "Carlos": 9.0,
    "Diana": 5.8,
    "Eduarda": 7.2
}

# Mostra o dicionário completo
print("Notas dos alunos:")
for nome, nota in alunos.items():
    print(f"{nome}: {nota}")

# Mostra apenas alunos com nota >= 7
print("\nAlunos com nota maior ou igual a 7:")
for nome, nota in alunos.items():
    if nota >= 7:
        print(f"{nome}: {nota}")
