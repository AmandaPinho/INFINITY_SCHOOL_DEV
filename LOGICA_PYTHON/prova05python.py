# Crie uma função chamada maior_numero que receberá três números como argumentos. 
# Esta função deve comparar os três números e identificar qual deles é o maior. 
# Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois. 
# A função deve então retornar o maior número encontrado.

def maior_numero(a, b, c):
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior

print(maior_numero(3, 9, 8))
