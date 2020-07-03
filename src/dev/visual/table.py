from tkinter import *
from tkinter import ttk
from src.dev.utils.log import Log


class Table:

    def create_table(self, root, data):
        Log().escrever("Criando a Tabela com o GUI TKinter")

        frame = Frame(root)
        frame.pack()

        tree = ttk.Treeview(frame, columns = (1,2,3,4), height = 5, show = "headings")
        tree.pack(side = 'left')

        tree.heading(1, text="Algoritmo")

        tree.heading(2, text="Tipo")
        tree.heading(3, text="Entrada 1")
        tree.heading(4, text="Entrada 2")

        tree.column(1, width = 100)
        tree.column(2, width = 100)
        tree.column(3, width = 100)
        tree.column(4, width = 100)

        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side = 'right', fill = 'y')

        tree.configure(yscrollcommand=scroll.set)

        for val in data:
            tree.insert('', 'end', values = (val[0], val[1], val[2], val[3]) )
