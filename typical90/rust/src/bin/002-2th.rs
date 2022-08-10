use proconio::input;

fn check(s: Vec<char>) -> bool {
    let mut dep = 0;
    for i in 0..s.len() {
        if s[i] == '(' {
            dep += 1;
        }
        if s[i] == ')' {
            dep -= 1;
        }
        if dep < 0 {
            return false;
        }
    }
    if dep == 0 {
        true
    } else {
        false
    }
}

fn main() {
    input! {
        n: usize,
    }
    for bit in 0..(1 << n) {
        // 初期化時にメモリ確保のヒントを与えることでわずかに性能がよくなる
        let mut candidate = String::with_capacity(n);
        for i in (0..n).rev() {
            // i & (1 << j) = 0 : iのjビットが０であるための条件
            // 1 << j = 2^j: ２進数でj番目の桁に1が立っている
            // bit & 1 << i: bit演算でbitの２進数表現と比較して２進数でj番目に１が立っていれば1
            // i = 4 => 1000 = 2^4 = 8 => else
            if bit & 1 << i == 0 {
                candidate += "(";
            } else {
                candidate += ")";
            }
        }
        if check(candidate.chars().collect()) {
            println!("{}", candidate);
        }
    }
}
