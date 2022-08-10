use proconio::{fastout, input};
use std::collections::BinaryHeap;
use std::cmp::Reverse;

// FIX: たぶんどっかの境界条件間違えてる

fn dijkstra(start: usize, n: usize, graph: &Vec<Vec<(usize, usize)>>) -> Vec<usize> {
    let mut queue = BinaryHeap::new();
    // initialize
    let mut dist = vec![0; n + 1];
    for i in 0..n {
        dist[i] = 1 << 29 as usize;
    }
    dist[start] = 0;
    // (cost, to)
    // 最小ヒープにするのにReverseする
    queue.push((Reverse(0), start));

    while !queue.is_empty() {
        let position = queue.pop().unwrap().1;
        for i in 0..graph[position].len() {
            let to = graph[position][i].0;
            let cost = graph[position][i].1;
            // println!("to => {}, cost => {}", to, cost);
            if dist[to] > dist[position] + cost {
                dist[to] = dist[position] + cost;
                queue.push((Reverse(dist[to]), to));
            }
        }
    }
    dist
}


#[fastout]
fn solve() {
    input! {
        n: usize, m: usize,
        abc: [(usize, usize, usize); m]
    }
    let mut graph: Vec<Vec<(usize, usize)>> = vec![vec![]; n];
    for (a, b, c) in abc {
        graph[a - 1].push((b - 1, c));
        graph[b - 1].push((a - 1, c));
    }
    // 頂点１からの最短距離を求める
    let dist_1 = dijkstra(0, n, &graph);

    // 頂点Nからの最短距離を求める
    let dist_n = dijkstra(n - 1, n, &graph);

    for i in 0..n {
        println!("{}", dist_1[i] + dist_n[i]);
    }

}
fn main() {
    solve()
}
