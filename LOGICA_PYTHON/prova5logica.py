# Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. 
# O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. 
# Utilize um loop 'for' para iterar sobre os alunos e suas notas.
# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, 
# considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

quant_alunos= int(input('Quantos alunos você deseja adicionar? '))
alunos=[]
for i in range(quant_alunos):
    nome=input('Nome do aluno: ')
    nota1=float(input('Digite a 1º nota: '))
    nota2=float(input('Digite a 2º nota: '))
    nota3=float(input('Digite a 3º nota: '))
    media= (nota1+nota2+nota3)/3
    if media>=7:
        situacao= 'Aprovado'
    else:
        situacao= 'Reprovado'
    aluno={
        'nome': nome,
        'notas': [nota1, nota2, nota3],
        'media': media,
        'situacao': situacao        
    }
    alunos.append(aluno)
for aluno in alunos:
    print('------------------------------')
    print(f"Nome: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Situação: {aluno['situacao']}")
    print('------------------------------')
