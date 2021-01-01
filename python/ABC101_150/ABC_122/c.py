import abc


import sys
def main():
    def input(): return sys.stdin.readline()[:-1]

    N, Q = map(int, input().split())
    S = input()

    # 累積和
    str_list = [0] * (N + 1)
    for i in range(N):
        if (i + 1 < N) and S[i] == "A" and S[i + 1] == "C":
            str_list[i + 1] = str_list[i] + 1
        else:
            str_list[i + 1] = str_list[i]

    # クエリ処理
    for q in range(Q):
        l, r = map(int, input().split())
        l -= 1; r -= 1
        print(str_list[r] - str_list[l])

if __name__ == '__main__':
    main()