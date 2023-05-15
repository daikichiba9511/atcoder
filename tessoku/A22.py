N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))
B = list(map(lambda x: int(x) - 1, input().split()))

INF = 10**10


def solve():
    # 更新系では無効な値で初期化しておくのが典型
    # solve2だと差分がでてwaになる
    # この差分がどうしてか例が作れてない。わかってない。
    S = [-INF] * N
    S[0] = 0
    for i in range(N - 1):
        S[A[i]] = max(S[A[i]], S[i] + 100)
        S[B[i]] = max(S[B[i]], S[i] + 150)
        # print(i, S)

    return S


def solve2():
    S = [0] * N
    for i in range(N - 1):
        S[A[i]] = max(S[A[i]], S[i] + 100)
        S[B[i]] = max(S[B[i]], S[i] + 150)
        # print(i, S)

    return S


print(solve())
