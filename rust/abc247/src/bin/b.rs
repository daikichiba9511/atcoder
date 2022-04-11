use proconio::{input, fastout};

#[fastout]
fn solve() {
    input! {
        n: u64,
        st: [[String; 2]; n],
    }
    // println!("{:?}", st);
    let mut flag = false;
    for i in 0..n {
        let si = &st[i as usize][0];
        let ti = &st[i as usize][1];
        let mut flag_s = true;
        let mut flag_t = true;
        for j in 0..n {
            if i == j {
                continue;
            }
            let sj = &st[j as usize][0];
            let tj = &st[j as usize][1];
            // println!("i: si={} ti={}", si, ti);
            // println!("j: sj={} tj={}", sj, tj);
            if si.eq(sj) || si.eq(tj) {
                flag_s = false;
            }
            if ti.eq(sj) || ti.eq(tj) {
                flag_t = false;
            }
            if !flag_s && !flag_t {
                break;
            }
        }
        if !flag_s && !flag_t {
            flag = true;
            break;
        }
    }
    if flag {
        println!("No")
    } else {
        println!("Yes")
    }
}

fn main() {
    solve();
}
