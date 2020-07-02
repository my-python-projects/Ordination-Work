from src.dev.ordenacao.ordenacao_insercao import Insert
from src.dev.ordenacao.ordenacao_bubblesort import *
from src.dev.ordenacao.ordenacao_quicksort import *
from src.dev.utils.leitor_csv import *
from src.dev.utils.log import Log


class Principal:

    def start_insert(self):
        # Ordenacao por insercao
        lista_desordenada = Csv().ler_csv("Entrada1.csv")
        Insert().ordenacao_insercao(lista_desordenada)

        lista_desordenada = Csv().ler_csv("Entrada2.csv")
        Insert().ordenacao_insercao(lista_desordenada)


    def start_bubbleSort(self):
        # Ordenação por Bubble Sort
        lista_desordenada = Csv().ler_csv("Entrada1.csv")
        bubbleSort(lista_desordenada)

        # Ordenação por Bubble Sort
        lista_desordenada = Csv().ler_csv("Entrada2.csv")
        bubbleSort(lista_desordenada)


    def start_quickSort(self):
        lista_desordenada = Csv().ler_csv("Entrada1.csv")
        QuickSort(lista_desordenada) 

        lista_desordenada = Csv().ler_csv("Entrada2.csv")
        QuickSort(lista_desordenada)


    def start_ordering(self):
        Log().escrever("Iniciando o processo de ordenação...")

        self.start_insert()
        self.start_bubbleSort()
        self.start_quickSort()

        Log().escrever("Finalizado o processo de ordenação\n")



if __name__ == '__main__':
    Principal().start_ordering()
       
    

