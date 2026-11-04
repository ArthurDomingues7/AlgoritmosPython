texto = int(input("digite uma letra: "))
chave = int(input("qual o passo de contagem: "))

def proxima_letra(letra, chave):
    codigo = ord(letra) + chave
    if codigo > ord ('z'):
        codigo = codigo - 26
    if codigo < ord ('a'):
        codigo = codigo + 26
    return chr(codigo)

def criptografar(chave,texto):
    resultado = ""
    for c in texto:
        reultado += proxima_letra(c,chave)
    return resultado

def criptografar(chave,texto):
    resultado = ""
    for c in texto:
        reultado += proxima_letra(c,-chave)
    return resultado

print(criptografar(chave,texto))