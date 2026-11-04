# Escreva uma função chamada remover_consecutivos(valores) que receba
# uma lista de números inteiros e retorne uma nova lista eliminando apenas repetições
# consecutivas.
# Por exemplo:
# [4, 4, 4, 2, 2, 7, 4, 4, 9]
# deve produzir:
# [4, 2, 7, 4, 9]
# Observe que o valor 4 aparece novamente na lista final porque sua última ocorrência
# não é consecutiva às ocorrências iniciais. Não utilize conjuntos para resolver a questão.
lista = []

def remover_consecutivos(valores):
    nova_lista = []
    for i in len(lista):
        if lista[i] != lista[i-1]:
            nova_lista.append(lista[i])

contador = 0
while contador == 0:
    valores = int(input("digite um valor: "))
    if valores != 0:
        lista.append(valores)
    else:
        print("finalizado")
        contador += 1
