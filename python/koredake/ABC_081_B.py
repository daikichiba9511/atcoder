from typing import Dict


def main() -> None:
    # 整数の数
    N: int = int(input())

    # 数字を配列で受けとって、あとで参照したい
    A = list(map(int, input().split()))

    res: int = 0

    # 操作が行える限り操作を繰り返す。
    while True:
        exist_odd = False
        range_N = range(N)
        # 奇数チェック
        for i in range_N:
            if A[i] % 2 != 0:
                exist_odd = True  # 奇数があったらフラグオン！！
        if exist_odd:
            break  # 奇数があったらブレーク

        # 操作を行える時操作を行う。
        for j in range_N:
            A[j] /= 2
        # 操作回数のカウント
        res += 1
    print(res)


if __name__ == "__main__":
    main()

