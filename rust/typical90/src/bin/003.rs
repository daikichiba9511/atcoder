use proconio::{input, marker::Usize1};
use std::collections::VecDeque;

/// 幅優先探索（BFS）によって最短距離を計算
///
/// * `n` - 都市の数
/// * `g` - 隣接リスト
/// * `s` - スタート地点
fn getdist(n: usize, g: &[Vec<usize>], s: usize) -> Vec<i64> {
    let mut dist = vec![-1; n];
    let mut que = VecDeque::with_capacity(n);
    que.push_back(s);
    dist[s] = 0;
    while let Some(u) = que.pop_front() {
        for &v in &g[u] {
            if dist[v] < 0 {
                dist[v] = dist[u] + 1;
                que.push_back(v);
            }
        }
    }
    dist
}

// Usize1: 読み込み方を支持する為の型. valueはusizeとして読み込まれる
// Ref: https://docs.rs/proconio/latest/proconio/
fn main() {
    input! {
        n: usize,
        edges: [(Usize1, Usize1); n - 1],
    }
    let mut g = vec![vec![]; n];
    for &(a, b) in &edges {
        g[a].push(b);
        g[b].push(a);
    }

    let dist = getdist(n, &g, 0);

    let mut s = 0;
    for i in 0..n {
        if dist[s] < dist[i] {
            s = i
        }
    }

    let dist = getdist(n, &g, s);
    let ans = dist.iter().max().unwrap() + 1;
    println!("{}", ans);
}
