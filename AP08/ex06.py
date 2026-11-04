#Crie um programa em Python que leia as notas de 
#10 alunos e armazene todas as notas em uma lista.

#Depois, calcule a média da turma e exiba:

#a média da turma;
#a quantidade de alunos com nota acima da média;
#uma lista com as notas acima da média.

lista_notas = []

for n in range(10):
    nota = int(input("digite a nota ", n, "do aluno: "))
    lista_notas.append(nota)
    media = nota / 10
    
