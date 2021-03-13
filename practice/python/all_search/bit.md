# bit全探索

- ２進数で多様な状態を表現することができる。
- 1の立ってる場所をフラグとして管理するこれを10進数に直したりすることで状態を表す。

N個のものからいくつか選ぶ方法を全列挙して調べる。

選ぶ、選ばないの２つの状態で表すので$2 ^ {N}$通りある。

- N個のアイテムからいくつか選ぶ方法
- 整数
とを1対１に対応つける方法

```cpp
for (int bit = 0; bit < (1<<N)); ++bit) {

}
```

いくつか選ぶ方法をbitという整数に対応つけてる。

```cpp

```

`bit_search`

```python
def bit_search():
    n = 5:

    # {0, 1, ... , n-1}の部分集合の全探索
    for i in range(2**n):

        """bit で表される集合の処理を書く"""


```

## bit DP

- n個の要素の順列としてありうるものの中から最適な物を求めたい時に使える。

- dp[S] $\coloneqq$ 全体集合の中の真の部分集合{1, 2, ... , n-1}についてその中で順序を最適化した時のSの中での最小コスト。

bitDP動くのを確認して答えもあってるけど完全に理解したわけではなくてcppのコードをpythonで書き換えただけ。。
DPはまた別途やる必要がある。

大事なのは状態を表す整数とbitを対応させて状態を保持することで色々できるよってこと。

## 参考

[ビット演算 (bit 演算) の使い方を総特集！ 〜 マスクビットから bit DP まで 〜 @drken](https://qiita.com/drken/items/7c6ff2aa4d8fce1c9361)