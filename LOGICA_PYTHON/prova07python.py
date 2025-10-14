# Crie uma função chamada lancar_dados que utilizará o módulo random para simular o lançamento de dois dados. 
# Cada dado deve gerar um número aleatório entre 1 e 6. A função deve somar os resultados desses dois lançamentos e retornar o valor total.


import random


def lancar_dados():
    dado= [1,2,3,4,5,6]
    numero1 = random.choice(dado)
    print(f'1º número sorteado: {numero1}')
    numero2 = random.choice(dado)
    print(f'2º número sorteado: {numero2}')
    return numero1+numero2
    

print(lancar_dados())
