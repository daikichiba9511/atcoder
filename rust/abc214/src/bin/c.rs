use itertools::Itertools;
use proconio::input;
use std::{cmp::Reverse, collections::BinaryHeap};

fn main() {
    input! {
        n: usize,
        s: [i32; n],
        t: [i32; n],
    }

    // dbg!("{:?}", &s);
    // dbg!("{:?}", t);

    let mut dist = vec![std::i32::MAX; n + 1];
    let mut heap = BinaryHeap::new();
    let t = t.into_iter().enumerate().collect_vec();
    // 始点から各頂点へのコストを足す O(N)
    for (i, t) in t {
        heap.push((Reverse(t), i));
    }

    // 始点から一番コストの低い点へ始める = Reverseを使って最小値をpopする
    // コストの最小値はlog|V|で取り出せる
    // 更新の回数は辺の数だけ発生する
    // -> O(|E| log|V| )
    while let Some((Reverse(cost), v)) = heap.pop() {
        // すでに決まってる値が小さいなら更新しない
        if dist[v] <= cost {
            continue;
        }

        // 更新できる
        dist[v] = cost;
        // 次の点には最小コスト+s[v]で行ける
        heap.push((Reverse(cost + s[v]), (v + 1) % n));
    }

    for i in 0..n {
        println!("{}", dist[i]);
    }
}
