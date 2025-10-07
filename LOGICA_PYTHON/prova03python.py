# Crie um dicionário para armazenar o nome e o preço de cinco produtos. 
# Peça ao usuário para inserir o nome de cada produto e o respectivo preço. 
# À medida que o usuário fornece os dados, armazene cada produto como uma chave 
# no dicionário e o preço como o valor associado a essa chave. Após a inserção 
# de todos os produtos e preços, calcule o valor total da compra somando todos 
# os preços armazenados no dicionário. Por fim, exiba o valor total da compra.

compras = {}
total_compras=0

for i in range(5):
    produto = input('Nome do produto: ')
    valor = float(input('Valor do produto: '))
    compras[produto] = valor

for valor in compras.values():
    total_compras += valor

print(total_compras)
