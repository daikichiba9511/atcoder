def main():
    N, M= map(int, input().split())
    
    acList = [False] * N
    waList = [0] * N
    waCount = 0

    for _ in range(M):
        p, s = map(str, input().split())
        p = int(p) - 1
        if acList[p]:
            continue
        if s == "WA":
            waList[p] += 1
            continue
        waCount += waList[p]
        acList[p] = True

    print(sum(acList), waCount)

if __name__ == "__main__":
    main()