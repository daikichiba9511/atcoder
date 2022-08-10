use proconio::{input, marker::Chars};

fn main() {
    // 長さNの文字列S、長さがKのSの部分列
    input! {
        n: usize,
        k: usize,
        s: Chars,
    }

    // shape: (26, n+1)
    let mut dp: Vec<Vec<i32>> = vec![vec![-1; 26]; n + 1];

    // tableを初期化
    for i in (0..n).rev() {
        for j in 0..26 {
            dp[i][j] = dp[i + 1][j]
        }
        // 文字をu8でencode
        // i番目の文字列からaまでの距離をu8で計算する
        // j: aからs_iまでどれくらいの距離か
        let j = s[i] as u8 - b'a' as u8;
        dp[i][j as usize] = i as i32;
    }

    let mut ans: Vec<char> = Vec::new();
    let mut current_pos: usize = 0;

    while ans.len() < k {
        // 辞書順に早い順から検討する <=> 'a'に最も近いやつ
        for j in 0..26 {
            // jはアルファベットを表す整数
            // jを採用したときに、残りの文字数でK文字以上にできるか
            let next_pos = dp[current_pos][j];
            if next_pos == -1 {
                continue;
            }
            // 残りの文字数(n-next_pos)が作るべき文字数(k-ans.len())より大きければ一文字追加して次の文字に
            if n as i32 - next_pos >= k as i32 - ans.len() as i32 {
                // char::from(j as u8 + b'a' as u8):
                // b'a'から連番でどの文字列かをu8で指定して文字列に変換して文字列作ってる
                // e.g.) char::from(1 as u8 + b'a' as u8) => 'b'
                ans.push(char::from(j as u8 + b'a' as u8));
                current_pos = next_pos as usize + 1;
                break;
            }
        }
    }
    // ans.iter()は配列→スライスに変換
    println!("{}", ans.iter().collect::<String>());
}
