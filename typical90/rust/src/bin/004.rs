use proconio::input;

fn main() {
    input! {
        h: usize, w: usize,
        a: [[usize; w]; h],
    }

    let mut sum_h = vec![0; h];
    let mut sum_w = vec![0; w];

    for i in 0..h {
        for j in 0..w {
            // sum_h: iに関する行の総和
            // sum_w: jに関する列の総和
            sum_h[i] += a[i][j];
            sum_w[j] += a[i][j];
        }
    }

    for i in 0..h {
        for j in 0..w {
            // a[i][j]は2度足されてるので一回分引けばいい
            let ans = sum_h[i] + sum_w[j] - a[i][j];
            print!("{} ", ans);
        }
        // B_i,jで出力するために1行終えたら改行
        println!("")
    }
}
