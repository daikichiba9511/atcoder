#[allow(unused_imports)]
use num::integer::gcd;
use proconio::{fastout, input};

// =============================================
// Library
// =============================================
#[allow(unused_macros)]
macro_rules! chmin {
    ($base:expr, $($cmps:expr),+ $(,)*) => {{
        let cmp_min = min!($($cmps),+);
        if $base > cmp_min {
            $base = cmp_min;
            true
        } else {
            false
        }
    }};
}

#[allow(unused_macros)]
macro_rules! chmax {
    ($base:expr, $($cmps:expr),+ $(,)*) => {{
        let cmp_max = max!($($cmps),+);
        if $base < cmp_max {
            $base = cmp_max;
            true
        } else {
            false
        }
    }};
}

#[allow(unused_macros)]
macro_rules! min {
    ($a:expr $(,)*) => {{
        $a
    }};
    ($a:expr, $b:expr $(,)*) => {{
        std::cmp::min($a, $b)
    }};
    ($a:expr, $($rest:expr),+ $(,)*) => {{
        std::cmp::min($a, min!($($rest),+))
    }};
}

#[allow(unused_macros)]
macro_rules! max {
    ($a:expr $(,)*) => {{
        $a
    }};
    ($a:expr, $b:expr $(,)*) => {{
        std::cmp::max($a, $b)
    }};
    ($a:expr, $($rest:expr),+ $(,)*) => {{
        std::cmp::max($a, max!($($rest),+))
    }};
}

#[allow(dead_code)]
const INF: i32 = 100_000_000;

#[fastout]
fn main() {
    // サイクルがあるか、ある場合はその最大長を求める問題
    // N頂点N-1辺の連結なグラフ=木構造
    // 単純なパスの長さの最大値を求める問題が木の直径を求める問題に帰着する
    // 始点の全探索した上で、DFS/BFSだと始点の探索でO(N)、始点を定めた上でのDFS/BFSでO(N)なので、O(N^2)で解ける
    // しかし、これだとN<=100_000=10^5なので大体10^10回計算が必要なので間に合わない
    // なのでO(N)で木の直径を求めるアルゴリズムを使う
    // 1. 頂点1から頂点Nまでの最短距離を求める
    // 2. 最も距離が大きかった点をuとして、頂点uから最短距離を求める. この時もとまった最短距離が木の直径になる
    input! {
        n: usize,
        ab: [(usize, usize); n-1],
    }

    let mut graph = vec![vec![]; n];
    for (a, b) in ab {
        graph[a - 1].push(b - 1);
        graph[b - 1].push(a - 1);
    }

    // 頂点1からの各頂点への最短距離を求める
    let mut dist = vec![INF; n];
    let mut queue = std::collections::VecDeque::new();
    queue.push_back(0);
    dist[0] = 0;

    while let Some(v) = queue.pop_front() {
        for &next in &graph[v] {
            if dist[next] == INF {
                dist[next] = dist[v] + 1;
                queue.push_back(next);
            }
        }
    }

    let mut max_dist = 0;
    let mut max_dist_index = 0;
    for i in 0..n {
        if chmax!(max_dist, dist[i]) {
            max_dist_index = i;
        }
    }

    // 木の直径を求める
    let mut dist = vec![INF; n];
    let mut queue = std::collections::VecDeque::new();
    queue.push_back(max_dist_index);
    dist[0] = 0;
    while let Some(v) = queue.pop_front() {
        for &next in &graph[v] {
            if dist[next] == INF {
                dist[next] = dist[v] + 1;
                queue.push_back(next);
            }
        }
    }

    let mut max_dist = -1;
    for dist_i in dist {
        chmax!(max_dist, dist_i);
    }

    // 答えを出力
    println!("{}", max_dist + 1);
}
