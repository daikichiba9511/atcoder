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
    for (i, t) in t {
        heap.push((Reverse(t), i));
    }

    // O(nlogn)
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
