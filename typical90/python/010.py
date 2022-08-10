
def main():
    N = int(input())
    memo = [[0] * 2 for _ in range(N+1)]
    for i in range(N):
        c, p = tuple(map(int, input().split()))
        # cじゃない方のクラスは前のメモの総和をそのままメモする
        if c == 1:
            memo[i][0] = memo[i-1][0] + p
            memo[i][1] = memo[i-1][1]
        elif c == 2:
            memo[i][0] = memo[i-1][0]
            memo[i][1] = memo[i-1][1] + p

    Q = int(input())
    for _ in range(Q):
        l, r = tuple(map(int, input().split()))
        print(f"{memo[r-1][0] - memo[l-2][0]} {memo[r-1][1] - memo[l-2][1]}")


if __name__ == "__main__":
    main()
