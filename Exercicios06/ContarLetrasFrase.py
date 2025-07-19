
def contar_letras(frase):
    contador = 0
    for caractere in frase:
        if caractere != " ":
            contador += 1
    return contador
texto = "Copilot é incrível"
total = contar_letras(texto)
print(f"A frase contém {total} letras (sem contar os espaços).")
