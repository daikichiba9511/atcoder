use proconio::{fastout, input};
#[fastout]
fn main() {
    input! {
        n:usize, k:usize,
        h:[i32; n],
    }
    const INF: i32 = 1_000_000_000;
    let mut dp = [INF; 100_110];
    dp[0] = 0;

    for i in 0..n {
        for j in 1..=k {
            if i + j < n {
                dp[i + j] = dp[i + j].min(dp[i] + (h[i] - h[i + j]).abs());
            };
        }
    }
    // println!("{:?}", &dp[0..10]);
    println!("{}", dp[n - 1]);
}
