from typing import Iterable

def findBiggerDigits(n: int)->int:
    digits: int = 0
    while n > 0:
        digits += 1
        n //= 10
    return digits 

def main()->None:
    n: int = int(input())
    sqrt_n: int = int(n ** (1/2))
    range_a: Iterable[int] = range(1, sqrt_n+1)

    min_value: int = 1000000
    for a in range_a:
        if n % a != 0: continue
        b: int = n / a
        a_digits: int = findBiggerDigits(a)
        b_digits: int = findBiggerDigits(b)
        max_dig: int = max(a_digits, b_digits)
        if max_dig < min_value:
            min_value = max_dig

    print(min_value)


if __name__ == "__main__":
    main()