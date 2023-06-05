from tratadados import abre_arquivo 
from tratadados import pegar_dados
from Cria_grafico import cria_grafico
aux_dado = abre_arquivo()

id = input("digite o id do pacote: ")
idenf = input("digite o identificador do pacote(formato: 0000): ")
dados, dadoshex = pegar_dados(aux_dado, id, idenf)
cria_grafico(dados)

