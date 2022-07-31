use proconio::{fastout, input};

/// 累積和をO(logN)
struct BIT {
    size: isize,
    bit: Vec<i64>,
}

impl BIT {
    fn new(size: isize) -> Self {
        BIT {
            size: size + 2,
            bit: vec![0; size as usize + 2],
        }
    }

    fn add(&mut self, pos: isize, x: i64) {
        let mut pos = pos + 1;
        while pos <= self.size {
            self.bit[pos as usize] += x;
            pos += pos & -pos;
        }
    }

    fn sum(&self, pos: isize) -> i64 {
        let mut s = 0;
        let mut pos = pos + 1;
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

    // Ans1
    // Ls,Lt,Rs,Rtの中に同じものがある、端点が交わるようなパターンの場合の数
    // 点iを選んだ時に点iで２つの線分が交わってると考える
    // 点iにつながってる線分n個から２つ選ぶ->nC2 = n(n-1)/2
    let mut v3 = vec![0; 300_000];
    for i in 0..m {
        v3[lr[i].0] += 1;
        v3[lr[i].1] += 1;
    }
    let mut ans1 = 0;
    for cnt_i in v3.iter().take(n) {
        ans1 += cnt_i * (cnt_i - 1) / 2;
    }
    println!("{:?}", ans1);

    // ans2
    let mut ans2 = 0;
    let mut v1 = vec![0; 300_000];
    let mut v2 = vec![0; 300_000];
    for i in 0..m {
        v1[lr[i].1] += 1;
        v2[lr[i].0] += 1;
        v1[i + 1] += v1[i];
        ans2 += v1[i] * v2[i];
    }

    println!("{:?}", ans2);
    // sorting
    lr.sort_by(|a, b| a.1.cmp(&b.1));
    // ans3
    let mut ans3 = 0;
    let mut bit = BIT::new(n as isize + 2);
    for &(l, r) in &lr {
        let ret = bit.sum(r as isize) - bit.sum(l as isize);
        ans3 += ret;
        bit.add(l as isize, 1);
    }

    println!("{:?}", ans3);
    let total = m as i64 * (m as i64 - 1) / 2;
    let sum_ans = ans1 + ans2 + ans3;
    println!("{}", total - sum_ans);
}
