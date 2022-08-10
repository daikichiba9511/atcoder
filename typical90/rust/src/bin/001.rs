use proconio::input;

fn solve1() {
    input! {
        n: usize, l: usize,
        k: usize,
        a: [usize; n],
    }
    // 対応する羊羹の長さ
    let mut length = vec![0; n + 1];
    length[0] = a[0];
    for i in 1..n {
        length[i] = a[i] - a[i - 1]
    }
    length[n] = l - a[n - 1];

    // 最小値の最大化
    // 境界の判定=> 二分探索
    let mut left = 0;
    let mut right = l;
    let mut ans = 0;
    while left <= right {
        // 何個のブロックを選ぶか
        let mut count = 0;
        // この中点が条件の境界かを探索
        let mid = (left + right) / 2;
        let mut num = 0;
        for i in 0..n + 1 {
            // 選んだ長さが探してる境界よりも小さければnumに長さを足して次にいく
            // 境界よりも大きければその境界を
            if num < mid {
                num += length[i];
            } else {
                count += 1;
                num = length[i]
            }
        }
        if num >= mid {
            count += 1
        }

        // 選んだ境界がk個より多ければ左
        if count > k {
            left = mid + 1;
            ans = mid;
        } else {
            right = mid - 1;
        }
    }
    println!("{}", ans);
}

fn solve2() {
    // n個の切れ目からk個を選ぶ
    input! {
        n: i32, l: i32,
        k: i32,
        a: [i32; n],
    }

    // initialize for binary search
    let mut ok = 0; // 条件を満たす
    let mut ng = l; // 条件を満たさない

    // 2分探索
    // O(NlogL)
    while (ok - ng).abs() > 1 {
        // 探してる境界
        // 座標じゃなくて長さ
        let mid = (ok + ng) / 2;

        let mut cut_cnt = 0; // 選んだ切れ目
        let mut prev = 0; // 前の切れ目の保存

        for &a_i in a.iter() {
            // 左端の切り込みから探索してく
            // 境界よりも長さが大きかったら切り込み入れる
            // a_i - prev: 左隣の切り込みからa_iまでの長さ
            // L - a_i: 右端からa_iまでの長さ
            // l - a_iは残り部分、これがmidよりも大きければきれる
            if a_i - prev >= mid && l - a_i >= mid {
                prev = a_i;
                cut_cnt += 1;
            }
        }

        // 答えはk個以上か？
        // k個より多くcutできた
        // <=> midは探してる値より小さかった
        // <=> ok = mid
        if cut_cnt >= k {
            ok = mid;
        } else {
            ng = mid
        }
    }
    println!("{}", ok)
}

fn main() {
    solve2()
}
