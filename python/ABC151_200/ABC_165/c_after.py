
from itertools import combinations_with_replacement

def main():
    n, m, q = map(int, input().split())
    abcd_l = [list(map(int, input().split())) for _ in range(q)]

    ans = 0
    # m+n_C_n で重複組み合わせで広義単調増加の数列を表現する(高々 20_C_10 \simeq 2 \times 10^5)
    for i in combinations_with_replacement(range(1, m+1), n-1):
        A = [1] + list(i) # A の最小値は必ず１なのでn-1個選んで端に１を足してる
        total = 0
        for abcd in abcd_l:
            # Python は  0-originだから−１に注意 A_b - A_a = c
            if A[abcd[1]-1] - A[abcd[0]-1] == abcd[2]:
                total += abcd[3]
        ans = max(ans, total)
    return ans

if __name__ == "__main__":
    print(main())