nome_dig = input('Digite seu nome: ')
idade_dig = input('Digite sua idade:')

if nome_dig and idade_dig:
    print(f'Seu nome é {nome_dig}')
    print(f'Seu nome invertido é {nome_dig[::-1]}')

    if ' ' in nome_dig:
        print('Seu nome contem espaços.')
    else:
        print('Seu nome nao contem espaços.')
    print(f'Seu nome contem {len(nome_dig)} letras.')
    print(f'A primeira letra do seu nome é {nome_dig[0]}')
    print(f'A ultima letra do seu nome é {nome_dig[-1]}')

else:
    print("Desculpa, voce deixou campos vazios. ")




#if nome_dig == ' ':
    #print('Seu nome contém espaços')
#else:
    #print('Seu nome não contem espaços')


