#[allow(unused_imports)]
use num::integer::gcd;
use proconio::marker::Chars;
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
        s: Chars
    };
    let mut stack = Vec::new();
    let mut ok = true;
    for s_i in s {
        if s_i == '(' || s_i == '[' || s_i == '<' {
            stack.push(s_i);
        } else {
            if stack.is_empty() {
                ok = false;
                break;
            }
            if let Some(tail) = Some(stack.pop()) {
                if (tail == Some('[') && s_i != ']')
                    || (tail == Some('(') && s_i != ')')
                    || (tail == Some('<') && s_i != '>')
                {
                    ok = false;
                    break;
                }
            }
        }
    }

    let ans = if ok && stack.is_empty() { "Yes" } else { "No" };
    println!("{}", ans);
}
