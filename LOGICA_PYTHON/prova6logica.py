# Crie um programa em Python que simule um sistema de login. 
# O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. 
# Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. 
# Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.
# Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes

login_certo= 'user'
senha_certa= '1234'
tentativas=0
for i in range(3):
    print(f'Tentativa {tentativas+1} de 3')
    login=input('Digite o login: ')
    senha = input('Digite a senha: ')    
    if login==login_certo and senha==senha_certa:
        print('Acesso liberado!')
        break
    elif login!=login_certo and senha==senha_certa:
        print('Login errado.')
        tentativas+=1
    elif login==login_certo and senha!=senha_certa:
        print('Senha errada.')
        tentativas+=1
    else:
        print('Login e senha errados.')
        tentativas+=1
else:
    for i in range(3):
        print('Acesso bloqueado!')
