valor_bruto = float(input("Por favor, informe o valor do seu pacote: "))
categoria = input("Por favor, informe a categoria dos assentos (Econômica, Executiva ou Primeira Classe): ")
quantidade_viajantes = int(input("Por favor, quantos viajantes estão inclusos no pacote: "))

if categoria.upper() == "ECONÔMICA":
    if quantidade_viajantes == 1:
        desconto = 0
    elif quantidade_viajantes == 2:
        desconto = 0.03
    elif quantidade_viajantes == 3:
        desconto = 0.04
    else:
        desconto = 0.05

if categoria.upper() == "EXECUTIVA":
    if quantidade_viajantes == 1:
        desconto = 0
    elif quantidade_viajantes == 2:
        desconto = 0.05
    elif quantidade_viajantes == 3:
        desconto = 0.07
    else:
        desconto = 0.08

if categoria.upper() == "PRIMEIRA CLASSE":
    if quantidade_viajantes == 1:
        desconto = 0
    elif quantidade_viajantes == 2:
        desconto = 0.1
    elif quantidade_viajantes == 3:
        desconto = 0.15
    else:
        desconto = 0.2

valor_final = valor_bruto * (1 - desconto)
valor_medio = valor_final / quantidade_viajantes

print("Valor bruto do pacote: R${}".format(valor_bruto))
print("O desconto recebido foi de {:.2f} % ".format(desconto * 100))
print("O valor final é R${:.2f}".format(valor_final))
print("Equivalente a um valor médio de R${:.2f} por viajante".format(valor_medio))