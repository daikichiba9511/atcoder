fn main() {
    for i in 0..10 {
        for j in 0..10 {
            if i + j >= 10 {
                break;
            }
            println!("{}-{}", i, j);
        }
    }
}
