from src.dev.utils.log import Log

class Insert:

    def __init__(self):
        self._comparacao = 0
        self._movimentacao = 0

    def ordenacao_insercao(self, A):
        n = len(A)
        
        # Percorre o arranjo A.
        for j in range(1, n):
            chave = A[j]
            i = j - 1
        
            self._comparacao += 1
            
            # Insere o elemento A[j] na posição correta.
            while i >= 0 and A[i] > chave:
                A[i + 1] = A[i]
                i = i - 1
                self._movimentacao += 1
                self._comparacao += 1
                

            A[i + 1] = chave
            self._movimentacao += 1

        texto = '''Resultados da Inserção: 
            \n\t\tComparacoes: {} 
            \n\t\tMovimentacoes: {}
        '''.format(self._comparacao, self._movimentacao)

        Log().escrever(texto)

    def get_comparacoes(self):
        return self._comparacao

    def get_movimentacoes(self):
        return self._movimentacao    
