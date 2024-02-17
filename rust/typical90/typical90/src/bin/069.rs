use proconio::{fastout, input};

#[fastout]
fn solve1() {
    input! {
        (n, k): (usize, usize)
    }
    let l = (k - 1).max(0);
    let mut m = (k - 2).max(0);
    const MOD: usize = 1_000_000_007;
    let mut ans = 1;
    if n < 2 {
        for i in 0..n {
            if i == 0 {
                ans = k
            } else if i == 1 {
                ans *= l
            } else {
                ans *= m
            }
            ans %= MOD;
        }
    } else {
        let mut x = n - 2;
        // NOTE: 繰り返し二乗法
        // xの1位のbitが立っている時はansにmをかける
        // x = 10
        // | iter\var| ans  | m   | x   |
        // |---------|------|-----|-----|
        // | 0       | 1    | m   | 10  |
        // | 1       | 1    | m^2 | 5   |
        // | 2       | m^2  | m^4 | 3   |
        // | 3       | m^6  | m^8 | 1   |
        //
        // ここで(K-2)^(N-2)を求める
        while x > 0 {
            if x & 1 == 1 {
                ans = ans * m % MOD
            }
            m = m * m % MOD;
            x >>= 1;
        }
        ans = ans * k % MOD;
        ans = ans * l % MOD;
    }
    println!("{}", ans);
}

fn main() {
    solve1();
}
