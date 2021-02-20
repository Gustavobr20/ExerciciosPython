# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))


if n1 > n2 and n3:
    if n2 < n3:
        print("O menor número é o", n2)
    else:
        print("O menor número é o", n3)
    print("O maior número é o", n1)
elif n2 > n3 and n1:
    if n3 < n1:
        print("O menor número é o", n3)
    else:
        print("O menor número é o", n1)
    print("O maior número é o", n2)
elif n3 > n1 and n2:
    if n1 < n2:
        print("O menor número é o", n1)
    else:
        print("O menor número é o", n2)
    print("O maior número é o", n3)
else:
    print("Todos os números são iguais!")
