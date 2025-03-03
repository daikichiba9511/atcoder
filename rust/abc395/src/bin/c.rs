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
        n: usize, a: [usize; n]
    };
    let mut ans = n + 1;
    // pos[a[i]]でaの値を使うので最大値入るように
    let mut pos = vec![Vec::new(); 10_usize.pow(6) + 1];
    for (i, &value) in a.iter().enumerate() {
        pos[value].push(i);
    }
    for indices in pos.iter().take(10_usize.pow(6) + 1) {
        // 一つしかindexがない場合は列に一つしか存在しないのでスキップ
        if indices.len() < 2 {
            continue;
        }
        // 複数存在するもののindex間の距離で最短のものを計算
        for j in 0..(indices.len() - 1) {
            chmin!(ans, indices[j + 1] - indices[j] + 1);
        }
    }
    if ans == n + 1 {
        println!("-1");
    } else {
        println!("{}", ans);
    }
}
