def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    border = (1 / (4 * M)) * sum_A
    count = 0
    for a in A:
        if a >= border:
            count += 1
    if count >= M:
        print("Yes")
    else:print("No")


if __name__ == "__main__":
    main()