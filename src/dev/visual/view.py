from tkinter import *
from src.dev.visual.table import *


class View:

    def createView(self,infos):
            
        # create root window 
        window = Tk()
        
        window.geometry('500x300+200+200')
        window.title('JProgram - Ordination Work')
        window.resizable(width=0, height=0)
        
        Table().create_table(window, infos)
        
        window.mainloop() 