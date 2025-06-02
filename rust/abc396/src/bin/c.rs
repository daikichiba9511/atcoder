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
        n: usize,
        m: usize,
        b: [usize; n],
        m: [usize; m]
    };
    // 白いボールを超えないように黒いボールを選んだ時の価値の最大値
    // dp[i][j]: i番目の黒いボールまで選んで、j番目の白いボールを選んだ時の価値の最大値
    // i番目の黒いボールを選ぶ/選ばないを1~nまでの黒いボールの中から選ぶ
    // dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + b[i])
    let mut dp = vec![vec![0; m + 1]; n + 1];
    for i in 1..=n {
        for j in 1..=m {
            // i番目の黒いボールを選ばない
            dp[i][j] = dp[i - 1][j];
            if i - j > 0 {
                // i番目の黒いボールを選ぶ
                dp[i][j] = dp[i][j].max(dp[i - 1][j - 1] + b[i - 1]);
            }
        }
    }
}
