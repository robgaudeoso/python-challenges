segunda = int(input("Por favor, informe a quantidade de votos que segunda-feira recebeu: "))
terca = int(input("Por favor, informe a quantidade de votos que terça-feira recebeu: "))
quarta = int(input("Por favor, informe a quantidade de votos que quarta-feira recebeu: "))
quinta = int(input("Por favor, informe a quantidade de votos que quinta-feira recebeu: "))
sexta = int(input("Por favor, informe a quantidade de votos que sexta-feira recebeu: "))
i = empate = 0

while i < segunda or i < terca or i < quarta or i < quinta or i < sexta:
    i += 1
if i == segunda:
    print("O dia escolhido foi segunda-feira com {} votos".format(i))
    empate += 1                                                        #Variável para checar empate ao final
if i == terca:
    print("O dia escolhido foi terça-feira com {} votos".format(i))
    empate += 1
if i == quarta:
    print("O dia escolhido foi quarta-feira com {} votos".format(i))
    empate += 1
if i == quinta:
    print("O dia escolhido foi quinta-feira com {} votos".format(i))
    empate += 1
if i == sexta:
    print("O dia escolhido foi sexta-feira com {} votos".format(i))
    empate += 1
if empate > 1:                                                         #Checa possibilidade de empate entre dois dias ou mais
    print("Ocorreu um empate entre os {} dias acima mencionados!".format(empate))
