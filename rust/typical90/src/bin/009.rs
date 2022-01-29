use proconio::{fastout, input};

fn is_ok(arr: &mut [f64], idx: isize, key: f64) -> bool {
    if arr[idx as usize] >= key {
        true
    } else {
        false
    }
}

fn binary_search(arr: &mut Vec<f64>, key: f64) -> isize {
    let mut ng = -1;
    let mut ok = arr.len() as isize;

    while (ok - ng).abs() > 1 {
        let mid = (ok + ng) / 2;
        if is_ok(arr, mid, key) {
            ok = mid;
        } else {
            ng = mid
        }
    }
    return ok;
}

fn get_angle(pt: &(isize, isize)) -> f64 {
    // cos(theta) = x / (x^2 + y^2)
    // theta = arccos(cos(theta)) = arccos(x/(x^2+y^2))
    let cos = pt.0 as f64 / (pt.0.pow(2) as f64 + pt.1.pow(2) as f64).sqrt();
    let angle = cos.acos() * 180.0 / std::f64::consts::PI;
    if pt.1 as f64 >= 0.0 {
        return angle;
    }
    // 第三、第四象限のとき(x, 0)との偏角なので
    return 360.0 - angle;
}

fn get_angle2(i1: f64, i2: f64) -> f64 {
    let diff = (i1 - i2).abs();
    if diff >= 180.0 {
        return 360.0 - diff;
    }
    return diff;
}

fn solve(pos: usize, n: usize, pts: &mut [(isize, isize)]) -> f64 {
    let mut v = Vec::with_capacity(n);
    for i in 0..n {
        if i == pos {
            continue;
        }
        // posは固定する点のindex
        // posの点との相対座標　＜＝＞　thetaがposを原点においたときのy=y_posとの偏角になる
        let sa = (pts[i].0 - pts[pos].0, pts[i].1 - pts[pos].1);
        let angle = get_angle(&sa);
        v.push(angle);
    }
    v.sort_by(|a, b| a.partial_cmp(b).unwrap());

    // 点Aを全探索して、最も偏角の大きくなる点Cを二部探索で求める
    let mut ret = 0.0 as f64;
    for i in 0..v.len() {
        // 180度反対に近い点が最適な点
        let mut target = v[i] + 180.0;
        if target >= 360.0 {
            target -= 360.0;
        }
        let pos1 = binary_search(&mut v, target);

        // 点Cの候補はたかだか２つに絞れる
        let cand_idx1 = pos1 % v.len() as isize;
        let cand_idx2 = (pos1 + v.len() as isize - 1) % v.len() as isize;
        let cand_1 = get_angle2(v[i], v[cand_idx1 as usize]);
        let cand_2 = get_angle2(v[i], v[cand_idx2 as usize]);
        ret = ret.max(cand_1).max(cand_2);
    }
    ret
}

/// 真ん中決め打ち＋偏角ソート
#[fastout]
fn main() {
    input! {
        n: usize,
        mut pts: [(isize, isize); n],
    }

    let mut ans = 0.0 as f64;
    for i in 0..n {
        ans = ans.max(solve(i, n, &mut pts));
    }
    println!("{}", ans)
}
