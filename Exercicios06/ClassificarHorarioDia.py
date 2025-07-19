
def saudacao():
    hora = int(input("Digite a hora atual (0 a 23): "))
    if 5 <= hora <= 12:
        print("Bom dia!")
    elif 13 <= hora <= 18:
        print("Boa tarde!")
    else:
        print("Boa noite!")
