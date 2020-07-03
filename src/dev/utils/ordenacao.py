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


    def start_insert(self):
        # Ordenacao por insercao
        lista_desordenada = Csv().ler_csv("Entrada1.csv")
        
        insercao = Insert()
        insercao.ordenacao_insercao(lista_desordenada)

        self._movimentacoes_insert.append(insercao.get_movimentacoes())
        self._comparacoes_insert.append(insercao.get_comparacoes())

        lista_desordenada = Csv().ler_csv("Entrada2.csv")
        insercao = Insert()
        insercao.ordenacao_insercao(lista_desordenada)

        self._movimentacoes_insert.append(insercao.get_movimentacoes())
        self._comparacoes_insert.append(insercao.get_comparacoes())


    def start_bubbleSort(self):
        # Ordenação por Bubble Sort
        lista_desordenada = Csv().ler_csv("Entrada1.csv")
        order = BubbleSort()
        
        order.bubbleSort(lista_desordenada)

        self._movimentacoes_bubble.append(order.get_movimentacoes())
        self._comparacoes_bubble.append(order.get_comparacoes())        

        # Ordenação por Bubble Sort
        lista_desordenada = Csv().ler_csv("Entrada2.csv")
        order = BubbleSort()
        
        order.bubbleSort(lista_desordenada)

        self._movimentacoes_bubble.append(order.get_movimentacoes())
        self._comparacoes_bubble.append(order.get_comparacoes())


    def start_quickSort(self):
        lista_desordenada = Csv().ler_csv("Entrada1.csv")
        order = QuickSort(lista_desordenada)

        self._movimentacoes_quicksort.append(order.get_movimentacoes())
        self._comparacoes_quicksort.append(order.get_comparacoes())

        lista_desordenada = Csv().ler_csv("Entrada2.csv")
        order = QuickSort(lista_desordenada)

        self._movimentacoes_quicksort.append(order.get_movimentacoes())
        self._comparacoes_quicksort.append(order.get_comparacoes())

    
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


    def get_comparacoes(self):
        return self._comparacoes_quicksort

    def get_comparacoes_insercao(self):
        return self._comparacoes_insert

    def get_comparacoes_bubblesort(self):
        return self._comparacoes_bubble
    

    def get_movimentacoes(self):
        return self._movimentacoes_quicksort

    def get_movimentacoes_insercao(self):
        return self._movimentacoes_insert        

    def get_movimentacoes_bubblesort(self):
        return self._movimentacoes_bubble