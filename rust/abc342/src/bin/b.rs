fn main() {
    proconio::input! {
        n: u32,
        p: [u32; n],
        q: usize,
    };
    for _ in 0..q {
        proconio::input! {
            a: u32,
            b: u32,
        }
        // a, bがpの中で何番目にあるかを求める
        let ia = p.iter().position(|&x| x == a).unwrap();
        let ib = p.iter().position(|&x| x == b).unwrap();
        if ia < ib {
            println!("{}", a);
        } else {
            println!("{}", b);
        }
    }
}
