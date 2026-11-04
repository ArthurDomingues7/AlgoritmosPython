#Um sistema recebeu um código numérico inteiro positivo e 
#precisa analisar os algarismos que compõem esse código,
#sem convertê-lo para texto.

#Escreva um programa que leia o código e determine:

#quantos algarismos ele possui;
#a soma de todos os algarismos;
#quantos algarismos são pares;
#qual é o maior algarismo presente no código.
#Utilize os operadores % e // para obter e remover, a cada repetição, o último algarismo do número.

#Por exemplo, para o código 58324, a soma dos algarismos é 22 e o maior algarismo é 8.

codigo = int(input("Digite o código numérico: "))                 
soma = 0
pares = 0
maior = 0
contador = 0

while contador == 0:
    numero_in = codigo % 10
    if maior < numero_in:
        maior = numero_in
    if numero_in % 2 == 0:
        pares = pares + 1
    soma = soma + numero_in
    codigo = codigo // 10
    if codigo < 1:
        contador = contador + 1
print(soma)
print(pares)
print(maior)
    #se o proximo numero for maior, o antigo é substituido, se nao, o antigo continua
    #além disso, preciso somar o antigo com o novo e guardar esse 
    #também preciso saber se o numero é par, ou seja, divisivel por 2 com resto 0.