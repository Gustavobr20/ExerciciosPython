''' Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220. '''

valor_hora = float(input('Digite aqui o valor da sua hora: '))
qnt_hora = float(
    input('Digite aqui a quantidade de horas trabalhados no mês: '))

salario_bruto = valor_hora * qnt_hora
desc_sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11

print("Salário bruto: (", valor_hora, " * ",
      qnt_hora, ") : R$", salario_bruto)

if salario_bruto > 900 and salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
    novo_salario = ((salario_bruto - desconto_ir) - desc_sindicato) + fgts

    print("(-) IR 5%: ", desconto_ir)
    print("(-) Sindicato 3%: ", desc_sindicato)
    print("(+) FGTS 11%: ", fgts)
    print("Total de descontos: ", desc_sindicato + desconto_ir)
    print("Salário Líquido: ", novo_salario)


elif salario_bruto > 1500 and salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.10
    novo_salario = ((salario_bruto - desconto_ir) - desc_sindicato) + fgts

    print("(-) IR 10%: ", desconto_ir)
    print("(-) Sindicato 3%: ", desc_sindicato)
    print("(+) FGTS 11%: ", fgts)
    print("Total de descontos: ", desc_sindicato + desconto_ir)
    print("Salário Líquido: ", novo_salario)


else:
    desconto_ir = salario_bruto * 0.20
    novo_salario = ((salario_bruto - desconto_ir) - desc_sindicato) + fgts

    print("(-) IR 20%: ", desconto_ir)
    print("(-) Sindicato 3%: ", desc_sindicato)
    print("(+) FGTS 11%: ", fgts)
    print("Total de descontos: ", desc_sindicato + desconto_ir)
    print("Salário Líquido: ", novo_salario)
