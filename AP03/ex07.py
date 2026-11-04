#Leia duas notas e o percentual de frequência. Calcule a média aritmética.
#Aprovado: média ≥ 60 e frequência ≥ 75%;
#Reprovado por frequência: frequência < 75%;
#Reprovado por nota: frequência suficiente, mas média < 60.
#Apresente a média e a situação final.

nota1 = int(input("digitar nota 1: "))
nota2 = int(input("digitar nota 2: "))
frequencia = int(input("digitar frquencia em %: "))
nota_final = (nota2 + nota1) // 2

if nota_final >= 60 and frequencia >= 75:
    print("Aprovado")
if nota_final >= 60 and frequencia < 74:
    print("reprovado por freq")
if frequencia >= 75 and nota <60:
    print("reprovado por nota")
print(f"sua nota foi: ", nota_final, "sua frequencia foi:", frequencia)

