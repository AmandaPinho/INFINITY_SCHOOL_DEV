# Você está criando um programa em Python para simular um jogo simples de adivinhação. 
# O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar. 
# O jogador terá até 3 tentativas para acertar o número.
# Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas até acertar ou atingir o limite de tentativas. 
# Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.

numero = 5
print('Você tem 3 tentativas para adivinhar o número!')
while True:
    tentativas = 0

    while tentativas < 3:
        palpite = int(input('Dê seu palpite de 0 a 10: '))
        tentativas += 1

        if palpite == numero:
            print('Parabéns! Você acertou!')
            break
        elif palpite > numero:
            print('Errou! Tente um número menor.')
        else:
            print('Errou! Tente um número maior.')
            
    else:
        print('Que pena! Você não conseguiu acertar em 3 tentativas.')

    continuar = input('Deseja continuar (s/n)? ').lower()
    if continuar == "n":
        print('Fim do programa.')
        break
