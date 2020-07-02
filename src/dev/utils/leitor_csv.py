import os
import csv
from src.dev.utils.log import *


class Csv:

    def ler_csv(self, arquivo):

        Log().escrever("Lendo o arquivo "+ arquivo)

        lista_valores = []

        valores_desordenados = "arquives\\"+arquivo

        with open(valores_desordenados, 'r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv, delimiter=';')
            
            for coluna in leitor:                    
                lista_valores.append(coluna)

        Log().escrever('Finalizado a leitura e agora retornando lista de itens...')
        
        return lista_valores
      