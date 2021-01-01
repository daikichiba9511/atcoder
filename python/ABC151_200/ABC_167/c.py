# bit全探索、　計算量O(2**n*n*m) \simeqq 10^5

def main():
    # 各本の各アルゴリズムの理解度をいれる配列
    a = [[0]*12 for _ in range(12)]
    INF = 1 << 29

    # input
    n, m, x = map(int, input().split())
    c = [0]*n
    for i in range(n):
        tmp = list(map(int, input().split()))
        c[i] = tmp[0]
        for j in range(m) :
            a[i][j] = tmp[j+1]

    # どの本を買うか、買わないかを２進数で表す（その状態と１０進数を1対１に対応させてる）
    # 例えば１の時001、２の時010みたいに各bitがその本iを買うなら１、買わないなら０
    ans = INF
    for bit in range(2**n) :
        cost = 0
        d = [0]*m # 各アルゴリズムの理解度をいれる配列
        for i in range(n): #　このループで２進数表現に直して、各桁の１を買った本と対応させてる
            # bitのi番目のbitが立ってる時に入る
            # & 1でシフトしたときにフラグが立っていたら入る。
            # bit(10進数)を2進数で表現したときにi桁目に１が入っていたらTrueを返す
            if (bit>>i&1):
                cost += c[i]
                for j in range(m) :
                    d[j] +=  a[i][j]

        # 条件：各アルゴリズムの理解度がx以上かのチェック
        ok = True
        for j in range(m) :
            if d[j] < x: # 各アルゴリズムで理解度がx以下のがあればFalseな組み合わせ
                ok = False

        if ok:
            ans = min(ans, cost)

    if ans == INF : print(-1)
    else : print(ans)

if __name__ == "__main__":
    main()