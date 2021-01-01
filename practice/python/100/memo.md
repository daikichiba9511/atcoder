# 分野別　初中級者が解くべき過去問精選１００問

## 1.[ITP1_7_8-How Many Ways](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja)

### 1.1 問題概要

1からnまでの数列から三つ重複なしでとってきて、その和と入力xとが等しい組み合わせの数を求める

### 1.2 メモ

組合せを求めるのでpythonならcombinationsを使って組み合わせを選んで返ってきたTupleの各成分のを足してxになる個数をカウントする。

[souce](./aoj.py)

## 2.[Atcoder ABC106 B-105](https://atcoder.jp/contests/abc106/tasks/abc106_b)

### 2.1 問題概要

1以上N以下の奇数のうち正の約数をちょうど８個もつようなものを求める

### 2.2 メモ

ます１以上N以下の奇数の数列を生成する。そこから一つ一つ要素を取り出していく。取り出した要素は、それ以前に取り出した要素の積で表せるはずだから１からその数までの奇数を探索する。判定したい数が奇数で奇数の積でないと奇数にならないので探索区域は１から取り出した数までの奇数でできた空間で探索点で対象の要素が割り切れる数をカウントして８になった対象の数を数えればいい。

[source](../../../python/ABC101~150/ABC_106/b.py)

## 3.[Atcoder ABC122 B - ATCoder](https://atcoder.jp/contests/abc122/tasks/abc122_b)

### 3.1 問題概要

与えられた文字列の部分文字列の条件を満たす最大の長さを求める

条件：全て"A", "C", "G", "T"のみで構成される

### 3.2 メモ

all関数をうまく使う。`str`の`Count`メソッドを使うと便利。

[source](../../../python/ABC101~150/ABC_122/b.py)　

## 4.[Atcoder パ研杯2019 C - カラオケ](https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c)

### 4.1 問題概要

Mこの中から二つ選んでN人分の得点の最大値

### 4.2 メモ

itertoolsのcombinationsで組み合わせを選んでそれについての得点を更新して最大値を求めれば良い

[source](../../../python/OtherWise/pa2019/c.py)

## 5.[Atcoder ABC095 C - Half and Half](https://atcoder.jp/contests/abc095/tasks/arc096_a)

### 5.1 問題概要

組み合わせの中から最低値を出す

### 5.2 メモ

ABが半分ずつのやつを$[1, 10 ^ {5}]$で探索して残りをA,Bで合わせるのが最低金額になるらしい。。

[source](../../../python/ABC51~100/ABC_095/c.py)

## 6.[Atcoder 三井住友信託銀行P.C. D - Luscky PIN](https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d)

### 6.1 問題概要

N桁の数字から３桁残して消して残りのものを左から並べた時の何組あり得るか

### 6.2 メモ



[source](../../../python/OtherWise/mituisumitomo2019/d.py)

## 7.[JOI 2007 本選３ - 最古の遺跡]（https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_c)

### 問題概要

### メモ

## 8.

## 9.

## 10.[AOJ ALDS_5_A 総当たり](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja)

### 問題概要

### メモ

## 11.[Atcoder ABC128 C - switches](https://atcoder.jp/contests/abc128/tasks/abc128_c)

### 問題概要

NこのスイッチとM個の電球があって、電球はonになっているスイッチの個数を２で割ったあまりが$p _ i$に等しいとき点灯する

全ての電灯が点灯するようなスイッチのon/offの状態の組み合わせは何通りあるか

### メモ
