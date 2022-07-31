use proconio::{input, fastout};

#[allow(dead_code)]
fn solve1() {
    input! {
       n: usize,
       mut dcs: [(usize, usize, usize); n],
    }
    dcs.sort();

    let d_max = dcs.last().unwrap().0;
    let mut dp = vec![0; d_max + 1];
    // DP
    for (d, c, s) in dcs {
        for i in (0..=d_max).rev() {
            if c > i || d < i {
                continue;
            }
            dp[i] = dp[i].max(dp[i - c] + s);
        }
    }

    println!("{}", dp.iter().max().unwrap());
}

fn solve2() {
    input! {
       n: usize,
       mut dcs: [(usize, usize, usize); n],
    }
    // d(締切日)で昇順にソートする
    dcs.sort();
    
    let mut dp = vec![vec![0; 5009]; 5009];
    for i in 0..n - 1 {
        for j in 0..=5000 {
            let (d, c, s) = dcs[i + 1];
            // 仕事i+1をやらない場合
            dp[i + 1][j] = std::cmp::max(dp[i + 1][j], dp[i][j]);

            // 仕事i+1をやる場合
            if j + c <= d {
                dp[i + 1][j + c] = std::cmp::max(dp[i + 1][j + c], dp[i][j] + s);
            }
        }
    }
    let mut ans = 0;
    for i in 0..=5000 {
        ans = std::cmp::max(ans, dp[n - 1][i]);
    }
    println!("{}", ans);
}


#[fastout]
fn main() {
    solve2()
}
