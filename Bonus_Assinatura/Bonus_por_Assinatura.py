assinatura = input("Por favor, informe o tipo de sua assinatura: ")
faturamento = float(input("Por favor, informe seu faturamento anual: "))
porcent = 0

if assinatura.upper() == "BASIC":
    porcent = 0.3
elif assinatura.upper() == "SILVER":
    porcent = 0.2
elif assinatura.upper() == "GOLD":
    porcent = 0.1
elif assinatura.upper() == "PLATINUM":
    porcent = 0.05
else:
    print("Tipo de assinatura inexistente")

if porcent != 0:
    bonus = faturamento * porcent
    print(
        "O cliente deve pagar um valor de bônus equivalente a R${:.2f}".format(bonus))
