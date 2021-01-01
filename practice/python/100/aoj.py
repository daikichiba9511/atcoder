# How many ways ?
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja
# 1からnまでの数の中から重複なしで３つの数を選びそれらの合計がxとなる組み合わせ
# 組み合わせを全探索

from itertools import combinations

def main():
    n, x = map(int, input().split())
    
    # 初期順列
    order = [i for i in range(1, n+1)]
    cnt = 0
    for o in combinations(order, 3): # o : Tuple[int]
        if o[0] + o[1] + o[2] == x:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()