# Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input('Digite aqui o 1º número: '))
n2 = float(input('Digite aqui o 2º número: '))
n3 = float(input('Digite aqui o 3º número: '))


if n1 > n2 and n3:
    print("O número", n1, "é o maior!")
elif n2 > n3 and n1:
    print("O número", n2, "é o maior!")
elif n3 > n1 and n2:
    print("O número", n3, "é o maior!")
else:
    print("Todos os números são iguais!")
