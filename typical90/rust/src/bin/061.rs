use proconio::{fastout, input};
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {q: usize, tx: [(usize, usize); q]}
    let mut que = VecDeque::new();
    for (t, x) in tx {
        if t == 1 {
            que.push_front(x);
            continue;
        }
        if t == 2 {
            que.push_back(x);
            continue;
        }
        if let Some(&ans) = que.get(x - 1) {
            println!("{}", ans);
        }
    }
}
