use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n: usize, k: usize, a: [i32; n], b: [i32; n]};
    // ｎ個の要素を持つ数列Aをk回の操作で数列Bにできるか
    // n個の要素があるとき１つ目から順に何回の操作で同じになるか(b_i - a_i).abs()

    // -- Check Difference
    // O(n)
    let mut sum_elementwise_diff = 0;
    for (&a_i, &b_i) in a.iter().zip(b.iter()) {
        sum_elementwise_diff += (b_i - a_i).abs();
    }

    if sum_elementwise_diff as usize > k {
        println!("No");
        return;
    }

    // check Parity
    // K以下で\sum | A_i - B_i| とKのパリティが同じじゃない時はA=Bは実現できない
    // 偶奇が同じなら+1と-1の和で0にする操作のペアが作れてちょうどK回でA=Bを達成できる操作の系を作れる
    // 逆に偶奇がそろってないと和で０にする操作ができないのでK回でA=Bを達成できない
    if sum_elementwise_diff as usize % 2 != k % 2 {
        println!("No");
        return;
    }

    println!("Yes")
}
