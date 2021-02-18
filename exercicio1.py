
''' 
1 - Faça um Programa que peça dois números e imprima o maior deles.
'''

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

if valor1 > valor2:
    print("O maior valor é o", valor1)
elif valor2 > valor1:
    print("O maior valor é o", valor2)
else:
    print("Os valores inseridos são os mesmos!")
