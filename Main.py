import lal as data
from criaGrafico import cria_grafico
aux_dado = data.abre_arquivo()

id = input("digite o id do pacote: ")
idenf = input("digite o identificador do pacote(formato: 0000): ")
dados, dadoshex = data.pegar_dados(aux_dado, id, idenf)
cria_grafico(dados)

