
def is_prime(x: int)->bool:
    # 解説見た
    if x <= 1:
        return True
    i: int = 2
    while i * i <= x:
        if x % i == 0:
            return True
        i += 1
    return False


def main()->None:
    X: int = int(input())
    p: int = X
    while is_prime(p):
        p += 1
    print(p)

if __name__ == "__main__":
    main()