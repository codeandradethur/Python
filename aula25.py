'''
Interpolação strings

s - strings
d e i - int
f - float
x e X hexadecimal
'''



nome = 'Arthur'
preco = 12000.10000
preco_metade = preco / 2

juntartudo = '%s o preço total é de R$%.2f, e o preço dividido é de %.2f' % (nome, preco, preco_metade)



print (juntartudo)

print ('o hexadecimal de %d, é %X' % (200,200)) 