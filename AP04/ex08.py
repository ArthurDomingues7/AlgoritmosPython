#Uma estação meteorológica registra a velocidade do vento em diferentes momentos do dia. 
#Como a quantidade de medições não é conhecida antecipadamente, 
#o operador digita as velocidades uma por vez e informa -1 quando deseja encerrar a coleta.
#O valor -1 é apenas um sentinela e não deve participar dos cálculos.
#Ao final, o programa deve apresentar:
#a quantidade de medições registradas;
#a velocidade média;
#a maior velocidade registrada;
#a menor velocidade registrada;
#quantas medições ficaram acima de 60 km/h.
#O programa também deve funcionar caso o operador digite -1 logo na primeira leitura.

#operador digita as velocidades do vento
#a condição de parada é -1


contador = 0
contagem_kms = 0
soma = 0
qtd_medicoes = 0
maior_velocidade = 0
menor_velocidade = 0
acima_60 = 0

while contador == 0:
    vento = int(input("digite a velocidade do vento: "))
    if vento == -1:
        media = soma // qtd_medicoes
        print(f"foram medidas", qtd_medicoes, "velocidades")
        print(f"a velocidade média é: ", media)
        print(f"a maior velocidade foi: ", maior_velocidade)
        print(f"a menor velocidade foi: ", menor_velocidade)
        print(f"as medições acima de 60kh/h foram: ", acima_60)
        contador += 1
    else:
        qtd_medicoes += 1
        if qtd_medicoes == 1:
            menor_velocidade = vento
        soma += vento
    if vento > 60:
        acima_60 += 1 
    if vento > maior_velocidade:
        maior_velocidade = vento
    if vento < menor_velocidade:
        menor_velocidade = vento
    

#falta a media dos ventos e fazer quantas medicoes tiveram