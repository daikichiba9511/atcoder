def main():
    n, d = map(int, input().split())
    per = 2 * d + 1
    res = n // per
    if n % per != 0:
        print(res + 1 )
    else:
        print(res)
if __name__ == '__main__':
    main()