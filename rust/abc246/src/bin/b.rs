use proconio::{input, fastout};

#[fastout]
fn solve() {
    input! {
        (a, b): (i64, i64)
    }
    let xy = a.pow(2) + b.pow(2);
    let xy = (xy as f64).sqrt();
}

fn main() {
    solve()
}
