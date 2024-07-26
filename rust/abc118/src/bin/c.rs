#[allow(unused_imports)]
use num::integer::gcd;
#[allow(unused_imports)]
use num_traits::{One, Signed, Zero};
#[allow(unused_imports)]
use proconio::{fastout, input};
#[allow(unused_imports)]
use std::cmp::{PartialEq, PartialOrd};
#[allow(unused_imports)]
use std::ops::{Add, Div, Mul, Rem, Sub};

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

/// 拡張ユークリッド法
///
/// ax + by = GCD(a, b)を満たす(x,y)を求める
///
/// @tparam T 整数型を取れるように
/// # Parameters
///
/// - `a`: 整数
/// - `b`: 整数
/// - `x`: 求めたい整数
/// - `y`: 求めたい整数
///
/// # Return
///
/// 最大公約数
///
/// # Example
///
/// ```
/// let a = 56;
/// let b = 15;
/// let mut x = 0;
/// let mut y = 0;
/// let gcd = ext_gcd(a, b, &mut x, &mut y);
/// println!("GCD of {} and {} is {}", a, b, gcd);
/// println!("x = {}, y = {}", x, y);
/// ```
fn ext_gcd<T>(a: T, b: T, x: &mut T, y: &mut T) -> T
where
    T: Add<Output = T>
        + Sub<Output = T>
        + Mul<Output = T>
        + Sub<Output = T>
        + PartialEq
        + PartialOrd
        + Zero
        + One
        + Copy
        + Signed,
{
    if b == T::zero() {
        *x = T::one();
        *y = T::zero();
        return a;
    } else {
        let mut x1 = T::zero();
        let mut y1 = T::zero();
        let d = ext_gcd(b, a % b, &mut x1, &mut y1);
        *x = y1;
        *y = x1 - (a / b) * y1;
        return d;
    }
}

// =============================================
// Main
// =============================================
#[fastout]
fn main() {
    // input! {
    //     n: usize,
    //     a: [i32; n],
    // };
    // let mut ans = 0;
    // for i in 0..n {
    //     ans = gcd(ans, a[i])
    // }
    // println!("{}", ans);
    let a = 56;
    let b = 15;
    let mut x = 0;
    let mut y = 0;
    let gcd = ext_gcd(a, b, &mut x, &mut y);
    println!("GCD of {} and {} is {}", a, b, gcd);
    println!("x = {}, y = {}", x, y);
}
