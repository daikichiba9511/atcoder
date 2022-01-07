//! 辞書順最小の部分文字列なのでaにちかい単語からK個取って並べたものが最適解
//! 普通にN文字のSを一文字ずつ見て一番近いものを取っていくのだとO(NK)?
//! 10^10では間に合わない
//!
//! 参考：
//! [1] https://atcoder.jp/contests/typical90/submissions/28303594
//! [2] https://qiita.com/hatoo@github/items/fa14ad36a1b568d14f3e#%E9%80%86%E9%A0%86%E3%81%A7%E3%80%87%E3%80%87%E3%81%99%E3%82%8B%E3%81%AB%E3%81%AF
use proconio::input;
use std::{cmp::Reverse, collections::BinaryHeap};

fn main() {
    input! {
        n: usize, k: usize,
        s: String,
    }
    // BinaryHeapは大きい順でpopされてくる
    // それをReverseを噛ませることで小さい方からでてくる
    let mut heap = BinaryHeap::new();
    let mut next = 0;
    let mut ans = String::new();

    for (i, c) in s.chars().enumerate() {
        // 辞書順で昇順にソートされてる
        heap.push(Reverse((c, i)));
        // 残りがk以上ないとそもそもk文字の部分文字列を作れない
        if n <= i + k {
            loop {
                let Reverse((d, j)) = heap.pop().unwrap();
                // nextには次回の文字列の開始位置が入ってる
                if next <= j {
                    next = j + 1;
                    ans.push(d);
                    break;
                }
            }
        }
    }
    println!("{}", ans);
}
