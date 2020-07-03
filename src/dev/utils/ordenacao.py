#---------------------------------------------------
#                   Imports
#---------------------------------------------------
from src.dev.ordenacao.ordenacao_insercao import Insert
from src.dev.ordenacao.ordenacao_bubblesort import *
from src.dev.ordenacao.ordenacao_quicksort import *
from src.dev.utils.leitor_csv import *
from src.dev.utils.log import Log
from src.dev.visual.view import *


class Ordenacao:    
    
    def __init__(self):
        self._movimentacoes_insert = []
        self._comparacoes_insert = []

        self._movimentacoes_bubble = []
        self._comparacoes_bubble = []

        self._movimentacoes_quicksort = []
        self._comparacoes_quicksort = []


    #----------------------------------#
    #   Inserção
    #----------------------------------#

    def start_insert(self):
        
        lista_desordenada = Csv().ler_csv("Entrada1.csv")
        self.save_information_insert(lista_desordenada)
        

        lista_desordenada = Csv().ler_csv("Entrada2.csv")
        self.save_information_insert(lista_desordenada)


    def save_information_insert(self, lista_desordenada):
        insercao = Insert()
        insercao.ordenacao_insercao(lista_desordenada)

        self._movimentacoes_insert.append(insercao.get_movimentacoes())
        self._comparacoes_insert.append(insercao.get_comparacoes())

    #--------------------------------------#
    #   Bubble Sort
    #--------------------------------------#
    def start_bubbleSort(self):
    
        lista_desordenada = Csv().ler_csv("Entrada1.csv")
        self.save_information_bubblesort(lista_desordenada)
             
        lista_desordenada = Csv().ler_csv("Entrada2.csv")
        self.save_information_bubblesort(lista_desordenada)


    def save_information_bubblesort(self, lista_desordenada):
        
        order = BubbleSort()
        order.bubbleSort(lista_desordenada)
        self._movimentacoes_bubble.append(order.get_movimentacoes())
        self._comparacoes_bubble.append(order.get_comparacoes())   

    #---------------------------------#
    #   QuickSort   
    #---------------------------------#
    
    def start_quickSort(self):
        
        lista_desordenada = Csv().ler_csv("Entrada1.csv")
        self.save_information_quicksort(lista_desordenada)

        lista_desordenada = Csv().ler_csv("Entrada2.csv")
        self.save_information_quicksort(lista_desordenada)
        

    def save_information_quicksort(self, lista_desordenada):
        
        order = QuickSort(lista_desordenada)
        self._movimentacoes_quicksort.append(order.get_movimentacoes())
        self._comparacoes_quicksort.append(order.get_comparacoes())


    #---------------------------------------------------------------------------#
    #   Informações de movimentacoes e comparações dos algoritmos de ordenação
    #---------------------------------------------------------------------------#

    def get_data(self):
        
        data = [
            ['Inserção', 'Comparações', self._comparacoes_insert[0], self._comparacoes_insert[1]],
            ['Inserção', 'Movimentações', self._movimentacoes_insert[0], self._movimentacoes_insert[1]],
            
            ['BubbleSort', 'Comparações', self._comparacoes_bubble[0], self._comparacoes_bubble[1]],
            ['BubbleSort', 'Movimentações', self._movimentacoes_bubble[0], self._movimentacoes_bubble[1]],
            
            ['QuickSort', 'Comparações', self._comparacoes_quicksort[0], self._comparacoes_quicksort[1]],
            ['QuickSort', 'Movimentações', self._movimentacoes_quicksort[0], self._movimentacoes_quicksort[1]]
        ]

        return data
