use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a: i32, b: i32,
        c: i32, d: i32,
    }
    let mut max_diff = -201;
    for x in a..=b {
        for y in c..=d {
            let diff = x - y;
            if diff > max_diff {
                max_diff = diff;
            }

        }
    }
    println!("{}", max_diff)
}
