# Você está criando um programa para calcular a área de um retângulo. 
# O programa deve solicitar ao usuário que forneça a base e a altura do retângulo. 
# Em seguida, o programa deve calcular a área usando a fórmula: Área=Base×Altura

base = float(input('Digite o tamanho da base em cm: '))
altura = float(input('Digite a altura em cm: '))

area= base*altura

print(f'A área do retangulo de base {base} e altura {altura} é {area:.2f}cm²')
