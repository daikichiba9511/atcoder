

# 各桁の和を計算する関数
def findSumDigits(n: int)->int:
    sum_digits:int = 0
    while n > 0: # nが０になるまで。
        sum_digits += n % 10
        n //= 10
    return sum_digits


# ハージャット数かどうかを判定する。
def main()->None:

    N:int = int(input())
    f_x:int = findSumDigits(N)
    if N % f_x == 0: # 割り切れれば、ハージャット数
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

