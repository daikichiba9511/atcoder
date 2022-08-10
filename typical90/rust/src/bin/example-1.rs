//! 参考：https://qiita.com/murai_mart/items/1a7a4d10abc0c3b5b53f
//! 0以上n以下の整数の個数
use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let s: Vec<char> = s.chars().collect();
    let digit = s.len();
    // println!("{:?}", s);

    // initialize dp table
    // dp[i][j] i: 頭からi桁目、j：未満フラグ（０ならn未満であることが確定してる）
    let mut dp = vec![vec![0; 2]; digit];

    // asciiコード'0'(=48)をひく
    let x0 = s[0] as usize - '0' as usize;
    dp[0][0] = x0; // 先頭の桁が0~(x0-1)のx0個なら未満フラグは０
    dp[0][1] = 1; // 先頭の桁がx0なら未満フラグは1

    for i in 1..digit {
        // i桁目を取り出す
        let x = s[i] as usize - '0' as usize;
        // println!("{}", x);

        // 頭からi桁目まででn未満が確定済み
        // 1項目：i-1桁まででn未満であることが確定済みなのでi桁目は0~9のどれでもいい
        // 2項目：i-1桁までnと一致しているのでi桁目はxを選べばi桁目までnと一致する
        dp[i][0] = dp[i - 1][0] * 10 + dp[i - 1][1] * x;

        // 頭からi桁目までnと一致してる
        // 1項目：i-1桁目までn未満であることが確定しているのでi桁目までをnと一致させるのはどれを選んでも不可能
        // 2項目：i-1桁目までnと一致してるのであれば、i桁目はxを選べばi桁目までnと一致する
        dp[i][1] = dp[i - 1][0] * 0 + dp[i - 1][1] * 1;
    }
    // 求めたいのは0以上n以下の整数の個数
    // dp[digit - 1][0]：先頭からn桁でn未満であることが確定してる個数。すなわち０以上n未満の整数の個数(n-1 - 0 + 1 = n)
    // dp[digit - 0][1]：全ての桁がnと一致してる数の個数(=1)
    println!("{}", dp[digit - 1][0] + dp[digit - 1][1]);
}
