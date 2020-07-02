from src.dev.utils.log import Log

class Insert:

    def ordenacao_insercao(self, A):
        n = len(A)
        
        comparacao = 0
        movimentacao = 0
        
        # Percorre o arranjo A.
        for j in range(1, n):
            chave = A[j]
            i = j - 1
        
            comparacao += 1
            
            # Insere o elemento A[j] na posição correta.
            while i >= 0 and A[i] > chave:
                A[i + 1] = A[i]
                i = i - 1
                movimentacao += 1
                comparacao += 1
                

            A[i + 1] = chave
            movimentacao += 1

        texto = '''Resultados da Inserção: 
            \n\t\tComparacoes: {} 
            \n\t\tMovimentacoes: {}
        '''.format(comparacao, movimentacao)

        Log().escrever(texto)
