entrada = input('Digite Entrar ou Sair | [E] ou [S] : ')
senha_cad = input('Cadastre sua senha: ') 
senha_dig = input('Senha: ')


if entrada == 'E' and senha_cad == senha_dig:
    print('Vc entrou no sistema e seus dados estão corretos.')

elif entrada == 'E' and senha_cad != senha_dig:
    print('Vc escolheu entrar no sistema mas seus dados estão incorretos.')

else:
    print('Vc saiu do sistema.')