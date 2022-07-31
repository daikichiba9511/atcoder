use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        n: usize,
        cp: [(usize, i32); n],
        q: usize,
        lr: [(usize, usize); q],
    }

    // 区間の累積和を取る
    let mut sum_1 = vec![0];
    let mut sum_2 = vec![0];
    for i in 1..n+1 {
        if cp[i - 1].0 == 1 {
            sum_1.push(sum_1[i - 1] + cp[i - 1].1);
            sum_2.push(sum_2[i - 1]);
        } else {
            sum_1.push(sum_1[i - 1]);
            sum_2.push(sum_2[i - 1] + cp[i - 1].1);
        }
    }

    for (l, r) in lr {
        println!("{} {}", sum_1[r] - sum_1[l -1], sum_2[r] - sum_2[l - 1]);
    }
}
