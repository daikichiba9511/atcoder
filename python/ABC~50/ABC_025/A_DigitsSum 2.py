

#　各桁の和を計算する
def findSumOfDigits(n):
    sum_digits = 0
    while n > 0 :
        sum_digits += n % 10
        n //= 10
    return sum_digits


def main()->None:
    N = int(input())
    # AとBの各桁の和を求める。
    range_A = range(1,N+1)
    min_total = 100000
    for a in range_A:
        b = N - a
        if b < 1 : continue
        sum_a = findSumOfDigits(a)
        sum_b = findSumOfDigits(b)
        total = sum_a + sum_b
        if total < min_total:
            min_total = total
    print(min_total)


if __name__ == "__main__":
    main()