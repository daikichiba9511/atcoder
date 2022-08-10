use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {h: usize, w: usize}
    println!(
        "{}",
        if h == 1 || w == 1 {
            h * w // 仮定部分の2x2が全体に含まれる時が成り立たないから
        } else {
            ((h + 1) / 2) * ((w + 1) / 2)
        }
    )
}
