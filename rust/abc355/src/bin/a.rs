use proconio;

fn main() {
    proconio::input! {
        a:i32, b:i32
    }
    if a == b {
        println!("-1")
    } else {
        for i in 1..4 {
            if i != a && i != b {
                println!("{}", i);
                return;
            }
        }
    }
}
