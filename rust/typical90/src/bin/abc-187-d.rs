use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        n: usize,
    }
    
    let mut x = 0;
    let mut voter = Vec::new();
    for _ in 0..n {
        input! {
            a: i64, b: i64,
        }
        x -= a;
        voter.push(2 * a + b);
    }

    voter.sort();

    let mut ans = 0;
    while x <= 0 {
        x += voter.pop().unwrap();
        ans += 1;
    }
    println!("{}", ans);
}
