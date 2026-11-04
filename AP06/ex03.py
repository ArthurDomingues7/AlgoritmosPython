#Leia um número binário como string, contendo apenas os caracteres 0 e 1.

#Converta esse número para decimal sem utilizar funções prontas de conversão de base.

#O programa deve percorrer a string por índice e construir o valor decimal progressivamente.

#Dica: ao ler um novo dígito binário da esquerda para a direita, o valor acumulado pode ser 
# atualizado por decimal = decimal * 2 + digito.
#Exemplo: 1101 deve resultar em 13.

bin = int(input("digite um numero binário (0 e 1): "))

if bin == 0 or bin == 1:
    