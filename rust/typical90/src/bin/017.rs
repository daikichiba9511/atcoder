use proconio::{fastout, input};

/// 累積和をO(logN)
struct BIT {
    size: isize,
    bit: Vec<i64>,
}

impl BIT {
    fn new(sz: isize) -> Self {
        BIT {
            size: sz + 2,
            bit: vec![0; sz as usize + 4],
        }
    }

    /// a_posにxを加算する
    fn add(&mut self, mut pos: isize, x: i64) {
        pos += 1;
        while pos <= self.size {
            self.bit[pos as usize] += x;
            pos += pos & -pos;
        }
    }

    /// 区間和を計算する \sum_{i=0}^{pos} a_i
    fn sum(&self, mut pos: isize) -> i64 {
        let mut s = 0;
        pos += 1;
        while pos >= 1 {
            s += self.bit[pos as usize];
            pos -= pos & -pos;
        }
        s
    }
}

#[fastout]
fn main() {
    input! {n: usize, m: usize, mut lr: [(usize, usize); m]};

    let mut L = vec![0; 300_010];
    let mut R = vec![0; 300_010];
    for i in 1..=m {
        let (l, r) = lr[i - 1];
        L[i] = l;
        R[i] = r;
    }
    // -- Ans1
    // Ls,Lt,Rs,Rtの中に同じものがある、端点が交わるようなパターンの場合の数
    // 点iを選んだ時に点iで２つの線分が交わってると考える
    // 点iにつながってる線分n個から２つ選ぶ->nC2 = n(n-1)/2
    let mut v3 = vec![0; 300_010];
    // preprocess that counts lines at the point i.
    for i in 1..=m {
        v3[R[i]] += 1;
        v3[L[i]] += 1;
    }
    let mut ans1 = 0;
    for &cnt_i in v3.iter().take(n) {
        ans1 += cnt_i as i64 * (cnt_i as i64 - 1) / 2;
    }
    // println!("{:?}", ans1);

    // -- Ans2
    // R_s < L_t
    let mut num_r = vec![0; 300_010];
    let mut num_l = vec![0; 300_010];
    for i in 1..=m {
        num_r[R[i]] += 1;
        num_l[L[i] - 1] += 1;
    }

    // i番目の点までの点Rの個数（累積和）
    for i in 1..=n {
        num_r[i] += num_r[i - 1];
    }

    // v2は点iにおいてLが何個ついてるか
    // i番目の点を考えたときに、この点についてるLの個数と
    // R_s < L_tを満たすようなRの個数をかけるとiにおけるR_s < L_tを満たす数が求めれる
    let mut ans2 = 0;
    for i in 1..=n {
        ans2 += num_r[i] * num_l[i];
    }

    // println!("{:?}", ans2);
    // lr := [(L_1, R_1),(L_2, R_2), ..., (L_n, R_n)]
    // sort by R_i
    let mut v = vec![];
    for i in 1..=m {
        v.push((R[i], L[i]))
    }
    v.sort_by(|a, b| a.0.cmp(&b.0));

    // -- Ans3
    // ２つの区間[L_s, R_s],[L_t,R_t]
    // について、片方の区間がもう一方を完全に含むパターンの場合の数を求める
    // 注目してる
    let mut ans3 = 0;
    let mut bit = BIT::new(n as isize + 2);
    for &(r, l) in &v {
        // \sum_{i=1}^{r} a_i - \sum_{i=1}^{l} a_i
        // a_i := 点iにおけるLの数
        // 線分sの点RまでのLの数から点LまでのLの数を引くと解説で黄色の線分の数を求められる
        ans3 += bit.sum(r as isize) - bit.sum(l as isize);
        // a_l に 1を足す
        bit.add(l as isize, 1);
    }

    // println!("{:?}", ans3);
    let total = m as i64 * (m as i64 - 1) / 2;
    let sum_ans = ans1 + ans2 + ans3;
    println!("{}", total - sum_ans);
}
