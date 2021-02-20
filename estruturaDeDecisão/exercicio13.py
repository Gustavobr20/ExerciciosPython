# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

num_dia = str(input(
    'Escolha um dia da semana de [1 a 7]:\n ----------------------------\n Digite aqui: '))


if num_dia == "1":
    print('1-Domingo')

elif num_dia == "2":
    print('2 - Segunda')

elif num_dia == "3":
    print('3 - Terça')

elif num_dia == "4":
    print('4 - Quarta')

elif num_dia == "5":
    print('5 - Quinta')

elif num_dia == "6":
    print('6 - Sexta')

elif num_dia == "7":
    print('7 - Sabado')

else:
    print("Valor Invalido")
