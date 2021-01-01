
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    half = (n - 1) / 2
    count = 0
    found = False
    for i in range(n):
        for j in range(n)[::-1]:
            if i == j or j <= half : continue
            count += 1
            if count == k:
                res = a[i] * a[j]
                found = True
                break
        if found: break
    print(res)
if __name__ == "__main__":
    main()