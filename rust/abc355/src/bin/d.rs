use proconio::{fastout, input};
#[fastout]
fn main() {
    input! {
        n: usize,
        mut lr: [[usize; 2]; n]
    }
    let mut l = lr.iter().map(|x| x[0]).collect::<Vec<usize>>();
    l.sort();
    let mut r = lr.iter().map(|x| x[1]).collect::<Vec<usize>>();
    r.sort();
    // println!("l={:?} r={:?}", &l, &r);
    let mut ans = n * (n - 1) / 2;
    let mut j = 0;
    // 尺取り法
    // 左端のiを固定して場合わけして考える
    for i in 0..n {
        // 右端のf(left)を求める
        // 交差しないパターンのギリギリまで右端をインクリメントする
        while r[j] < l[i] {
            j += 1;
        }
        // 上で求めた個数は交差しないパターンの数に等しいので、組み合わせの総数から引く
        ans -= j;
    }
    println!("{}", ans);
}
