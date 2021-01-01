# ABC165

## 感想

悲しみの２完でした。パフォーマンスは４９１でした。Cは広義単調増加の数列の作り方がわからずできず、Dはx＝Nの時の条件の考察が抜けていてできませんでした。厳しい。。楽しかったがもっとできるようになりたいのでD問題まで復習していきたいと思います。また基本的なアルゴリズムの勉強もしていきます。。

## A. We Love Golf

### 問題

- a以上b以下の数列の中にKの倍数があるかの判定
- あれは`OK`、なければ`NG`

### 制約

- 入力は全て整数
- $1 \leq A \leq B \leq 1000$
- $1 \leq K \leq 1000$

### 考察

`range(a, b+1)`で数列を作りそこから一つずつ取り出してKで割った余りが０かどうか調べればいい。

### 解答

```python
def main():
    K = int(input())
    a, b = map(int, input().split())
    flag = False
    for i in range(a, b+1):
        if i % K == 0:
            flag = True
    if flag:print("OK")
    else:print("NG")

if __name__ == "__main__":
    main()
```

## B. １％

### 問題

- 100円に毎年１％利子つけて入力x以上になるのが何年後か

### 制約

- $101 \leq X \leq 10 ^ {18}$
- 入力は全て整数

### 考察

100から初めて1.01かけて再帰代入してその数をカウントすればいい

### 解答

```python
def main():
    x = int(input())
    cnt = 0
    money = 100
    while True:
        money = int(1.01 * money)
        cnt += 1
        if money >= x:
            break
    print(cnt)

if __name__ == "__main__":
    main()

```

## C. Many Requirements

### 問題

- 自然数N , M , Qと４つの整数の組み合わせ(a, b, c, d)がQ組み
- 長さNで$1 \leq A _ {1} \leq \cdots \leq A _ {N} \leq M$の広義単調増加の数列で以下の条件で得点の最大値を求める。
  
  - $A _ {b _ {i}} - A _ {a _ {i}} = c _ {i}$を満たす$i$の$d _ {i}$の総和が得点

### 制約

- $2 \leq N \leq 10$
- $1 \leq M \leq 10$
- $1 \leq Q \leq 50$
- $1 \leq a _ {i} \leq b _ {i} \leq N (i = 1, 2, \cdots, Q)$
- $0 \leq c _ {i} \leq M - 1 (i = 1, 2, \cdots, Q)$
- $(a _ {i}, b _ {i}, c _ {i}) \not = (a _ {j}, b _ {j}, c _ {i})(i \not = j\text{のとき})$
- $1 \leq d _ {i} \leq 10 ^ {5}(i = 1, 2, \cdots, Q)$

### 考察

広義単調増加の数列を作るのに`range(1, m+1)`の範囲の整数から$A _ {1} \sim A _ {N}$までの数列を作るのに、重複を許して組み合わせをつくる。
なので`n-1`個指定して`itertools.combination_with_replacement`で数列を探索する。数列は１始まりなのでリストに１を足している。

これは N, M がたかだか１０であることから計算量は$O (_ {20} C _ {10}) \simeq 2.0 \times 10 ^ {5}$程度であるので全探索でも間に合う。

この`itertools`を初めて知ったけど便利だ〜と思った。

### 解答

```python
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
```

## D. Floor functions

### 問題

- 整数A, B, N
- N以下の非負の整数xに対して

$$floor(\frac{Ax}{B}) - A \times floor(\frac{x}{B})$$

　の最大値を求める。$floor(t)$は実数$t$以下の最大の整数

### 制約

- $1 \leq A \leq 10 ^ {6}$
- $1 \leq B \leq 10 ^ {12}$
- $1 \leq N \leq 10 ^ {12}$
- 入力は全て整数

### 考察

$x = B -1 $のときあるいは $x = N$ のとき最大値をとる。

問題のような関数は条件を満たす中で第1項目が一番大きく第2項が一番小さく、つまり０になれば最大になる。

これは$\displaystyle{\frac{x}{B}}$の整数部分をZ、小数部分をMとすると

$$\displaystyle{\frac{Ax}{B}} = AZ + AM\tag{1}$$

$$floor(\frac{Ax}{B}) = AZ + floor(AM)\tag{2}$$

$$A \times floor(\frac{x}{B}) = AZ\tag{3}$$

と表せる。つまり$\displaystyle{\frac{x}{B}}$の小数部分が最大になれば良い。

これが$x = B - 1$のとき。他に$x = B - 1$を取れないような$x$のときがあって$B$が$N$より大きいときでこの時は$x = N$にすれば良い

あとは小さい方を代入すれば良い

例えば$B$が$N$より大きい時として,$A = 5, B = 10, N = 3$の時を考えてみる。

この時,$f(x) = floor(\displaystyle{\frac{Ax}{B}}) - A \times floor(\displaystyle{\frac{x}{B}})$とおくと

- $N = 1$の時

$$
\begin{aligned}
    f(1) &= floor(\displaystyle{\frac{5\cdot1}{10}}) - 5 \times floor(\displaystyle{\frac{1}{10}})\\\\
    &= 0
\end{aligned}
$$

- $N = 2$の時

$$
\begin{aligned}
    f(2) &= floor(\displaystyle{\frac{5\cdot2}{10}}) - 5 \times floor(\displaystyle{\frac{2}{10}})\\\\
    &= 1
\end{aligned}
$$

- $N = 3$の時

$$
\begin{aligned}
    f(3) &= floor(\displaystyle{\frac{5\cdot3}{10}}) - 5 \times floor(\displaystyle{\frac{3}{10}})\\\\
    &= 1
\end{aligned}
$$

のようになる。

例が一つだとわかりづらいが、第２項の入力がやはり肝でここで$x$が$B$より小さい時は$x = N$になりそうだということが分かる。

### 解答



```python
def f(x, a, b):
    return a * x // b - a * (x // b)

def main():
    a, b, n = map(int, input().split())
    return f(min(b-1, n), a, b)

if __name__ == "__main__":
    print(main())
```