fn main() {
    proconio::input! {
        s: proconio::marker::Chars,
    };

    for i in 0..s.len() {
        let mut diff = true;
        for j in 0..s.len() {
            if i != j && s[i] == s[j] {
                diff = false;
                break;
            }
        }
        if diff {
            println!("{}", i + 1);
        }
    }
}
