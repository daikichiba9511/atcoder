use num::integer::gcd;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {a: usize, b: usize, c: usize}
    let r = gcd(a, gcd(b, c));
    let ans = (a / r - 1) + (b / r - 1) + (c / r - 1);
    println!("{}", ans);
}
