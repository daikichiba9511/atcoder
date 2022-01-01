use proconio::input;

fn is_ok() {
    i
}

fn main() {
    input! {
        n: usize,
        mut a: [i32; n],
        q: usize,
        b: [i32; q]
    }
    // println!("{:?}, {:?}, {:?}, {:?}", b, a, q, b)
    // 愚直にやったらO(nq)=10^10
    // rustのsortはmerge sortらしい
    a.sort();
}
