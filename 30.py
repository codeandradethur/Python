
velocidade1 = input('Qual a velocidade que o carro passou?: ')
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade=int(velocidade1)
vel_multa_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro <= (LOCAL_1 + RADAR_RANGE) and local_carro >= (LOCAL_1 - RADAR_RANGE)
carro_multado = carro_passou_radar_1 and vel_multa_radar_1  

if vel_multa_radar_1:
    print('O Carro Passou Do Limite De Velocidade.')

if carro_passou_radar_1:
    print('O Carro Passou Pelo radar.')

if carro_multado:
    print('O carro foi multado.')
else:
    print('O carro não foi multado.')

