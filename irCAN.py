from tkinter import Tk
from tkinter.filedialog import askopenfilename

def set_arq():
    # Cria uma janela oculta do Tkinter
    root = Tk()
    root.withdraw()

    # Define as extensões de arquivo permitidas
    tipos_arquivo = [("Arquivos de Texto", "*.txt"), ("Arquivos CSV", "*.csv")]

    # Abre o explorador de arquivos e retorna o caminho do arquivo selecionado
    arquivo = askopenfilename(filetypes=tipos_arquivo)

    # Verifica se o usuário selecionou um arquivo e atribui ele a uma variavel
    if arquivo:
        return arquivo
    else:
        print("Nenhum arquivo selecionado.")

def abre_arquivo():
    #Chama a função de selecionar arquivo e define uma variavel q recebe o arquivo e retorna um arquivo com os dados
    arq_can = set_arq()
    aux_can = open(arq_can)
    return aux_can

#converte hexadecimal para decimal
def hex_to_decimal(hex_num):
    decimal_num = int(hex_num, 16)
    return decimal_num

def format_data(numero):
    if numero == '0' or numero == '00':
        return '0'
    else:
        numero_formatado = str(numero).lstrip('0')
        return numero_formatado

#formata o valor para o padrao, 00 00
def format_value(numero):
    numero_formatado = str(numero).zfill(2)
    return numero_formatado

def slipt_value(valor):
    if len(valor) != 4:
        raise ValueError("O valor deve ter 4 caracteres.")
    parte1 = valor[:2]
    parte2 = valor[2:]
    parte1 = format_data(parte1)
    parte2 = format_data(parte2)
    return parte1, parte2

def pegar_dados(arq, id, idenf):
    
    dados = []
    dadoshex = []
    linhas = arq.readlines()
    idenfs = slipt_value(idenf)
    idenf1 = idenfs[0]
    idenf2 = idenfs[1]
    for linha in linhas:
      if id in linha:
        dados_can = linha.strip().split(',')
        i = 0
        for i in range(2, len(dados_can) - 3):
           if dados_can[i] == idenf1 and idenf2 :
             dado_linha1 = dados_can[i + 2]
             dado_linha2 = dados_can[i + 3]
             dado_linha1 = format_value(dado_linha1)
             dado_linha2 = format_value(dado_linha2)
             dado_linha = dado_linha1 + dado_linha2
             dadosi = hex_to_decimal(dado_linha)
             dadosi = str(dadosi)
             dados.append(dadosi)
             dadoshex.append(dado_linha)
    return dados, dadoshex
