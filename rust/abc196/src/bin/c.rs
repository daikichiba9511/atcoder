#[allow(dead_code)]
use proconio::{input, fastout};

fn solve1() {
    input! {
        n: u64,
    };
    
    let res = (1..1_000_000)
        .filter(|&i| {
            let m: u64 = format!("{0}{0}", i).as_str().parse().unwrap();
            m <= n
        })
        .count();
    println!("{}", res);

}


// Ref: https://atcoder.jp/contests/abc196/submissions/21606266
fn solve2() {
    input! { n: u64 }
    let mut ans = 0;
    let mut p = 10;
    for _ in 0..6 {
        for x in p / 10..p {
            if x * (1 + p) <= n {
                ans += 1;
            }
        }
        p *= 10;
    }
    println!("{}", ans);
}

#[fastout]
fn main() {
    // solve1();
    solve2()
}
