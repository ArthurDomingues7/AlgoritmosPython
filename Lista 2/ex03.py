#Crie um programa que leia 20 números inteiros e os armazene em uma lista. 
# Crie uma função eliminar_duplicatas(lista) que retorne uma nova lista 
# contendo os mesmos elementos, mas mantendo apenas a primeira ocorrência de cada
# número (preservando a ordem original). Observação: Não utilize conjuntos (sets)
# para resolver a questão.

contador = 0
lista = []

while contador < 20:
    numeros_inteiros = int(input("Digite um numero inteiro: "))
    lista.append(numeros_inteiros)
    contador += 1

def eliminar_duplicatas(lista):
    nova_lista = []
    for n in lista:
        if n not in nova_lista:
            nova_lista.append(n)
    return nova_lista

resultado = eliminar_duplicatas(lista)

print(resultado)

