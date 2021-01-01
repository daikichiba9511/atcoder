
def main()->None:
    A, B, K = map(int, input().split())

    if A > K:
        print(A-K, B)
    else:
        diff = K - A
        if diff < B:
            print(0, B-diff)
        else:
            print(0, 0)





if __name__ == "__main__":
    main()