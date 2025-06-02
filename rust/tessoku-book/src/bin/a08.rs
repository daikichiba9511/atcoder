use std::vec;

#[allow(unused_imports)]
use num::integer::gcd;
use proconio::{input, fastout};

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
    input!{
        h: usize, w: usize,
        x: [[i32; w]; h],
        q: i32,
    };
    dbg!(&x);

    let mut cum = vec![vec![0; w + 1]; h + 1];
    // 横方向に累積和
    for ih in 0..h {
        for iw in 0..w {
            cum[ih][iw + 1] = cum[ih][iw] + x[ih][iw];
        }
    }
    // 縦方向に累積和
    for iw in 0..w {
        for ih in 0..h {
            cum[ih + 1][iw] = cum[ih][iw] + x[ih][iw];
        }
    }

    for _ in 0..q {
        // a行b列, c行d列
        input! {
            a: usize, b: usize, c: usize, d: usize,
        }
        let z = cum[c][d] + cum[a - 1][b - 1] - cum[c][b - 1] - cum[a - 1][d];
        println!("{}", z);
    }
}
