




def main():
    mod = 10**9 + 7 
    n, a, b = map(int, input().split()) 
    # init
    fac = [0]*(n+1)
    finv = [0]*(n+1)
    inv = [0]*(n+1)
    
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2, n+1):
        if i == a or i == b:continue
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod%i] * (mod / i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod

    def comb(n, k):
        if (n < k): return 0
        if (n < 0 or k < 0): return 0
        return fac[n] * (finv[k] * finv[n-k] % mod) % mod

    print(comb())

if __name__ == "__main__":
    main()