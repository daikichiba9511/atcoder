use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        x: String
    };

    let mut v = vec![];
    for c in x.chars() {
        if c == '.' {
            break
        } else {
            v.push(c);
        }
    }
    println!("{}", v.into_iter().collect::<String>());

}
