def main():
    N, X, T = map(int, input().split())
    if N <= X:
        print(T)
    else:
        r = N // X
        if N % X > 0:
            r += 1

        print(r * T)


if __name__ == "__main__":
    main()