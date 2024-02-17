import itertools

n = int(input())
R = input()
C = input()


def head(s: list[str]) -> str:
    for c in s:
        if c != ".":
            return c
    raise ValueError


# (5!) ** 3 = 120 ** 3 = 1728000 ≒ 10 ** 6の全探索
for a, b, c in itertools.product(itertools.permutations(range(n)), repeat=3):
    # 同じ組合せは除外
    # a,b,cはそれぞれどの列に"A", "B", "C"を置くかを表す
    # 各行、各列にA, B, Cはたかだか一つずつしか置けないので、重複してる
    # 要は同じindexに同じ数字が入ってると同じ箇所に置くことになるので、あとにある方が先においてる文字を上書きするのがだめ
    if any(ai == bi or bi == ci or ci == ai for ai, bi, ci in zip(a, b, c)):
        continue

    s = [["."] * n for _ in range(n)]
    for i, j in enumerate(a):
        s[i][j] = "A"
    for i, j in enumerate(b):
        s[i][j] = "B"
    for i, j in enumerate(c):
        s[i][j] = "C"

    # zip(*s)で転置
    r_ok = "".join(map(head, s)) == R
    c_ok = "".join(map(head, zip(*s))) == C
    if r_ok and c_ok:
        print("Yes")
        print(*map(lambda x: "".join(x), s), sep="\n")
        exit()
print("No")
