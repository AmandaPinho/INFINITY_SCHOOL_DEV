# Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. 
# O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).
# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' 
# para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.

numero_inicial = int(input('Informe o primeiro número: '))
numero_final = int(input('Informe o último número: '))

soma_pares = 0

for i in range(numero_inicial, numero_final + 1):
    if i % 2 == 0:
        soma_pares += i

if soma_pares == 0:
    print('Não existem números pares no intervalo.')
else:
    print(f'A soma dos números pares é {soma_pares}')
