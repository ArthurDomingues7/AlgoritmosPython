#Crie uma função chamada gerar_resumo_correcao(nota) que receba uma nota e retorne dois valores:

#a classificação de desempenho;
#a situação final do aluno.
#Importante: para resolver este exercício, utilize as funções criadas nos exercícios 7 e 8 dentro da nova função.

#No programa principal:

#leia uma nota;
#chame a função;
#exiba os dois valores retornados.

def classificar_desempenho(nota):
    if nota >= 90 and nota <= 100:
        print("Excelente")
    if nota >= 70 and nota <= 89:
        print("Bom")
    if nota >= 60 and nota <= 69:
        print("Regular")
    if nota < 60:
        print("Insuficiente")

def calcular_situacao(nota):
    if nota >= 70:
        print("aprovado")
    elif nota >= 50 and nota <= 69:
        print("recuperação")
    else:
        print("reprovado")
    return classificar_desempenho

def gerar_resumo_correcao(nota):
    calcular_situacao(nota)
    classificar_desempenho(nota)

nota = int(input("digite aqui sua nota: "))
gerar_resumo_correcao(nota)