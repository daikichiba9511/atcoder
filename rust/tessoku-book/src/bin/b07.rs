use itertools_num::ItertoolsNum;
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
        t: usize,
        n: usize,
    };
    let mut dr = vec![0; t + 3];
    for _ in 0..n {
        input!{
            il: usize, ir: usize,
        }
        dr[il + 1] += 1;
        dr[ir + 1] -= 1;
    }
    // dbg!(&dr);
    let sum_t: Vec<_> = dr.iter().cumsum::<i32>().collect();
    for st in &sum_t[1..t + 1] {
        println!("{}", st);
    }
    
}
