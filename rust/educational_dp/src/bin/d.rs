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

    // 大きすぎる配列はスタックじゃなくてヒープに確保する
    // dp[i][w] := 選んだ品物の重さの総和がwの時のi番目までの品物の価値の総和の最大値
    let mut dp = vec![vec![0; 100_110]; 110];

    for i in 0..n {
        let w_i = wv[i][0];
        let v_i = wv[i][1];

        for sum_w in 0..=w {
            // i番目を選べる時
            let cost = sum_w as i64 - w_i;
            if cost >= 0 {
                chmax!(dp[i + 1][sum_w], dp[i][cost as usize] + v_i);
            }
            // i番目を選べない時
            chmax!(dp[i + 1][sum_w], dp[i][sum_w]);
        }
    }
    println!("{}", dp[n][w]);
}
