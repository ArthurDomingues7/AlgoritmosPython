#Um sistema precisa analisar os identificadores numéricos de 1 até um limite informado pelo usuário. 
# Para uma etapa do processamento, interessam apenas os valores divisíveis por 3.

#Escreva um programa que leia um inteiro positivo N e percorra 
#todos os valores de 1 até N. Ao final, apresente:

#a soma de todos os múltiplos de 3 encontrados;
#a quantidade de múltiplos de 3 encontrados.
#Para N = 10, os valores considerados são 3, 6 e 9.

positivo = int(input("Digite o numero inteiro: "))
contador_multiplos = 0
soma = 0
contador = 0

while contador <= positivo:
    if contador % 3 == 0:
        soma += contador
        contador += 1
    else:
        contador +=1
    print(soma)