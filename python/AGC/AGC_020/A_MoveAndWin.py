
def main()->None:
    N, A, B = map(int, input().split())
    diff: int = B - A - 1 # A,Bが初期位置にある時の間のマス目の数
    if diff % 2 == 0:
        print("Borys")

    else:
        print("Alice")


if __name__ == "__main__":
    main()