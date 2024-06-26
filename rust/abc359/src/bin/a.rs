use proconio::{fastout, input, marker};

#[fastout]
fn main() {
    input! {
        n:i32,
        s:[String; n],
    };
    let mut cnt = 0;
    for s_i in &s {
        if s_i == "Takahashi" {
            cnt += 1;
        }
    }
    println!("{}", cnt)
}
