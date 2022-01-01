use proconio::input;

fn solve(n: usize, m: usize, k: usize, l: usize, a: &[usize]) -> bool {
    // 左から順に調べていき、ブロックがm以上になったらカウントする
    let mut cnt = 0;
    let mut pre = 0;
    for i in 0..n {
        // a[i] - pre >= m: 前の切れ目からmを超えるとき
        // l - a[i] >= m: 最後の切れ目がmを超えてるとき
        if a[i as usize] - pre as usize >= m && l - a[i as usize] >= m {
            cnt += 1;
            pre = a[i];
        }
    }
    if cnt >= k {
        true
    } else {
        false
    }
}

fn main() {
    input! {
        n: usize, l: usize,
        k: usize,
        a: [usize; n],
    }
    // println!("{:?} {:?} {:?} {:?}", n, l, k, a);
    let mut left = 0;
    let mut right = l;
    while right - left > 1 {
        // mid:最大化したい最小値m
        let mid = left + (right - left) / 2;

        if solve(n, mid, k, l, &a) == false {
            right = mid;
        } else {
            left = mid;
        }
    }
    println!("{}", left);
}
