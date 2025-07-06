nome = input('Digite o seu nome: ')
letra = input('Digite a letra q quer encontrar: ')

if letra not in nome:
    print(f'{letra} nao está em {nome}')
else:   
    print(f'{letra} está em {nome}')

 