Q = int(input())


def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


# O(Q * sqrt(x)) = 10**4 * (3 * 10**5) ** 0.5
#                = 10**4 * 10**2.5
#                = 10**6.5
#                < 10**7
for _ in range(Q):
    x = int(input())
    # 素数判定
    print("Yes" if is_prime(x) else "No")
