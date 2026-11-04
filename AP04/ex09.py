#Um robô autônomo realiza uma missão de inspeção em um túnel. 
#Antes de iniciar, o sistema recebe a quantidade inicial de energia da bateria, em unidades de energia.
contador = 0
qtd_trechos = 0
qtd_consumida = 0
trechos_restantes = 1
qtd_necessaria = 0
qtd_inicial = int(input("qual a quantidade inicial de energia? "))
#Durante a missão, cada trecho do túnel exige uma determinada quantidade de energia. 
#Os custos dos trechos são informados um por vez. O valor 0 indica que não existem
#mais trechos e que a rota foi concluída.
while contador == 0:
    if trechos_restantes == 0:
        print("rota concluida")
        contador +=1
    if qtd_inicial < qtd_necessária:
        print("faltou energia")
        contador +=1
    qtd_necessária = int(input("digite a quantidade de energia necessária para percorrer esse trecho:"))
    if qtd_necessaria == 0:
        trechos_restantes -= 1
    if qtd_necessária >= qtd_inicial:
        qtd_inicial -= qtd_necessaria
        qtd_consumida += qtd_necessaria
        qtd_trechos += 1
print("a quantidade de trechos é", qtd_trechos)
print("o total de energia consumida é", )
print("a quantidade de trechos é", qtd_trechos)
print("a quantidade de energia que restou foi", qtd_inicial)
#Um trecho só pode ser percorrido se a bateria atual possuir energia suficiente 
# para pagar todo o seu custo. Se o custo informado for maior que a energia restante, 
# o robô não percorre esse trecho e a missão é encerrada imediatamente por falta de energia.

#Para cada trecho percorrido, o programa deve descontar seu custo da bateria e 
# manter as informações necessárias para, ao final, apresentar:

#a quantidade de trechos concluídos;
#o total de energia consumida;
#a energia restante na bateria;
#o maior custo entre os trechos efetivamente percorridos;
#quantos trechos terminaram com a bateria em 20% ou menos da energia inicial;
#o motivo do encerramento: Rota concluída ou Energia insuficiente.
#Considere que a energia inicial é positiva e que todos os custos informados são valores inteiros não negativos.

#Exemplo: para energia inicial igual a 100 e custos 20, 35, 30 e 25, o robô percorre os três primeiros trechos. 
# Depois deles, restam 15 unidades de energia, portanto o trecho de custo 25 não pode ser percorrido.

