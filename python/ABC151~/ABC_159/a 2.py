import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

def main():
    n, m = map(int, input().split())
    if n >= 2:
        n_comb = comb(n,2)
    elif n < 2:
        n_comb = 0
    if m >= 2:
        m_comb = comb(m, 2)
    elif m < 2:
        m_comb = 0
    print(n_comb + m_comb)

if __name__ == "__main__":
    main()