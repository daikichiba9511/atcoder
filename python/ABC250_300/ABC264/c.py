import numpy as np
from itertools import combinations

H1, W1 = map(int, input().split())
A = []
for _ in range(H1):
    A.append(list(map(int, input().split())))

H2, W2 = map(int, input().split())
B = []
for _ in range(H2):
    B.append(list(map(int, input().split())))

# 全てのi,jにおいてA_i,j == B_i,j
# 単純に探索するとO(HW)
# 好きなだけ繰り返していい->Bと同じ大きさ
# 場合の数は(H1 (H1 - H2))^T * (W1 (W1 - W2))^T 通り
# O(10^10)
# 行列Aは行列Bを含んでる
A = np.array(A)
B = np.array(B)
found = False
for i in combinations(range(H1), (H1 - H2)):
    for j in combinations(range(W1), (W1 - W2)):
        A_prime = np.delete(np.delete(A, i, axis=0), j, axis=1)
        if (A_prime == B).all():
            found = True
            break


if found:
    print("Yes")
else:
    print("No")
