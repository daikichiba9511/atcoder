


def main()->None:
    N:int = int(input()) # 支払い金学
    A:int = int(input()) # 1円の枚数
    B:int = N % 500 # ５００円が商枚使われた時の余り、これが１円より多いか少ないかで決める
    if B <= A:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()