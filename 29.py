#NO TRY QUALQUER ERRO QUE DER ELE AUTOMATICAMENTE IRA PARA O EXCEPT.

numero = input('Digite um numero: ')
quantidade_dobrar = input('Digite o numero no qual vc quer dobrar: ')

try:
    numero_float = float(numero)
    quantidade_dobra = float(quantidade_dobrar)
    print(f'O seu numero {numero} dobrado é: {numero_float * quantidade_dobra:.1f}')

except:
    print('O conteudo digitado não é um numero')
