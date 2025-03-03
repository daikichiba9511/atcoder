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

fn init_vec(n: usize) -> Vec<i32> {
    (0..n).enumerate().map(|(i, _)| i as i32).collect()
}

// =============================================
// Main
// =============================================
#[fastout]
fn main() {
    input! {
        n: usize, q: usize,
    };
    let mut b2l = init_vec(n);
    let mut l2b = init_vec(n);
    let mut p2b = init_vec(n);

    for _ in 0..q {
        input! {i: i32}
        if i == 1 {
            input! {a: usize, b: usize}
            p2b[a - 1] = l2b[b - 1];
        } else if i == 2 {
            input! {a: usize, b: usize}
            // ラベル鳩 -> 巣の情報を更新
            l2b.swap(a - 1, b - 1);
            // 巣 -> ラベル鳩の情報を更新
            b2l.swap(l2b[a - 1] as usize, l2b[b - 1] as usize);
        } else {
            input! {a: usize}
            println!("{}", b2l[p2b[a - 1] as usize] + 1);
        }
    }
}
