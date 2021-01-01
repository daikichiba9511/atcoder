# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
from itertools import combinations

# 000から９９９まで決め打ちで全探索。計算量はO(1000*N)程度
def solution1():
    # 入力
    n = int(input())
    s = [int(i) for i in input()]
    cnt = 0
    for c in range(1000):
        # 100の桁、１０の桁、１の桁に分解
        candidate = [c//100, (c//10)%10, c%10]
        f = -1
        for j in range(n):
            if s[j] == candidate[f]:
                f += 1
            if f == 2:
                break
        if f == 2:
            cnt += 1
    print(cnt)



def solution2():

    seen = [[[False]*30009 for _ in range(4)] for _ in range(1009)]

    n : int = int(input())
    s : str = input()

    seen[0][0][0] = True

    # 探索開始
    for i in range(n):
        for j in range(4):
            for k in range(1000):
                if seen[i][j][k] == False:
                    continue

                seen[i+1][j][k] = True
                if j <= 2:
                    seen[i + 1][j + 1][k * 10 + int(s[i])] = True

    cnt = 0
    for i in range(1000):
        if seen[n][3][i] == True:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    solution1()
    solution2()