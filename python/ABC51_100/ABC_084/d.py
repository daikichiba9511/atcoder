import sys
def main():
    def input(): return sys.stdin.readline()[:-1]
    MAX = 100_005

    # エラトステネスのふるい
    is_prime = [1] * MAX
    is_prime[0] = 0; is_prime[1] = 0
    for i in range(MAX):
        if not is_prime[i]: continue
        j = i * 2
        while j < MAX:
            is_prime[j] = 0
            j += i

    # 2017に似た数かどうか
    a = [0] * MAX
    for i in range(MAX):
        if i % 2 == 0: continue
        if is_prime[i] and is_prime[(i + 1) // 2]:
            a[i] = 1
    
    # 累積和
    s = [0] * (MAX + 1)
    for i in range(MAX):
        s[i + 1] = s[i] + a[i]
    
    # クエリ処理
    Q = int(input())
    for q in range(Q):
        l, r = map(int, input().split())
        r += 1
        print(s[r] - s[l])
if __name__ == '__main__':
    main()