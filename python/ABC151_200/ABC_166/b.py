def main():
    n, k = map(int, input().split())
    cnt = [0]*101
    for _ in range(k):
        d = int(input())
        A_i = list(map(int, input().split()))
        for i in range(1, n+1):
            if i not in A_i:
                cnt[i] += 1
    res = 0
    for j in cnt:
        if j == k:
            res += 1
    print(res)

if __name__ == "__main__":
    main()