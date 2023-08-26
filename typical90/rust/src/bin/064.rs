#[allow(dead_code)]
fn solve() {
    proconio::input! {
        nq: (usize, usize),
        mut a: [i64; nq.0],
        lrv: [(usize, usize, i64); nq.1],
    };

    // dbg!("{:?}, {:?}, {:?}", &nq, &a, &lrv);

    // O(QN) = 10^5 * 10^5 = 10^10
    for (l, r, v) in &lrv {
        // O(N)
        for i in *l..=*r {
            a[i - 1] += *v as i64;
        }

        // 不便さを求める
        // O(N)
        let mut ans = 0;
        for i in 0..nq.0 - 1 {
            ans += a[i + 1] - a[i]
        }
        println!("{}", ans);
    }
}

fn solve2() {
    proconio::input! {
        nq: (usize, usize),
        mut a: [i64; nq.0],
        lrv: [(usize, usize, i64); nq.1],
    }

    // 階差数列を求める
    // 端を0で埋めておくとl=1|r=nの時に楽
    // bは階差数列なので隣り合う区間の変化量に差が合った時に実際に変化がでる
    // [l, r]のときにはb[l-1]とb[r]にvを足し引きする
    // 0-originに直してかんがえた時にl=0の時は何もしないことになるので0埋めにしておくと楽
    let mut b = vec![0; nq.0 + 1];
    for i in 0..nq.0 - 1 {
        b[i + 1] = a[i + 1] - a[i];
    }

    dbg!("{:?}", &b);

    let mut ans: i64 = b.iter().map(|x| x.abs()).sum();

    // O(Q)
    for (l, r, v) in &lrv {
        // 変化があるところだけ計算する
        let previous = b[l - 1].abs() + b[*r].abs();
        if *l > 1 {
            b[l - 1] += v;
        }
        if *r <= nq.0 - 1 {
            b[*r] -= v;
        }
        let after = b[l - 1].abs() + b[*r].abs();
        ans += after - previous;
        println!("{}", ans);
    }
}

fn main() {
    // solve();
    solve2();
}
