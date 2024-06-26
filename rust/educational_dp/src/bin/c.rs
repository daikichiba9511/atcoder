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

// =============================================
// Main
// =============================================
#[fastout]
fn main() {
    input! {
        n: usize,
        abc: [[i32; 3]; n],
    }

    // i番目にjを選んだ時の最大値
    // 0:a, 1:b, 2:c
    let mut dp = [[0; 3]; 100_010];

    for i in 0..n {
        for j in 0..3 {
            for k in 0..3 {
                if j == k {
                    continue;
                } else {
                    // jが決まってる時に、kを選んで更新する
                    // 例: (j,k)=(1,0),(1,2)
                    // 1. (j,k)=(1,0)
                    // dp[i+1][0] = max(dp[i+1][0], dp[i][1] + abc[i][0])
                    // 2. (j,k)=(1,2)
                    // dp[i+1][2] = max(dp[i+1][2], dp[i][1] + abc[i][2])
                    chmax!(dp[i + 1][k], dp[i][j] + abc[i][k]);
                }
            }
        }
    }

    // println!("{:?}", &dp[0..10]);
    let mut ans = 0;
    for j in 0..3 {
        chmax!(ans, dp[n][j]);
    }
    println!("{}", ans);
}
