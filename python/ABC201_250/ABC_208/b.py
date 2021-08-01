import math
import sys


def main():
    def input():
        return sys.stdin.readline()[:-1]

    p = int(input())

    num = 10
    res = 0
    while True:
        num_factorial = math.factorial(num)

        if num_factorial > p:
            num -= 1

        else:
            quotient = p // num_factorial
            if quotient <= 100:
                res += quotient
                p -= quotient * num_factorial
                num -= 1

        if num < 0:
            break
    print(res)


if __name__ == "__main__":
    main()
