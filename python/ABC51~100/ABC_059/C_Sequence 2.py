



def main()->None:
    # 回答見た
    n = int(input())
    a = list(map(int, input().split()))
    range_N = range(n)
    acounter = 0
    bcounter = 0
    num = 0
    for i in range_N:
        num += a[i]
        if i % 2 == 0:
            if num <= 0:
                acounter += abs(num) + 1
                num = 1
    
        else:
            if num >= 0:
                acounter += num + 1
                num = -1


    num = 0
    for i in range_N:
        num += a[i]
        if i % 2 != 0:
            if num <= 0:
                bcounter += abs(num) + 1

        else:
            if num >= 0:
                bcounter += num + 1
                num = -1

    print(min(acounter, bcounter))


if __name__ == "__main__":
    main()