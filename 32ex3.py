'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
'''

nome = input('Digite seu nome: ')

tamanho_nome = len(nome)

nome_pequeno = tamanho_nome <= 4
nome_medio = tamanho_nome >=5 and tamanho_nome <=6
nome_grande = tamanho_nome >6

if nome_pequeno:
    print('O seu nome é curto')

if nome_medio:
    print('Seu nome é normal')

if nome_grande:
    print('Seu nome é muito grande')