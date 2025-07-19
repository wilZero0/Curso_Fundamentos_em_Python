
def nome_completo(nome, sobrenome):
    return f"{nome} {sobrenome}"
n = input("Digite seu nome: ")
s = input("Digite seu sobrenome: ")
print(f"Olá, {nome_completo(n, s)}!")
