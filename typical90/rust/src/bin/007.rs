use proconio::{fastout, input};
use superslice::*;

#[fastout]
fn main() {
    input! {
        n: usize,
        mut a: [i32; n],
        q: usize,
        b: [i32; q]
    }
    // u32だとl31でパニックする
    // println!("{:?}, {:?}, {:?}, {:?}", b, a, q, b)
    // 愚直にやったらO(nq)=10^10
    // rustのsortはmerge sortらしい
    a.sort();
    for b_i in b {
        // supersliceでlower_boundを使えるようになる
        // &b_i以上の要素のなかで最小の要素のindex
        let i = a.lower_bound(&b_i);
        // i = 0 のときはaの全要素がb_iよりおおきいのでいちばん近い要素の上限はa[0]
        if i == 0 {
            let a1 = (a[0] - b_i).abs();
            println!("{}", a1);
            continue;
        }
        // i >= n のときはaの全要素がb_iよりちいさいので上限はなくて一番近い要素はa[n-1]
        if i >= n {
            let a2 = (a[n - 1] - b_i).abs();
            println!("{}", a2);
            continue;
        }
        let a1 = (a[i] - b_i).abs();
        let a2 = (a[i - 1] - b_i).abs();
        let ans = a1.min(a2);
        println!("{}", ans)
    }
}
