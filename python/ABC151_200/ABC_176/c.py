# maをi-1番目までにでてる最大値としてi番目との差分を足していく

def main():
    # INF = 10 ** 9
    N = int(input())
    A = list(map(int, input().split()))

    # initialize
    ma = A[0]

    res = 0
    for i in range(1, N):
        if A[i] <= ma:
            res += ma - A[i]
        else:
            ma = A[i]
    print(res)

if __name__ == "__main__":
    main()