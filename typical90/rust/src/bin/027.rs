use proconio::{fastout, input};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {n: usize, s: [String; n]};
    let mut map = HashMap::new();
    for (idx, s_i) in s.iter().enumerate() {
        if map.contains_key(s_i) {
            continue;
        }
        println!("{}", idx + 1);
        map.insert(s_i, 1);
    }
}
