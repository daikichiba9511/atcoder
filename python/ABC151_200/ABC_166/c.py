
def main1():
    # O(10 ^ 10)
    n, m = map(int, input().split())
    H = list(map(int, input().split()))
    p = [tuple(map(int, input().split())) for _ in range(m)]
    cnt = 0
    for i, h in enumerate(H):
        flag = True
        for a, b in p:
            if a != i and b != i:continue
            elif a == i:
                if h < H[b-1]:
                    flag = False
                    break
            elif b == i:
                if h < H[a-1]:
                    flag = False
                    break
        if flag:
            cnt += 1
    print(cnt)

def main2():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))

    ma = [0]*100010
    for i in range(m):
        a, b = map(int, input().split())
        ma[a] = max(ma[a-1], h[b-1])
        ma[b] = max(ma[b-1], h[a-1])

    ans = 0
    for i in range(n):
        if h[i] > ma[i]:
            ans += 1

    print(ans)

if __name__ == "__main__":
    # main()
    main2()