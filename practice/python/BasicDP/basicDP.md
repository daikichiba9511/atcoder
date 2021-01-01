# 典型的DP

ナップザックDP

## 問題１

```python

from typing import List

def main():
    n = int(input())

    dp : List[int] = []*(n+100)
    a : List[List[int]] = [list(map(int, input().split())) for _ in range(n)]

    # 初期値０
    dp[0] = 0
    for i in range(n):
        dp[i+1] = max(dp[i], dp(i)+a[i])

    print(dp[n])
```

## ナップサック問題

- 解法

`dp[i] := i番目までの品物の中から重さがWを超えないように選んだ時の、価値の総和の最大値`

とすると詰まる。dpテーブルに価値についての情報を持っているが、重さについての情報は持っていない。

加えたときに重さがWを超えてしまうのかが分からない問題が発生する。

つまり今重さがどうなっているかの情報が必要

`dp[i+1][w] := i番目までの品物の中から重さがwを超えてしまわないように選んだ時の価値の総和`

<DP漸化式>
$$
dp[i+1][w] =
\begin{cases}
    max(dp[i][w - weight[i], dp[i][w]]) &(w \geq weight[i]) \\\\
    dp[i][w] &(w < weight[i])
\end{cases}
$$
<DP初期化条件>
$$dp[0][w] = 0 \space (w = 0, 1, \cdots, W)$$

実際にDPを設計するときに、これだけじゃ情報が足りない→添字を足してdpのテーブルを二次元にするはよくあるらしい。

```python
def main():
    n, W = map(int, input().split())

    value = []*110
    weight = []*110

    # dp テーブル
    dp = [[]*110 for _ in range(10010)]

    for i in range(n):
        value[i], weight[i] = map(int, input().split())

    # DP初期条件： dp[0][w] = 0
    for w in range(W):
        dp[0][w] = 0

    # DPループ
    for i in range(n):
        for w in range(W):
            if w >= weight[i]:
                dp[i+1][w] = max(dp[i][w- weight[i]] + value[i], dp[i][w])
            else:
                dp[i+1][w] = dp[i][w]

    print(dp[n][w])
```

## 部分和数え上げ問題

i は与えられた数列Aのインデックス

`dp[i+1][j] := i番目までの整数の中からいくつか選んで総和をjとする場合の数`

- 整数a[j]を選ぶ場合(j$\geq$a[j]の場合のみ)

<div align="center">dp[ i ][ j - a[ j ] ]通り</div>

- 整数a[i]を選ばない場合

<div align="center">dp[ i ][ j ]通り</div>

まとめると

<DP漸化式>
$$
dp[i + 1][j] =
\begin{cases}
    dp[i][j - a[j]] + dp[i][j]&(j\geq a[i])\\\\
    dp[i][j] &(i < a[i])
\end{cases}
$$

<DP初期条件>
$$
dp[0][j] =
\begin{cases}
    1 &(j=0)\\\\
    0 &(j\not= 0)
\end{cases}
$$

```python

MOD = 1000000009

def main():
    n, A = map(int, input().split())
    a = list(map(int, input().split()))

    # dpテーブル 余裕を持って大きめに作る
    dp = [[0]*110 for _ in range(10010)]
    dp[0][0] = 1

    for i in range(i):
        for j in range(A):
            dp[i + 1][j] += dp[i][j] %= MOD

    print(dp[n][A])

```

## 最小個数部分和問題

`dp[ i + 1 ][j]:=i番目までの整数の中からいくつかの整数を選んで総和がjとする方法を全て考えた時の、選んだ整数の個数の最小値`

dp[ i + 1][j]の値を求めるには以下の２つの場合のminimumをとる

- 整数a[i]を選ぶ場合(j $\geq$ a[i]の場合のみ)

<div align="center">dp[i][j - a[i]] + 1</div>

- 整数a[i]を選ばない場合

<div align="center">dp[i][j]</div>

<DP漸化式>

$$
dp[i+1][j] =
\begin{cases}
    min(dp[i][j-a[i]]+1, dp[i][j]) &(j\geq a[i])\\\\
    dp[i][j]&(i < a[i])
\end{cases}
$$

<DP初期値>

$$
dp[0][j] =
\begin{cases}
    0&(j=0)\\\\
    \infin &(j\not=0)
\end{cases}
$$

```python
INF : int = 1 << 29

def main():
    n, A = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [[INF]*110 for _ in range(10010)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(A):
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - a[i]] + 1)
            if j >= a :
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-a[i]]+1)
    if dp[n][A] < Inf : print(dp[n][A])
    else : print(-1)

```

## k個以内部分和問題

添字を増やしたくなるけどdpテーブルのサイズはnKA

計算時間はO(nKA) $\lessapprox 500 \times 1000 \times 10000 = 5 \times 10 ^ {9}$

だから普通に添字増やす程度では間に合わない。

「DPの添字ではなくそのものに情報を持たせることを考える」

一般にbool値を求めるDPをすることは無駄が多いらしい。

`dp[i=1][j]:=i番目までの整数の中からいくつかの整数を選んで総和がjとする方法を全て考えた時の、選んだ整数の個数の最小値`


# 区間DP

http://kutimoti.hatenablog.com/entry/2018/03/10/220819


まずdpの保持する値を決める

`dp[l][r]:=区間[l,r)で取り除くことができるブロックの数`

