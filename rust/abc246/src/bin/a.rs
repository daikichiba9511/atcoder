use std::collections::HashMap;
use proconio::{input, fastout};

#[allow(dead_code)]
fn value_counts(x: &Vec<i64>) -> HashMap<i64, i64> {
    let mut m: HashMap<i64, i64> = HashMap::new();
    for &v in x {
        *m.entry(v).or_default() += 1;
    }
    m
}

#[allow(dead_code)]
fn find_lack_value(m: &HashMap<i64, i64>) -> i64 {
    let mut res: i64 = -1;
    for (k, v) in m.iter() {
        if *v == 1 {
            res = *k;
        }
    }
    res
}

#[fastout]
fn solve() {
    input! {
        x1: i64, y1: i64,
        x2: i64, y2: i64,
        x3: i64, y3: i64,
    }
    
    let x = vec![x1, x2, x3];
    let y = vec![y1, y2, y3];

    let x_cnt = value_counts(&x);
    let y_cnt = value_counts(&y);

    let x_res = find_lack_value(&x_cnt);
    let y_res = find_lack_value(&y_cnt);
    println!("{} {}", x_res, y_res)


}

#[fastout]
fn solve2() {
    input! {
        x1: i64, y1: i64,
        x2: i64, y2: i64,
        x3: i64, y3: i64,
    }

    // ^: Bitwise XOR
    // ２つ同じ数ならXORで0、違う箇所で1が立つ
    // https://doc.rust-lang.org/reference/expressions/operator-expr.html
    let x = x1 ^ x2 ^ x3;
    let y = y1 ^ y2 ^ y3;
    println!("{} {}", x, y)
}

fn main() {
    // solve();
    solve2();
}
