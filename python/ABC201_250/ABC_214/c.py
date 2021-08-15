def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    INF = 1 << 28
    res = [INF] * N
    res[0] = min(T)
    for i in range(1, N):
        res[i] = min(T[i], res[i - 1] + S[i - 1])
    for ans in res:
        print(ans)


def sol1():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    """ T_{i} が良いか、T_{i} + S_{i}が良いか

    2N 回回さないと行けないのがわからなかった。
    """
    for i in range(2 * N):
        T[(i + 1) % N] = min(T[(i + 1) % N], T[i % N] + S[i % N])

    for ans in T:
        print(ans)


if __name__ == "__main__":
    main()
