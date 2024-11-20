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
        h: usize, w: usize,
        a: [[i32; w]; h],
    }
    let mut sum_h = vec![0; h];
    let mut sum_w = vec![0; w];
    for i in 0..sum_h.len() {
        for j in 0..sum_w.len() {
            sum_h[i] += a[i][j];
            sum_w[j] += a[i][j];
        }
    }
    // dbg!(&sum_h, &sum_w);
    for (i, h_i) in sum_h.iter().enumerate() {
        for (j, w_j) in sum_w.iter().enumerate() {
            print!("{}", h_i + w_j - a[i][j]);
            if j != sum_w.len() - 1 {
                print!(" ");
            }
        }
        println!();
    }
}
