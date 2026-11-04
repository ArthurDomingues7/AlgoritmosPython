#Crie um programa em Python que leia 7 números inteiros e armazene os valores em uma lista.

#Depois, encontre e exiba:

#o maior valor da lista;
#a posição em que o maior valor aparece pela primeira vez;
#o menor valor da lista;
#a posição em que o menor valor aparece pela primeira vez.
#Importante: não use as funções prontas max(), min() ou index().

lista = []
maior = 0
menor = 0
numeros_lista = 0
pos_maior = 0
pos_menor = 0

for n in range(7):
    menor = numeros_lista #não é aqui que fica
    numeros_lista = int(input("digite um numero: "))
    if maior < numeros_lista:
        maior = numeros_lista
        pos_maior = n
    elif menor > numeros_lista:
        menor = numeros_lista
        pos_menor = n
    lista.append(numeros_lista)

print("o maior valor é", maior)
print("o menor valor é", menor)
print("a posição do maior valor é", pos_maior)
print("a posição do menor valor é", pos_menor)

#ainda falta atribuir o n apenas se for a primeira vez que aquele numero aparece