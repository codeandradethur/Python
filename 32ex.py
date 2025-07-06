numero = input('Digite um numero int: ')


try:
    numero1 = int(numero)
    numero_par = numero1 % 2 == 0

    if numero_par:
        print('O numero é par.')
    else:
        print('O numero é impar.')   
except:
    print('O numero não é inteiro.')


