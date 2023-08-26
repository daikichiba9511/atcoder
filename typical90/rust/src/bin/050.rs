use proconio::{fastout, input};

/// solution #1
/// 配るDP
///
fn solve() {
    input! {
        n: usize,
        l: usize,
    }

    let m = 1_000_000_007;

    // 配る方法で考える
    // 各段で1つ進むか、L個進むかの選択肢がある
    let mut dp: Vec<u64> = vec![0; n + 1];
    dp[0] = 1;
    for i in 0..n {
        dp[i + 1] += dp[i] % m;
        if i + l <= n {
            dp[i + l] += dp[i] % m;
        }
    }
    println!("{}", dp[n] % m);
}

struct DP {
    dp: Vec<u64>,
    n: usize,
    l: usize,
    m: u64,
}

impl DP {
    /// new function for DP
    ///
    /// * `n` - the number of steps
    /// * `l` - the number of steps to jump
    /// * `m` - the modulo
    fn new(n: usize, l: usize, m: u64) -> Self {
        DP {
            dp: vec![0; n + 1],
            n,
            l,
            m,
        }
    }
    fn solve(&mut self) -> u64 {
        self.dp[0] = 1;
        for i in 0..self.n {
            self.dp[i + 1] += self.dp[i] % self.m;
            if i + self.l <= self.n {
                self.dp[i + self.l] += self.dp[i] % self.m;
            }
        }
        self.dp[self.n] %= self.m;
        self.dp[self.n]
    }
}

fn solve2() {
    input! {
        n: usize,
        l: usize,
    }
    let m = 1_000_000_007;

    // もらう方法で考える
    // i段目にたどり着いた時に、i-1段目から1段進んだ場合と、i-L段からL段進んだ場合の2通りの遷移がある
    // overflowに注意する
    let mut dp: Vec<u64> = vec![0; n + 1];
    dp[0] = 1;
    for i in 1..n + 1 {
        if i >= l {
            dp[i] += dp[i - l] % m;
        }
        dp[i] += dp[i - 1] % m;
    }

    println!("{}", dp[n] % m);
}

fn solve3() {
    input! {
        n: usize,
        l: usize,
    }
    let m = 1_000_000_007;

    // let mut dp = DP::new(n, l, m);
    // println!("{}", dp.solve());
    println!("{}", DP::new(n, l, m).solve())
}

#[fastout]
fn main() {
    // solve();
    // solve2();
    solve3();
}
