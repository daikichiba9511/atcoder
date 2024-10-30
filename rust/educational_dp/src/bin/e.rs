#[allow(unused_imports)]
use num::integer::gcd;
use proconio::{fastout, input};

// =============================================
// Library
// =============================================
#[allow(unused_macros)]
macro_rules! chmin {
    ($base:expr, $($cmps:expr),+ $(,)*) => {{
        let cmp_min = min!($($cmps),+);
        if $base > cmp_min {
            $base = cmp_min;
            true
        } else {
            false
        }
    }};
}

#[allow(unused_macros)]
macro_rules! chmax {
    ($base:expr, $($cmps:expr),+ $(,)*) => {{
        let cmp_max = max!($($cmps),+);
        if $base < cmp_max {
            $base = cmp_max;
            true
        } else {
            false
        }
    }};
}

#[allow(unused_macros)]
macro_rules! min {
    ($a:expr $(,)*) => {{
        $a
    }};
    ($a:expr, $b:expr $(,)*) => {{
        std::cmp::min($a, $b)
    }};
    ($a:expr, $($rest:expr),+ $(,)*) => {{
        std::cmp::min($a, min!($($rest),+))
    }};
}

#[allow(unused_macros)]
macro_rules! max {
    ($a:expr $(,)*) => {{
        $a
    }};
    ($a:expr, $b:expr $(,)*) => {{
        std::cmp::max($a, $b)
    }};
    ($a:expr, $($rest:expr),+ $(,)*) => {{
        std::cmp::max($a, max!($($rest),+))
    }};
}

#[allow(dead_code)]
const INF: i32 = 100_000_000;

// =============================================
// Main
// =============================================
#[fastout]
fn main() {
    input! {
        n: usize, w: usize,
        wv: [[i64; 2]; n],
    }
    let max_n = 110;
    let max_v = 100_100;

    // dp[i][sum_v] := i - 1番目までの品物から価値がちょうどsum_vとなるように選んだ時の重さの総和の最小値
    let mut dp = vec![vec![0; max_v]; max_n];
    dp[0][0] = 0;

    for i in 0..n {
        let w_i = wv[i][0];
        let v_i = wv[i][1];
        for sum_v in 0..max_v {
            // i番目を選ぶ場合
            let v = sum_v as i64 - v_i;
            if v >= 0 {
                chmin!(dp[i + 1][sum_v], dp[i][v as usize] + w_i);
            }
            chmin!(dp[i + 1][sum_v], dp[i][sum_v]);
        }
    }
    let mut res = 0;
    for sum_v in 0..max_v {
        if dp[n][sum_v] <= w as i64 {
            res = sum_v;
        }
    }
    println!("{}", res);
}
