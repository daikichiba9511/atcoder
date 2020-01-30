


def main()->None:
    A, B, C, D = map(int, input().split())
    if A < C < B:
        if D <= B:
            print(D - C)
        else:
            print(B - C)
    elif C < A:
        if D <= A:
            print(0)
        elif A < D:
            print(D - A)
        else:
            print(B - A)
    else:
        print(0)

if __name__ == "__main__":
        main()