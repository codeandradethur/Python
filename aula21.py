entrada = input('Digite Entrar ou Sair | [E] ou [S] : ')
senha_dig = input('Senha: ')

senha_perm = '12345'

if entrada == 'E' and senha_dig == senha_perm:
    print('Vc entrou no sistema e seus dados estão corretos.')

elif entrada == 'E' and senha_dig != senha_perm:
    print('Vc escolheu entrar no sistema mas seus dados estão incorretos.')

else:
    print('Vc saiu do sistema.')