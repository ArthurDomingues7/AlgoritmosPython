#Leia dois números inteiros positivos A e B, com A < B.

#Percorra todos os números do intervalo de A até B, inclusive, e determine:

#quantos números são múltiplos de 3;
#a soma de todos os múltiplos de 3 encontrados;
#quantos números são pares.
#Ao final, exiba os três resultados.

num_inteiro_1 = int(input("digite o numero inteiro 1: "))
num_inteiro_2 = int(input("digite o numero inteiro 2: "))
soma = 0
pares = 0
multiplos_de3 = 0

for n in range(num_inteiro_1, num_inteiro_2, 1):
    if n % 2 == 0:
        pares += 1
    if n % 3 == 0:
        soma += n
        multiplos_de3 += 1


print(soma)
print(pares)
print(multiplos_de3)