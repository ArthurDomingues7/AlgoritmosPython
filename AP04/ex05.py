#Um serviço web realiza periodicamente testes de tempo de resposta. 
# Durante uma rodada de monitoramento, serão registradas exatamente 8 medições, em milissegundos.

#Escreva um programa que leia as 8 medições e, ao final, apresente:

#o tempo médio das medições;
#quantas medições ficaram acima de 200 ms;
#o maior tempo de resposta registrado.
#Considere que todos os tempos informados serão valores positivos.

medicao = 0
contador = 0

while contador <= 8:
    medicao == int(input("Digite a medição nº", contador))
    contador += 1 
    if contador == 8:
        media = medicao // 8
print("o tempo médio das medições é:", media)