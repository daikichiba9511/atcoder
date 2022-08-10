use proconio::{fastout, input};

#[fastout]
fn main() {
    let moduler = 1_000_000_007;
    input! {
        n: usize,
        s: String,
    }

    let target = "atcoder";
    // println!("{:?}", target);

    // dp[i][j] := i番目の文字列でatcoderの文字が何文字目まで選んでるか
    let mut dp = vec![vec![0; 8]; n + 1];
    for i in 0..=n {
        dp[i][0] = 1;
    }
    for (i, c) in s.chars().enumerate() {
        for (j, d) in target.chars().enumerate() {
            // 単語をえらばないパターン
            dp[i + 1][j + 1] += dp[i][j + 1];
            // 単語をえらぶパターン
            // atcoderのどの単語かだったら選ぶ
            if c == d {
                // println!("choiced !! {}", c);
                // modulerの世界での加算
                dp[i + 1][j + 1] += dp[i][j];
                dp[i + 1][j + 1] %= moduler;
            }
        }
    }
    println!("{:?}", dp[n][7]);
}
