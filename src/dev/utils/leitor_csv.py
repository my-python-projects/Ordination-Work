import os
import csv
from src.dev.utils.log import *


class Csv:

    def ler_csv(self):

        escrever("Lendo arquivo CSV")

        lista_valores = []

        valores_desordenados = 'arquives\Entrada1.csv'

        with open(valores_desordenados, 'r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv, delimiter=';')
            
            for coluna in leitor:                    
                lista_valores.append(coluna)

        escrever('Finalizado a leitura e agora retornando lista de itens...')
        
        return lista_valores
      