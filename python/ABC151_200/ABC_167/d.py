def main():
    # input
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # 訪れた頂点のメモ
    s = []
    # sの中のインデックスに対応, 訪れていない点は−１に対応
    order = [-1]*(n+1)
    c = 1 # 周期
    v = 1 # vertex, 1から始める
    while order[v] == -1:
        order[v] = len(s)
        s.append(v) # 訪れた頂点の記録
        v = a[v-1] # 次の頂点へ


    l = order[v] # 例外部分の長さ
    c = len(s) - l
    if k < l :
        print(s[k])
    else:
        k -= l # 例外部分を引いて周期を持つ部分のみにする。
        k %= c # 周期のうちどれになるかは剰余に等しい。
        print(s[l+k])

if __name__ == "__main__":
    main()