#Crie um programa em Python que leia 10 números inteiros e armazene todos eles em uma lista.

#Depois, percorra a lista e exiba:

#a quantidade de números pares;
#a quantidade de números ímpares;
#uma lista contendo apenas os pares;
#uma lista contendo apenas os ímpares.

lista = []
lista_pares = []
lista_impares = []
pares = 0
impares = 0

for n in range(10):
    numeros_lista = int(input("digite um numero: "))
    lista.append(numeros_lista)
for n in lista:
    if n % 2 == 0:
        pares += 1
        lista_pares.append(n)
    elif n % 2 == 1:
        impares +=1
        lista_impares.append(n)
print(pares)
print(impares)
print(lista_pares)
print(lista_impares)