use proconio::{fastout, input};
#[fastout]
fn main() {
    input! {
        n:usize,t:i32,
        a:[i32;t]
    }
    let mut r = vec![0; n];
    let mut c = vec![0; n];
    let mut d = vec![0; 2];
    for (i, a_i) in a.iter().map(|&x| x - 1).enumerate() {
        let x = a_i % n as i32;
        let y = a_i / n as i32;
        r[x as usize] += 1;
        if r[x as usize] == n {
            println!("{}", i + 1);
            return;
        }
        c[y as usize] += 1;
        if c[y as usize] == n {
            println!("{}", i + 1);
            return;
        }

        // 左上 -> 右下
        if x == y {
            d[0] += 1;
            if d[0] == n {
                println!("{}", i + 1);
                return;
            }
        }

        // 左下 -> 右上
        if (x + y) as usize == n - 1 {
            d[1] += 1;
            if d[1] == n {
                println!("{}", i + 1);
                return;
            }
        }
    }
    println!("-1")
}
