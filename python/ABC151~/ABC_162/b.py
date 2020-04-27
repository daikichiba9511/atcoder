def main():
    N = int(input())
    res = 0
    for i in range(1, N+1):
        if i % 3 != 0 and i % 5 != 0:
            res += i
    print(res)


if __name__ == "__main__":
    main()