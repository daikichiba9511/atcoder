use proconio::{fastout, input};
use std::cmp::min;
#[fastout]
fn main() {
    input! {
        n:usize,
        h:[i32;n],
    }
    const INF: i32 = 100000000;
    let mut dp = [INF; 100_000];
    dp[0] = 0;
    dp[1] = (h[1] - h[0]).abs();

    for i in 2..n {
        dp[i] = min(
            dp[i - 2] + (h[i] - h[i - 2]).abs(),
            dp[i - 1] + (h[i] - h[i - 1]).abs(),
        )
    }

    // println!("{:?}", &dp[0..10]);
    println!("{}", dp[(n - 1) as usize]);
}
