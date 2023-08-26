use proconio::input;
use std::collections::BinaryHeap;

fn dijkstra(adj_list: Vec<Vec<(usize, i32)>>, start: usize, goal: usize) -> Option<Vec<i32>> {
    let mut dist = vec![std::i32::MAX; adj_list.len()];
    let mut heap = BinaryHeap::new();
    dist[start] = 0;
    heap.push((0, start));

    while let Some((cost, u)) = heap.pop() {
        if u == goal {
            return Some(dist);
        }

        if dist[u] < cost {
            // すでに最短経路が確定している
            continue;
        }
        for &(v, c) in &adj_list[u] {
            if dist[v] > dist[u] + c {
                // 最短経路が更新できる
                dist[v] = dist[u] + c;
                heap.push((dist[v], v));
            }
        }
    }
    None
}

fn main() {
    input! {
        n: usize,
        s: [i32; n],
        t: [i32; n],
    }

    // dbg!("{:?}", &s);
    // dbg!("{:?}", t);

    // ダイクストラ法で解く
    let mut adj_list = vec![vec![]; n + 1];

    // Tから全頂点への辺を張る
    for i in 0..n {
        adj_list[0].push((i + 1, t[i]));
    }

    // T以外の頂点から、その頂点以外の頂点への辺を張る
    for i in 0..n {
        adj_list[i + 1].push(((i + 2) % n, s[i]));
    }

    dbg!(&adj_list);
    dbg!(&adj_list.len());

    for i in 0..n {
        dbg!(i);
        let dist = dijkstra(adj_list.clone(), 0, i + 1).unwrap();
        println!("{:?}", &dist);
        println!("{}", dist[i]);
    }
}
