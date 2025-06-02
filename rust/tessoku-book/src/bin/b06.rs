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
        a: [i32; n],
        q: usize,
    };
    let mut cum_hit = vec![0; n + 1];
    let mut cum_miss = vec![0; n + 1];
    // 前計算で累積和を計算、計算量O(n)
    for i in 0..n {
        let (flg_hit, flg_miss) = if a[i] == 1 { (1, 0) } else { (0, 1) };
        cum_hit[i + 1] = cum_hit[i] + flg_hit;
        cum_miss[i + 1] = cum_miss[i] + flg_miss;
    }
    // クエリに回答するフェーズ
    for _ in 0..q {
        input! {
            il: usize, ir:usize,
        }
        let sum_hit = cum_hit[ir] - cum_hit[il - 1];
        let sum_miss = cum_miss[ir] - cum_miss[il - 1];
        let ans = if sum_hit > sum_miss {
            "win"
        } else if sum_hit == sum_miss {
            "draw"
        } else {
            "lose"
        };
        println!("{}", ans);
    }
}
