#[allow(unused_imports)]
use num::integer::gcd;
use proconio::marker::Chars;
#[allow(unused_imports)]
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

/// Calculate the next appearance indexes for each character from the tail.
///
/// This function computes the minimum indexes for the first appearance of each character
/// in the string `s` when traversing from the tail.
///
/// # Arguments
///
/// * `s` - A vector of characters.
///
/// # Returns
///
/// * A 2D vector of `i32`, where `res[i][j]` represents the next index of the character
///   corresponding to `j` (relative to `'a'`) after index `i`. If the character does not
///   appear, the value is set to `s.len()`.
fn calc_next_appearance_indexes(s: Vec<char>) -> Vec<Vec<i32>> {
    let n = s.len();
    let mut res = vec![vec![n as i32; 26]; n + 1];
    // make minimum index from tail
    for i in (0..n).rev() {
        // copy results of later j+1 into j
        for j in 0..26 {
            res[i][j] = res[i + 1][j];
        }
        // update index of s[i]
        let idx_char = s[i] as u8 - b'a';
        res[i][idx_char as usize] = i as i32;
    }
    res
}

#[fastout]
fn main() {
    input! {
        n: usize,
        k: usize,
        s: Chars,
    }
    // Preprocess: calculate the next appearance indexes for each character from
    let mut res = vec![];
    let nex = calc_next_appearance_indexes(s);
    // Greedy algorithm: choose the character with the smallest index.
    let mut j = -1;
    for i in 0..k {
        for ordc in 0..26 {
            let k_i = nex[(j + 1) as usize][ordc];
            // If I can make a string of length k, it's fine.
            if n as i32 - k_i >= k as i32 - i as i32 {
                res.push((ordc as u8 + b'a') as char);
                j = k_i;
                break;
            }
        }
    }
    println!("{}", res.iter().collect::<String>());
}
