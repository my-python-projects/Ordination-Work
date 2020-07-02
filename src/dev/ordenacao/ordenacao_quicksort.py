
class QuickSort:

    def __init__(self, alist):
        self._comparacoes = 0
        self._movimentacoes = 0
        self.quickSort(alist)
        
        print(
            '\nComparacoes: ', self._comparacoes,
            '\nMovimentacoes: ', self._movimentacoes
        )


    def quickSort(self, alist):
        self.quickSortHelper(alist,0,len(alist)-1, self._comparacoes, self._movimentacoes)


    def quickSortHelper(self, alist,first,last, comparacoes, movimentacoes):

        self._comparacoes += 1
        
        if first<last:

            splitpoint = self.partition(alist,first,last, self._comparacoes, self._movimentacoes)

            self.quickSortHelper(alist, first, splitpoint-1, self._comparacoes, self._movimentacoes)
            self.quickSortHelper(alist, splitpoint+1, last, self._comparacoes, self._movimentacoes)
        



    def partition(self, alist, first, last, comparacoes, movimentacoes):
        pivotvalue = alist[first]

        leftmark = first+1
        rightmark = last

        done = False
        while not done:

            self._comparacoes += 1

            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1
                self._comparacoes += 1

            self._comparacoes += 1

            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark -1
                self._comparacoes += 1

            self._comparacoes += 1
            if rightmark < leftmark:
                done = True
            
            else:
                temp = alist[leftmark]

                alist[leftmark] = alist[rightmark]
                self._movimentacoes += 1

                alist[rightmark] = temp
                self._movimentacoes += 1
        
        temp = alist[first]

        alist[first] = alist[rightmark]
        self._movimentacoes += 1

        alist[rightmark] = temp
        self._movimentacoes += 1

        return rightmark