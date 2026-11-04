#Crie uma função chamada intercalar(lista1, lista2) que receba duas listas 
# de tamanhos possivelmente diferentes e produza uma terceira lista intercalando seus elementos.
# Por exemplo:
# lista1=[1,2,3,4]
# lista2=[10,20]
# deveproduzir:
# [1, 10,2,20,3,4]
# Quando umadas listas terminar,os elementos restantes da outra devem ser 
# acrescentados ao final do resultado.
lista1=[1,2,3,4]
lista2=[10,20]

def intercalar(lista1, lista2):
    lista3 = []
    i = 0
    while i < len(lista1) or i < len(lista2):
        if i < len(lista1):
            lista3.append(lista1[i])
        if i < len(lista2):
            lista3.append(lista2[i])
        i += 1

    return lista3

resultado = intercalar(lista1, lista2)
print(resultado)
    
