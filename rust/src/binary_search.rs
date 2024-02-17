/// 基本的にVecのメソッド使うので使い方を認識するテストメイン
/// Ref:
/// [1] https://qiita.com/hossie/items/e170eb80f48cdb4f6b51#%E3%82%BD%E3%83%BC%E3%83%88%E4%BA%8C%E5%88%86%E6%8E%A2%E7%B4%A2
#[cfg(test)]
mod tests {
    #[test]
    fn test() {
        let mut v = vec![2, 4, 6, 6, 6];
        assert_eq!(v.binary_search(&2), Ok(1));
        assert_eq!(v.binary_search(&6), Ok(3));
    }
}
