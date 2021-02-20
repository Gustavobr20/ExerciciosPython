# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso

turno = str(
    input("Qual o seu turno?\n [M] - Matutino\n [V] - Vespertino\n [N] - Noturno\n"))

if turno in ("M", "m"):
    print("Bom dia!")

elif turno in ("V", "v"):
    print("Boa tarde!")

elif turno in ("N", "n"):
    print("Boa noite!")

else:
    print("Valor invalido!")
