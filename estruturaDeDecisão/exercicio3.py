# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input('Digite: F - Feminino ou M - Masculino: '))

if sexo == "F" or sexo == "f":
    print('Você é do sexo feminino!')
elif sexo == "M" or sexo == "m":
    print('Você é do sexo masculino!')
else:
    print('Sexo invalido!')
