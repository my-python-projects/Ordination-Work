from src.dev.ordenacao.ordenacao_insercao import Insert
from src.dev.ordenacao.ordenacao_bubblesort import *
from src.dev.ordenacao.ordenacao_quicksort import *
from src.dev.utils.leitor_csv import *


class Principal:

    def start_ordering(self):
        # Ordenacao por insercao
        lista_desordenada = Csv().ler_csv()
        Insert().ordenacao_insercao(lista_desordenada)

        # Ordenação por Bubble Sort
        lista_desordenada = Csv().ler_csv()
        bubbleSort(lista_desordenada)

        lista_desordenada = Csv().ler_csv()
        QuickSort(lista_desordenada) 


if __name__ == '__main__':
    Principal().start_ordering()
       
    

