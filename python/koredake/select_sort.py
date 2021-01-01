#%%
"""
選択ソート、
N個の要素を含む０ーオリジン配列
"""
def selectionSort(A, N):
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        # 見つけた最小値を未整列末尾要素と交換
        tmp = A[minj]
        A[minj] = A[i]
        A[i] = tmp
    return A


# main
# N = int(input())
# A = list(map(int, input()))
N = 5
A = [1, 3, 7, 6, 2]
ss = selectionSort(A, N)
print(ss)



#%%
"""
バブルソートおよび、選択ソートを用いて
与えられたN枚のカードをそれらの数字順に並び替える
"""


class StableSort(self, array, num):
    
    def __init__(self, array, num):
        self.input_num = int(input())
        t = 0
        while t < self.input_num:
            self.arr = input().split()
            t += 1
         
        self.dict = [{key:value} for key, value in items(self.arr)]
        

    def _bubbleSsort(self.arr1, self.num):
        for i in range(0, self.num):
            for j in range(i+1, self.num):
                if self.arr1[i] < self.arr1[j-1]:
                    tmp = self.arr[j]
                    self.arr1[j] = self.arr1[j-1]
                    self.arr1[j-1] = tmp
        return self.arr1


    def _selectionSort(self.arr, self.num):
        for i in range(i, self.num):
            minj = i
            for j in range(i, self.num):
                if self.arr[j] < self.arr[minj]:
                    minj=j
            tmp = self.arr[minj]
            self.arr[minj] = self.arr[i]
            self.arr[i] = tmp
        return self.arr


    def _print_stable(self.arr, self.num):
        for i in range(0, self.num)
            if i > 0 :
        print(self.arr)
"""
バブルソートと選択ソートの結果を比較
"""    
    def isStable(self, self.arr, self.arr1 self.num):
        for i in range(0, self.num):
            if self.arr1

#%%
#self.input_num = int(input())
"""
todo : 文字と数字を分けたい、あとで安定かどうかをprintする判定に使う
案１：文字と数字で別々に分けてリストで持っておく、けどメモリくいそうだし、遅そうだけどなんとなくできそう
案２：ワンライナーdictにkey;文字、value；数字部分で分けて保存しておきたい

→　タプルの方がいいのではないか
正規表現ならstrの中のintに簡単にアクセスできそう
"""
input_num = 3
t = 0
array = []
while t < input_num:
    arr = ['s1', 'c4', 'd9']
    array.append(arr)
    t += 1
    print('%.1d times' %t)
list_card = [(st, num) for st, num in ]
print(len(dict))
print(dict)
        


#%%
