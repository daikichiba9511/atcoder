fn main() {
    proconio::input! {
        n: u32,
        s: String,
        q: usize,
        cd: [(char, char); q]
    }
    // alphabetの文字列
    let from = String::from("abcdefghijklmnopqrstuvwxyz");
    let mut to = from.clone();

    for (c, d) in cd {
        to = to.replace(c, d.to_string().as_str());
    }
    let mut ans = String::new();
    for c in s.chars() {
        let i = from.find(c).unwrap();
        ans.push(to.chars().nth(i).unwrap());
    }
    println!("{}", ans);
}
