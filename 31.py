# v1 = 'A'
# v2 = 'B'

# print(id(v1))
# print(id(v2))


condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo.')

else:
    print('Nao faça algo.')

if passou_no_if is None:
    print('Nao passou no if')
if passou_no_if is not None:
    print('Passou no if. ')