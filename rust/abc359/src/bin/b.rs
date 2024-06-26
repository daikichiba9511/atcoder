use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: i32,
        a: [i32; 2 * n],
    };
    let mut cnt = 0;
    for i in 0..(a.len() - 2) {
        if a[i] == a[i + 2] {
            cnt += 1;
        }
    }
    println!("{}", cnt);
}
