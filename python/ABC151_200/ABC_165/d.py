def floor(t):
    return int(t)

def g(x, a, b):
    return floor( (a * x ) / b ) - a * floor( x / b)

def main():
    a, b, n = map(int, input().split())

    res = 0
    if a >= b :
        for i in range(10*6):
            if i <= n:
                tmp = g(i, a, b)
                if tmp > res:
                    res = tmp
            else: break
    else:
        for i in range(10**6, 10**12):
            if i <= n:
                tmp = g(i, a, b)
                if tmp > res:
                    res = tmp
            else: break
    print(res)

if __name__ == "__main__":
    main()