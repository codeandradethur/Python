"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horas = input('Horas: ')
int_horas = int(horas)

bom_dia = int_horas >=0 and int_horas <=11
boa_tarde  = int_horas >= 12 and int_horas <= 17
boa_noite  = int_horas = 18 and int_horas >= 23

if bom_dia:
    print(f'Bom dia, são {int_horas=}')
if boa_tarde:
    print(f'Boa tarde, são {horas=}')
if boa_noite:
    print(f'Boa noite, são {horas=}')