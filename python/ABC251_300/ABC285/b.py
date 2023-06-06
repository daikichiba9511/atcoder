N = int(input())
S = input()


def solve():
    for i in range(1, N):
        for x in range(N - 1):
            if x + i <= N - 1 and S[x] != S[x + i]:
                if x == N - 2:
                    print(x + 1)
                    continue
                continue
            else:
                print(x)
                break


# solve()


def solve1():
    for i in range(1, N):
        for j in range(1, N + 1):
            if i + j > N:
                print(j - 1)
                break
            if S[j - 1] == S[j + i - 1]:
                print(j - 1)
                break


solve1()
