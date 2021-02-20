''' As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 incluindo : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento. '''

salario = float(input('Digite aqui o seu salário: '))


print("Salário antes do reajuste:", salario)

if salario <= 280:
    print("O percentual de reajuste é 20%")
    reajuste = salario * 0.20
    novo_salario = salario + reajuste

elif salario >= 280 and salario <= 700:
    print("O percentual de reajuste é 15%")
    reajuste = salario * 0.15
    novo_salario = salario + reajuste

elif salario >= 700 and salario <= 1500:
    print("O percentual de reajuste é 10%")
    reajuste = salario * 0.10
    novo_salario = salario + reajuste

else:
    print("O percentual de reajuste é 5%")
    reajuste = salario * 0.05
    novo_salario = salario + reajuste

print("O valor do aumento é: R$", reajuste)
print("Salário após aumento: R$", novo_salario)
