#Um professor deseja criar um programa simples para apoiar o fechamento da correção de uma atividade. 
# Em vez de analisar apenas um aluno, ele quer processar as notas de vários estudantes em sequência, 
# reutilizando as mesmas funções para evitar repetir a mesma lógica várias vezes no código.

#Escreva um programa que faça a correção de 3 alunos. Para cada aluno, o programa deve:

#ler o nome do aluno;
#ler a nota obtida;
#verificar se a nota é válida;
#se a nota for válida, calcular a classificação de desempenho;
#calcular também a situação final;
#gerar um resumo da correção;
#exibir as informações daquele aluno.
#Entradas:

#Para cada um dos 3 alunos:

#nome;
#nota.
#Saídas esperadas:

#Para cada aluno, o programa deve mostrar:

#nome;
#nota informada;
#se a nota é válida;
#classificação de desempenho;
#situação final.

def classificar_desempenho(nota):
    if nota >= 90 and nota <= 100:
        return("Excelente")
    if nota >= 70 and nota <= 89:
        return("Bom")
    if nota >= 60 and nota <= 69:
        return("Regular")
    if nota < 60:
        return("Insuficiente")

def calcular_situacao(nota):
    if nota >= 70:
        return("aprovado")
    elif nota >= 50 and nota <= 69:
        return("recuperação")
    else:
        return("reprovado")

def gerar_resumo_correcao(nome, nota):
    print("\n--- Resumo da Correção ---") 
    print("Nome:", nome) 
    print("Nota:", nota) 
    print("Nota válida: Sim") 
    print("Desempenho:", classificar_desempenho(nota)) 
    print("Situação final:", calcular_situacao(nota))

contador = 0

while contador < 3:
    nome = str(input("digite seu nome: "))
    nota = int(input("digite sua nota: "))
    if nota >= 0 and nota <= 100:
        print("Nota Válida")
        contador += 1
        print(nome, nota)
        gerar_resumo_correcao(nome, nota)
    else:
        print("Nota Inválida")
        print("Vamos tentar novamente, digite o nome e uma nota válida!")