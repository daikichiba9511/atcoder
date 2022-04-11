use proconio::{input, fastout};


#[fastout]
fn solve() {
    input! {
        s: String,
    };
    
    let s: Vec<char> = s.chars().collect();
    let mut res = String::from("0");
    for v in 1..s.len() {
        let c = s[v - 1];
        if c == '1' {
            res.push('1');
        } else {
            res.push('0');
        }
    }
    println!("{}", res);
}

fn main() {
    solve()
}
