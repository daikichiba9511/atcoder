use proconio::input;

fn solve1() {
    input! {
        n: usize
    }

    // 奇数の時は、正しい括弧列にならない
    if n % 2 == 1 {
        println!("");
    } else {
        let mut bracket = Vec::new();
        for i in 0..n {
            if i % 2 == 0 {
                bracket.push(1)
            } else {
                bracket.push(-1)
            }
        }
        println!("{:?}", bracket)
    }
}

fn main() {
    solve1()
}
