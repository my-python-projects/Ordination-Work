from src.dev.ordenacao.ordenacao_insercao import Insert
from src.dev.ordenacao.ordenacao_bubblesort import *
from src.dev.ordenacao.ordenacao_quicksort import *
from src.dev.utils.leitor_csv import *
from src.dev.utils.log import Log
from src.dev.visual.view import *
from src.dev.utils.ordenacao import *

class Principal:

    def __init__(self):
        self.start_order = Ordenacao()
    
    def start_ordering(self):
        Log().escrever("Iniciando o processo de ordenação...")

        self.start_order.start_insert()
        self.start_order.start_bubbleSort()
        self.start_order.start_quickSort()

        Log().escrever("Finalizado o processo de ordenação\n")


if __name__ == '__main__':
    
    initi = Principal()
    initi.start_ordering()

    data = [
        
        ['Inserção', 'Comparações', initi.start_order.get_comparacoes_insercao()[0], initi.start_order.get_comparacoes_insercao()[1]],
        ['Inserção', 'Movimentações', initi.start_order.get_movimentacoes_insercao()[0], initi.start_order.get_movimentacoes_insercao()[1]],
        ['BubbleSort', 'Comparações', initi.start_order.get_comparacoes_bubblesort()[0], initi.start_order.get_comparacoes_bubblesort()[1]],
        ['BubbleSort', 'Movimentações', initi.start_order.get_movimentacoes_bubblesort()[0], initi.start_order.get_movimentacoes_bubblesort()[1]],
        ['QuickSort', 'Comparações', initi.start_order.get_comparacoes()[0], initi.start_order.get_comparacoes()[1]],
        ['QuickSort', 'Movimentações', initi.start_order.get_movimentacoes()[0], initi.start_order.get_movimentacoes()[1]]
    ]

    View().createView(data)

       
    

