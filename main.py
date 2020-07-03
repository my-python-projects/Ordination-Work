#---------------------------------------------------
#                   Imports
#---------------------------------------------------
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
        self.start_ordering()
    
    def start_ordering(self):
        Log().escrever("Iniciando o processo de ordenação...")

        self.start_order.start_insert()
        self.start_order.start_bubbleSort()
        self.start_order.start_quickSort()

        Log().escrever("Finalizado o processo de ordenação\n")

        self.start_gui()


    def start_gui(self):
        View().createView(self.start_order.get_data())


if __name__ == '__main__':
    Principal()

    
