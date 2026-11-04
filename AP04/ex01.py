#Um reservatório automatizado possui um sensor que informa o percentual
#de água armazenado, em uma escala de 0 a 100.

#Escreva um programa que leia o percentual atual do reservatório e apresente sua situação:

#abaixo de 25%: Nível baixo;
#de 25% até 80%: Nível adequado;
#acima de 80%: Nível alto.
#Considere que o valor informado estará entre 0 e 100.


perc_reservatorio = int(input("Digite o percentual do reservatorio: "))

if perc_reservatorio > 0 and perc_reservatorio < 25:
    print("Nivel Baixo", "o percentual no reservatorio é",perc_reservatorio)
if perc_reservatorio >= 25 and perc_reservatorio <= 80:
    print("Nível Adequado", "o percentual no reservatorio é",perc_reservatorio)
if perc_reservatorio > 80:
    print("Nível Alto", "o percentual no reservatorio é",perc_reservatorio)
