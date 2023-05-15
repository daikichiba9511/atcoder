use proconio::marker::Chars;
use proconio::{fastout, input};

fn is_number(s_i: char) -> bool {
    s_i.is_digit(10)
}

#[fastout]
fn solve1() {
    input! {s: String};
    if s.len() != 8 {
        println!("No");
        return;
    }

    // assert!(!is_number("Q".chars().next().unwrap()));
    // assert!(is_number("1".chars().next().unwrap()));
    // assert!(is_number("11".chars().next().unwrap()));

    for (i, s_i) in s.as_str().chars().enumerate() {
        if (i == 0) && (is_number(s_i)) {
            println!("No");
            return;
        }
        if [1, 2, 3, 4, 5, 6].contains(&i) && (!is_number(s_i)) {
            println!("No");
            return;
        }
        if (i == 1) && (is_number(s_i)) && (s_i.to_digit(10) == Some(0)) {
            println!("No");
            return;
        }
        if (i == 7) && (is_number(s_i)) {
            println!("No");
            return;
        }
    }
    println!("Yes");
}

fn solve2() {
    input! {s: Chars};
    if s.len() != 8 {
        println!("No");
        return;
    }
    for (i, s_i) in s.into_iter().enumerate() {
        if (i == 0 && s_i.is_numeric())
            || ((1..6).contains(&i) && s_i.is_alphabetic())
            || ((i == 1) && s_i.to_digit(10) == Some(0))
            || (i == 7 && s_i.is_numeric())
        {
            println!("No");
            return;
        }
    }
    println!("Yes");
}

fn main() {
    // solve1()
    solve2()
}
