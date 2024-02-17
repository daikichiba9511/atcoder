pub fn add(left: usize, right: usize) -> usize {
    left + right
}

#[cfg(test)]
mod tests {

    #[test]
    fn should_match_only_one_elem() {
        let v = vec![2, 4, 6, 6, 6];
        assert_eq!(v.binary_search(&6), Ok(2));
        assert_eq!(v.binary_search(&4), Ok(1));
    }

    #[test]
    fn should_not_match_some_elem() {
        let v = vec![2, 4, 6, 6, 6];
        assert_eq!(v.binary_search(&8), Err(5)); // enable to insert 8 at index 5
        assert_eq!(v.binary_search(&3), Err(1)); // enable to insert 3 at index 1
    }

    #[test]
    fn should_match_elems() {
        let v = vec![2, 4, 6, 6, 6];
        assert!(match v.binary_search(&6) {
            Ok(2..=4) => true,
            _ => false,
        });
    }

    #[test]
    fn ignore_if_match_or_not() {
        let v = vec![2, 4, 6, 6, 6];
        let i = v.binary_search(&6).unwrap_or_else(|x| x);
        assert_eq!(i, 2); // enable to insert 6 between 4 and 6 so, index is 2
    }
}
