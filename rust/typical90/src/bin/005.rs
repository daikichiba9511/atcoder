//! 問題: https://atcoder.jp/contests/typical90/tasks/typical90_e
//! 回答参考：https://atcoder.jp/contests/typical90/submissions/25533563

use proconio::input;
const MOD: usize = 1e9 as usize + 7;

/// baseのexp_idx乗をo(logn)で求める二分累乗法
///
/// 通常ならa^nはa*a*...aでn回掛けるのでO(n)
///
/// 参考：
/// [1] https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a#4-%E7%B4%AF%E4%B9%97-an
fn modpow(mut base: usize, exp_idx: usize, modular: usize) -> usize {
    // baseは最大でもmodular
    let mut ans: usize = 1;
    for i in 0..63 {
        // 指数をi回右シフトして1と同じ箇所がフラグが立っていたら入る（底^ 1)
        if (exp_idx >> i) & 1 == 1 {
            ans *= base;
            ans %= modular;
        }
        // base^2を計算
        base = base.pow(2);
        base %= modular;
    }
    ans
}

fn solve1() {
    input! {
        n: usize, b: usize, k: usize,
        chs: [usize; k],
    }

    // 10の2のi乗の前処理
    // 64 = 2^6
    let mut power10: Vec<usize> = vec![0; 64];
    for i in 0..64 {
        power10[i] = modpow(10, 1 << i, b);
    }

    // dp[i][j] i: 上から何桁目か、j:bで割ったあまり
    let mut dp: Vec<Vec<usize>> = vec![vec![0; b]; 64];
}

fn main() {
    solve1()
}
