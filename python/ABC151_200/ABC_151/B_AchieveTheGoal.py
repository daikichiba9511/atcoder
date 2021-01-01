def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    flag = False
    for i in range(0, K+1):
        mean_score = (sum(A) + i) / N
        if mean_score >= M:
            flag = True
            break
    if flag:print(i)
    else:print(-1)


if __name__ == "__main__":
    main()