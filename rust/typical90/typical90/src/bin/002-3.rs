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
fn is_correct(s: &str) -> bool {
    let mut dep = 0;
    for c in s.chars() {
        if c == '(' {
            dep += 1;
        } else {
            dep -= 1;
        }
        if dep < 0 {
            return false;
        }
    }
    dep == 0
}
#[fastout]
fn main() {
    input! {
        n: u32,
    }
    // if n is odd, there is no answer
    if n % 2 == 1 {
        return;
    } else {
        // make right bracket row using stack
        for i_n in 0..(1 << n) {
            let s = format!("{:0n$b}", i_n, n = n as usize);
            let candidate = s
                .chars()
                .map(|c| if c == '0' { '(' } else { ')' })
                .collect::<String>();
            let is_correct_candidate = is_correct(&candidate);
            if is_correct_candidate {
                println!("{}", candidate);
            }
        }
    }
}
