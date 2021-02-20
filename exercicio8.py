# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input('Digite aqui o valor do 1º produto: '))
produto2 = float(input('Digite aqui o valor do 2º produto: '))
produto3 = float(input('Digite aqui o valor do 3º produto: '))

if produto1 < produto2 and produto3:
    print("O primeiro produto é o mais barato!")
elif produto2 < produto3 and produto1:
    print("O segundo produto é o mais barato!")
elif produto3 < produto2 and produto1:
    print("O terceiro produto é o mais barato!")
else:
    print("Todos os produtos tem o mesmo valor!")
