from src.dev.utils.log import Log

class BubbleSort:

    def __init__(self):
        self._comparacoes = 0
        self._movimentacoes = 0

    def bubbleSort(self, alist):
        
        for passnum in range(len(alist)-1,0,-1):
            for i in range(passnum):
                
                self._comparacoes += 1
                if alist[i]>alist[i+1]:
                    temp = alist[i]
                    
                    alist[i] = alist[i+1]
                    self._movimentacoes += 1

                    alist[i+1] = temp
                    self._movimentacoes += 1
        
        texto = '''Resultados do Bubble Sort: 
            \n\t\tComparacoes: {} 
            \n\t\tMovimentacoes: {}
        '''.format(self._comparacoes, self._movimentacoes)

        Log().escrever(texto)


    def get_comparacoes(self):
        return self._comparacoes

    def get_movimentacoes(self):
        return self._movimentacoes    
