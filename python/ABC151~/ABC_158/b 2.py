
def main():
    n, a, b = map(int, input().split())
    res = n
    count = 0
    if a == 0:
        print(0)
        exit(0)
    count = res // (a + b)
    res = n - ( ( a + b ) * count )
    if a < res:
        print(a * (count + 1))
    else:
        print(a * count + res)
    


if __name__ == "__main__":
    main()