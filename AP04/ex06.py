#O sensor do reservatório utilizado no Exercício 1 pode apresentar leituras inválidas por falha momentânea. 
# Uma leitura válida deve estar entre 0 e 100.

#Escreva um programa que solicite o percentual do reservatório e continue pedindo um novo valor 
# enquanto a leitura estiver fora do intervalo válido.

#Quando uma leitura válida for finalmente informada, o programa deve classificá-la como:

#abaixo de 25%: Nível baixo;
#de 25% até 80%: Nível adequado;
#acima de 80%: Nível alto.

perc_acumulado = 0
contador = 0

while contador == 0:
    perc_reservatorio = int(input("Digite o percentual do reservatorio: "))
    if perc_reservatorio > 100 or perc_acumulado > 100:
            print("Inválido")
            contador = contador + 1
    if perc_reservatorio <= 100:
        perc_acumulado += perc_reservatorio
        if perc_acumulado < 25:
            print("nivel baixo")
        if perc_acumulado >= 25 and perc_reservatorio <= 80:
            print("nivel adequado")
        if perc_acumulado > 80:
            print("nivel alto")
        if perc_acumulado == 100:
            contador = contador + 1
