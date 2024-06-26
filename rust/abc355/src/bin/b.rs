use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n:i32,m:i32,
        a:[i32;n],
        b:[i32;m]
    }
    let mut c = Vec::from(a.clone());
    c.extend(b);
    c.sort();
    for i in 0..(c.len() - 1) {
        if a.contains(&c[i]) && a.contains(&c[i + 1]) {
            println!("Yes");
            return;
        }
    }
    println!("No")
}
