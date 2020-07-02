from src.dev.ordenacao.ordenacao_insercao import *
from src.dev.ordenacao.ordenacao_bubblesort import *
from src.dev.ordenacao.ordenacao_quicksort import *
from leitor_csv import *


if __name__ == '__main__':
    
    # Ordenacao por insercao
    lista_desordenada = ler_csv()
    ordenacao_insercao(lista_desordenada)

    # Ordenação por Bubble Sort
    lista_desordenada = ler_csv()
    bubbleSort(lista_desordenada)

    lista_desordenada = ler_csv()
    QuickSort(lista_desordenada)    
    

