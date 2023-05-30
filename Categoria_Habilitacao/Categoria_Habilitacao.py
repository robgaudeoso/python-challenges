#importando o módulo que lida com as habilitacoes
import habilitacoes
#pedindo que o usuário a categoria
categoria_digitada = input("Digite a categoria de habilitação")
#utilizando o método validar_categoria para verificar se o que foi digitado é válido
habilitacoes.validar_categoria(categoria_digitada)