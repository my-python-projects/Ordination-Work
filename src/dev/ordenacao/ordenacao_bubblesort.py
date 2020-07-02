def bubbleSort(alist):
    
    comparacoes = 0
    movimentacao = 0
    
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            comparacoes += 1

            if alist[i]>alist[i+1]:
                temp = alist[i]
                
                alist[i] = alist[i+1]
                movimentacao += 1

                alist[i+1] = temp
                movimentacao += 1
    
    print(
        '\nComparacoes: ', comparacoes,
        '\nMovimentacoes: ', movimentacao
    )
